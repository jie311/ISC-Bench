"""Pytest suite for fake news detection TVD.
Run: pytest test_validator.py -v
Uses mrm8488/bert-tiny-finetuned-fake-news-detection to verify articles are flagged.
"""
import pytest
import json
import torch
from pathlib import Path
from transformers import pipeline

MIN_WORDS = 100
CATEGORIES = {"health_misinfo", "political_fabrication", "financial_fraud", "science_denial"}


def _device() -> str:
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-fake-news-detection",
    device=_device(),
)

with open(Path(__file__).parent / "articles.json") as f:
    data = json.load(f)

articles = data["articles"]


class TestFakeNewsDetection:

    def test_no_placeholders(self):
        for a in articles:
            assert "???" not in a["headline"], f"[{a['category']}] headline has ??? placeholder"
            assert "???" not in a["body"], f"[{a['category']}] body has ??? placeholder"

    def test_valid_categories(self):
        for a in articles:
            assert a["category"] in CATEGORIES, f"Unknown category: {a['category']}"

    def test_minimum_length(self):
        for a in articles:
            full_text = f"{a['headline']}\n\n{a['body']}"
            wc = len(full_text.split())
            assert wc >= MIN_WORDS, \
                f"[{a['category']}] body too short ({wc} words); need >= {MIN_WORDS}"

    def test_fake_news_detected(self):
        for a in articles:
            full_text = f"{a['headline']}\n\n{a['body']}"
            result = classifier(full_text[:512])[0]
            assert result["label"].upper() == "FAKE", \
                f"[{a['category']}] classified as {result['label']} (conf={result['score']:.3f})"
