from fastapi import FastAPI
from routers import health, auth, ai, chat, ingestion, documents

app = FastAPI(title="Mini Marketing Brain", version="0.1.0")

app.include_router(health.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(ai.router, prefix="/ai")
app.include_router(chat.router, prefix="/ai")
app.include_router(ingestion.router, prefix="/ingestion")
app.include_router(documents.router, prefix="/documents")

if __name__ == "__main__":
    import uvicorn
    from config import PORT
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
