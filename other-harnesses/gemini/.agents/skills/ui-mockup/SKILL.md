---
name: ui-mockup
description: Turn a PRD or feature description into a single static HTML + Tailwind (CDN) mockup with no backend, so the UI is agreed before any logic is wired. Use right after a PRD and before the frontend_design_agent implements anything.
---

# UI Mockup Generator

A mockup is the cheapest way to be wrong. You build one static HTML file, the human looks at
it, you adjust — all before a single route or database table exists. Changing a layout in a
mockup costs seconds; changing it after the backend is wired costs an hour.

> **No real behaviour here.** No backend, no database, no fetch calls, no JS framework.
> Realistic *placeholder* content only. This is for visual sign-off.

## What you produce

ONE self-contained file: `projects/<name>/mockup.html`.

- **Tailwind via CDN** (`<script src="https://cdn.tailwindcss.com"></script>`), no build step.
- **Every screen and state** the PRD implies — not just the happy path. See the checklist below.
- **Realistic placeholder content** (real-sounding item names, a few rows, a filled form)
  so the layout reads the way it will in real life. Three lorem-ipsum rows hide layout bugs.
- **Accessible by default:** real `<label>`s, sensible heading order, visible focus, text
  contrast that passes (see [`reference/design-checklist.md`](reference/design-checklist.md)).

## Cover every state (the bit beginners skip)

For each screen, mock all of these — empty and error states are where real apps fall apart:

- **List / data view** — with several rows of believable data.
- **Empty state** — what the user sees on day one (and make it *teach* the next action,
  not just say "nothing here").
- **Add / edit form** — every field from the PRD's data model, with its label.
- **Validation error** — show what a rejected field looks like (red text, message).
- **Result / confirmation** — the "it worked" moment (results page, success banner).

## Make it not look like AI slop

A mockup that screams "an AI made this" undersells the workshop. Spend two minutes on a
point of view. Quick wins (full list in [`reference/design-checklist.md`](reference/design-checklist.md)):

- **Pick one accent colour** and a tinted neutral — not pure `#000`/`#fff`, not the
  purple-to-blue-gradient-on-dark cliché.
- **Vary spacing for rhythm** — tight groups, generous separations. Not the same padding everywhere.
- **Don't wrap everything in a card.** Don't nest cards in cards. Flatten the hierarchy.
- **Establish type hierarchy** with weight and size, not five different fonts.
- **Real labels and microcopy**, not "Lorem ipsum" and not "Submit" on every button.

The test: *would someone ask "how was this made?" rather than "which AI made this?"*

## How to run it

1. Read the PRD (or the feature description) and list every screen + state it implies.
2. Start from [`scripts/mockup_starter.html`](scripts/mockup_starter.html) — it already has
   the Tailwind CDN tag, a tinted palette, and a layout skeleton.
3. Build each screen as a section in the one file. Stack them top-to-bottom with a small
   label above each ("— Empty state —") so the human can review them all at once.
4. **Note which parts are placeholder** vs real (a short comment list at the top of the file).
5. Hand the agreed mockup to `frontend_design_agent` to implement as real Flask templates.

## Done criteria

- One file, `projects/<name>/mockup.html`, opens standalone in a browser.
- Every screen *and* its empty + error states are shown.
- Every form field from the PRD's data model has a real `<label>`.
- It has a clear visual point of view (one accent, intentional spacing, type hierarchy).
- A note at the top lists what's placeholder.

## Reference material

- [`reference/design-checklist.md`](reference/design-checklist.md) — the anti-slop + a11y checklist.
- [`scripts/mockup_starter.html`](scripts/mockup_starter.html) — copy-to-start skeleton with Tailwind CDN.
