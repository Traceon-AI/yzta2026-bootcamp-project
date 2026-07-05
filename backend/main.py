from fastapi import FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI(title="Traceon-AI Backend API")

# Arayüzün (frontend) backend ile sorunsuz konuşabilmesi için CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Regülasyonları Listeleme Endpoint'i (Sözleşmedeki Madde 2)
@app.get("/regulations")
async def get_regulations():
    return {
        "regulations": [
            { "id": "gdpr", "name": "GDPR", "article_count": 14 },
            { "id": "kvkk", "name": "KVKK", "article_count": 11 }
        ]
    }

# 2. Doküman Yükleme ve Analiz (Mock / Sahte) Endpoint'i (Sözleşmedeki Madde 1)
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    regulation: str = Form(...)
):
    # Dosya uzantısı kontrolü
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ["pdf", "docx"]:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "unsupported_file_type",
                "message": "Sadece PDF ve DOCX dosyaları desteklenmektedir."
            }
        )
    
    # Gerçek yapay zeka analizi yapılıyormuş gibi 2 saniye bekletme simülasyonu
    time.sleep(2)
    
    # api-contract.md sözleşmesindeki başarılı cevabın (JSON) birebir aynısı
    return {
        "regulation": regulation,
        "document_name": file.filename,
        "overall_score": 62,
        "results": [
            {
                "article_id": f"{regulation}-art-13",
                "title": "Bilgilendirme Yükümlülüğü",
                "status": "partial",
                "evidence": "We collect your name, email, and usage data...",
                "evidence_location": "sayfa 1, paragraf 2",
                "recommendation": "Hukuki dayanak ve saklama süresi eklenmeli."
            },
            {
                "article_id": f"{regulation}-art-6",
                "title": "Hukuki Dayanak",
                "status": "missing",
                "evidence": None,
                "evidence_location": None,
                "recommendation": "Verinin hangi hukuki gerekçeyle (rıza, sözleşme vb.) işlendiği belirtilmeli."
            }
        ]
    }