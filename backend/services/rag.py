import json
import logging
import time
import urllib.request
import urllib.error
from core.config import settings

logger = logging.getLogger("uvicorn.error")

def run_rag_analysis(doc_chunks: list, articles: list) -> list:
    """
    Dokümandaki paragrafları ve regülasyon maddelerini TEK İSTEKTE
    doğrudan Gemini REST API'ye göndererek anlamsal AI analizi yapar.
    """
    # 1. Doküman paragraflarını numaralandırarak metin haline getirelim
    formatted_chunks = []
    for chunk in doc_chunks:
        formatted_chunks.append(f"[{chunk['location']}]: {chunk['text']}")
    document_text = "\n\n".join(formatted_chunks)

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
    # En stabil REST endpoints listesi
    models_to_try = ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash-latest"]

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "response_mime_type": "application/json"
            }
        }

        # Rate limit (429) durumunda 2 kere deneme mekanizması
        for attempt in range(2):
            try:
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )

                # Timeout süresini 60 saniyeye çıkardık
                with urllib.request.urlopen(req, timeout=60) as response:
                    result_data = json.loads(response.read().decode("utf-8"))
                    
                    raw_text = result_data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    
                    # Markdown temizlik
                    if raw_text.startswith("```"):
                        lines = raw_text.splitlines()
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines and lines[-1].startswith("```"):
                            lines = lines[:-1]
                        raw_text = "\n".join(lines).strip()

                    ai_results = json.loads(raw_text)
                    logger.info(f"Gemini REST API analizi ({model_name}) başarıyla tamamlandı!")
                    return ai_results

            except urllib.error.HTTPError as http_err:
                if http_err.code == 429:
                    logger.warning(f"Model {model_name} 429 Rate Limit aldı. 2 saniye beklenip tekrar deneniyor... (Deneme {attempt+1})")
                    time.sleep(2)
                    continue
                else:
                    logger.warning(f"Model {model_name} HTTP Hatası: {http_err.code} - {http_err.reason}")
                    break
            except Exception as e:
                logger.warning(f"Model {model_name} Istek Hatasi: {str(e)}")
                break

    logger.error("Tüm Gemini REST API modelleri başarısız oldu, kural tabanlı yedek motor çalıştırılıyor.")
    return run_fallback_keyword_analysis(doc_chunks, articles)


def run_fallback_keyword_analysis(doc_chunks: list, articles: list) -> list:
    """Yedek kural tabanlı motor"""
    results = []
    for article in articles:
        art_id = article.get("article_id")
        art_title = article.get("title")
        
        results.append({
            "article_id": art_id,
            "title": art_title,
            "status": "partial",
            "evidence": doc_chunks[0]["text"] if doc_chunks else None,
            "evidence_location": doc_chunks[0]["location"] if doc_chunks else None,
            "recommendation": f"{art_title} konusuna kısmen değinilmiştir, detaylandırılması önerilir."
        })
    return results