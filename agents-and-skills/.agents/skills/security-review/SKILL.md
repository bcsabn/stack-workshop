---
name: security-review
description: Review generated code against a focused security checklist before you call it done. Use after writing any route, form, template, SQL query, or AI integration — especially anything that touches user input, shareable links, or model output.
---

# Security Review

LLM-generated code is fast but trusting — it tends to skip validation, forget to escape
output, and treat anything text-shaped as safe. This skill is the gate before "done": a
focused pass that catches the handful of bugs that actually bite small Flask apps.

> **You report, you don't rewrite.** Point at the lines that matter and give the fix. Don't
> refactor the whole app — that hides the lesson and risks new bugs.

## How to run it

1. **Scope it.** Review the changed files (or the named folder). For a fast first pass, run
   the helper to surface obvious smells, then read the flagged lines yourself:
   ```bash
   python .agents/skills/security-review/scripts/scan.py projects/<name>
   ```
   The script is a *smell detector*, not a judge — it greps for risky patterns (string-built
   SQL, `|safe`, `eval`, hardcoded keys). You confirm each hit by reading the code.
2. **Walk the checklist below, in order.** It's ordered by how often each bug shows up in
   LLM-written Flask apps.
3. **Report every finding as `Issue · Risk · Fix`** with a `file:line` pointer. Use the
   format in [`reference/report-format.md`](reference/report-format.md).
4. **If nothing is wrong, say so explicitly** — "checked X, Y, Z; no issues". Silence isn't
   a pass.

## The checklist (ordered by how often it bites)

1. **Input validation** — is every field checked server-side: type, length, range,
   required-ness, date sanity? Reject bad input with a friendly message. *Client-side checks
   don't count — they're trivially bypassed.*
2. **SQL injection** — is every query **parameterised** (`?` placeholders / bound params)?
   Any query built by string concatenation or f-strings with user data is a finding.
3. **XSS / output escaping** — is dynamic content escaped in templates? Jinja autoescapes by
   default — flag every `| safe`, `Markup(...)`, and `{% autoescape false %}` over user data.
4. **Prompt injection** (AI features) — is text the model reads (notes, vote options, fetched
   content) treated as **data, not instructions**? Could a crafted note hijack the model's
   behaviour? Keep the user's text in a clearly-fenced data slot, never concatenated into the
   instruction.
5. **Untrusted model output** — is model-returned JSON **validated (shape + ranges)** before
   it's stored or rendered? Never `eval`/`exec` it; never trust it to be well-formed.
6. **Access control / IDOR** — can a user reach someone else's record by guessing or editing
   an id or share link? Are share tokens unguessable (not `poll/1`, `poll/2`…)? Is one
   vote-per-visitor actually enforced server-side?
7. **Secrets** — no hardcoded keys/tokens anywhere; `OPENAI_API_KEY` read from the
   environment; nothing secret written to logs or returned in responses.
8. **Error handling** — no stack traces, SQL errors, or file paths leaked to the user.
   `FLASK_DEBUG` is off in anything shared. Errors are friendly, internals stay server-side.

Full explanation + a vulnerable-vs-fixed code example for each item is in
[`reference/checklist.md`](reference/checklist.md).

## Severity (keep it simple)

- **High** — exploitable now: SQL injection, stored XSS, IDOR exposing other users' data,
  a leaked/ hardcoded key.
- **Medium** — missing validation, unescaped output not yet reachable, debug mode on.
- **Low** — defence-in-depth, hardening, nice-to-have.

Lead your report with the High findings.

## Done criteria

- Every changed route, form, template, query, and AI call has been walked against the checklist.
- Each finding is `Issue · Risk · Fix` with a `file:line`.
- Findings are ordered by severity, High first.
- If clean, that's stated explicitly per checklist area — not left implied.
- Fixes point at specific lines; the whole app was not rewritten.

## Reference material

- [`reference/checklist.md`](reference/checklist.md) — each check with vulnerable→fixed examples.
- [`reference/report-format.md`](reference/report-format.md) — the `Issue · Risk · Fix` format + a sample report.
- [`scripts/scan.py`](scripts/scan.py) — grep-based smell detector for a fast first pass.
