# Sprint 1 Review

## Ne planlanmıştı
Fikir netleştirme, kapsam belirleme. Kod geliştirmenin Sprint 2'de
başlaması bekleniyordu.

## Ne tamamlandı

**Planlama ve dokümantasyon (tam):**
- İlk fikir (ISO 27001) değerlendirildi, telif riski nedeniyle GDPR +
  KVKK ikili kapsamına karar verildi.
- Regülasyon-agnostik mimari yaklaşımı belirlendi.
- `constitution.md`, `spec.md`, `plan.md`, `tasks.md`, `api-contract.md`
  dokümanları hazırlandı.
- GitHub organizasyonu, repo ve sprint board kuruldu.
- README hazırlandı.

**Beklenenin ötesinde — erken MVP çıktıları:**
Ekibin geç entegre olması nedeniyle Sprint 1 başlangıçta sadece
planlamayla sınırlı tutulmuştu. Ancak ekibin yoğun eforuyla, üç cephede
de sprint bitmeden somut çıktılar elde edildi:
- **Backend:** `api-contract.md` sözleşmesine birebir uyan, çalışan bir
  mock API (`GET /regulations`, `POST /analyze`) geliştirildi
  (`backend/main.py`).
- **Frontend:** Landing page, regülasyon seçimi (GDPR/KVKK), drag-drop
  dosya yükleme, analiz süreci göstergesi ve mock veriyle uçtan uca
  çalışan sonuç ekranı tamamlandı (`frontend/`).
- **Bilgi Tabanı:** GDPR (15 madde) ve KVKK (12 madde) veri dosyaları
  hedeflenen kapsamı karşılayacak şekilde tamamlandı; ayrıca test için
  örnek doküman (`docs/privacy-policy-test.md`) hazırlandı.

Bu çıktıların **birbirine entegrasyonu Sprint 2'ye devredilmiştir** —
Sprint 1 içinde parçalar ayrı ayrı üretilmiş ve doğrulanmış, ancak uçtan
uca birlikte test edilmemiştir.

## Tamamlanmayan / ertelenen
- Backend'in gerçek RAG pipeline'a geçişi (chunking, embedding, LLM
  karşılaştırma) henüz başlamamıştır — Sprint 2'nin ana işi.
- Frontend'in gerçek API'ye bağlanması (mock verinin kaldırılması)
  Sprint 2 kapsamındadır.
- `/regulations` endpoint'indeki madde sayıları güncellenmelidir (bkz.
  `docs/sprint-1-product-status.md` — ilgili issue açıldı).

## Kanıtlar
- Ekran görüntüleri: `docs/evidence/sprint-1/`
- Ürün durumu detayı: `docs/sprint-1-product-status.md`
- Daily Scrum kayıtları: `docs/sprint-1-daily-scrum.md`
