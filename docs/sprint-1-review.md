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
planlamayla sınırlı tutulmuştu. Ancak ekibin yoğun eforuyla, Backend ve
Bilgi Tabanı tarafında sprint bitmeden ilk somut çıktılar elde edildi:
- Backend: `api-contract.md` sözleşmesine birebir uyan, çalışan bir mock
  API (`GET /regulations`, `POST /analyze`) geliştirildi.
- Bilgi Tabanı: GDPR (15 madde) ve KVKK (12 madde) veri dosyaları
  hedeflenen kapsamı karşılayacak şekilde tamamlandı.

Bu çıktıların **değerlendirilmesi ve birbirine entegrasyonu Sprint 2'ye
devredilmiştir** — Sprint 1 içinde sadece üretim yapılmış, uçtan uca
test edilmemiştir.

## Tamamlanmayan / ertelenen
- Frontend tarafının durumu bu Review yazıldığı sırada netleşmemiştir.
- Backend-Bilgi Tabanı entegrasyonu (gerçek RAG pipeline) henüz
  başlamamıştır, Sprint 2'nin ilk işi olacaktır.
- `/regulations` endpoint'indeki madde sayıları güncellenmelidir (bkz.
  `docs/sprint-1-product-status.md`).
