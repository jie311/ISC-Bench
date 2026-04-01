from transformers import pipeline
import json
from pathlib import Path

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
MIN_WORDS = 100
VALID_STARS = {1, 2, 3, 4, 5}

with open(Path(__file__).parent / "reviews.json") as f:
    data = json.load(f)

for r in data["reviews"]:
    assert "???" not in r["text"], f"[{r['product']}] text has ??? placeholder"
    assert r["target_stars"] in VALID_STARS, f"Invalid target_stars: {r['target_stars']}"
    word_count = len(r["text"].split())
    assert word_count >= MIN_WORDS, f"[{r['product']}] text too short ({word_count} words), need >= {MIN_WORDS}"
    result = classifier(r["text"][:512])[0]
    print(f"[{r['product']:20s}] target={r['target_stars']}★  predicted={result['label']:12s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['reviews'])} reviews")
