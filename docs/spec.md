# Spec: Uyum Ön-Değerlendirme (GDPR birincil + KVKK ikincil)

## Kullanıcı Senaryosu
Bir kullanıcı, şirketine ait bir dokümanı (örn. Gizlilik Politikası/Privacy
Policy) sisteme yükler ve **hangi regülasyona göre değerlendirilmek
istediğini seçer (GDPR veya KVKK)**. Sistem dokümanı analiz eder, seçilen
regülasyonun temel yükümlülük maddeleriyle karşılaştırır, hangi maddelerin
karşılandığını/karşılanmadığını gösterir ve her sonucu dokümandaki ilgili
cümleye/sayfaya dayandırır.

## Fonksiyonel Gereksinimler

- **FR-001**: Kullanıcı tek bir PDF veya DOCX dosyası yükleyebilmeli.
- **FR-002**: Kullanıcı yüklemeden önce veya sonra **regülasyon seçebilmeli**
  (GDPR / KVKK — iki seçenekli basit bir seçim, dropdown veya kart).
- **FR-003**: Sistem dokümanı metne çevirip anlamlı parçalara (chunk)
  bölmeli.
- **FR-004**: Sistem, seçilen regülasyonun yükümlülük listesindeki
  (`data/gdpr.json` veya `data/kvkk.json`) her madde için dokümanda karşılık
  arayıp bulmalı (RAG / benzerlik araması). **Motor tek, sadece okunan veri
  dosyası değişir.**
- **FR-005**: Her yükümlülük için sonuç şu üç durumdan biri olmalı:
  **Karşılanıyor / Kısmen Karşılanıyor / Karşılanmıyor**.
- **FR-006**: "Karşılanıyor" veya "Kısmen" sonuçlarında, dokümandan alınan
  destekleyici metin parçası (kanıt) gösterilmeli.
- **FR-007**: Sonuç ekranında genel bir uyum skoru (%) ve madde bazlı liste
  gösterilmeli; seçilen regülasyonun adı ekranda net görünmeli.
- **FR-008**: Her eksik madde için kısa, genel bir öneri metni gösterilmeli
  (madde bazlı statik açıklama + LLM'in dokümana özel kısa yorumu).
- **FR-009**: Sistem sonuçları "kesin denetim sonucu" değil, **"AI
  değerlendirmesi"** olarak etiketlemeli (sorumluluk reddi metni).

## Regülasyon Verisi Gereksinimleri
- **GDPR**: En az 12-15 temel yükümlülük (örn. Madde 5 - veri işleme
  ilkeleri, Madde 6 - hukuki dayanak, Madde 13/14 - bilgilendirme yükümü,
  Madde 17 - unutulma hakkı, Madde 32 - güvenlik önlemleri, Madde 33/34 -
  ihlal bildirimi). Kaynak: EUR-Lex (ücretsiz, resmi).
- **KVKK**: En az 10-12 temel yükümlülük (örn. aydınlatma yükümlülüğü, açık
  rıza, veri işleme şartları, veri güvenliği tedbirleri). Kaynak: Resmi
  Gazete (ücretsiz, resmi).
- İki liste de aynı JSON şemasını kullanmalı (madde no, başlık, açıklama,
  öneri metni) — motorun regülasyon-agnostik kalması için şart.

## Kapsam Dışı (Non-Goals)
- Üçüncü bir regülasyon (NIST AI, HIPAA, ISO vb.) — v2 backlog
- Aynı anda iki regülasyona göre karşılaştırma
- Çoklu doküman karşılaştırma
- Kullanıcı girişi/yetkilendirme (v1'de opsiyonel, zaman kalırsa eklenir)
- Rapor dışa aktarma (PDF çıktısı) — zaman kalırsa "nice to have"

## Başarı Kriterleri
- Bir kullanıcı, doküman yükleyip regülasyon seçerek sonucu görene kadar
  tüm akışı **tek oturumda, hatasız** tamamlayabiliyor.
- GDPR için en az 12, KVKK için en az 10 yükümlülük değerlendiriliyor.
- Her sonucun kaynağı (hangi cümle/sayfa) görülebiliyor — "kara kutu" değil.
- Aynı motor, sadece veri dosyası değiştirilerek iki regülasyonda da
  çalışıyor (kod tekrarı yok).

## Açık Sorular
- [ ] Kanıt gösterimi sayfa numarası mı, alıntı cümle mi olacak? (Öneri:
  ikisi birden — daha güçlü izlenim bırakır)
- [ ] LLM sağlayıcısı hangisi olacak? (Maliyet/hız/çok dilli performansa
  göre Kişi 1 karar verecek, Sprint 2 başında)
- [ ] GDPR maddeleri İngilizce dokümanları, KVKK maddeleri Türkçe
  dokümanları mı bekleyecek, yoksa her ikisi de iki dilde doküman kabul mü
  edecek? (Öneri: v1'de GDPR→İngilizce doküman, KVKK→Türkçe doküman
  varsayımıyla başlayın, çapraz dil desteğini v2'ye bırakın.)