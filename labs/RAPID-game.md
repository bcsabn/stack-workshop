# Rapid Build — Bangkatan Rooftop Run (Brunei Web Game)

**Goal:** a fun, frontend-led build that reuses the same agents and skills. A one-screen
canvas game, no real backend, built mostly by the `frontend_design_agent`.

The game: a **bangkatan** (proboscis monkey) hops across the rooftops of **Kampong Ayer**
collecting bananas. One mechanic (hop / jump), shapes or emoji for art, single HTML file.

> **Workspace:** open the **`agents-and-skills/`** folder. Build into `projects/game/`.

---

## Prompts (run in order)

1. **(Optional) shape the idea:**
   > Use the prd-expander skill on: "a one-screen browser game: a bangkatan hops Kampong Ayer
   > rooftops collecting bananas, score goes up, one jump mechanic, no backend."

2. **Build the game:**
   > frontend_design_agent: build a single-screen HTML5 canvas game in `projects/game/` —
   > a bangkatan (proboscis monkey) hopping across Kampong Ayer rooftops collecting bananas.
   > One mechanic: press Space / tap to jump. Use shapes or emoji for art, no image assets.
   > Score on screen, simple game-over and restart. One self-contained HTML file served by
   > Flask. No backend, no build step.
   >
   > Also generate the project's own `Dockerfile`, `docker-compose.yml` (serving on
   > http://localhost:5000), and `requirements.txt` inside `projects/game/`, so it runs with
   > `cd projects/game && docker compose up`.

3. **Light security pass (only if you add a leaderboard):**
   > Use the security-review skill on `projects/game/`, focused on any leaderboard/name
   > input: validate and escape the player name, parameterise any SQL, no XSS.

---

## Run it

```bash
cd projects/game
docker compose up          # then open http://localhost:5000
```

Keep it to a **single HTML file** served by a tiny Flask route (render it or serve it
static). Docker is **per app** — the files live in `projects/game/`.

## What to notice

- The **same subagents and skills** from Lab 2 carried over with zero new setup.
- A frontend-heavy app barely touched the backend — the right agent did the right job.
- The agent generated the per-app Docker files on its own, because `AGENTS.md` told it to.
