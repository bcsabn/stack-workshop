# Rapid Build — Makan Mana (Group Vote)

**Goal:** a small group-voting app that reuses **all** the agents and skills. Create a
poll for "where should we eat?", share a link, friends vote, everyone sees live results.

> **Workspace:** open the **`agents-and-skills/`** folder. Build into `projects/makan-vote/`.

---

## Prompts (run in order)

1. **PRD from a one-liner:**
   > Use the prd-expander skill on: "a group vote for where to eat — create a poll, share a
   > link, friends vote, see live results".

2. **Mockup + UI:**
   > frontend_design_agent + ui-mockup: the create, vote, and results screens in
   > `projects/makan-vote/`. Cover empty and error states too.

3. **Backend (with its own Docker setup):**
   > coding_agent: poll + vote model, a shareable poll link, results endpoint. One vote per
   > visitor (cookie or token). Generate the project's own `Dockerfile`,
   > `docker-compose.yml` (serving on http://localhost:5000), and `requirements.txt` inside
   > `projects/makan-vote/` so it runs with `cd projects/makan-vote && docker compose up`.

4. **Security pass (the important one here):**
   > Use the security-review skill on `projects/makan-vote/`, focusing on IDOR on the share
   > link, vote tampering, and XSS in poll options. Run `scripts/scan.py` first, then walk
   > the checklist and fix the findings.

---

## Run it

```bash
cd projects/makan-vote
docker compose up          # then open http://localhost:5000
```

---

## Optional AI step (suggest options)

> coding_agent: suggest 4 makan options from a vibe like "cheap, halal, near Gadong".

Reminders the agents already know (from `AGENTS.md`): read `OPENAI_API_KEY` from the
environment, never hardcode it, and treat both the vibe text and the model's suggestions as
**untrusted** — fence the vibe as data, validate the JSON shape, and escape the options
before they are stored or shown.

---

## What to notice

- **Security mattered most here** (share links, vote integrity, user-supplied options) and
  the security-review skill gave you a focused checklist — plus a scanner — instead of guesswork.
- The **share-link IDOR** is the headline lesson: sequential ids (`/poll/1`, `/poll/2`) leak
  every poll; an unguessable token fixes it. See the skill's `reference/checklist.md` §6.
- By now the **agents + skills loop is muscle memory**: PRD → mockup → UI → backend → review.
