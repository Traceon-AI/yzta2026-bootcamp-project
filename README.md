# Traceon-AI

Traceon-AI, şirket dokümanlarını (gizlilik politikası, aydınlatma metni vb.) GDPR veya KVKK maddelerine göre ön-uyum açısından analiz eden bir AI destekli RAG aracıdır.

## Takım
- Takım No: 21
- Takım İsmi: Namüsaitler
- Ahmet Faruk Bilgin — Product Owner
- Abdullah Önder Aksu — Scrum Master, Frontend
- Eylül Zengin — Developer (Backend)
- Efnan Demircan — Developer (Bilgi Tabanı & Test)
- Ezgi Yıldırım — Developer (Bilgi Tabanı & Test)

## Özellikler
- Regülasyon-agnostik analiz motoru (GDPR/KVKK için tek akış)
- PDF ve DOCX doküman yükleme
- Madde bazlı analiz sonucu: `met` / `partial` / `missing`
- Madde bazlı kanıt metni ve konum bilgisi
- Genel uyum skoru (0-100)
- AI çağrısı başarısız olduğunda fallback analizi ile kesintisiz cevap

## Teknoloji Yığını
- Backend: FastAPI
- Frontend: React + Vite + TypeScript
- AI: Gemini REST API

## Proje Yapısı
```text
backend/
  main.py
  core/
  services/
frontend/
  src/
data/
  gdpr.json
  kvkk.json
docs/
```

## Gereksinimler
- Python 3.11+ (önerilir)
- Node.js 18+
- npm 9+

## 1) Backend Kurulumu

### A. Ortam dosyası
`backend/.env.example` dosyasını `backend/.env` olarak kopyalayın ve doldurun.

Zorunlu alan:
```env
GEMINI_API_KEY=your_api_key_here
```

Opsiyonel ayarlar (önerilen):
```env
LLM_MODEL=gemini-flash-lite-latest
LLM_TIMEOUT_SECONDS=60
LLM_MAX_RETRIES=4
LLM_BACKOFF_BASE_SECONDS=2
LLM_MAX_DOC_CHUNKS=40
LLM_MAX_CHARS_PER_CHUNK=800
```

### B. Bağımlılıklar
Windows PowerShell:
```powershell
cd backend
python -m venv venv_yzta_backend
.\venv_yzta_backend\Scripts\Activate.ps1
pip install -r requirements.txt
```

### C. Backend'i çalıştırma
```powershell
cd backend
.\venv_yzta_backend\Scripts\Activate.ps1
python -m uvicorn main:app --reload --port 8000
```

Backend adresleri:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## 2) Frontend Kurulumu

### A. Ortam dosyası
`frontend/.env.example` dosyasını `frontend/.env` olarak kopyalayın.

```env
VITE_API_URL=http://127.0.0.1:8000
```

Not: Frontend kodunda fallback vardır. `VITE_API_URL` yoksa `http://localhost:8000` kullanılır.

### B. Bağımlılıklar ve çalıştırma
```powershell
cd frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

Frontend adresi:
- UI: http://127.0.0.1:5173

## 3) Hızlı Doğrulama (Smoke Test)

1. Backend açık olsun (`8000`).
2. Frontend açık olsun (`5173`).
3. UI'dan bir DOCX/PDF dosyası yükleyin.
4. Regülasyon seçin (`GDPR` veya `KVKK`).
5. Analyze butonuna basın.

Beklenen:
- Sonuç ekranında `overall_score`
- Madde listesinde `status`, `evidence`, `evidence_location`, `recommendation`

## Test Dosyaları
- Örnek test dokümanlarını `docs/test-files/` klasöründe tutabilirsiniz.
- Bu klasöre zamanla yeni GDPR/KVKK test dosyaları eklenebilir.

## API Sözleşmesi
- Detay: [docs/api-contract.md](./docs/api-contract.md)

## Sprint Dokümantasyonu
- Genel görev listesi: [docs/tasks.md](./docs/tasks.md)
- Sprint dokümanları: `docs/sprint-*` klasörleri altında tutulur (ör. `docs/sprint-1`, `docs/sprint-2`, `docs/sprint-3`).
- Sprint kanıtları ve ek çıktılar ilgili sprint klasörü veya `docs/` altındaki uygun dizinlerde konumlandırılabilir.

## Sık Karşılaşılan Sorunlar

### 1) Frontend backend'e bağlanmıyor
- `frontend/.env` içindeki `VITE_API_URL` doğru mu kontrol edin.
- Backend gerçekten `8000` portunda açık mı kontrol edin.

### 2) AI yerine fallback çalışıyor
- `backend/.env` içinde `GEMINI_API_KEY` var mı kontrol edin.
- Loglarda `429` varsa rate limit nedeniyle fallback devrededir.
- `LLM_MODEL=gemini-flash-lite-latest` genelde daha stabil çalışır.

### 3) `npm run dev` açılıp kapanıyor
- Yanlış terminal girdisi gönderilmiş olabilir.
- Komutu tekrar temiz bir terminalde çalıştırın.

## Product Backlog
- https://github.com/orgs/Traceon-AI/projects/1
