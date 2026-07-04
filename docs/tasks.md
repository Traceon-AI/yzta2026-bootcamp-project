# Tasks: Uyum Ön-Değerlendirme (GDPR birincil + KVKK ikincil)

Kutucuklar GitHub'da işaretlenerek ilerleme takibi yapılabilir (`- [x]`).

## Sprint 2 (6–19 Temmuz) — Çalışan İskelet (GDPR ile)

### Kişi 1 — Backend / RAG
- [ ] Repo iskeleti + bağımlılıklar (FastAPI/benzeri, PDF/DOCX kütüphaneleri)
- [ ] Doküman yükleme endpoint'i (dosya al, metne çevir)
- [ ] Chunking fonksiyonu (paragraf bazlı, basit)
- [ ] Embedding entegrasyonu (çok dilli performansı iyi bir model seç)
- [ ] In-memory benzerlik araması (chunk ↔ regülasyon maddesi eşleştirme) —
      **regülasyon parametre olarak alınmalı, hardcode edilmemeli**
- [ ] LLM'e "bu chunk bu maddeyi karşılıyor mu?" prompt'u + JSON çıktı formatı
- [ ] Uçtan uca test: 1 örnek GDPR dokümanıyla pipeline'ı çalıştır

### Kişi 2 — Frontend
- [ ] Kişi 1 ile API sözleşmesini netleştir (istek/cevap formatı, regülasyon
      parametresi dahil — 1 sayfalık not)
- [ ] Dosya yükleme ekranı (drag-drop veya basit input)
- [ ] Regülasyon seçim bileşeni (GDPR / KVKK — şimdilik sadece GDPR aktif,
      KVKK "yakında" olarak görünebilir)
- [ ] Yükleniyor/işleniyor durumu (spinner, basit)
- [ ] Sonuç tablosu iskeleti (madde adı, durum, boş kanıt alanı) — backend
      hazır olmadan mock veriyle çalış

### Kişi 3 — Bilgi Tabanları + Süreç
- [ ] **GDPR**: EUR-Lex'ten en az 12-15 temel yükümlülüğü derle, kendi
      cümlelerinle özetle (`data/gdpr.json`)
- [ ] Her GDPR maddesi için: kısa açıklama + "eksikse önerilen aksiyon" metni
- [ ] Test için 1-2 örnek İngilizce doküman bul/oluştur (örnek/anonim metin)
- [ ] **KVKK**: Resmi Gazete'den en az 10-12 temel yükümlülüğü derle, aynı
      JSON şemasıyla hazırla (`data/kvkk.json`) — Sprint 2'de sadece
      hazırlık, motora bağlama Sprint 3'te
- [ ] GitHub reposu: README (takım ismi, roller, ürün açıklaması, hedef
      kitle) — kılavuzdaki formatta
- [ ] Sprint board (GitHub Projects/Trello/Miro) kur ve linki README'ye ekle
- [ ] Sprint 2 sonu: Daily Scrum notlarını ve sprint board güncellemelerini
      GitHub'a işle (kanıt için)

### Sprint 2 Bitiş Kriteri (Definition of Done)
Bir kullanıcı örnek bir GDPR dokümanı yükleyip en az birkaç madde için
karşılanıyor/karşılanmıyor sonucu ve kanıt metni görebiliyor. KVKK verisi
hazır ama henüz arayüzde aktif değil olabilir.

---

## Sprint 3 (20 Temmuz–2 Ağustos) — KVKK Entegrasyonu + Doğruluk + Cila

### Kişi 1 — Backend / RAG
- [ ] `data/kvkk.json`'ı motora bağla (yeni kod yazmadan, sadece veri
      seçimini aktif et) — bu adım motorun gerçekten regülasyon-agnostik
      olduğunu kanıtlar
- [ ] Prompt'u iyileştir, tutarsız sonuçları azalt (GDPR + KVKK
      dokümanlarında test et)
- [ ] Hata yönetimi (bozuk dosya, boş içerik, timeout)
- [ ] Genel uyum skoru (%) hesaplama mantığı
- [ ] Performans/hız kontrolü (kabul edilebilir bekleme süresi)

### Kişi 2 — Frontend
- [ ] Backend ile tam entegrasyon (mock veri kaldır)
- [ ] Regülasyon seçimini tam aktif et (GDPR + KVKK ikisi de çalışır durumda)
- [ ] Sonuç ekranını sadeleştir: seçilen regülasyon adı + skor + madde
      listesi + kanıt gösterimi
- [ ] Hata durumlarını kullanıcıya göster (yükleme başarısız vb.)
- [ ] "AI değerlendirmesi" sorumluluk reddi metnini görünür yere ekle

### Kişi 3 — İçerik + Teslim Hazırlığı
- [ ] Her iki bilgi tabanını da gözden geçir, eksik/yanlış maddeleri düzelt
- [ ] Test için 1-2 örnek Türkçe (KVKK) doküman hazırla
- [ ] Ürün fikri dokümanını tamamla (Takım İsmi, Roller, Ürün Adı,
      Açıklama, Özellikler, Hedef Kitle, "çoklu regülasyon" vizyonu — README)
- [ ] Demo senaryosu ve 3 dakikalık video için akış/senaryo metni yaz
      (hem GDPR hem KVKK örneğini gösterecek şekilde)
- [ ] Teslim formunun sorularını önceden gözden geçir, eksik bırakma

### Ekip — Ortak (son hafta)
- [ ] GitHub reposunu public yap, tüm commit geçmişi düzenli olsun
- [ ] 3 dakikalık video çek (GDPR demo + KVKK'ya hızlı geçiş), YouTube'a yükle
- [ ] Teslim formunu 2 Ağustos 23:59'dan önce, son güne bırakmadan doldur

### Sprint 3 / Final Bitiş Kriteri
`spec.md` içindeki Başarı Kriterleri karşılanıyor (her iki regülasyon da
çalışıyor), video ve form hazır, repo public ve güncel.