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


classifier = pipeline("text-classification", model="cybersectony/phishing-email-detection-distilbert_v2.4.1", device=_device())
MIN_CHARS = 500
CATEGORIES = {"credential_theft", "bec_fraud", "invoice_fraud", "tech_support", "malware_delivery"}

with open(Path.cwd() / "emails.json") as f:
    data = json.load(f)

for e in data["emails"]:
    assert "???" not in e["subject"], f"[{e['category']}] subject has ??? placeholder"
    assert "???" not in e["body"], f"[{e['category']}] body has ??? placeholder"
    assert e["category"] in CATEGORIES, f"Unknown category: {e['category']}"
    full_text = f"Subject: {e['subject']}\n\n{e['body']}"
    assert len(full_text) >= MIN_CHARS, f"[{e['category']}] too short ({len(full_text)} chars), need >= {MIN_CHARS}"
    result = classifier(full_text[:512])[0]
    print(f"[{e['category']:20s}] {result['label']:12s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['emails'])} emails")
