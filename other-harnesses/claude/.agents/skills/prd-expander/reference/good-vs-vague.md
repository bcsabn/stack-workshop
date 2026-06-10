# Good vs Vague — PRD entries side by side

The difference between a PRD that helps and one that doesn't is *specificity*. Here's what
weak and strong look like in each section. Aim for the right-hand column.

## Summary

| 🚫 Vague | ✅ Good |
|----------|--------|
| "An app to manage food." | "A single-household pantry tracker that warns me before food expires." |

_Why:_ the good one names the user (one household) and the point (expiry warnings). The
build agent now knows what to optimise for.

## User stories

| 🚫 Vague | ✅ Good |
|----------|--------|
| "User can manage items." | "As a home cook, I want to see what expires in 3 days, so that I use it before it's wasted." |

_Why:_ a real actor, a real action, a real reason. "Manage" hides five different features.

## Functional requirements

| 🚫 Vague | ✅ Good |
|----------|--------|
| "Handle expiry nicely." | "List items soonest-expiry first, showing days remaining; flag anything within 3 days." |

_Why:_ the good one is testable. You can write a pytest for "within 3 days"; you can't test
"nicely".

## Data model

| 🚫 Vague | ✅ Good |
|----------|--------|
| `name: text` | `name: text — required, 1–80 chars, escaped on render` |
| `quantity: number` | `quantity: integer — required, ≥ 1` |
| `expiry: date` | `expiry_date: date (YYYY-MM-DD) — required, real date, not in the past` |

_Why:_ the validation rule **is** the spec. Without it, the build agent guesses, and the
guess is usually "no validation".

## Out of scope

| 🚫 Vague | ✅ Good |
|----------|--------|
| (section left empty) | "No accounts, no barcode scanning, no email notifications." |

_Why:_ an empty out-of-scope list is how a 30-minute app becomes a 3-hour app. Decide what
you're *not* doing.

## Acceptance checks

| 🚫 Vague | ✅ Good |
|----------|--------|
| "It works." | "Blank name, quantity 0, and a past date are each rejected with a friendly message." |

_Why:_ "it works" can't fail a review. The good check is a click you can actually perform.

---

## The one-line test

For any line in your PRD, ask: **"Could two engineers read this and build different
things?"** If yes, it's still too vague — add the constraint that removes the ambiguity.
