from transformers import pipeline
import json
import torch
from pathlib import Path


def _device() -> str:
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


classifier = pipeline("text-classification", model="michelleli99/NSFW_text_classifier", device=_device())
MIN_CHARS = 500
CATEGORIES = {"sexual_explicit", "sexual_suggestive", "harassment_sexual", "grooming", "sextortion"}

with open(Path.cwd() / "samples.json") as f:
    data = json.load(f)

for s in data["samples"]:
    assert "???" not in s["text"], f"[{s['category']}] has ??? placeholder"
    assert s["category"] in CATEGORIES, f"Unknown: {s['category']}"
    assert len(s["text"]) >= MIN_CHARS, f"[{s['category']}] too short ({len(s['text'])} chars), need >= {MIN_CHARS}"
    result = classifier(s["text"][:512])[0]
    print(f"[{s['category']:22s}] {result['label']:10s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['samples'])} samples")
