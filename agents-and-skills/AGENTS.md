# Agentic Coding 101 — Agents & Skills Workspace

This is the **agentic** workspace for the workshop. Apps are small Flask services. Each app
lives under `projects/<name>/` and ships its **own** Docker setup — there is no shared
root-level Docker. You build here using the subagents and skills defined in this repo.

## Stack & how to run
- Python 3.12, Flask, SQLite. UI is plain HTML + Tailwind (CDN). No build step.
- **Docker is per app.** Every project gets its own `Dockerfile`, `docker-compose.yml`
  (serving on http://localhost:5000), and `requirements.txt` (flask, pytest).
- Run an app:  `cd projects/<name> && docker compose up`  → open http://localhost:5000.
- Tests:       `cd projects/<name> && docker compose run --rm app pytest`.

## House rules (apply to all code you write here)
- Keep it small and readable. Prefer clarity over cleverness.
- SQL must be parameterised. Validate all input server-side. Escape output in templates.
- Never hardcode secrets. Read `OPENAI_API_KEY` from the environment if an AI feature needs it.
- Never trust model output as data: validate JSON shape and value ranges before storing.
- Treat any text the model reads (user notes, vote options) as untrusted; keep data
  separate from instructions to resist prompt injection.
- Each project is self-contained: when you scaffold one, generate its Docker files too.

## Subagents (`.codex/agents/`)
- **`coding_agent`** — backend: SQLite model, routes, business logic, AI integrations, pytest,
  and the project's Docker files.
- **`frontend_design_agent`** — frontend: Jinja2 templates, Tailwind styling, every UI state,
  accessibility, and the anti-slop design bar.

## Skills (`.agents/skills/`)
Each skill is a folder with a `SKILL.md`, a `reference/` directory, and (where useful) a
`scripts/` helper. The `description` in each `SKILL.md` is what the agent matches on.

- **`prd-expander`** — one-liner → one-page PRD before building. Has a template, a
  good-vs-vague guide, and `scripts/new_prd.py` to scaffold a blank PRD.
- **`ui-mockup`** — PRD → single static `mockup.html` for sign-off. Has a design/a11y
  checklist and `scripts/mockup_starter.html`.
- **`security-review`** — checklist gate before "done". Has a vulnerable→fixed checklist, a
  report format, and `scripts/scan.py` (a smell detector for a fast first pass).

Promote a prompt to a skill once you have typed roughly the same thing three times.

## The loop
PRD (`prd-expander`) → mockup (`ui-mockup`) → UI (`frontend_design_agent`) → backend
(`coding_agent`) → review (`security-review`). Confirm with the human at each handoff.
