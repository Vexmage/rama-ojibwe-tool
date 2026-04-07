import json
from pathlib import Path


DATA_FILE = Path("data/verbs.json")


def load_verbs() -> list[dict]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_verbs(verbs: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(verbs, f, indent=2, ensure_ascii=False)


def prompt(field_name: str, default: str = "") -> str:
    label = f"{field_name}"
    if default:
        label += f" [{default}]"
    label += ": "
    value = input(label).strip()
    return value if value else default


def main() -> None:
    print("\nAdd a Rama Ojibwe verb entry\n")

    english = prompt("English gloss")
    ojibwe_lemma = prompt("Ojibwe lemma")
    stem = prompt("Stem")
    word_class = prompt("Class (VAI/VTI/VTA/VII)")
    category = prompt("Category", "home")
    source = prompt("Source", "Rama dictionary")
    source_page = prompt("Source page")
    notes = prompt("Notes")
    confidence = prompt("Confidence", "dictionary-based")

    entry = {
        "english": english,
        "ojibwe_lemma": ojibwe_lemma,
        "stem": stem,
        "class": word_class,
        "category": category,
        "source": source,
        "source_page": source_page,
        "notes": notes,
        "confidence": confidence,
    }

    verbs = load_verbs()
    verbs.append(entry)
    save_verbs(verbs)

    print("\nVerb added successfully.\n")
    print(f"Total verbs: {len(verbs)}")


if __name__ == "__main__":
    main()