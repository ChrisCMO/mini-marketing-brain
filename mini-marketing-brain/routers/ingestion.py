from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
import uuid

from config import DOCUMENTS_DIR
from services.ingestion import ingest_file, ingest_text

router = APIRouter()


class IngestRequest(BaseModel):
    text: str
    title: str = "Untitled"
    organization_slug: str = "yorcmo"
    metadata: dict = {}


@router.post("/upload-file")
async def upload_file(
    file: UploadFile = File(...),
    organization_slug: str = Form("yorcmo"),
    title: str = Form(None),
):
    doc_id = str(uuid.uuid4())
    file_title = title or file.filename
    file_path = DOCUMENTS_DIR / f"{doc_id}_{file.filename}"

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    entries_created = ingest_file(str(file_path), organization_slug, file_title, doc_id)

    return {
        "document_id": doc_id,
        "filename": file.filename,
        "title": file_title,
        "entries_created": entries_created,
        "status": "completed",
    }


@router.post("/ingest")
def ingest(req: IngestRequest):
    doc_id = str(uuid.uuid4())
    entries_created = ingest_text(req.text, req.organization_slug, req.title, doc_id)
    return {
        "document_id": doc_id,
        "title": req.title,
        "entries_created": entries_created,
        "status": "completed",
    }


@router.get("/status")
def ingestion_status():
    return {"jobs": []}
