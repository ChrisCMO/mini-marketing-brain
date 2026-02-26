from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

from config import API_KEY
from services.query_engine import query

router = APIRouter()


class QueryRequest(BaseModel):
    message: str
    organization_slug: str = "yorcmo"


class AnalyzeContext(BaseModel):
    session_id: Optional[str] = None
    product: Optional[str] = "brain"
    folder_name: Optional[str] = None
    user_id: Optional[str] = None


class AnalyzeRequest(BaseModel):
    message: str
    context: Optional[AnalyzeContext] = None


def _check_api_key(x_api_key: str = Header(None), authorization: str = Header(None)):
    """Accept either X-API-Key header or Authorization: Bearer token."""
    if x_api_key and x_api_key == API_KEY:
        return
    if authorization:
        return  # Accept any bearer token for local dev
    raise HTTPException(status_code=401, detail="Invalid or missing API key")


@router.post("/query")
def ai_query(req: QueryRequest, x_api_key: str = Header(None), authorization: str = Header(None)):
    _check_api_key(x_api_key, authorization)
    result = query(req.message, req.organization_slug)
    session_id = f"mini-brain-session-{uuid.uuid4().hex[:8]}"
    return {
        "response": result["response"],
        "sources": result["sources"],
        "session_id": session_id,
        "confidence": result["confidence"],
        "llm_model": "mini-brain-local",
        "llm_provider": "local",
    }


@router.post("/analyze")
def ai_analyze(req: AnalyzeRequest, x_api_key: str = Header(None), authorization: str = Header(None)):
    _check_api_key(x_api_key, authorization)
    org_slug = "yorcmo"  # Default; real Brain infers from context
    if req.context and req.context.folder_name:
        org_slug = req.context.folder_name
    result = query(req.message, org_slug)
    session_id = req.context.session_id if req.context and req.context.session_id else f"mini-brain-session-{uuid.uuid4().hex[:8]}"
    return {
        "response": result["response"],
        "sources": result["sources"],
        "session_id": session_id,
        "confidence": result["confidence"],
        "llm_model": "mini-brain-local",
        "llm_provider": "local",
    }


@router.post("/analyze/stream")
def ai_analyze_stream(req: AnalyzeRequest, x_api_key: str = Header(None), authorization: str = Header(None)):
    """Real Brain uses SSE streaming. Mini version returns non-streaming."""
    _check_api_key(x_api_key, authorization)
    org_slug = "yorcmo"
    if req.context and req.context.folder_name:
        org_slug = req.context.folder_name
    result = query(req.message, org_slug)
    session_id = req.context.session_id if req.context and req.context.session_id else f"mini-brain-session-{uuid.uuid4().hex[:8]}"
    return {
        "response": result["response"],
        "sources": result["sources"],
        "session_id": session_id,
        "confidence": result["confidence"],
        "llm_model": "mini-brain-local",
        "llm_provider": "local",
    }
