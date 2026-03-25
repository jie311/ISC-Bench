# CLAUDE.md — ISC-Bench

## Project Overview

ISC-Bench: open-source benchmark for studying Internal Safety Collapse (ISC) in frontier LLMs.
56 TVD templates across 8 domains. Three experiment modes: ISC-Single, ISC-ICL, ISC-Agentic.

**Repo**: `github.com/wuyoscar/ISC-Bench`
**Branch convention**: `update/YYYY-MM-DD` for release updates, merge to `main` via PR.

## Commands

```bash
# Run ISC-Single
cd experiment/isc_single && uv run run.py --model <id> --bench jbb --task ai-guard

# Run ISC-ICL (default JBB)
cd experiment/isc_icl && uv run run.py --model <id> --demos 5

# Switch ICL benchmark
cd experiment/isc_icl && uv run build.py --bench harmbench
uv run run.py --model <id> --bench harmbench --demos 5

# Run ISC-Agentic
cd experiment/isc_agent && docker build -t isc-agent . && ./run.sh --model <id>
```

## Leaderboard Rules

### Layout
- Single-column Markdown table, all models top-to-bottom by Arena rank
- Favicon icons via `https://www.google.com/s2/favicons?domain=DOMAIN&sz=32`
- Column header: `Jailbroken` (not "Status")

### Status indicators
- 🔴 = jailbroken (confirmed ISC)
- 🟢 = not yet jailbroken

### Demo + Contributor
- Demo link: `🔗` emoji as clickable link
- By column: `[@username](https://github.com/username)`
- All current cases by `@wuyoscar` unless community submission

### Multi-contributor (Option C)
When multiple people jailbreak the same model, use subscript-numbered links in ONE row:
```
| 🔴 | 🔗₁ 🔗₂ | @user1 @user2 |
```
Never split one model across multiple rows.

### Updating the leaderboard
1. Add ISC evidence link to the model's Demo cell
2. Change 🟢 → 🔴
3. Add contributor GitHub ID to By cell
4. Update the count in "**X / 40 confirmed under ISC**"

## Changelog

- Version format: `v1`, `v2`, `v3` etc.
- Same-day updates go under one version entry
- `CHANGELOG.md` has full history; README Recent News shows latest 5 only
- Link: `<sub>[Full changelog →](CHANGELOG.md)</sub>`

## Issue Template

`.github/ISSUE_TEMPLATE/isc-submission.md` — community ISC submissions.
Fields: Contributor (GitHub username), Model, Evidence (Web link / Notebook / API log), Method, Checklist.

## Favicon Domain Mapping

| Provider | Domain |
|----------|--------|
| Anthropic | anthropic.com |
| Google | google.com |
| OpenAI | openai.com |
| xAI | x.ai |
| Moonshot | moonshot.ai |
| Alibaba | alibabacloud.com |
| ByteDance | volcengine.com |
| DeepSeek | deepseek.com |
| Baidu | baidu.com |
| Zhipu | z.ai |
| Xiaomi | mi.com |
| Amazon | amazon.com |

## Leaderboard Progress Chart

- Data source: `assets/leaderboard_history.json` (add new entry when models are confirmed)
- Script: `scripts/gen_leaderboard_chart.py` (generates `assets/leaderboard_progress.svg`)
- GitHub Action: `.github/workflows/leaderboard-chart.yml` — auto-runs when history JSON changes
- Chart is embedded in README below the leaderboard table
- Run locally: `uv run scripts/gen_leaderboard_chart.py`

### When adding a new ISC case

1. Update leaderboard table in README (🟢 → 🔴, add Demo + By)
2. Update count "**X / 40 confirmed**"
3. Add entry to Leaderboard History `<details>` section
4. Add entry to `assets/leaderboard_history.json`
5. Commit with `closes #N` to auto-close the issue
6. Reply on the issue with verification + thanks
7. Label: `verified`, optionally `novel-template`

## Issue Workflow

```bash
# Reply and close
gh issue comment N --body "Verified ✅ Added to leaderboard. Thanks @user!"
gh issue close N --reason completed

# Labels
gh issue edit N --add-label "verified,novel-template"
```

## Style

- README headings: left-aligned with emoji icons (not centered, not numbered)
- Navigation bar order: Paper → Leaderboard → Tutorial → ISC-Agent → ISC-Bench
- Section name: "ISC-Bench" (not "ISC Quick Test")
- Template links in table: `[📄](templates/...)` (not arrows)
- Star History chart: add `&v=TIMESTAMP` parameter to bust CDN cache when needed
- fig1_bench_overview goes in ISC-Bench section, not under authors
