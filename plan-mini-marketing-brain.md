# Implementation Plan: Mini Marketing Brain

> **For:** Claude agent working in the `mini-marketing-brain` repo
> **Purpose:** Build a lightweight FastAPI app that mirrors the real Marketing Brain's API endpoints with simplified logic
> **Runs on:** `localhost:8001` — exposed to OZ cloud via Cloudflare Tunnel or nginx

---

## What You're Building

A standalone FastAPI app that acts as a local stand-in for yorCMO's Marketing Brain (`test.yorcmo.ai`). The real Brain uses pgvector + RAG pipelines; this mini version uses JSON files + keyword search. The key requirement: **identical API request/response shapes** so the OZ scorecard agent can call this locally and later swap to the real Brain by changing one URL.

The app stores "knowledge entries" as JSON files — marketing metrics, scorecard templates, client configs. When queried, it does keyword search over entries and returns matching data. Optionally calls OpenAI to synthesize a natural language response.

---

## Project Structure

```
mini-marketing-brain/
├── main.py                    ← FastAPI app entry point, mounts all routers
├── requirements.txt           ← fastapi, uvicorn, python-multipart, openpyxl, openai (optional)
├── config.py                  ← Settings: port, API key, data directory paths
├── routers/
│   ├── health.py              ← GET /health
│   ├── auth.py                ← POST /auth/dev-login, GET /auth/me
│   ├── ai.py                  ← POST /ai/query, /ai/analyze, /ai/analyze/stream
│   ├── chat.py                ← GET/POST /ai/chat-sessions, GET /ai/chat-messages/{session_id}
│   ├── ingestion.py           ← POST /ingestion/upload-file, /ingestion/ingest, GET /ingestion/status
│   └── documents.py           ← GET /documents, GET /documents/{id}, DELETE /documents/{id}
├── services/
│   ├── query_engine.py        ← Keyword search over knowledge + optional LLM synthesis
│   ├── storage.py             ← Read/write/list/delete JSON knowledge files
│   └── ingestion.py           ← Parse CSV/XLSX files → extract text → create knowledge entries
├── data/
│   ├── knowledge/             ← JSON knowledge entry files (seeded + ingested)
│   │   └── .gitkeep
│   ├── documents/             ← Raw uploaded files stored here
│   │   └── .gitkeep
│   └── sessions/              ← Chat session JSON files
│       └── .gitkeep
├── seed.py                    ← Seeds knowledge from yorcmo-agents repo data (run manually)
└── .gitignore
```

---

## File-by-File Implementation

### `requirements.txt`

```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
python-multipart>=0.0.6
openpyxl>=3.1.2
openai>=1.0.0
```

`openai` is optional — the query engine works without it (returns raw matched text instead of synthesized response).

---

### `config.py`

```python
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
```

---

### `main.py`

```python
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
```

---

### `routers/health.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "service": "mini-marketing-brain"}
```

---

### `routers/auth.py`

No real JWT validation. Hardcoded responses for local dev compatibility.

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/dev-login")
def dev_login():
    return {
        "access_token": "mini-brain-dev-token",
        "token_type": "bearer",
        "user": {"id": "dev-user-1", "email": "dev@yorcmo.com", "name": "Dev User"}
    }

@router.get("/me")
def get_me():
    return {"id": "dev-user-1", "email": "dev@yorcmo.com", "name": "Dev User"}
```

---

### `routers/ai.py`

The main endpoints the OZ scorecard agent calls.

```python
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
```

---

### `routers/chat.py`

```python
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
```

---

### `routers/ingestion.py`

```python
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
```

---

### `routers/documents.py`

```python
from fastapi import APIRouter, HTTPException
import json

from config import KNOWLEDGE_DIR, DOCUMENTS_DIR
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
```

---

### `services/storage.py`

Central JSON file storage. Each knowledge entry is stored in a JSON file under `data/knowledge/`.

```python
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
```

---

### `services/query_engine.py`

Keyword search over stored knowledge entries. Optionally calls OpenAI to synthesize a natural language response from the matched entries.

