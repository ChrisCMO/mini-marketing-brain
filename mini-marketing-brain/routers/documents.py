from fastapi import APIRouter, HTTPException

from services.storage import list_knowledge_entries, delete_knowledge_entry

router = APIRouter()


@router.get("")
def list_documents(organization_slug: str = None, offset: int = 0, limit: int = 50):
    entries = list_knowledge_entries(organization_slug)
    # Deduplicate by doc_id
    docs = {}
    for entry in entries:
        doc_id = entry.get("doc_id", entry.get("id", "unknown"))
        if doc_id not in docs:
            docs[doc_id] = {
                "id": doc_id,
                "title": entry.get("source", "Unknown"),
                "organization_slug": entry.get("org_slug", "yorcmo"),
                "created_at": entry.get("created_at", ""),
                "chunk_count": 0,
            }
        docs[doc_id]["chunk_count"] += 1

    doc_list = list(docs.values())
    return {
        "documents": doc_list[offset:offset + limit],
        "total": len(doc_list),
    }


@router.get("/{doc_id}")
def get_document(doc_id: str):
    entries = list_knowledge_entries()
    for entry in entries:
        if entry.get("doc_id") == doc_id or entry.get("id") == doc_id:
            return {
                "id": doc_id,
                "title": entry.get("source", "Unknown"),
                "organization_slug": entry.get("org_slug", "yorcmo"),
                "created_at": entry.get("created_at", ""),
            }
    raise HTTPException(status_code=404, detail="Document not found")


@router.delete("/{doc_id}")
def delete_document(doc_id: str):
    deleted = delete_knowledge_entry(doc_id)
    if deleted:
        return {"status": "deleted", "id": doc_id}
    raise HTTPException(status_code=404, detail="Document not found")
