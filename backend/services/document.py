from io import BytesIO
from pypdf import PdfReader
from docx import Document
from fastapi import HTTPException

def extract_chunks(file_bytes: bytes, file_extension: str) -> list:
    """
    Dokümandan metin parçalarını konum bilgisi (metadata) ile birlikte çıkarır.
    Her eleman: {"text": "...", "location": "..."} döndürür.
    """
    chunks = []
    
    if file_extension == "pdf":
        try:
            reader = PdfReader(BytesIO(file_bytes))
            for page_num, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if text and text.strip():
                    # Basit ve etkili chunking: Sayfayı çift alt satırlara göre paragraflara bölme
                    paragraphs = text.split("\n\n")
                    for p_num, para in enumerate(paragraphs, start=1):
                        if para.strip():
                            chunks.append({
                                "text": para.strip(),
                                "location": f"sayfa {page_num}, paragraf {p_num}"
                            })
        except Exception as e:
            raise HTTPException(status_code=400, detail={"error": "processing_failed", "message": f"PDF okunurken hata oluştu: {str(e)}"})
                        
    elif file_extension == "docx":
        try:
            doc = Document(BytesIO(file_bytes))
            for p_num, paragraph in enumerate(doc.paragraphs, start=1):
                if paragraph.text and paragraph.text.strip():
                    chunks.append({
                        "text": paragraph.text.strip(),
                        "location": f"paragraf {p_num}"
                    })
        except Exception as e:
            raise HTTPException(status_code=400, detail={"error": "processing_failed", "message": f"DOCX okunurken hata oluştu: {str(e)}"})
            
    return chunks