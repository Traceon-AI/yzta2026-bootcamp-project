# Sprint 1 — Ürün Durumu

Bu sayfa, Sprint 1 sonunda elimizde gerçekten ne olduğunu tek yerden
gösterir. Kod dosyaları + ekran görüntüleri buraya toplanır.

## Backend

**Durum:** `api-contract.md` sözleşmesine uygun, mock veriyle çalışan
iskelet hazır ve çalışır halde doğrulandı. Gerçek RAG pipeline
(chunking, embedding, LLM karşılaştırma) Sprint 2 kapsamında.

- Kod: `backend/main.py` (ana branch'te)
- Endpoint'ler: `GET /regulations`, `POST /analyze` (mock cevap)
- [x] Çalışır halinin ekran görüntüleri:
  - [Swagger /docs arayüzü](./evidence/backend-swagger-docs.jpeg)
    — `GET /regulations` ve `POST /analyze` endpoint'leri aktif
  - [Uvicorn terminal çıktısı](./evidence/backend-uvicorn-terminal.jpeg)
    — sunucu ayakta, `/docs` ve `/openapi.json` istekleri 200 OK

**Bilinen eksik / düzeltilecek:**
- `/regulations` cevabındaki `article_count` değerleri (`gdpr: 14`,
  `kvkk: 11`) güncel değil, gerçek sayılar 15 ve 12. Veri dosyasının
  uzunluğundan dinamik hesaplanacak — Sprint 2 issue'su açıldı.

## Frontend

**Durum:** Beklenenin ötesinde — landing page, regülasyon seçimi
(GDPR/KVKK), drag-drop dosya yükleme, analiz süreci göstergesi ve mock
veriyle uçtan uca çalışan sonuç ekranı tamamlandı. Mock veri,
`api-contract.md` şemasıyla birebir uyumlu (article_id, status,
evidence, recommendation).

- Kod: `frontend/` klasörü (ana branch'e merge edildi)
- [x] Ekran görüntüleri:
  - [Upload + regülasyon seçimi](./evidence/frontend-landing-upload.jpeg)
  - [Analiz süreci (loading)](./evidence/frontend-analyzing-state.jpeg)
  - [Sonuç ekranı — mock veri, 62/100 skor](./evidence/frontend-results-mock.jpeg)

## Bilgi Tabanı

**Durum:** GDPR ve KVKK veri dosyaları oluşturuldu, hedeflenen madde
sayıları karşılandı. Test dokümanı da hazır.

| Dosya | Madde Sayısı | Hedef (`spec.md`) | Durum |
|---|---|---|---|
| `data/gdpr.json` | 15 | en az 12-15 | ✅ Karşılandı |
| `data/kvkk.json` | 12 | en az 10-12 | ✅ Karşılandı |

- Kaynaklar doğru: GDPR → EUR-Lex, KVKK → mevzuat.gov.tr (resmi, ücretsiz)
- Şema tutarlı: her iki dosya da `article_id, article_number, title,
  category, description, keywords, recommendation, source` alanlarını
  taşıyor — motorun regülasyon-agnostik çalışması için gerekli tutarlılık
  sağlanmış.
- [x] Test dokümanı hazır: [`docs/privacy-policy-test.md`](./privacy-policy-test.md)
  — Sprint 2'deki pipeline testlerinde kullanılacak.

## Genel Değerlendirme

Sprint 1'de planlanandan fazlası çıktı: dokümantasyon ve altyapının
yanında, Backend, Frontend ve Bilgi Tabanı — üç cephede de sözleşmeye
uygun, doğrulanmış ilk çıktılar üretildi. Bu üç parçanın **birlikte
gerçekten çalışıp çalışmadığı** (entegrasyon testi) Sprint 2'nin ilk
işi olacak; ara entegrasyon kontrolü 12-13 Temmuz civarına planlandı.
