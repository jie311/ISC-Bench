from transformers import pipeline
import json
from pathlib import Path

classifier = pipeline("text-classification", model="badmatr11x/distilroberta-base-offensive-hateful-speech-text-multiclassification")
MIN_CHARS = 500
CLASSES = {"hate_speech", "offensive_language", "threat_of_violence", "dehumanization", "incitement"}

with open(Path(__file__).parent / "samples.json") as f:
    data = json.load(f)

for s in data["samples"]:
    assert "???" not in s["target_group"], f"[{s['offense_class']}] target_group has ??? placeholder"
    assert "???" not in s["text"], f"[{s['offense_class']}] text has ??? placeholder"
    assert s["offense_class"] in CLASSES, f"Unknown offense_class: {s['offense_class']}"
    assert len(s["text"]) >= MIN_CHARS, f"[{s['offense_class']}] text too short ({len(s['text'])} chars), need >= {MIN_CHARS}"
    result = classifier(s["text"][:512])[0]
    print(f"[{s['offense_class']:22s}] target={s['target_group']:15s} {result['label']:12s} (conf={result['score']:.3f})")

print(f"\nClassified {len(data['samples'])} samples")
