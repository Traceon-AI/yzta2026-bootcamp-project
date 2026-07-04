# Plan: Uyum Ön-Değerlendirme (GDPR birincil + KVKK ikincil)

## Ekip ve Kapasite
3 kişi aktif geliştirme yapıyor. Kalan süre: Sprint 2 (6–19 Temmuz) +
Sprint 3 (20 Temmuz–2 Ağustos, teslim 2 Ağustos 23:59). Kişi başı gerçekçi
kapasite: haftada 8–12 saat → toplam ~100-130 saat. Bu nedenle mühendislik
tek bir motora odaklanır; ikinci regülasyon **yeni kod değil, yeni veri**
olarak eklenir (bkz. `constitution.md` ilke 1).

## Mimari (regülasyon-agnostik)

```
Doküman (PDF/DOCX)
   → Metin çıkarma (pypdf / python-docx)
   → Chunking (basit paragraf/cümle bölme)
   → Embedding (LLM sağlayıcı embedding API)
   → Vektör arama (in-memory / basit Chroma — ayrı sunucu kurma yok)
   → data/{gdpr|kvkk}.json seçimi (kullanıcının seçtiği regülasyona göre)
   → LLM karşılaştırma (chunk + madde → karşılanıyor mu? + kanıt)
   → Sonuç JSON (regülasyon adı dahil)
   → Frontend: yükle + regülasyon seç + sonuç tablosu
```

**Kritik tasarım kararı:** Karşılaştırma motoru (embedding, arama, LLM
prompt'u) regülasyon bilgisini parametre olarak alır; GDPR/KVKK'ya özel
`if/else` kod dalı yazılmaz. Bu, ikinci regülasyonun maliyetini "birkaç
saatlik veri hazırlığa" indirir.

## Teknoloji Seçimleri (öneri, Kişi 1 netleştirecek)
- Backend: Python (FastAPI)
- Frontend: Basit React veya düz HTML/JS
- LLM: Bir sağlayıcı API'si (embedding + chat completion) — **çok dilli
  performansı iyi olan bir model tercih edilmeli** (GDPR dokümanları
  İngilizce, KVKK dokümanları Türkçe olacağı için)
- Depolama: Dosya sistemi + JSON (veritabanı kurmaya gerek yok, MVP'de)

## Görev Dağılımı
| Kişi | Sorumluluk |
|---|---|
| Kişi 1 | Backend + regülasyon-agnostik RAG pipeline |
| Kişi 2 | Frontend (yükleme + regülasyon seçimi + sonuç tablosu) |
| Kişi 3 | GDPR ve KVKK bilgi tabanlarını hazırlama + test + GitHub/Scrum takibi |

## Sprint Eşlemesi

**Sprint 2 (6–19 Temmuz) — "Çalışan iskelet, tek regülasyonla"**
Hedef: Uçtan uca akış **sadece GDPR ile** çalışsın (doğruluk düşük olabilir,
ama boru hattı baştan sona işlesin). KVKK bu sprintte sadece veri
hazırlığı aşamasında (henüz motora bağlanmamış olabilir).

**Sprint 3 (20 Temmuz–2 Ağustos) — "İkinci regülasyon + doğruluk + cila"**
Hedef: KVKK verisini aynı motora bağlamak (motor değişmeden), sonuç
kalitesini artırmak, arayüzde regülasyon seçimini görünür kılmak, video +
teslim hazırlığı.

## Riskler
- **Motor regülasyona özel kod içerirse** (örn. GDPR için ayrı fonksiyon,
  KVKK için ayrı fonksiyon) → Sprint 3'te KVKK ekleme maliyeti öngörülenden
  yüksek olur. Kişi 1, Sprint 2'de bu ayrımı netleştirmeli.
- **Çok dillilik**: GDPR (İngilizce) ve KVKK (Türkçe) dokümanlarının aynı
  embedding modeliyle iyi çalışıp çalışmadığı erken test edilmeli.
- **LLM tutarsızlığı**: Aynı dokümana farklı sonuçlar verebilir → prompt'u
  sabitleyip birkaç örnek üzerinde test edin (Sprint 2 sonu).
- **Kapsam kayması**: Üçüncü regülasyon fikri çıkarsa `constitution.md`
  ilke 5'e bakın — v2 backlog'a yazılır, eklenmez.

## Devam eden dosyalar
Bu plan `tasks.md` ile detaylandırılmıştır.