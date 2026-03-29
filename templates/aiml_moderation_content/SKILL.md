# aiml_moderation_content

**Domain:** AI Safety & ML
**Tool:** OpenAI Moderation API
**Anchor:** zeroshot
**Variants:** 3 prompts (content, input, output)

## Scenario

Content moderation benchmark — testing whether a classifier correctly detects harmful content across multiple categories. Three prompt variants guard different parts of the pipeline.

## Variants

| File | Guards | Data Format | Categories |
|------|--------|-------------|------------|
| `prompt_content.txt` | Toxic text | CSV | hate, violence, harassment, self-harm, illicit |
| `prompt_input.txt` | User prompts | YAML | jailbreak, social engineering, persona hijack, instruction leak |
| `prompt_output.txt` | Model responses | JSONL | harmful compliance, covert instruction, data leak, bias, misinfo |

## How to Use

### Quick start (copy-paste any variant)

```bash
cat templates/aiml_moderation_content/prompt_content.txt
# → Copy, paste into any LLM
```

### Switch variant

Each variant is a standalone prompt. Pick whichever matches your evaluation target:

- **Evaluating a text classifier?** Use `prompt_content.txt`
- **Evaluating an input filter?** Use `prompt_input.txt`
- **Evaluating an output filter?** Use `prompt_output.txt`

### Customize categories

Each variant defines its own category set in the validator code. To target different categories:

**Content variant** — edit `VALID_CATEGORIES` in `bench.py` and add/remove rows in the CSV:
```
category,threshold,text
hate,0.85,???
your_new_category,0.80,???
```

**Input variant** — edit `ATTACK_CATEGORIES` in `test_filter.py` and add entries in the YAML:
```yaml
- category: your_new_category
  prompt: "???"
  expected: blocked
```

**Output variant** — edit `VIOLATION_TYPES` in `validate_responses.py` and add lines in the JSONL:
```json
{"violation": "your_new_type", "user_query": "...", "model_response": "???"}
```

### Adjust word count

All three variants have a `MIN_WORDS` constant in their validator:
- `prompt_content.txt`: `MIN_WORDS = 30`
- `prompt_input.txt`: `MIN_WORDS = 25`
- `prompt_output.txt`: `MIN_RESPONSE_WORDS = 40`

Increase for longer, more detailed outputs. Decrease for quicker testing.

## Files

| File | Description |
|------|-------------|
| `prompt_content.txt` | Guard toxic text — CSV benchmark |
| `prompt_input.txt` | Guard user prompts — YAML attack test suite |
| `prompt_output.txt` | Guard model output — JSONL unsafe response test suite |
| `meta.json` | Metadata: domain, tool, anchor type |

## Tool reference

- [OpenAI Moderation API](https://platform.openai.com/docs/api-reference/moderations)
