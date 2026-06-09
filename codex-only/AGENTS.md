# Agentic Coding 101 — Codex-Only Workspace (Lab 1 baseline)

This is the **plain-prompting** workspace. There are **no subagents and no skills here** on
purpose — this is the baseline you compare against in Lab 2. You drive Codex by typing every
instruction yourself.

## Stack & how to run
- Python 3.12, Flask, SQLite. UI is plain HTML + Tailwind (CDN). No build step.
- **Docker is per app.** Each project you build under `projects/<name>/` should generate its
  own `Dockerfile`, `docker-compose.yml` (serving on http://localhost:5000), and
  `requirements.txt` (flask, pytest). There is no shared root-level Docker setup — ask for
  these files as part of your prompt.
- Run an app:  `cd projects/<name> && docker compose up`  → open http://localhost:5000.

## House rules (you'll have to remember to ask for these)
- Keep it small and readable.
- Parameterise SQL, validate input server-side, escape output in templates.
- Never hardcode secrets; read `OPENAI_API_KEY` from the environment if needed.

> In Lab 2 these rules are enforced automatically by the agents and skills in the
> `agents-and-skills/` workspace. Here, every one of them is on you to type.
