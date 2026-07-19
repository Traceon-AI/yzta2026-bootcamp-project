# Sprint 2 Review

## Ne planlanmıştı
Sprint 2 hedefi: GDPR ile uçtan uca çalışan iskelet — gerçek RAG pipeline
(doküman metne çevirme, chunking, embedding, LLM karşılaştırma) ve
frontend'in gerçek API'ye bağlanması.

## Ne tamamlandı

**Backend (Eylül Zengin) — sprint kapanışında teslim edildi:**
- Doküman işleme motoru: PDF (pypdf) ve DOCX (python-docx) dosyaları
  gerçekten okunuyor, paragraf bazlı chunk'lara ayrılıyor ve her parçanın
  konumu (evidence_location) otomatik üretiliyor (#16, #17).
- `GET /regulations` statik mock'tan çıkarıldı; madde sayıları artık
  data/ altındaki json dosyalarından dinamik okunuyor (#49).
- GDPR veri dosyası analiz akışına bağlandı (#20).
- Kod modüler yapıya taşındı (core/config, core/security,
  services/document, services/rag) ve API key .env mimarisine alındı.
- Swagger üzerinden uçtan uca test: sözleşmeye (api-contract.md) birebir
  uyan gerçek JSON çıktısı doğrulandı, mock cevaplar devre dışı.

**Süreç ve altyapı:**
- Sprint 1 kapanış paketi tamamlandı, repo sprint bazlı klasör yapısına
  geçirildi.
- Branch temizliği yapıldı; branch isimlendirme ve "küçük PR, sık push"
  standardı ilan edildi.
- Sprint sonunda kapsamlı yeniden planlama: görevler güncel
  müsaitliklere göre dağıtıldı, entegrasyon (#51), Docker (#52), deploy
  (#53) ve PR review (#54) görevleri tanımlandı.

## Tamamlanmayan / ertelenen
- **LLM analiz katmanı devreye alınamadı:** Ücretsiz API anahtarının hız
  sınırı (madde başına ayrı istek → 15 istekte limit) nedeniyle analiz,
  anahtar kelime eşleştirme motoruyla (fallback) çalışıyor. Gerçek AI
  analizi (embedding ön-filtreleme + tek batch LLM çağrısı) Sprint 3'ün
  kritik işi olarak planlandı (#18, #19).
- Frontend'in gerçek API'ye bağlanması sprint içinde yapılamadı —
  Sprint 3 başına alındı (#51, hedef 22 Temmuz).
- Planlanan ara entegrasyon testi (12-13 Temmuz) yapılamadı.

## Sprint 2 Bitiş Kriteri karşılandı mı?
**Kısmen.** "Kullanıcı bir GDPR dokümanı yükleyip madde bazlı sonuç ve
kanıt görebiliyor" akışı backend tarafında (Swagger üzerinden) çalışır
durumda; ancak sonuçlar LLM yerine anahtar kelime eşleştirmesiyle
üretiliyor ve frontend henüz bağlı değil. Yani iskelet var, "AI" katmanı
ve arayüz bağlantısı eksik.

## Kanıtlar
- Backend teknik devir dokümanı (Eylül Zengin)
- Swagger uçtan uca test çıktısı (örnek JSON — devir dokümanında)
- Sprint board: #16, #17, #49, #20 → Review/Done