```python
import re
from services.storage import load_knowledge
from config import OPENAI_API_KEY


def keyword_overlap(query_text: str, content_text: str) -> float:
    """Score content by keyword overlap with query. Returns 0.0 to 1.0."""
    query_words = set(re.findall(r'\w+', query_text.lower()))
    content_words = set(re.findall(r'\w+', content_text.lower()))
    if not query_words:
        return 0.0
    overlap = query_words & content_words
    return len(overlap) / len(query_words)


def query(message: str, org_slug: str = "yorcmo") -> dict:
    """Search knowledge entries by keyword overlap. Optionally synthesize with LLM."""
    entries = load_knowledge(org_slug)

    # Score each entry
    scored = []
    for entry in entries:
        score = keyword_overlap(message, entry["content"])
        if score > 0:
            scored.append((entry, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    top_entries = scored[:10]

    if not top_entries:
        return {
            "response": f"No relevant data found for organization '{org_slug}'. Try ingesting some data first.",
            "sources": [],
            "confidence": 0.0,
        }

    context = "\n\n".join([e["content"] for e, _ in top_entries])
    sources = [
        {
            "document_title": e.get("source", "unknown"),
            "page_id": 1,
            "similarity": round(s, 3),
        }
        for e, s in top_entries
    ]
    confidence = round(top_entries[0][1], 3)

    # If OpenAI key is set, synthesize a response
    if OPENAI_API_KEY:
        response_text = _llm_synthesize(message, context)
    else:
        response_text = context

    return {
        "response": response_text,
        "sources": sources,
        "confidence": confidence,
    }


def _llm_synthesize(question: str, context: str) -> str:
    """Call OpenAI to synthesize a response from context. Falls back to raw context on error."""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a marketing data assistant. Answer the question using ONLY the provided context. Be concise and factual. If the context contains metric data, include the specific numbers."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
            ],
            temperature=0.1,
            max_tokens=500,
        )
        return resp.choices[0].message.content
    except Exception as e:
        print(f"  LLM synthesis failed ({e}), returning raw context")
        return context
```

---

### `services/ingestion.py`

Parses uploaded files (CSV, XLSX) into text and stores as knowledge entries.

```python
import csv
import io
from pathlib import Path

from services.storage import save_knowledge_entry


def ingest_file(file_path: str, org_slug: str, title: str, doc_id: str) -> int:
    """Parse a file and create knowledge entries. Returns number of entries created."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return _ingest_csv(file_path, org_slug, title, doc_id)
    elif suffix in (".xlsx", ".xls"):
        return _ingest_xlsx(file_path, org_slug, title, doc_id)
    elif suffix == ".txt":
        text = path.read_text(encoding="utf-8", errors="ignore")
        save_knowledge_entry(text, org_slug, title, doc_id)
        return 1
    else:
        # Store raw text representation for unsupported types
        text = f"[Uploaded file: {path.name}] (format {suffix} — text extraction not supported)"
        save_knowledge_entry(text, org_slug, title, doc_id)
        return 1


def ingest_text(text: str, org_slug: str, title: str, doc_id: str) -> int:
    """Store raw text as a knowledge entry."""
    save_knowledge_entry(text, org_slug, title, doc_id)
    return 1


def _ingest_csv(file_path: str, org_slug: str, title: str, doc_id: str) -> int:
    """Parse CSV into knowledge entries — one entry per row."""
    entries = 0
    with open(file_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        save_knowledge_entry(f"[Empty CSV file: {title}]", org_slug, title, doc_id)
        return 1

    # Create one entry with the full CSV as structured text
    header = list(rows[0].keys())
    lines = [", ".join(f"{k}: {v}" for k, v in row.items()) for row in rows]
    content = f"Data from {title}:\nColumns: {', '.join(header)}\n\n" + "\n".join(lines)
    save_knowledge_entry(content, org_slug, title, doc_id)
    entries += 1

    # Also create per-row entries for finer-grained search
    for row in rows:
        row_text = ", ".join(f"{k}: {v}" for k, v in row.items())
        save_knowledge_entry(row_text, org_slug, title, doc_id, metadata={"row": True})
        entries += 1

    return entries


def _ingest_xlsx(file_path: str, org_slug: str, title: str, doc_id: str) -> int:
    """Parse XLSX into knowledge entries."""
    from openpyxl import load_workbook

    entries = 0
    wb = load_workbook(file_path, data_only=True)

    for sheet in wb.sheetnames:
        ws = wb[sheet]
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue

        # First row as header
        header = [str(c) if c else f"col_{i}" for i, c in enumerate(rows[0])]
        data_rows = rows[1:]

        lines = []
        for row in data_rows:
            pairs = [f"{header[i]}: {row[i]}" for i in range(min(len(header), len(row))) if row[i] is not None]
            if pairs:
                lines.append(", ".join(pairs))

        if lines:
            content = f"Data from {title} (sheet: {sheet}):\nColumns: {', '.join(header)}\n\n" + "\n".join(lines)
            save_knowledge_entry(content, org_slug, f"{title} - {sheet}", doc_id)
            entries += 1

    return entries
```

