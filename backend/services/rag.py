import json
import logging
import time
import urllib.request
import urllib.error
from core.config import settings

logger = logging.getLogger("uvicorn.error")


def _build_document_text(doc_chunks: list) -> str:
    """Limit prompt size to reduce quota pressure and latency."""
    limited_chunks = doc_chunks[: settings.LLM_MAX_DOC_CHUNKS]
    formatted_chunks = []
    for chunk in limited_chunks:
        chunk_text = (chunk.get("text") or "")[: settings.LLM_MAX_CHARS_PER_CHUNK]
        formatted_chunks.append(f"[{chunk.get('location', 'unknown')}]: {chunk_text}")
    return "\n\n".join(formatted_chunks)


def _normalize_ai_results(ai_results: list, articles: list) -> list:
    """Guarantee api-contract shape even when model output is imperfect."""
    by_id = {}
    for item in ai_results:
        if isinstance(item, dict) and item.get("article_id"):
            by_id[item["article_id"]] = item

    normalized = []
    for article in articles:
        art_id = article.get("article_id")
        art_title = article.get("title")
        candidate = by_id.get(art_id, {})
        status = candidate.get("status")
        if status not in {"met", "partial", "missing"}:
            status = "missing"

        evidence = candidate.get("evidence")
        evidence_location = candidate.get("evidence_location")
        recommendation = candidate.get("recommendation")

        if status == "missing":
            evidence = None
            evidence_location = None
            if not recommendation:
                recommendation = article.get("recommendation") or f"{art_title} gerekliliği dokümana eklenmelidir."
        elif status == "met":
            recommendation = None
        elif not recommendation:
            recommendation = f"{art_title} konusundaki açıklamalar güçlendirilmelidir."

        normalized.append(
            {
                "article_id": art_id,
                "title": art_title,
                "status": status,
                "evidence": evidence,
                "evidence_location": evidence_location,
                "recommendation": recommendation,
            }
        )

    return normalized

