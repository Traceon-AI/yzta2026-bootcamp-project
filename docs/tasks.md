# Tasks: Uyum Ön-Değerlendirme (GDPR birincil + KVKK ikincil)

Kutucuklar GitHub'da işaretlenerek ilerleme takibi yapılabilir (`- [x]`).

> **Not (Sprint 1 kapanışı):** Ekibin yoğun eforuyla, Sprint 2'de planlanan
> bazı görevler (backend iskeleti, GDPR/KVKK veri dosyaları) Sprint 1
> içinde erken tamamlandı. Bunlar `[x]` olarak işaretlidir.
> Detay: `docs/sprint-1-review.md`

## Sprint 1 (19 Haziran–5 Temmuz) — Fikir, Kapsam, Altyapı ✅ TAMAMLANDI

### Planlama ve Kapsam
- [x] Proje fikri netleştirildi: ISO 27001 değerlendirildi, telif riski
      nedeniyle GDPR + KVKK ikili kapsamına geçildi
- [x] Kapsam daraltma kararı: tek doküman + tek regülasyon seçimi + gap
      analizi akışı MVP olarak belirlendi
- [x] Regülasyon-agnostik mimari kararı: tek motor, regülasyonlar sadece
      veri dosyası olarak değişiyor

### Dokümantasyon (Spec-Kit)
- [x] Proje anayasası (`docs/constitution.md`)
- [x] Özellik spesifikasyonu (`docs/spec.md`) — FR-001–FR-009
- [x] Teknik plan (`docs/plan.md`)
- [x] Görev listesi (`docs/tasks.md`)
- [x] API sözleşmesi (`docs/api-contract.md`)

### Altyapı
- [x] GitHub organizasyonu ve repo kuruldu (Traceon-AI /
      yzta2026-bootcamp-project)
- [x] Sprint board (GitHub Projects) kuruldu, Sprint 1-2-3 milestone'ları
      tanımlandı
- [x] README hazırlandı (takım ismi, roller, ürün açıklaması, hedef kitle)

### Erken Tamamlanan Geliştirme Çıktıları (Sprint 2'den öne çekildi)
- [x] Backend iskeleti: `main.py` — `api-contract.md`'ye uygun mock API
      (`GET /regulations`, `POST /analyze`) — Eylül Zengin
- [x] GDPR bilgi tabanı: `data/gdpr.json`, 15 madde (hedef 12-15 aşıldı)
      — Efnan Demircan
- [x] KVKK bilgi tabanı: `data/kvkk.json`, 12 madde (hedef 10-12
      karşılandı) — Efnan Demircan

### Sprint 1 Kapanış Kanıtları
- [x] Sprint Review (`docs/sprint-1-review.md`)
- [x] Sprint Retrospective (`docs/sprint-1-retrospective.md`)
- [x] Ürün Durumu (`docs/sprint-1-product-status.md`)
- [x] Ekran görüntüleri: Backend Swagger `/docs` (Hazırlayan: Eylül),
      Frontend (upload +
      analiz + sonuç ekranları) (Hazırlayan: Önder)
- [x] Daily Scrum kanıtları `docs/sprint-1-daily-scrum.md`

---

## Sprint 2 (6–19 Temmuz) — Çalışan İskelet (GDPR ile)

### Eylül Zengin — Backend / RAG
*(Repo iskeleti + mock API Sprint 1'de erken tamamlandı — bkz. Sprint 1 bölümü)*
- [ ] Doküman yükleme endpoint'ini gerçek işleme bağla (dosya al, metne çevir —
      PDF: pypdf, DOCX: python-docx)
