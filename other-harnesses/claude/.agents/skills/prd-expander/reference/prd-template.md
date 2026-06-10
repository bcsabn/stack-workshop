# PRD Template (fill this in)

Copy this whole block into `projects/<name>/PRD.md` and replace every `[…]`. Keep it under
one page. Delete the helper notes in _italics_ once you've used them.

---

# PRD: [App / feature name]

## 1. Summary
[One sentence: what we are building and for whom.]
_e.g. "A single-household pantry tracker that warns me before food expires."_

## 2. User stories
_Write 3–6. Every line is `As a [who], I want [what], so that [why]`._

- As a [home cook], I want to [add an item with an expiry date], so that [I don't forget it exists].
- As a [home cook], I want to [see what expires in the next 3 days], so that [I use it before it's wasted].
- As a [home cook], I want to [mark an item used or thrown out], so that [my list stays accurate].

## 3. Functional requirements
_Concrete, checkable behaviours. If you can't write a test for it, it's too vague._

- [Add an item: name, quantity, expiry date.]
- [List all items, soonest-expiry first, showing days remaining.]
- [Flag items expiring within 3 days.]
- [Mark an item "used" or "thrown out" (removed from the active list).]
- [Data persists across a container restart (SQLite file).]

## 4. Data model
_Entities, fields, types — and the validation rule for each field. The rule is the spec._

**Item**
| Field | Type | Rule |
|-------|------|------|
| id | integer | auto, primary key |
| name | text | required, 1–80 chars, escaped on render |
| quantity | integer | required, ≥ 1 |
| expiry_date | date (YYYY-MM-DD) | required, a real date, not in the past |
| status | text | one of: active / used / thrown_out |
| created_at | timestamp | set by server |

## 5. Out of scope
_What we are deliberately NOT building. A non-empty list here is how you protect the session._

- [No user accounts / multi-user — single household.]
- [No barcode scanning.]
- [No notifications/email — on-screen flags only.]

## 6. Acceptance checks
_How a tester confirms it works. These become your pytest tests and manual click-through._

- [ ] Adding a valid item shows it in the list.
- [ ] An item expiring tomorrow is flagged; one expiring next month is not.
- [ ] Blank name, quantity 0, and a past date are each rejected with a friendly message.
- [ ] Restarting the container keeps the data.
- [ ] A name like `<script>alert(1)</script>` renders as text, not script.

## 7. Open questions (for the human)
_Anything you had to guess. Ask before building._

- [ ] [Is there an AI "natural-language add" step in v1, or later?]
- [ ] [Any limit on number of items?]

---

## If the app has an AI feature
Add this mini-section so security is planned, not bolted on:

- **What the model does:** [e.g. parse "2 tofu, expires Friday" into name/qty/date.]
- **Input trust:** the user's phrase is **untrusted data**, never an instruction.
- **Output validation:** the model returns JSON; validate shape + ranges (same rules as the
  data model) **before** saving. Reject and ask again on mismatch.
- **Key handling:** `OPENAI_API_KEY` read from the environment, never hardcoded, never logged.
