from fastapi import FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.security import setup_cors
import os
import json

from core.config import settings
from services.document import extract_chunks
from services.rag import run_rag_analysis

app = FastAPI(title=settings.PROJECT_TITLE)

# CORS güvenlik ayarlarını modüler olarak uyguluyoruz
setup_cors(app)

def load_regulation_data(regulation_id: str):
    """Kök dizinde (backend klasörünün bir üstünde) duran data klasöründen JSON okur."""
    # main.py dosyasının olduğu klasör (backend/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Bir üst klasöre çık ve oradaki data/ klasörüne git
    file_path = os.path.join(current_dir, "..", "data", f"{regulation_id}.json")
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail={
            "error": "processing_failed",
            "message": f"{regulation_id} veri dosyası bulunamadı. Aranan konum: {file_path}"
        })
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 1. Regülasyonları Listeleme Endpoint'i (Dinamik)
@app.get("/regulations")
async def get_regulations():
    try:
        gdpr_data = load_regulation_data("gdpr")
        kvkk_data = load_regulation_data("kvkk")
        gdpr_count = len(gdpr_data) if isinstance(gdpr_data, list) else len(gdpr_data.get("articles", []))
        kvkk_count = len(kvkk_data) if isinstance(kvkk_data, list) else len(kvkk_data.get("articles", []))
    except Exception:
        gdpr_count, kvkk_count = 15, 12

    return {
        "regulations": [
            { "id": "gdpr", "name": "GDPR", "article_count": gdpr_count },
            { "id": "kvkk", "name": "KVKK", "article_count": kvkk_count }
        ]
    }

# 2. Doküman Yükleme ve Gerçek Analiz Endpoint'i
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    regulation: str = Form(...)
):
    # Dosya türü doğrulama
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ["pdf", "docx"]:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "unsupported_file_type",
                "message": "Sadece PDF ve DOCX dosyaları desteklenmektedir."
            }
        )
    
    # 1. Adım: Dosyayı oku ve parçala
    file_bytes = await file.read()
    doc_chunks = extract_chunks(file_bytes, file_extension)
    
    if not doc_chunks:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "empty_document",
                "message": "Dokümandan anlamlı bir metin çıkarılamadı."
            }
        )
        
    # 2. Adım: Seçilen regülasyon yasa maddelerini yükle (Regülasyon-Agnostik)
    reg_data = load_regulation_data(regulation)
    articles = reg_data if isinstance(reg_data, list) else reg_data.get("articles", [])
    
    # 3. Adım: Modüler RAG analizini tetikle
    results = run_rag_analysis(doc_chunks, articles)
    
    # 4. Adım: api-contract.md formülüne göre overall_score hesapla
    met_count = sum(1 for r in results if r["status"] == "met")
    partial_count = sum(1 for r in results if r["status"] == "partial")
    
    total_articles = len(articles)
    overall_score = int(((met_count + (partial_count * 0.5)) / total_articles) * 100) if total_articles > 0 else 0
    
    return {
        "regulation": regulation,
        "document_name": file.filename,
        "overall_score": overall_score,
        "results": results
    }