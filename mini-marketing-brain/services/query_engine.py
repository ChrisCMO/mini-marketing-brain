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
