import os
from pathlib import Path

# Base directory (repo root)
BASE_DIR = Path(__file__).parent

# Data directories
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_DIR = DATA_DIR / "knowledge"
DOCUMENTS_DIR = DATA_DIR / "documents"
SESSIONS_DIR = DATA_DIR / "sessions"

# Create dirs on import
for d in [KNOWLEDGE_DIR, DOCUMENTS_DIR, SESSIONS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Server
PORT = int(os.environ.get("PORT", "8001"))

# Auth — hardcoded for local dev, matches real Brain's test key
API_KEY = os.environ.get("API_KEY", "askfanny_test_key_local")

# Optional: OpenAI for LLM synthesis in query engine
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
