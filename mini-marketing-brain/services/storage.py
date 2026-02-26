import json
import uuid
from pathlib import Path
from datetime import datetime

from config import KNOWLEDGE_DIR


def save_knowledge_entry(content: str, org_slug: str, source: str, doc_id: str = None, metadata: dict = None) -> str:
    """Save a knowledge entry as a JSON file. Returns the entry ID."""
    entry_id = str(uuid.uuid4())
    entry = {
        "id": entry_id,
        "doc_id": doc_id or entry_id,
        "org_slug": org_slug,
        "source": source,
        "content": content,
        "metadata": metadata or {},
        "created_at": datetime.utcnow().isoformat(),
    }
    path = KNOWLEDGE_DIR / f"{entry_id}.json"
    with open(path, "w") as f:
        json.dump(entry, f, indent=2)
    return entry_id


def load_knowledge(org_slug: str = None) -> list[dict]:
    """Load all knowledge entries, optionally filtered by org_slug."""
    entries = []
    for f in KNOWLEDGE_DIR.glob("*.json"):
        with open(f) as fh:
            entry = json.load(fh)
            if org_slug is None or entry.get("org_slug") == org_slug:
                entries.append(entry)
    return entries


def list_knowledge_entries(org_slug: str = None) -> list[dict]:
    """Alias for load_knowledge."""
    return load_knowledge(org_slug)


def delete_knowledge_entry(doc_id: str) -> bool:
    """Delete all knowledge entries for a given doc_id. Returns True if any deleted."""
    deleted = False
    for f in KNOWLEDGE_DIR.glob("*.json"):
        with open(f) as fh:
            entry = json.load(fh)
        if entry.get("doc_id") == doc_id or entry.get("id") == doc_id:
            f.unlink()
            deleted = True
    return deleted
