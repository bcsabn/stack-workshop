---
name: prd-expander
description: Turn a one-line feature request into a short, structured product requirements doc (PRD) before any code is written. Use at the start of a build when the requirement is vague, one sentence, or you are not yet sure what "done" looks like.
---

# PRD Expander

A vague request ("a pantry tracker", "a group vote app") hides a dozen decisions. This
skill drags those decisions into the open *before* a single line of code is written, so the
build agents have an unambiguous target and you have a checklist for "done".

> **You do not write code in this skill.** You produce a one-page plan and get the human to
> sign off on it. Building comes after.

## When to reach for it

- The request is one sentence or fuzzy.
- You are about to start a new app or a sizeable feature.
- Two people would read the request and picture different apps.

If the task is tiny and obvious (a copy tweak, a colour change), skip the PRD — don't
ceremony-wrap trivial work.

## How to run it

1. **Read the one-liner and the repo's `AGENTS.md`** so the PRD respects the house stack
   (Python 3.12 + Flask + SQLite, Tailwind via CDN, Docker per app, no secrets hardcoded).
2. **Fill the template** in [`reference/prd-template.md`](reference/prd-template.md). Keep
   the whole thing under one page — this is a workshop app, not an enterprise rollout.
3. **Make every assumption explicit.** If you have to guess the DB, the auth model, or
   whether there's an AI feature, say so out loud in *Open questions* rather than silently
   deciding.
4. **End by asking the human to confirm or adjust.** Do not proceed to building until they
   say go.

## The six sections (what good looks like)

| Section | What it pins down | Beginner trap it avoids |
|---------|-------------------|-------------------------|
| **Summary** | One sentence: what + for whom | Building the wrong thing politely |
| **User stories** | 3–6 `As a…, I want…, so that…` | Features with no user behind them |
| **Functional requirements** | Concrete, testable behaviours | "It should be nice" hand-waving |
| **Data model** | Entities, fields, types | Schema churn halfway through the build |
| **Out of scope** | What you're *not* doing | Scope creep eating the whole session |
| **Acceptance checks** | How you'll know it works | "Looks done" with no proof |

See [`reference/good-vs-vague.md`](reference/good-vs-vague.md) for side-by-side examples of
weak vs strong entries in each section.

## Security & trust, baked in from line one

A PRD is the cheapest place to catch a security problem — before it's code.

- For **every input field**, the data-model row should already note its validation rule
  (type, length, range, required-ness). "name: text" is weak; "name: text, 1–80 chars,
  required" is a spec the build agent can't skip.
- If the feature has an **AI step** (parse free text, suggest options), the PRD must state
  that the model's input is **untrusted data** and its JSON output gets **validated before
  storage**. Flag it now so `security-review` isn't surprised later.
- If records are addressable by id or link, note **who is allowed to see each one** —
  that's where IDOR bugs are born.

## Helper script

Generate a blank, pre-sectioned PRD file to fill in:

```bash
python .agents/skills/prd-expander/scripts/new_prd.py "pantry tracker with expiry alerts"
# writes projects/<slug>/PRD.md with all six sections stubbed
```

The script only scaffolds the file — you still do the thinking.

## Done criteria

- A one-page PRD exists with all six sections filled (no `[TODO]` left).
- Every data field carries its validation rule.
- Any AI step names its untrusted-input / validated-output handling.
- Out-of-scope list is non-empty (you decided what *not* to build).
- You asked the human to confirm before building.

## Reference material

- [`reference/prd-template.md`](reference/prd-template.md) — the fill-in template.
- [`reference/good-vs-vague.md`](reference/good-vs-vague.md) — weak vs strong examples.
- [`scripts/new_prd.py`](scripts/new_prd.py) — scaffold a blank PRD into a project folder.
