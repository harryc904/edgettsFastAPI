from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Edge TTS API",
    description="Edge TTS (Text-to-Speech) API using Microsoft's Edge TTS service",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Edge TTS API",
        "description": "Edge TTS (Text-to-Speech) API using Microsoft's Edge TTS service",
        "docs": "/api/v1/docs",
        "version": "1.0.0",
        "endpoints": {
            "/api/v1/tts/voices": "Get all available TTS voices",
            "/api/v1/tts/voices/search": "Search TTS voices by filters",
            "/api/v1/tts/synthesize": "Convert text to speech (returns metadata)",
            "/api/v1/tts/synthesize/stream": "Convert text to speech (returns audio stream)",
        },
    }
