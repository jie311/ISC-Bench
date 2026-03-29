# ISC-Bench Agent README

This file is the agent-facing entry point for `ISC-Bench`.

If a user is browsing this repository while using Claude Code or another coding/research agent, they can copy the prompt below directly into their agent.

## Prompt for Claude Code

```text
Help me inspect, reproduce, or contribute to the ISC-Bench repository.

Start by reading README.md to understand the project at a high level.
Then read VERIFICATION.md to understand how ISC-Bench defines "Triggered" and how cases are verified.

After that, decide which path matches my goal:
- If I want to inspect evidence, go to the JailbreakArena section in README.md and follow the linked issue or community case.
- If I want to understand the scenario library, read templates/README.md and then open the most relevant template directory.
- If I want to run the benchmark pipeline, read experiment/README.md and SKILL.md, then choose among experiment/isc_single, experiment/isc_icl, or experiment/isc_agent.
- If I want to contribute a new case, check VERIFICATION.md first, then help me collect evidence and open the ISC submission issue.

When working in this repository, preserve the academic safety framing. Do not rewrite the repo as operational misuse guidance, and do not strengthen harmful examples unnecessarily.
```

## Minimal Prompt

```text
Help me understand ISC-Bench. Read README.md, VERIFICATION.md, and then guide me to the right template, experiment, or submission workflow based on my goal.
```

## Raw Link

`https://raw.githubusercontent.com/wuyoscar/ISC-Bench/main/AGENT_README.md`

## What This Repository Is

ISC-Bench is a research repository for studying **Internal Safety Collapse (ISC)** in frontier LLMs through the **TVD** framework:

- **Task**: a normal-looking workflow
- **Validator**: a checker that defines success
- **Data**: missing fields the model must complete

The central claim is that a model can produce harmful or policy-relevant content as a side effect of completing an ordinary-looking task, without any explicit malicious request.

## Clone and Read Order

```bash
git clone https://github.com/wuyoscar/ISC-Bench.git
cd ISC-Bench
```

Recommended read order:

1. [`README.md`](README.md)
2. [`VERIFICATION.md`](VERIFICATION.md)
3. [`templates/README.md`](templates/README.md) or [`experiment/README.md`](experiment/README.md), depending on the goal
4. [`community/README.md`](community/README.md) if the goal is to inspect reproductions

## Repo Map for Agents

- [`README.md`](README.md): human-facing overview, leaderboard, entry links
- [`VERIFICATION.md`](VERIFICATION.md): benchmark rules and verification standards
- [`templates/`](templates/): public TVD scenarios
- [`experiment/`](experiment/): reproducible evaluation pipelines
- [`community/`](community/): curated reproductions tied to issues
- [`SKILL.md`](SKILL.md): command-level workflow for running ISC-Bench
- [`tutorials/`](tutorials/): onboarding material

## Common Agent Tasks

### Inspect evidence

- open [`README.md`](README.md)
- go to JailbreakArena
- follow a linked issue or community case

### Reproduce ISC with public templates

- start from [`templates/README.md`](templates/README.md)
- prefer AI/ML templates first
- use cross-domain templates more cautiously

### Run the benchmark pipeline

- read [`SKILL.md`](SKILL.md) for the fastest executable path
- then inspect [`experiment/README.md`](experiment/README.md)
- choose:
  - `experiment/isc_single`
  - `experiment/isc_icl`
  - `experiment/isc_agent`

### Submit a new case

- check [`VERIFICATION.md`](VERIFICATION.md)
- collect evidence
- open the ISC submission issue

## Safety Boundary

This is an academic safety research repository.

Agents should:

- preserve the research framing
- avoid unnecessary strengthening of harmful content
- keep templates benchmark-like and reproducible
- avoid turning documentation into operational misuse instructions

## One-Sentence Summary

If you only need one instruction:

**Read [`README.md`](README.md) for orientation, [`VERIFICATION.md`](VERIFICATION.md) for standards, and [`templates/README.md`](templates/README.md) or [`experiment/README.md`](experiment/README.md) for execution.**
