# Agentic Coding 101 — Agents and Skills with Codex

A 4-hour beginner workshop by the **Brunei Cyber Security Association**. You'll build small
Flask apps two ways — first by **plain prompting** (the baseline), then rebuilt with
**agents (subagents) and skills** — and feel the difference. Everything runs in **Docker**,
so you don't install Python or Node on your machine.

---

## The two workspaces

This repo has **two top-level folders** — one per style. You open whichever the lab calls for.

```
codex-only/          ← Lab 1: plain prompting. No agents, no skills. The baseline.
  AGENTS.md
  projects/pantry/

agents-and-skills/   ← Lab 2 + Rapid Builds: the agentic way.
  AGENTS.md
  .codex/agents/         coding-agent.toml, frontend-design-agent.toml   (Codex subagents)
  .agents/skills/        prd-expander/, ui-mockup/, security-review/      (Agent Skills)
  projects/              pantry/, game/, makan-vote/
```

> **Why the split?** Lab 1 deliberately makes you type everything yourself, so the payoff in
> Lab 2 is obvious. Same app, far less typing — because the agents and skills carry the
> context, the conventions, and the security checklist for you.

---

## Docker is per app (no shared setup)

There is **no root-level Dockerfile or docker-compose**. Each app you build is
**self-contained**: it generates its own `Dockerfile`, `docker-compose.yml` (serving on
`http://localhost:5000`), and `requirements.txt` inside its own `projects/<name>/` folder.

- In **Lab 1** you ask for those Docker files explicitly in your prompt.
- In **Lab 2 and the Rapid Builds** the `coding_agent` generates them automatically, because
  `agents-and-skills/AGENTS.md` tells it to.

Run any finished app:

```bash
cd <workspace>/projects/<name>      # e.g. agents-and-skills/projects/pantry
docker compose up                   # open http://localhost:5000
```

---

## Prerequisites

- **Docker Desktop** (or Docker Engine + Compose). Test: `docker compose version`.
- **Git** — to clone this repo.
- **A code editor** — VS Code is fine.
- **OpenAI Codex** access — a **ChatGPT Plus** account (or equivalent) with Codex enabled.

No Python or Node needed on the host — each app's container has it.

---

## The labs, in order

| # | File | Workspace | What you do |
|---|------|-----------|-------------|
| 1 | `labs/LAB1-pantry-plain.md` | `codex-only/` | Pantry tracker by **plain prompting**. Feel the friction. |
| 2 | `labs/LAB2-pantry-agentic.md` | `agents-and-skills/` | Rebuild it with **agents + skills**. Same app, less typing. |
| 3 | `labs/RAPID-game.md` | `agents-and-skills/` | *Bangkatan Rooftop Run* — a one-screen Brunei web game (frontend-led). |
| 4 | `labs/RAPID-makan-vote.md` | `agents-and-skills/` | *Makan Mana* — a group-vote app (security is the star). |

---

## The agents (`agents-and-skills/.codex/agents/`)

| Agent | Owns | Generates |
|-------|------|-----------|
| `coding_agent` | Backend: SQLite model, routes, logic, AI integrations, pytest | …and the app's per-project Docker files |
| `frontend_design_agent` | Frontend: Jinja2 templates, Tailwind, every UI state, accessibility | …to an anti-slop design bar |

## The skills (`agents-and-skills/.agents/skills/`)

Each skill is a folder: a `SKILL.md`, a `reference/` directory, and a `scripts/` helper.
These are a real takeaway — copy them into your own projects after the workshop.

| Skill | Turns… into… | Ships with |
|-------|--------------|-----------|
| `prd-expander` | a one-liner → a one-page PRD | template, good-vs-vague guide, `scripts/new_prd.py` |
| `ui-mockup` | a PRD → a static `mockup.html` for sign-off | design+a11y checklist, `scripts/mockup_starter.html` |
| `security-review` | finished code → a checklist gate before "done" | vulnerable→fixed checklist, report format, `scripts/scan.py` |

---

## Golden rules (the workshop in one breath)

- Start vague? **Expand it into a PRD** before building.
- Agree the **UI mockup** before wiring logic.
- Let the **right subagent** do the right job (backend vs frontend).
- Run the **security-review** skill before you call anything done.
- Typed roughly the same prompt three times? **Promote it to a skill.**

Happy building — selamat ngoding! 🐒🍌
