# Sprint 2 — Ürün Durumu

Bu sayfa, Sprint 2 sonunda elimizde gerçekten ne olduğunu tek yerden
gösterir.

## Backend

**Durum:** Mock aşaması geçildi — doküman işleme gerçek. Yüklenen
PDF/DOCX dosyaları okunuyor, paragraf bazlı chunk'lanıyor, konum
bilgisi (evidence_location) üretiliyor ve sözleşmeye birebir uyan
gerçek JSON dönülüyor. Analiz katmanı ise geçici olarak anahtar kelime
eşleştirmesiyle çalışıyor (aşağıya bkz.).

- Kod: `backend/` — modüler yapı: `main.py`, `core/config.py`,
  `core/security.py`, `services/document.py`, `services/rag.py`
- Çalışan pipeline adımları: metin çıkarma ✅, chunking ✅, konum
  metadata ✅, dinamik regülasyon verisi okuma ✅, sözleşme uyumlu
  çıktı ✅
- Swagger uçtan uca test: 200 OK, örnek çıktı devir dokümanında

**Bilinen eksik / kritik not:**
- **LLM analizi devrede değil.** Ücretsiz Gemini anahtarının hız sınırı
  (madde başına ayrı istek) nedeniyle analiz, keyword eşleştirme
  motoruna (fallback) düşürüldü. Örnek çıktıdaki kanıtların niteliği
  bunu yansıtıyor (başlık satırlarının kanıt sayılması gibi). Sprint
  3'ün kritik işi: embedding ön-filtreleme + tek batch LLM çağrısı ile
  gerçek AI analizine geçiş (#18, #19 — hedef 24 Temmuz). Keyword
  motoru fallback olarak korunacak.

## Frontend

**Durum:** Sprint 1'deki haliyle — mock veriyle çalışıyor, gerçek
API'ye henüz bağlı değil.

- Sprint 3 planı: gerçek backend'e bağlanma (#51, Efnan, hedef 22
  Temmuz — backend artık gerçek cevap döndüğü için entegrasyon
  doğrudan gerçek akışa yapılacak), UX iyileştirmeleri (#33-35, Önder),
  canlıya alma (#53, Önder, hedef 29 Temmuz)

## Bilgi Tabanı / Test

| Varlık | Durum |
|---|---|
| `data/gdpr.json` (15 madde) | ✅ Hazır ve analize bağlı |
| `data/kvkk.json` (12 madde) | ✅ Hazır (motor agnostik — uçtan uca doğrulama #26'da) |
| GDPR test dokümanı | ✅ Hazır, Swagger testinde kullanıldı |
| KVKK test dokümanı (Türkçe) | ⏳ Ezgi, hedef 24 Temmuz (#37) |
| Bilgi tabanı ikinci göz kontrolü | ⏳ Ezgi, hedef 28 Temmuz (#36) |

## Entegrasyon Testi

12-13 Temmuz'da planlanan ara test yapılamadı. Ancak backend'in sprint
kapanışında gerçek cevap döner hale gelmesiyle Sprint 3'teki entegrasyon
(#51) artık mock'a değil doğrudan gerçek akışa yapılacak — tam
entegrasyon hedefi: 26 Temmuz.

## Genel Değerlendirme

Sprint 2'nin görünümü sprint boyunca "ilerleme yok" iken, kapanış
push'uyla tablo değişti: doküman işleme katmanı gerçek ve sağlam, mock
tamamen devre dışı. Eksik olan iki şey net: (1) analizin gerçek AI'a
(embedding + LLM) taşınması — jüri kriterlerindeki 35 puanlık "Yapay
Zeka Öğeleri" doğrudan buna bağlı, (2) frontend bağlantısı. İkisi de
Sprint 3'ün ilk haftasına tarihli olarak planlandı; 24-26 Temmuz
penceresi projenin belirleyici dönemeci.