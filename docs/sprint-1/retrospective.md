# Sprint 1 Retrospective

## İyi giden
- Kapsam kararı net ve gerekçeli şekilde alındı (telif riski, pazar
  genişliği, regülasyon-agnostik mimari).
- Dokümantasyon (constitution/spec/plan/tasks/api-contract) süreç
  boyunca referans olarak kullanıldı ve gerçekten işe yaradı — Backend,
  Frontend ve Bilgi Tabanı çıktıları, sözleşmeye birebir uyacak şekilde
  üretildi.
- Ekip geç entegre olmasına rağmen, planlamanın ötesine geçilip somut
  ilk çıktılar üretildi: çalışan mock API, mock veriyle uçtan uca
  çalışan bir arayüz ve iki regülasyonun veri dosyaları. Sprint 1
  hedefi yalnızca planlamayken, fiilen Sprint 2 kapsamındaki işlerin
  önemli bir kısmı erken tamamlandı.
- API sözleşmesi (contract-first) yaklaşımı işe yaradı: Frontend,
  backend'i beklemeden mock veriyle geliştirildi ve iki taraf birbirini
  bloklamadan paralel ilerledi.

## İyi gitmeyen
- Ekip rolleri/isimleri ve görev dağılımı geç netleşti.
- Fikir değişikliği (ISO → GDPR+KVKK) sprint içinde zaman aldı.
- Roller planlama sürecinin sonlarında bir kez daha güncellendi (PO ve
  Scrum Master rolleri yer değiştirdi, Frontend sorumluluğu netleşti) —
  bu, dokümanların (README vb.) senkron tutulmasını zorlaştırdı.
- Ekip üyelerinin müsaitlik durumları sprint başında netleşmediği için
  görev dağılımı ancak sprint sonuna doğru oturabildi.

## Ekip Katılımı
Sprint 1'de tüm ekip üyeleri farklı yoğunluklarda katkı sağladı:

- **Abdullah Önder Aksu** — Fikir/governance kararının şekillenmesinde
  aktif rol aldı; Scrum Master rolünü üstlendi ve Frontend'i mock
  veriyle uçtan uca çalışır hale getirdi.
- **Ahmet Faruk Bilgin** — Spec-Kit metodolojisini kurdu, tüm
  dokümantasyonu hazırladı ve Product Owner olarak süreç koordinasyonunu
  yürüttü.
- **Eylül Zengin** — Backend iskeletini (`backend/main.py`) API
  sözleşmesine birebir uygun şekilde geliştirdi ve çalışır halde teslim
  etti.
- **Efnan Demircan** — Hem GDPR (15 madde) hem KVKK (12 madde) bilgi
  tabanlarını hedeflenen kapsamı karşılayacak/aşacak şekilde hazırladı —
  Sprint 1'in en kapsamlı içerik üretimi.
- **Ezgi Yıldırım** — Bu sprint'teki katılımı kişisel müsaitlik durumu
  nedeniyle sınırlı kaldı; kendisi Sprint 2'de daha aktif olacağını
  belirtti ve görev planlaması buna göre yapıldı.

## Sprint 2'de değişecek
- Roller kesinleşti, geliştirmeye kesintisiz devam edilecek.
- Öncelik, erken üretilen parçaların gerçek entegrasyonuna kayıyor:
  Backend'in mock cevaptan gerçek RAG pipeline'a geçmesi (chunking,
  embedding, LLM karşılaştırma) ve Frontend'in gerçek API'ye bağlanması.
- Sprint ortasında (12-13 Temmuz civarı) bir ara entegrasyon testi
  yapılacak — parçaların gerçekten birlikte çalıştığı erken doğrulanacak.
- Ekip üyelerinin müsaitlik durumları sprint başında netleştirilecek,
  görev dağılımı buna göre erken oturtulacak.
- Kapsam sabit, artık değişmeyecek (`constitution.md` ilke 5).
