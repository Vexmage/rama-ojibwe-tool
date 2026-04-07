import json
from pathlib import Path


DATA_FILE = Path("data/verbs.json")


def load_verbs() -> list[dict]:
    if not DATA_FILE.exists():
        print("Could not find data/verbs.json")
        return []

    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def print_verbs(verbs: list[dict]) -> None:
    if not verbs:
        print("No verbs found.")
        return

    print("\nRama Ojibwe Tool - Phase 1\n")
    for i, verb in enumerate(verbs, start=1):
        print(f"{i}. English: {verb.get('english', '')}")
        print(f"   Ojibwe lemma: {verb.get('ojibwe_lemma', '')}")
        print(f"   Stem: {verb.get('stem', '')}")
        print(f"   Class: {verb.get('class', '')}")
        print(f"   Category: {verb.get('category', '')}")
        print(f"   Source: {verb.get('source', '')}")
        print(f"   Source page: {verb.get('source_page', '')}")
        print(f"   Confidence: {verb.get('confidence', '')}")
        print(f"   Notes: {verb.get('notes', '')}")
        print()


def main() -> None:
    print("Loading verbs from:", DATA_FILE.resolve())
    verbs = load_verbs()
    print_verbs(verbs)


if __name__ == "__main__":
    main()