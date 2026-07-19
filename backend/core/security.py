from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """
    Frontend arayüzünün backend API ile güvenli ve sorunsuz 
    bir şekilde haberleşmesini sağlayan CORS ayarları.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Geliştirme aşamasında tüm originlere izin veriyoruz
        allow_credentials=True,
        allow_methods=["*"],  # GET, POST gibi tüm metotlar aktif
        allow_headers=["*"],  # Tüm header tiplerine izin verili
    )