- [ ] Chunking fonksiyonu (paragraf bazlı, basit)
- [ ] Embedding entegrasyonu (çok dilli performansı iyi bir model seç)
- [ ] Embedding sonrası hızlı çapraz dil testi: 1 Türkçe metin ↔ İngilizce
      GDPR maddesi eşleşiyor mu? (5 dk'lık sağlamlık kontrolü)
- [ ] In-memory benzerlik araması (chunk ↔ regülasyon maddesi eşleştirme) —
      **regülasyon parametre olarak alınmalı, hardcode edilmemeli**
- [ ] LLM'e "bu chunk bu maddeyi karşılıyor mu?" prompt'u + JSON çıktı formatı
- [ ] `/regulations` madde sayılarını statikten dinamiğe çevir (bkz. ilgili issue)
- [ ] Uçtan uca test: 1 örnek GDPR dokümanıyla pipeline'ı çalıştır

### Abdullah Önder Aksu — Frontend (+ Scrum Master)
- [x] API sözleşmesi hazır (`docs/api-contract.md`) — mock veri şemaya uygun geliştirildi
- [x] Dosya yükleme ekranı (drag-drop veya basit input)
- [x] Regülasyon seçim bileşeni (GDPR / KVKK — şimdilik sadece GDPR aktif,
      KVKK "yakında" olarak görünebilir)
- [x] Yükleniyor/işleniyor durumu (spinner, basit)
- [x] Sonuç tablosu iskeleti (madde adı, durum, kanıt alanı) — backend
      hazır olmadan sözleşmedeki örnek JSON'la (mock) çalış
- [ ] (SM) Daily Scrum notlarının `docs/sprint-2-daily-scrum.md` altına işlenmesini takip et

### Efnan Demircan — Bilgi Tabanı & Test
*(GDPR bilgi tabanı Sprint 1'de erken tamamlandı — bkz. Sprint 1 bölümü)*
- [x] Test için 1-2 örnek İngilizce doküman hazırla (kurgusal/anonim
      Privacy Policy) — **Eylül'ün pipeline testi için hazır**
- [ ] GDPR maddelerini entegrasyon sırasında gözden geçir (Eylül'den geri
      bildirim gelirse hızlı düzeltme)

### Ezgi Yıldırım — Bilgi Tabanı & Test
- [ ] GitHub collaborator davetini kabul et
- [ ] Test için örnek Türkçe (KVKK) doküman hazırla (kurgusal Aydınlatma
      Metni) — Sprint 3 KVKK entegrasyonuna hazırlık
- [ ] Müsaitlik durumuna göre ek görev alımı (Sprint 2 ortasında netleşecek)

### Ortak (Sprint 2 sonu)
- [ ] Daily Scrum notları ve sprint board güncellemeleri GitHub'a
      işlenecek (kanıt için)

### Sprint 2 Bitiş Kriteri (Definition of Done)
Bir kullanıcı örnek bir GDPR dokümanı yükleyip en az birkaç madde için
karşılanıyor/karşılanmıyor sonucu ve kanıt metni görebiliyor. KVKK verisi
hazır ama henüz arayüzde aktif değil olabilir.

---

## Sprint 3 (20 Temmuz–2 Ağustos) — KVKK Entegrasyonu + Doğruluk + Cila

### Eylül Zengin — Backend / RAG
- [ ] `data/kvkk.json`'ı motora bağla (yeni kod yazmadan, sadece veri
      seçimini aktif et) — bu adım motorun gerçekten regülasyon-agnostik
      olduğunu kanıtlar
- [ ] Prompt'u iyileştir, tutarsız sonuçları azalt (GDPR + KVKK
      dokümanlarında test et)
- [ ] Hata yönetimi (bozuk dosya, boş içerik, timeout)
- [ ] Genel uyum skoru (%) hesaplama mantığı
- [ ] Performans/hız kontrolü (kabul edilebilir bekleme süresi)

### Abdullah Önder Aksu — Frontend
- [ ] Backend ile tam entegrasyon (mock veri kaldır)
- [ ] Regülasyon seçimini tam aktif et (GDPR + KVKK ikisi de çalışır durumda)
- [ ] Sonuç ekranını sadeleştir: seçilen regülasyon adı + skor + madde
      listesi + kanıt gösterimi
- [ ] Hata durumlarını kullanıcıya göster (yükleme başarısız vb.)
- [ ] "AI değerlendirmesi" sorumluluk reddi metnini görünür yere ekle

### Efnan Demircan & Ezgi Yıldırım — İçerik + Test
- [ ] Her iki bilgi tabanını da gözden geçir, eksik/yanlış maddeleri düzelt
- [ ] KVKK test dokümanlarını finalize et
- [ ] Uçtan uca kullanıcı testi: her iki regülasyonla gerçek akışı dene,
      bulguları raporla

### Ahmet Faruk Bilgin — PO + Teslim Hazırlığı
- [ ] Ürün fikri dokümanını tamamla (README son kontrol — "çoklu
      regülasyon" vizyonu dahil)
- [ ] Demo senaryosu ve 3 dakikalık video için akış/senaryo metni yaz
      (hem GDPR hem KVKK örneğini gösterecek şekilde)
- [ ] Teslim formunun sorularını önceden gözden geçir, eksik bırakma
- [ ] Sonuçların `spec.md` Başarı Kriterleri'ne uygunluğunu doğrula

### Ekip — Ortak (son hafta)
- [ ] GitHub reposunu public yap, tüm commit geçmişi düzenli olsun
- [ ] 3 dakikalık video çek (GDPR demo + KVKK'ya hızlı geçiş), YouTube'a yükle
- [ ] Teslim formunu 2 Ağustos 23:59'dan önce, son güne bırakmadan doldur

### Sprint 3 / Final Bitiş Kriteri
`spec.md` içindeki Başarı Kriterleri karşılanıyor (her iki regülasyon da
çalışıyor), video ve form hazır, repo public ve güncel.
