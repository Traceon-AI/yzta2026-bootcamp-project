# API Sözleşmesi — Traceon-AI (v1 taslak)

Bu doküman Backend (Efnan) ve Frontend (Ezgi) arasındaki sözleşmedir.
Değişiklik gerekirse burada güncellenir, ikisi de haberdar olur.
Frontend, backend hazır olmadan bu şemaya uygun **mock veriyle** çalışabilir.

---

## 1. Doküman Yükleme + Analiz

**Endpoint:** `POST /analyze`

**İstek (multipart/form-data):**
| Alan | Tip | Zorunlu | Açıklama |
|---|---|---|---|
| `file` | dosya (PDF/DOCX) | Evet | Analiz edilecek doküman |
| `regulation` | string | Evet | `"gdpr"` veya `"kvkk"` |

**Örnek istek (curl):**
```bash
curl -X POST http://localhost:8000/analyze \
  -F "file=@privacy-policy.pdf" \
  -F "regulation=gdpr"
```

**Başarılı cevap (200):**
```json
{
  "regulation": "gdpr",
  "document_name": "privacy-policy.pdf",
  "overall_score": 62,
  "results": [
    {
      "article_id": "gdpr-art-13",
      "title": "Bilgilendirme Yükümlülüğü",
      "status": "partial",
      "evidence": "We collect your name, email, and usage data...",
      "evidence_location": "sayfa 1, paragraf 2",
      "recommendation": "Hukuki dayanak ve saklama süresi eklenmeli."
    },
    {
      "article_id": "gdpr-art-6",
      "title": "Hukuki Dayanak",
      "status": "missing",
      "evidence": null,
      "evidence_location": null,
      "recommendation": "Verinin hangi hukuki gerekçeyle (rıza, sözleşme vb.) işlendiği belirtilmeli."
    }
  ]
}
```

**`status` alanı üç değerden birini alır:**
- `"met"` → Karşılanıyor
- `"partial"` → Kısmen karşılanıyor
- `"missing"` → Karşılanmıyor

**Hata cevabı (4xx/5xx):**
```json
{
  "error": "unsupported_file_type",
  "message": "Sadece PDF ve DOCX dosyaları desteklenmektedir."
}
```

Olası `error` kodları: `unsupported_file_type`, `file_too_large`,
`empty_document`, `processing_failed`.

---

## 2. Desteklenen Regülasyonları Listeleme (opsiyonel, kolay eklenir)

**Endpoint:** `GET /regulations`

**Cevap:**
```json
{
  "regulations": [
    { "id": "gdpr", "name": "GDPR", "article_count": 14 },
    { "id": "kvkk", "name": "KVKK", "article_count": 11 }
  ]
}
```

Frontend, regülasyon seçim ekranını (dropdown/kart) bu endpoint'ten
besleyebilir — ileride üçüncü regülasyon eklenirse frontend kodu
değişmeden otomatik güncellenir.

---

## Notlar / Kararlar
- `overall_score`, 0-100 arası tam sayı. Hesaplama: karşılanan madde
  sayısı / toplam madde sayısı (kısmi karşılananlar 0.5 ağırlık alır).
- `article_id` formatı: `{regulation}-art-{numara}` — hem GDPR hem KVKK
  için tutarlı, frontend'de key olarak kullanılabilir.
- Analiz süresi uzun sürebileceği için (embedding + LLM çağrıları),
  Frontend loading state'i **en az 5-10 saniye** bekleyecek şekilde
  tasarlanmalı.
- v1'de tek dosya, senkron cevap yeterli — async/polling (job queue)
  gerekmiyor. Eğer analiz 15 saniyeyi geçerse bu karara dönüp
  async'e geçmeyi değerlendirin.

## Açık Sorular (Backend + Frontend birlikte karar verecek)
- [ ] `evidence_location` sayfa numarası mı, karakter aralığı mı olacak?
- [ ] Dosya boyutu limiti ne olsun? (Öneri: 10 MB)
- [ ] CORS ayarları — frontend hangi origin'den çağıracak?
