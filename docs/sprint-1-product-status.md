# Sprint 1 — Ürün Durumu

Bu sayfa, Sprint 1 sonunda elimizde gerçekten ne olduğunu tek yerden
gösterir. Kod dosyaları + ekran görüntüleri buraya toplanır.

## Backend

**Durum:** `api-contract.md` sözleşmesine uygun, mock veriyle çalışan
iskelet hazır. Gerçek RAG pipeline (chunking, embedding, LLM
karşılaştırma) henüz başlamadı — bu Sprint 2 kapsamında.

- Kod: `main.py` ([repo linki eklenecek])
- Endpoint'ler: `GET /regulations`, `POST /analyze` (mock cevap)
- [x] Çalışır halinin ekran görüntüleri:
  - [Swagger /docs arayüzü](./evidence/sprint-1/backend-swagger-docs.jpeg)
    — `GET /regulations` ve `POST /analyze` endpoint'leri aktif
  - [Uvicorn terminal çıktısı](./evidence/sprint-1/backend-uvicorn-terminal.jpeg)
    — sunucu ayakta, `/docs` ve `/openapi.json` istekleri 200 OK
    
**Bilinen eksik / düzeltilecek:**
- `/regulations` cevabındaki `article_count` değerleri (`gdpr: 14`,
  `kvkk: 11`) güncel değil, gerçek sayılar 15 ve 12. Sabit yazmak yerine
  veri dosyasının uzunluğundan dinamik hesaplanması önerilir.

## Frontend

**Durum:** [Önder'den bilgi/kanıt bekleniyor]

- [ ] Kod/branch linki
- [x] Ekran görüntüleri:
  - [Upload + regülasyon seçimi](./evidence/sprint-1/frontend-landing-upload.png)
  - [Analiz süreci (loading)](./evidence/sprint-1/frontend-analyzing-state.png)
  - [Sonuç ekranı — mock veri, 62/100 skor](./evidence/sprint-1/frontend-results-mock.png)

## Bilgi Tabanı

**Durum:** GDPR ve KVKK veri dosyaları oluşturuldu, hedeflenen madde
sayıları karşılandı.

| Dosya | Madde Sayısı | Hedef (`spec.md`) | Durum |
|---|---|---|---|
| `data/gdpr.json` | 15 | en az 12-15 | ✅ Karşılandı |
| `data/kvkk.json` | 12 | en az 10-12 | ✅ Karşılandı |

- Kaynaklar doğru: GDPR → EUR-Lex, KVKK → mevzuat.gov.tr (resmi, ücretsiz)
- Şema tutarlı: her iki dosya da `article_id, article_number, title,
  category, description, keywords, recommendation, source` alanlarını
  taşıyor — motorun regülasyon-agnostik çalışması için gerekli tutarlılık
  sağlanmış.
- [ ] Test dokümanı (örnek GDPR/KVKK metni) linki eklenecek —
      **Efnan/Ezgi'den istenecek**

## Genel Değerlendirme

Sprint 1'de planlanandan fazlası çıktı: dokümantasyon ve altyapının
yanında, Backend ve Bilgi Tabanı tarafında gerçek, sözleşmeye uygun ilk
çıktılar üretildi. Frontend tarafının durumu netleşince bu sayfa
güncellenecek. Bu üç parçanın **birlikte gerçekten çalışıp çalışmadığı**
(entegrasyon testi) Sprint 2'nin ilk işi olacak.
