# Proje Anayasası — Uyum Copilot (GDPR + KVKK)

## Neden bu belge var?
Ekip 3 kişi, süre ~4 hafta (2 sprint), sıfırdan başlıyoruz. Bu belge, kapsam
tartışmalarında "buna zamanımız var mı?" sorusuna hızlı cevap vermek için var.
Her yeni özellik fikri önce bu ilkelerden geçmeli.

## İlkeler

**1. Tek senaryo, uçtan uca çalışsın; regülasyon sadece bir "veri seçimi"dir.**
Yarım çalışan 5 özellik yerine, tam çalışan 1 akış tercih edilir.
Akış: *kullanıcı 1 doküman yükler → bir regülasyon seçer (GDPR veya KVKK)
→ sistem ilgili maddelerle karşılaştırır → eksik/karşılanan listesi + kaynak
gösterir.* Motor tek, regülasyonlar sadece farklı veri dosyalarıdır — ikinci
regülasyon eklemek yeni kod değil, yeni JSON demektir.

**2. GDPR birincil (derinlemesine test edilir), KVKK ikincil (aynı motor
üzerinde çalışır).**
Geliştirme ve test önceliği GDPR'da. KVKK, GDPR motoru olgunlaştıktan sonra
aynı pipeline'a veri olarak eklenir.

**3. Telifli/lisanslı kaynak kullanılmaz.**
Satın alınan içerik, izinsiz veri seti — hiçbiri sisteme girmez. Bilgi
tabanları GDPR (EUR-Lex, ücretsiz) ve KVKK (Resmi Gazete, ücretsiz) temelli
ve ekip tarafından elle derlenir.

**4. Hazır proje / dışarıdan satın alma yasak.**
LLM API'si (embedding + completion) ve açık kaynak kütüphaneler serbest.
Bitmiş bir SaaS ürünü entegre etmek veya kod satın almak diskalifiye sebebidir.

**5. Kapsam sadece daralır, genişlemez.**
Sprint ortasında yeni özellik veya üçüncü bir regülasyon önerisi gelirse,
önce "v2 backlog"a yazılır, mevcut sprint'e eklenmez.

**6. Her sprint sonunda GitHub'da kanıt olur.**
Commit, README güncellemesi, sprint board ekran görüntüsü — boş sprint yok.

**7. Roller eşit sorumluluk taşır, hepsi kod/içerik üretir.**
Product Owner ve Scrum Master da geliştirmeye dahildir; sadece süreç
yönetmezler.

## Kapsam Dışı (v1 için kesin hayır)
- GDPR/KVKK dışında üçüncü bir regülasyon (NIST AI, HIPAA, ISO vb. — v2 backlog)
- Çoklu doküman aynı anda karşılaştırma
- Kullanıcı hesap yönetimi, çoklu şirket desteği
- Otomatik politika/metin üretimi
- Üçüncü parti entegrasyon (Slack, e-posta vb.)