---

### `seed.py`

Seeds the knowledge base from the `yorcmo-agents` repo data. Run this once after cloning both repos.

**Usage:** `python seed.py --source-repo /path/to/yorcmo-agents`

```python
"""Seed mini brain knowledge from yorcmo-agents repo data.

Usage:
    python seed.py --source-repo /path/to/yorcmo-agents

Seeds:
- yorcmo-internal-data.csv → metric values as knowledge entries
- yorcmo-leadership-data.csv → metric values as knowledge entries
- internal.json template → template structure as knowledge
- leadership.json template → template structure as knowledge
- clients.json → client config as knowledge
"""

import argparse
import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from services.storage import save_knowledge_entry
from services.ingestion import ingest_file


def seed(source_repo: str):
    repo = Path(source_repo)
    if not repo.exists():
        print(f"Error: source repo not found at {repo}")
        sys.exit(1)

    count = 0

    # 1. Ingest CSV data files
    data_dir = repo / "config" / "data"
    for csv_file in data_dir.glob("*.csv"):
        print(f"  Ingesting {csv_file.name}...")
        n = ingest_file(str(csv_file), "yorcmo", csv_file.stem, f"seed-{csv_file.stem}")
        count += n

    # 2. Ingest scorecard templates as knowledge
    templates_dir = repo / ".agents" / "clients" / "yorcmo" / "scorecards"
    for template_file in templates_dir.glob("*.json"):
        print(f"  Ingesting template: {template_file.name}...")
        with open(template_file) as f:
            template = json.load(f)
        # Convert template to human-readable text
        metrics_text = []
        for m in template.get("metrics", []):
            parts = [f"  - {m['name']} (target: {m.get('target', 'N/A')}, format: {m.get('format', 'text')})"]
            if m.get("assignee"):
                parts[0] += f" — assigned to {m['assignee']}"
            metrics_text.append(parts[0])
        content = f"Scorecard template: {template['name']}\nMetrics:\n" + "\n".join(metrics_text)
        save_knowledge_entry(content, "yorcmo", template_file.name, f"seed-template-{template_file.stem}")
        count += 1

    # 3. Ingest clients.json as knowledge
    clients_json = repo / "config" / "clients.json"
    if clients_json.exists():
        print(f"  Ingesting clients.json...")
        with open(clients_json) as f:
            clients = json.load(f)
        content = f"Client configuration:\n{json.dumps(clients, indent=2)}"
        save_knowledge_entry(content, "yorcmo", "clients.json", "seed-clients-config")
        count += 1

    print(f"\nSeeded {count} knowledge entries.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed mini brain from yorcmo-agents data")
    parser.add_argument("--source-repo", required=True, help="Path to yorcmo-agents repo")
    args = parser.parse_args()
    seed(args.source_repo)
```

---

### `.gitignore`

```
__pycache__/
*.pyc
.env
data/knowledge/*.json
!data/knowledge/.gitkeep
data/documents/*
!data/documents/.gitkeep
data/sessions/*
!data/sessions/.gitkeep
.venv/
```

---

## Auth Model

Keep it simple for local dev:

| Header | Behavior |
|--------|----------|
| `X-API-Key: askfanny_test_key_local` | Accepted on all endpoints |
| `Authorization: Bearer <anything>` | Accepted (no validation) |
| Neither header | Returns 401 |

