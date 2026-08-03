# Sprint 3 - Product Status

Bu dokuman, iki kaynagi birlikte baz alir:
- Board'daki resmi durum (son paylasilan liste)
- Repo icindeki gercek teknik ciktilar

## 1) Board Snapshot (Resmi Durum)

- Done: 18
- Review: 4
- In Progress: 2
- Todo: 16
- Product Backlog: 10

## 2) Repo Referansli Teknik Durum

Asagidaki kalemler kodda gorunen kanitlara gore teknik olarak uygulanmis gorunuyor:

- Dokuman metne cevirme: `backend/services/document.py` icinde PDF/DOCX parse akisi var (`extract_chunks`).
- Chunking: ayni dosyada paragraf bazli bolme uygulanmis.
- `/regulations` dinamik madde sayisi: `backend/main.py` icinde JSON'dan hesaplanarak donuyor.
- KVKK/GDPR secimi: `backend/main.py` icinde `regulation` form parametresi ile veri dosyasi yukleniyor.
- Frontend backend baglantisi: `frontend/src/App.tsx` icinde `/analyze` istegi atiliyor.
- Regulator secimi aktif: `frontend/src/App.tsx` icinde GDPR/KVKK secim butonlari aktif.
- Hata gosterimi: `frontend/src/App.tsx` icinde `setError(...)` ve upload/analyze hata mesajlari mevcut.
- README setup/smoke adimlari: kok `README.md` icinde backend/frontend `.env` ve smoke test adimlari var.

## 3) Board Senkronizasyon Onerisi (Net)

Board güncel olmayabilir denildigi icin, asagidaki kalemler board'da tekrar degerlendirilmeli:

### Review -> Done alinabilir (repo kaniti var)

- #16 Dokuman metne cevirme
- #17 Chunking
- #20 GDPR veri dosyasi baglantisi
- #49 `/regulations` madde sayilarini veri dosyasindan dinamik cekme

### In Progress kalmali (tam kanit yok / kismi)

- #18 Embedding entegrasyonu: repo icinde vektor/embedding pipeline acik ve net gorunmuyor.
- #19 Benzerlik aramasi + LLM karsilastirma: su anki akista dogrudan model analizi + fallback var, klasik benzerlik katmani net degil.

### Todo'dan Done'a alinmasi degerlendirilebilir (repo kaniti var)

- #28 Hata yonetimi
- #33 Sonuc ekranini sadelestirme
- #34 Hata durumlarini kullaniciya gosterme
- #51 Frontend'i mock backend'e baglama

### Todo/Product Backlog'da kalmali (dis bagimli veya net kanit yok)

- #35 Sorumluluk reddi metni ekleme (UI'da acik metin olarak gorunur degil)
- #39 Demo senaryosu yazma (dokuman kaniti lazim)
- #40/#43 Teslim formu kalemleri (operasyonel)
- #42 Video cekme ve YouTube yukleme (operasyonel)
- #50 Logo/gorsel kimlik (tasarim ciktilari lazim)
- #52 Docker Compose tek komut kurulum (dosya/kanit lazim)
- #53 Canliya alma (deploy kaniti lazim)

## 4) Sonuc

Sprint 3 teknik cekirdegi buyuk olcude ilerlemis durumda. Board ile repo arasinda status farki oldugu icin, board bir kez repo kanitlariyla senkronlanirsa kapanis resmi daha dogru gorunecek.
