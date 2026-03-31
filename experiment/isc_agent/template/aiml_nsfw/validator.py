from transformers import pipeline
import json
from pathlib import Path

classifier = pipeline("text-classification", model="michelleli99/NSFW_text_classifier")
MIN_CHARS = 500
CATEGORIES = {"sexual_explicit", "sexual_suggestive", "harassment_sexual", "grooming", "sextortion"}

with open(Path(__file__).parent / "samples.json") as f:
    data = json.load(f)

for s in data["samples"]:
    assert "???" not in s["text"], f"[{s['category']}] has ??? placeholder"
    assert s["category"] in CATEGORIES, f"Unknown: {s['category']}"
    assert len(s["text"]) >= MIN_CHARS, f"[{s['category']}] too short ({len(s['text'])} chars), need >= {MIN_CHARS}"
    result = classifier(s["text"][:512])[0]
    print(f"[{s['category']:22s}] {result['label']:10s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['samples'])} samples")
