# Sprint 2 Retrospective

## İyi giden
- Backend, sprint kapanışında sözleşmeye birebir uyan, modüler ve
  çalışır bir yapıyla teslim edildi — doküman işleme, chunking ve
  dinamik veri okuma gerçek anlamda tamamlandı.
- Rate limit engeli karşısında sistemin tamamen çökmesi yerine anahtar
  kelime tabanlı bir fallback motoru kuruldu — dayanıklılık açısından
  doğru refleks (ancak bkz. iyi gitmeyen: bunun ana yol olmaması gerek).
- Sprint sonunda "ürün ilerlemiyor" tespiti ekip içinde açıkça dile
  getirildi (SM) ve savunma yerine somut yeniden planlamayla karşılandı.
- Yeniden planlama gerçekçi oldu: görevler fiili müsaitlik pencerelerine
  göre dağıtıldı, kartlara hedef tarihler eklendi, kritik yol netleşti.
- Repo hijyeni sağlandı: branch temizliği, isimlendirme standardı;
  API anahtarı koddan çıkarılıp .env mimarisine taşındı (GitHub Push
  Protection ile uyumlu, .gitignore'da).

## İyi gitmeyen
- **İş sprint boyunca görünmezdi:** Backend çalışması ancak sprint
  kapanışında push'landı. Ara push olmadığı için ekip iki hafta boyunca
  gerçek durumu okuyamadı, planlama "hiç ilerleme yok" varsayımıyla
  yapıldı ve sprint sonunda iki kez revize edilmek zorunda kaldı.
- Sprint 1 retrosunda verilen sözler tutulamadı: müsaitlikler sprint
  başında netleşmedi, 12-13 Temmuz entegrasyon testi yapılamadı.
- Daily Scrum kayıtları düzenli tutulamadı; iletişim sprint sonunda
  yoğunlaştı.
- LLM analizi, madde başına ayrı istek atan tasarım nedeniyle rate
  limit'e takıldı ve devre dışı bırakıldı — mimari karar (batch çağrı)
  baştan konuşulsaydı bu kayıp yaşanmayabilirdi.

## Ekip Katılımı
- **Eylül Zengin** — Sprint'in en kapsamlı teknik çıktısını üretti:
  doküman işleme motoru, modüler mimari, dinamik veri okuma ve detaylı
  bir teknik devir dokümanı. Gelişim alanı: işin ara push'larla görünür
  kılınması.
- **Ahmet Faruk Bilgin** — Sprint 1 kapanışını tamamladı, repo yapısını
  düzenledi, yeniden planlamayı yürüttü ve backend'in AI katmanını
  (embedding + batch LLM) devralma kararı aldı.
- **Abdullah Önder Aksu** — Ürünün ilerlemediğini açıkça gündeme
  getirerek yeniden planlamayı tetikledi; kendisine backend'i beklemeyen
  6 görev tanımlandı.
- **Efnan Demircan** — 24 Temmuz'a kadar olan müsaitlik penceresini
  bildirdi ve entegrasyon + Docker görevlerini üstlendi.
- **Ezgi Yıldırım** — Sprint sonunda iletişim kuruldu; Salı (21 Temmuz)
  itibarıyla müsaitliğini bildirdi, test ve gözden geçirme görevlerini
  üstlendi.

## Sprint 3'te değişecek
- **"Push'lanmamış iş yok hükmündedir":** ilerleme beyanla değil küçük
  ve sık PR'larla takip edilecek — bu sprint'in ana dersi.
- LLM analizi ana yol olacak: embedding ön-filtreleme + tek batch çağrı
  (rate limit çözümü); keyword motoru yalnızca fallback olarak kalacak.
- Kartlar hedef tarihlerle (target date) takip edilecek; kritik
  kilometre taşları: 24 Temmuz ilk gerçek AI sonucu, 26 Temmuz tam
  entegrasyon, 29 Temmuz demo hazır, 1 Ağustos teslim tamam.
- Son gün (2 Ağustos) tampon: yeni iş planlanmayacak.