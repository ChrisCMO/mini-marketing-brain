from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import json
import uuid
from datetime import datetime

from config import SESSIONS_DIR

router = APIRouter()


class CreateSessionRequest(BaseModel):
    title: Optional[str] = "Untitled Session"


@router.get("/chat-sessions")
def list_sessions():
    sessions = []
    for f in SESSIONS_DIR.glob("*.json"):
        with open(f) as fh:
            sessions.append(json.load(fh))
    return {"sessions": sessions}


@router.post("/chat-sessions")
def create_session(req: CreateSessionRequest):
    session_id = str(uuid.uuid4())
    session = {
        "id": session_id,
        "title": req.title,
        "created_at": datetime.utcnow().isoformat(),
        "messages": [],
    }
    with open(SESSIONS_DIR / f"{session_id}.json", "w") as f:
        json.dump(session, f, indent=2)
    return session


@router.get("/chat-messages/{session_id}")
def get_messages(session_id: str):
    path = SESSIONS_DIR / f"{session_id}.json"
    if not path.exists():
        return {"messages": []}
    with open(path) as f:
        session = json.load(f)
    return {"messages": session.get("messages", [])}
