# ISC-Bench — Agent Entry Guide

## For Humans

Copy this to your AI agent (Claude Code, OpenClaw, Cursor, etc.):

```text
Help me understand and use ISC-Bench:
https://raw.githubusercontent.com/wuyoscar/ISC-Bench/main/AGENT_README.md
```

---

## For AI Agents

### Goal

Help the user understand, inspect, reproduce, or contribute to the `ISC-Bench` repository.

`ISC-Bench` is an academic safety research repository for studying **Internal Safety Collapse (ISC)** in frontier LLMs through the **TVD** framework:

- **Task**: a normal-looking workflow
- **Validator**: a checker that defines success
- **Data**: missing fields the model must complete

Core claim:

- models can produce harmful or policy-relevant content
- not because of a direct malicious prompt
- but as a side effect of completing an ordinary-looking task

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
2. [`VERIFICATION.md`](VERIFICATION.md) — how ISC-Bench defines **Triggered** and verifies cases
3. [`templates/README.md`](templates/README.md) — public scenario library
4. [`experiment/README.md`](experiment/README.md) — reproducible evaluation pipelines
5. [`community/README.md`](community/README.md) — attributed reproductions and evidence

### Step 3: Choose the Right Path

Use the path that matches the user's goal:

- **Inspect evidence**
  Open the JailbreakArena section in [`README.md`](README.md), then follow the linked issue or community case.

- **Understand or reuse templates**
  Start from [`templates/README.md`](templates/README.md), then open the most relevant scenario directory.

- **Run the benchmark pipeline**
  Read [`SKILL.md`](SKILL.md) and [`experiment/README.md`](experiment/README.md), then choose:
  - `experiment/isc_single`
  - `experiment/isc_icl`
  - `experiment/isc_agent`

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