def run_rag_analysis(doc_chunks: list, articles: list, force_fallback: bool = False) -> tuple[list, str]:
    """
    Dokümandaki paragrafları ve regülasyon maddelerini TEK İSTEKTE
    doğrudan Gemini REST API'ye göndererek anlamsal AI analizi yapar.
    """
    if force_fallback:
        logger.info("Fallback analizi istemci istegiyle zorlandi.")
        return run_fallback_keyword_analysis(doc_chunks, articles), "fallback_forced"

    # 1. Doküman paragraflarını prompt boyutunu kontrollü tutarak hazırlayalım
    document_text = _build_document_text(doc_chunks)

    # 2. Regülasyon maddelerini hazırlayalım
    formatted_articles = []
    for art in articles:
        formatted_articles.append({
            "article_id": art.get("article_id"),
            "title": art.get("title"),
            "description": art.get("description")
        })
    articles_json_str = json.dumps(formatted_articles, ensure_ascii=False)

    # 3. Gemini Prompt
    prompt = f"""
You are an expert Data Protection & Legal Compliance Auditor (GDPR & KVKK Expert).
Analyze the provided DOCUMENT PARAGRAPHS against the REGULATION ARTICLES.

DOCUMENT PARAGRAPHS:
{document_text}

REGULATION ARTICLES:
{articles_json_str}

TASK:
For each regulation article, search the document paragraphs and evaluate compliance.
Return ONLY a JSON list adhering strictly to the schema below.

RULES:
1. `status` MUST be one of:
   - "met": The document clearly and fully addresses this article.
   - "partial": The document mentions or partially addresses this article, but lacks detail.
   - "missing": The document completely fails to mention or address this requirement.

2. `evidence`: 
   - If status is "met" or "partial", extract the EXACT snippet from the matching paragraph.
   - If status is "missing", set `evidence` to null.

3. `evidence_location`: 
   - If status is "met" or "partial", provide the exact location label like "paragraf X".
   - If status is "missing", set `evidence_location` to null.

4. `recommendation`:
   - If status is "met", set to null.
   - If status is "partial", write a brief advice in Turkish on what is missing.
   - If status is "missing", write a clear recommendation in Turkish explaining how to implement this rule.

OUTPUT FORMAT:
Return ONLY raw valid JSON array. Do not use Markdown formatting or backticks.

Example format:
[
  {{
    "article_id": "gdpr-art-5",
    "title": "Principles relating to processing of personal data",
    "status": "met",
    "evidence": "We process personal data for...",
    "evidence_location": "paragraf 12",
    "recommendation": null
  }}
]
"""

    api_key = settings.GEMINI_API_KEY
    model_name = settings.LLM_MODEL

    if not api_key:
        logger.error("GEMINI_API_KEY bulunamadı, kural tabanlı yedek motor çalıştırılıyor.")
        return run_fallback_keyword_analysis(doc_chunks, articles), "fallback_no_api_key"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"response_mime_type": "application/json"},
    }

    for attempt in range(settings.LLM_MAX_RETRIES):
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )

            with urllib.request.urlopen(req, timeout=settings.LLM_TIMEOUT_SECONDS) as response:
                result_data = json.loads(response.read().decode("utf-8"))
                raw_text = result_data["candidates"][0]["content"]["parts"][0]["text"].strip()

                if raw_text.startswith("```"):
                    lines = raw_text.splitlines()
                    if lines and lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].startswith("```"):
                        lines = lines[:-1]
                    raw_text = "\n".join(lines).strip()

                ai_results = json.loads(raw_text)
                logger.info(f"Gemini REST API analizi ({model_name}) başarıyla tamamlandı!")
                return _normalize_ai_results(ai_results, articles), "ai"

        except urllib.error.HTTPError as http_err:
            if http_err.code == 429 and attempt < settings.LLM_MAX_RETRIES - 1:
                wait_seconds = settings.LLM_BACKOFF_BASE_SECONDS * (2 ** attempt)
                logger.warning(
                    f"Model {model_name} 429 Rate Limit aldı. {wait_seconds:.0f} saniye beklenip tekrar deneniyor... "
                    f"(Deneme {attempt + 1})"
                )
                time.sleep(wait_seconds)
                continue

            logger.warning(f"Model {model_name} HTTP Hatası: {http_err.code} - {http_err.reason}")
            break
        except Exception as e:
            logger.warning(f"Model {model_name} Istek Hatasi: {str(e)}")
            break

    logger.error("Gemini REST API başarısız oldu, kural tabanlı yedek motor çalıştırılıyor.")
    return run_fallback_keyword_analysis(doc_chunks, articles), "fallback_error"


def run_fallback_keyword_analysis(doc_chunks: list, articles: list) -> list:
    """Yedek kural tabanlı motor"""
    results = []

    normalized_chunks = []
    for chunk in doc_chunks:
        normalized_chunks.append(
            {
                "text": chunk.get("text") or "",
                "text_lower": (chunk.get("text") or "").lower(),
                "location": chunk.get("location"),
            }
        )

    for article in articles:
        art_id = article.get("article_id")
        art_title = article.get("title")
        art_keywords = [kw.lower() for kw in article.get("keywords", []) if isinstance(kw, str)]

        best_chunk = None
        best_hits = 0

        for chunk in normalized_chunks:
            hits = sum(1 for kw in art_keywords if kw and kw in chunk["text_lower"])
            if hits > best_hits:
                best_hits = hits
                best_chunk = chunk

        if best_chunk and best_hits >= 2:
            status = "met"
            evidence = best_chunk["text"]
            evidence_location = best_chunk["location"]
            recommendation = None
        elif best_chunk and best_hits == 1:
            status = "partial"
            evidence = best_chunk["text"]
            evidence_location = best_chunk["location"]
            recommendation = f"{art_title} konusuna kısmen değinilmiştir, detaylandırılması önerilir."
        else:
            status = "missing"
            evidence = None
            evidence_location = None
            recommendation = article.get("recommendation") or f"{art_title} gerekliliği dokümana açıkça eklenmelidir."

        results.append({
            "article_id": art_id,
            "title": art_title,
            "status": status,
            "evidence": evidence,
            "evidence_location": evidence_location,
            "recommendation": recommendation
        })
    return results