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
