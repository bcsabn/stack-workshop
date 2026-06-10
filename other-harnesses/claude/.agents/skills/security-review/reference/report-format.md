# Report Format — Issue · Risk · Fix

Keep findings short, specific, and actionable. One finding = one problem at one location.

## The shape of one finding

```
[SEVERITY] Issue: <what is wrong, in one line>
  Location: <file:line>
  Risk:     <what an attacker/user could do because of it>
  Fix:      <the concrete change — point at the line, don't rewrite the app>
```

## Severity tags

- **[HIGH]** — exploitable now (SQLi, stored XSS, IDOR exposing other users, leaked key).
- **[MED]**  — missing validation, unescaped-but-not-yet-reachable output, debug on.
- **[LOW]**  — hardening / defence-in-depth.

Order the report High → Med → Low.

## Sample report

> **Security review — `projects/makan-vote/`**
>
> **[HIGH] Issue:** Poll share links use sequential ids.
> Location: `app.py:42`
> Risk: Anyone can enumerate `/poll/1`, `/poll/2`, … and read or vote on every poll (IDOR).
> Fix: Replace the integer id in the URL with `secrets.token_urlsafe(12)` stored as a
> `token` column; look polls up by token, not id.
>
> **[HIGH] Issue:** Poll option rendered with `| safe`.
> Location: `templates/results.html:18`
> Risk: A poll option like `<script>…</script>` runs in every voter's browser (stored XSS).
> Fix: Remove `| safe`; let Jinja autoescape (`{{ option.text }}`).
>
> **[MED] Issue:** Vote endpoint doesn't validate the option id belongs to the poll.
> Location: `app.py:67`
> Risk: A crafted POST can add a vote to an option from a different poll.
> Fix: `WHERE option_id = ? AND poll_id = ?` before counting the vote.
>
> **[LOW] Issue:** `FLASK_DEBUG=1` in the compose file.
> Location: `docker-compose.yml:9`
> Risk: If shared, visitors get stack traces and an interactive console.
> Fix: Drop it (or set `0`) for anything beyond your own machine.
>
> **Checked and clean:** SQL is parameterised throughout (`app.py`); `OPENAI_API_KEY` is
> read from the environment, not hardcoded.

## Rules

- Always include the **Checked and clean** line — it shows what you actually looked at.
- If everything is clean, the whole report is the clean line(s). Don't invent findings.
- Don't rewrite the app. Each Fix points at the line(s) that change.
