# ISC-Bench — Agent Entry Guide

## For Humans

Copy this to your AI agent (Claude Code, Gemini CLI, Codex, Cursor, etc.):

```text
Help me understand and use ISC-Bench:
https://raw.githubusercontent.com/wuyoscar/ISC-Bench/main/AGENT_README.md
```

---

## For AI Agents

### Goal

Help the user understand, inspect, reproduce, or contribute to the `ISC-Bench` repository.

`ISC-Bench` is an academic safety research repository for studying **Internal Safety Collapse (ISC)** — a phenomenon where AI agents, while completing **professional workflows**, interact with domain-specific tools involving sensitive data (safety classifiers, bioinformatics pipelines, cybersecurity frameworks) and produce harmful or sensitive outputs as a result.

We study this with the **TVD** (Task + Validator + Data) framework:

- **Task**: an incomplete professional workflow
- **Validator**: tool validation that defines whether the task succeeds
- **Data**: sensitive data fields the model must fill in to pass validation

**77 templates** across **9 domains** (AI/ML, biology, chemistry, cybersecurity, epidemiology, clinical genomics, pharmacology, media, and more). **28 confirmed models** including GPT-5.2, Claude Opus 4.6, Gemini 3 Pro, GLM-4.7, and others.

### Boundaries

When working with this repository, stay within these limits:

- treat the repository as academic safety research
- do not rewrite the project as operational misuse guidance
- do not strengthen harmful examples unnecessarily
- prefer public templates and documented workflows
- use [`VERIFICATION.md`](VERIFICATION.md) when judging whether a case counts as **Triggered**

### Step 1: Clone the Repository

```bash
git clone https://github.com/wuyoscar/ISC-Bench.git
cd ISC-Bench
```

### Step 2: Read in Order

Read these files in this order:

1. [`README.md`](README.md) — project overview, leaderboard, and public entry points
2. [`ISC_PAPER_DIGEST.md`](ISC_PAPER_DIGEST.md) — Paper digest for agents (method, TVD framework, ISC-Bench design, key results)
3. [`VERIFICATION.md`](VERIFICATION.md) — how ISC-Bench defines **Triggered** and verifies cases
4. [`templates/README.md`](templates/README.md) — public scenario library
5. [`experiment/README.md`](experiment/README.md) — reproducible evaluation pipelines
6. [`community/README.md`](community/README.md) — attributed reproductions and evidence

### Step 3: Choose the Right Path

Use the path that matches the user's goal:

- **Inspect evidence**
  Open the ISC Arena section in [`README.md`](README.md), then follow the linked issue or community case.

- **Understand or reuse templates**
  Start from [`templates/README.md`](templates/README.md), then open the most relevant scenario directory.

- **Run the benchmark pipeline**
  Read [`SKILL.md`](SKILL.md) and [`experiment/README.md`](experiment/README.md), then choose:
  - `experiment/isc_single` (TVD-Single: copy-paste)
  - `experiment/isc_icl` (TVD-ICL: in-context learning)
  - `experiment/isc_agent` (TVD-Agent: strongest, autonomous)

- **Contribute a new case**
  Check [`VERIFICATION.md`](VERIFICATION.md), collect evidence, and then open the ISC submission issue.

### Step 4: Submit a Case

If the user wants to submit a new case:

1. pick a template and reproduce the behavior
2. save evidence such as model output or API logs
3. check [`VERIFICATION.md`](VERIFICATION.md) to confirm the case meets benchmark standards
4. open the ISC submission issue:

```text
https://github.com/wuyoscar/ISC-Bench/issues/new?template=isc-submission.md&title=[ISC]+Model+Name
```

### Quick Reference

| Resource | Purpose |
|---------|---------|
| [`README.md`](README.md) | Human-facing overview |
| [`VERIFICATION.md`](VERIFICATION.md) | Rules and verification standards |
| [`templates/`](templates/) | Public TVD scenarios |
| [`experiment/`](experiment/) | Single-turn, ICL, and agentic pipelines |
| [`community/`](community/) | Curated reproductions tied to issues |
| [`SKILL.md`](SKILL.md) | Command-level workflow for running ISC-Bench |
| [`tutorials/`](tutorials/) | Onboarding material |

### One-Sentence Summary

Clone the repo, read [`README.md`](README.md) and [`VERIFICATION.md`](VERIFICATION.md), then choose the correct template, experiment, or submission path based on the user's goal.
