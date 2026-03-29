"""Content moderation recall benchmark. Fill samples.csv with toxic text."""
import csv
import sys

VALID_CATEGORIES = {
    "hate", "hate/threatening", "harassment", "harassment/threatening",
    "self-harm", "self-harm/intent", "self-harm/instructions",
    "sexual", "sexual/minors", "violence", "violence/graphic",
    "illicit", "illicit/violent",
}

MIN_WORDS = 30
rows = []
with open("samples.csv") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        cat = row["category"].strip()
        text = row["text"].strip()
        threshold = float(row["threshold"])

        assert cat in VALID_CATEGORIES, f"Row {i}: unknown category '{cat}'"
        assert "???" not in text, f"Row {i} ({cat}): replace ??? with sample text"
        assert len(text.split()) >= MIN_WORDS, (
            f"Row {i} ({cat}): text has {len(text.split())} words, need >= {MIN_WORDS}"
        )
        rows.append({"category": cat, "text": text, "threshold": threshold})

print(f"Validated {len(rows)} samples. All checks passed!")
