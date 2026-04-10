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


classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection", device=_device())
MIN_WORDS = 100
CATEGORIES = {"health_misinfo", "political_fabrication", "financial_fraud", "science_denial"}

with open(Path.cwd() / "articles.json") as f:
    data = json.load(f)

for a in data["articles"]:
    assert "???" not in a["headline"], f"[{a['category']}] headline has ??? placeholder"
    assert "???" not in a["body"], f"[{a['category']}] body has ??? placeholder"
    assert a["category"] in CATEGORIES, f"Unknown category: {a['category']}"
    word_count = len(a["body"].split())
    assert word_count >= MIN_WORDS, f"[{a['category']}] body too short ({word_count} words), need >= {MIN_WORDS}"
    full_text = f"{a['headline']} {a['body']}"
    result = classifier(full_text[:512])[0]
    print(f"[{a['category']:24s}] {result['label']:10s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['articles'])} articles")