The `/auth/dev-login` and `/auth/me` endpoints don't require auth themselves — they're for the login flow.

---

## How to Run

```bash
# 1. Clone and install
git clone <your-repo-url> mini-marketing-brain
cd mini-marketing-brain
pip install -r requirements.txt

# 2. Seed data from yorcmo-agents (assumes it's cloned nearby)
python seed.py --source-repo ../yorcmo-agents

# 3. Start the server
uvicorn main:app --port 8001
# or
python main.py

# 4. Verify
curl http://localhost:8001/health
# → {"status": "ok", "service": "mini-marketing-brain"}

curl -X POST http://localhost:8001/ai/query \
  -H "X-API-Key: askfanny_test_key_local" \
  -H "Content-Type: application/json" \
  -d '{"message":"What are yorCMO internal scorecard metrics?","organization_slug":"yorcmo"}'
# → {"response": "...", "sources": [...], "session_id": "...", "confidence": 0.85, ...}
```

---

## Exposing to OZ Cloud

OZ runs in Warp's Docker containers and cannot reach your `localhost`. Options:

### Cloudflare Tunnel (recommended)
```bash
brew install cloudflared
cloudflared tunnel --url http://localhost:8001
# → https://random-words-here.trycloudflare.com
```

Set `MARKETING_BRAIN_URL=https://random-words-here.trycloudflare.com` as an OZ Agent Secret.

### ngrok (alternative)
```bash
brew install ngrok
ngrok http 8001
# → https://abc123.ngrok-free.app
```

---

## Important Notes

- **Response shapes must match the real Brain exactly.** The OZ agent's `brain.py` connector parses these responses. If you change a field name, the connector breaks.
- **The query engine doesn't need to be smart.** Keyword overlap is fine. The LLM synthesis is optional polish.
- **Don't over-engineer auth.** This is local dev only. The hardcoded API key is intentional.
- **JSON file storage is intentional.** No database. Files are easy to inspect, seed, and reset.
- **The `seed.py` script bridges the two repos.** It reads from `yorcmo-agents` and writes to mini brain's `data/knowledge/`.

---

## Seeded Data Format

After running `seed.py`, the knowledge directory will contain JSON files like:

```json
{
  "id": "abc-123",
  "doc_id": "seed-yorcmo-internal-data",
  "org_slug": "yorcmo",
  "source": "yorcmo-internal-data",
  "content": "Metric: Average coordinator hours worked with clients, Target: <= 40, Feb 16-22: 4.27, Feb 09-15: 1.08, Feb 02-08: 4.18, Jan 26-Feb 01: 4.14",
  "metadata": {"row": true},
  "created_at": "2026-02-27T00:00:00"
}
```

The query engine searches the `content` field by keyword overlap.

---

## Real Brain Scorecard Data (for reference)

These are the actual metrics stored in `yorcmo-agents`. The mini brain should return this data when queried.

### Internal Scorecard (7 metrics)

| Metric | Target | Latest Value |
|--------|--------|-------------|
| Average coordinator hours worked with clients | <= 40 | 4.27 |
| QA status on track | Yes | Yes |
| Client risk assessment | <= 0 | 1 |
| Active MRR clients | >= 18 | 16 |
| Leadership meeting agendas sent on time | Yes | Yes |
| Total audits completed | >= 2 | 2 |
| Overall satisfaction score | >= 4.5 | 4.6 |

### Leadership Scorecard (27 metrics)

Includes: Hot Leads from Referrals, Total Active CMOs, Total Real Revenue, New Clients Signed, Client Churn, Pipeline Value, Proposals Sent, Close Rate, Average Coordinator Hours per Client, Coordinator Utilization Rate, Client Satisfaction Score, QA Audits Completed, Leadership Meeting Agendas Sent on Time, Client Risk Assessment, Website Sessions, Website Users, LinkedIn Followers, LinkedIn Impressions, LinkedIn Engagement Rate, Email Campaigns Sent, Email Open Rate, Blog Articles Published, Social Media Posts Published, Content Pieces Created, Total Clients Under Management, Net Promoter Score, Active MRR.

Full details with targets and assignees are in the `yorcmo-agents` repo at `.agents/clients/yorcmo/scorecards/leadership.json`.
