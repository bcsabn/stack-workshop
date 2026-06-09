# Lab 1 — Pantry Tracker (Plain Prompting)

**Goal:** build a small pantry tracker the "type everything yourself" way — no agents,
no skills. This is the baseline. Notice how much context *you* have to carry.

> **Workspace:** open the **`codex-only/`** folder for this lab.
> Do **not** use any subagents or skills. Just talk to Codex directly.

---

## Starting prompt (copy-paste)

> Build a small Flask pantry tracker in `projects/pantry/`. It should let me add an item
> with a name, quantity, and expiry date; list items; flag items expiring within 3 days;
> mark an item used or thrown out; and persist to SQLite so data survives a restart.
> Plain HTML, a little Tailwind via CDN. Keep it in one or two files.
>
> The project must be self-contained: also generate its own `Dockerfile`,
> `docker-compose.yml` (serving on http://localhost:5000), and `requirements.txt`
> (flask, pytest) **inside `projects/pantry/`**, so I can run it with
> `cd projects/pantry && docker compose up`.

---

## Follow-up prompts (run them in order — feel the friction)

1. **Re-explaining context it forgot:**
   > Remember this is the pantry app in `projects/pantry/` using SQLite — don't start a
   > new project. Now make the expiry list sort soonest-first and show how many days are left.

2. **Adding the validation it skipped:**
   > It accepts blank names and negative quantities, and it crashes on a bad date. Add
   > server-side validation: name required (1–80 chars), quantity a positive integer,
   > expiry a real date not in the past. Show a friendly error, don't leak a stack trace.

3. **Keeping the style consistent:**
   > The "mark used" page looks nothing like the list page. Make all pages share the same
   > Tailwind layout, header, and button styles.

4. **Plugging a security gap you noticed yourself:**
   > Double-check the SQL is parameterised and the item name is escaped when rendered, so a
   > name like `<script>alert(1)</script>` can't run. Fix it if it isn't.

---

## Run it

```bash
cd projects/pantry
docker compose up          # then open http://localhost:5000
```

(Docker is **per app** — the files live in `projects/pantry/`, not at the repo root.)

---

## What to notice

- You had to **re-state context** ("the pantry app", "use SQLite", "don't start over")
  more than once.
- The model **skipped validation and consistency** until you explicitly asked.
- **Security was on you** to remember and request.
- You even had to remember to ask for the **Docker files**.
- There was **no reusable workflow** — every instruction was bespoke typing.

Lab 2 rebuilds the same app in the **`agents-and-skills/`** workspace, where the PRD, the UI
mockup, the build split, the Docker files, and the security pass all come from **agents and
skills** you can reuse across every later project.
