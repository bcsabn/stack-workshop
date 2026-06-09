# Lab 2 — Pantry Tracker (Agents + Skills)

**Goal:** rebuild the Lab 1 pantry tracker, but drive the whole workflow with the
**subagents** (`coding_agent`, `frontend_design_agent`) and **skills** (`prd-expander`,
`ui-mockup`, `security-review`) shipped in this repo. Same app, far less typing — and the
workflow is reusable for every later project.

> **Workspace:** open the **`agents-and-skills/`** folder for this lab (it contains
> `.codex/agents/`, `.agents/skills/`, and `AGENTS.md`).
> Build into `projects/pantry/`. You can clear it first if you like.

---

## Prompts (run in order)

1. **Expand the one-liner into a PRD:**
   > Use the prd-expander skill on: "a pantry tracker with expiry alerts". Confirm the PRD
   > with me.
   >
   > _(Tip: the skill ships `scripts/new_prd.py` to scaffold the file, and a
   > `reference/good-vs-vague.md` so the PRD is specific, not fuzzy.)_

2. **Agree the UI before any logic:**
   > Use the ui-mockup skill to turn that PRD into `projects/pantry/mockup.html`. Cover the
   > list, empty, add-form, error, and success states.

3. **Implement the UI:**
   > frontend_design_agent: implement the mockup as Flask templates in `projects/pantry/`.

4. **Build the backend (with its own Docker setup):**
   > coding_agent: build the SQLite model, routes, expiry logic, and a couple of pytest
   > tests for `projects/pantry/`. Also generate the project's own `Dockerfile`,
   > `docker-compose.yml` (serving on http://localhost:5000), and `requirements.txt` inside
   > `projects/pantry/` so it runs with `cd projects/pantry && docker compose up`.

5. **Security pass:**
   > Use the security-review skill on everything in `projects/pantry/`. Run its
   > `scripts/scan.py` first, then walk the checklist. Fix what it finds.

---

## Run it

```bash
cd projects/pantry
docker compose up          # then open http://localhost:5000
docker compose run --rm app pytest
```

---

## Optional AI step (natural-language add)

> coding_agent: add a natural-language add box ("2 tofu, expires Friday") that parses to
> fields; validate the parsed JSON before saving.

Reminders the agents already know (from `AGENTS.md`): read `OPENAI_API_KEY` from the
environment, never hardcode it, and treat the typed phrase as **untrusted data** — fence it
as data, never instructions, and validate the parsed shape and value ranges before it
touches SQLite.

---

## What changed vs Lab 1

- The **PRD skill** captured scope, the data model with validation rules, and acceptance
  checks up front — no more mid-build "wait, also...".
- The **mockup skill** got UI sign-off *before* logic, so there was no restyling churn.
- The **two subagents** split backend and frontend cleanly; each already knew the house
  rules, so validation, escaping, and the **per-app Docker files** came for free — you didn't
  have to ask.
- The **security-review skill** made the security pass a one-liner (plus a script) instead of
  something you had to remember to do.
- Everything here is **reusable** — the Rapid Build labs use the exact same agents and
  skills with no new setup.
