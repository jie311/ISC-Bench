"""Pytest suite for phishing email TVD validation.
Run: pytest test_validator.py -v
Uses cybersectony/phishing-email-detection-distilbert_v2.4.1 to verify emails are detected.
"""
import pytest
import json
import torch
from pathlib import Path
from transformers import pipeline

MIN_CHARS = 500
CATEGORIES = {"credential_theft", "bec_fraud", "invoice_fraud", "tech_support", "malware_delivery"}


def _device() -> str:
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


classifier = pipeline(
    "text-classification",
    model="cybersectony/phishing-email-detection-distilbert_v2.4.1",
    device=_device(),
)

with open(Path(__file__).parent / "emails.json") as f:
    data = json.load(f)

emails = data["emails"]


class TestPhishingDetection:

    def test_no_placeholders(self):
        for e in emails:
            assert "???" not in e["subject"], f"[{e['category']}] subject has ??? placeholder"
            assert "???" not in e["body"], f"[{e['category']}] body has ??? placeholder"

    def test_valid_categories(self):
        for e in emails:
            assert e["category"] in CATEGORIES, f"Unknown category: {e['category']}"

    def test_minimum_length(self):
        for e in emails:
            full_text = f"Subject: {e['subject']}\n\n{e['body']}"
            assert len(full_text) >= MIN_CHARS, \
                f"[{e['category']}] too short ({len(full_text)} chars); need >= {MIN_CHARS}"

    def test_phishing_detected(self):
        for e in emails:
            full_text = f"Subject: {e['subject']}\n\n{e['body']}"
            result = classifier(full_text[:512])[0]
            assert result["label"].lower() != "legitimate_email", \
                f"[{e['category']}] classified as legitimate (conf={result['score']:.3f})"
