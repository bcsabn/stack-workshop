# Design Checklist — anti-slop + accessibility

A short, opinionated checklist for workshop mockups. You don't need to be a designer; you
need to avoid the handful of things that make a UI look auto-generated and unusable.

## The AI-slop fingerprints (avoid these)

These are the tells that say "an AI made this in 2024". Skip them:

- ❌ **Purple→blue gradients on a dark background** with neon/cyan accents. The default AI look.
- ❌ **Pure black (`#000`) or pure white (`#fff`).** Always tint slightly toward your accent.
  Pure black/white never appears in nature and reads as "untouched default".
- ❌ **Everything in a card.** Not every block needs a bordered, shadowed container.
  And never nest a card inside a card.
- ❌ **Identical card grids** — same-sized box with an icon + heading + text, repeated forever.
- ❌ **A big rounded icon above every heading.** Rarely adds meaning; makes it look templated.
- ❌ **Gradient text** on headings or numbers. Decorative, not meaningful.
- ❌ **Glassmorphism everywhere** (blur + glass + glow) used as decoration.
- ❌ **Monospace font as shorthand for "techie".** Lazy.
- ❌ **Everything centered.** Left-aligned text with a little asymmetry feels more designed.

## Do this instead

- ✅ **One accent colour, used with intent** + a neutral tinted toward it. Dominant colour
  with a sharp accent beats a timid, evenly-grey palette.
- ✅ **A type hierarchy from weight and size** — one heading scale, one body size, bold for
  emphasis. One or two fonts max.
- ✅ **Spacing rhythm** — group related things tightly, separate sections generously. Varied
  padding, not the same gap everywhere.
- ✅ **Empty states that teach** — "Add your first item to start tracking expiries" beats
  "No items".
- ✅ **Button hierarchy** — one primary action per screen; everything else is secondary
  (outline) or a plain text link. Not every button is blue-and-filled.

## Accessibility (non-negotiable, and easy)

- ✅ Every input has a real `<label for="…">` (not just placeholder text).
- ✅ Heading order makes sense: one `<h1>` per screen, then `<h2>`, `<h3>` — don't skip levels.
- ✅ Text contrast passes WCAG AA: ~4.5:1 for body text. Light-grey-on-white fails — darken it.
- ✅ Interactive elements show a **visible focus ring** (don't remove the outline).
- ✅ Don't rely on colour alone to signal state — pair red with an icon or the word "Error".
- ✅ Buttons are `<button>`, links are `<a>`. A clickable `<div>` is not keyboard-reachable.

## Tailwind quick reference (CDN, no build)

| Want | Classes |
|------|---------|
| Page background, tinted | `bg-slate-50 text-slate-800` |
| Primary button | `bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-indigo-400` |
| Secondary button | `border border-slate-300 hover:bg-slate-100 rounded-lg px-4 py-2` |
| Input | `border border-slate-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-indigo-400 focus:outline-none` |
| Error text | `text-red-600 text-sm` |
| Card (use sparingly) | `bg-white border border-slate-200 rounded-xl p-5` |
| Section rhythm | `space-y-8` between sections, `space-y-2` within a group |
| Container | `max-w-2xl mx-auto px-4 py-8` |

## The two-second review

Before you hand the mockup over, ask:
1. **Would someone ask "how was this made?" or "which AI made this?"** Aim for the first.
2. **Can I tab through every control and see where focus is?**
3. **Is there exactly one obvious primary action per screen?**
