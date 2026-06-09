# Bonus Rapid — Makan Mana with Accounts (Auth + Multi-User)

**Goal:** upgrade the Makan Mana group-vote app from "anyone with the link" to a real
**multi-user app with accounts** — sign up, log in, log out, and polls that belong to the
user who made them. Auth is the single richest security surface in the whole workshop, so
this is where the `security-review` skill earns its keep.

> **Prerequisite:** finish `RAPID-makan-vote.md` first — you're extending that app.
> **Workspace:** open the **`agents-and-skills/`** folder. Build into `projects/makan-vote/`.

---

## What "multi-user" adds

- **Accounts:** email/username + password, with a proper password **hash** (never plaintext).
- **Sessions:** stay logged in across requests; log out clears it.
- **Ownership:** each poll has an `owner_id`. Only the owner can edit/close/delete their poll.
- **Identity-based voting:** one vote **per logged-in user** per poll (replaces the
  cookie/token guest rule). Optionally still allow guest voting via the share link.
- **"My polls":** a logged-in user sees the polls they created.

---

## Prompts (run in order)

1. **PRD the upgrade (don't skip — auth has many decisions):**
   > Use the prd-expander skill on: "add user accounts to the makan-vote app — sign up, log
   > in, log out; polls belong to their creator; one vote per logged-in user per poll;
   > a 'my polls' page." Make the data model and the access-control rules explicit (who can
   > do what to which poll). Confirm the PRD with me.

2. **Mockup the new screens:**
   > Use the ui-mockup skill to add sign-up, log-in, and "my polls" screens to
   > `projects/makan-vote/mockup.html`. Include the logged-in vs logged-out header states and
   > the auth error states (wrong password, email already taken).

3. **Implement the auth UI:**
   > frontend_design_agent: implement the sign-up, log-in, log-out, and "my polls" screens as
   > Flask templates in `projects/makan-vote/`. Show the logged-in user in the header with a
   > log-out button; hide owner-only actions (edit/close/delete) when not the owner.

4. **Build the backend (auth + ownership):**
   > coding_agent: add a users table and auth to `projects/makan-vote/`.
   > - Hash passwords with `werkzeug.security` (`generate_password_hash` /
   >   `check_password_hash`). Never store or log plaintext.
   > - Use Flask server-side sessions for login state; a `@login_required` decorator for
   >   protected routes.
   > - Add `owner_id` to polls; enforce that only the owner can edit/close/delete.
   > - Enforce one vote per logged-in user per poll at the database level (a unique
   >   constraint on (poll_id, user_id)), not just in the UI.
   > - Add a couple of pytest tests: signup+login happy path, and a rejection test (a
   >   non-owner cannot delete someone else's poll).
   > Update the project's own Docker files if needed so it still runs with
   > `cd projects/makan-vote && docker compose up`.

5. **Security pass — this is the main event:**
   > Use the security-review skill on `projects/makan-vote/`. Run `scripts/scan.py` first,
   > then walk the checklist with auth in focus:
   > - Passwords hashed (not plaintext, not reversible)?
   > - Session cookie flags set (`HTTPONLY`, `SECURE` where applicable, `SameSite`)?
   > - **Broken access control / IDOR:** can a logged-in user edit/delete a poll they don't
   >   own by changing the id? Can they vote twice by replaying the request?
   > - **Auth bypass:** are all owner-only and login-only routes actually protected
   >   server-side (not just hidden in the template)?
   > - No user enumeration leak ("wrong password" vs "no such user" giving it away)?
   > - `SECRET_KEY` read from the environment, not hardcoded?
   > Fix every finding and point at the lines.

---

## Run it

```bash
cd projects/makan-vote
docker compose up                     # then open http://localhost:5000
docker compose run --rm app pytest
```

Set a session secret in your `.env` (don't hardcode it):

```
SECRET_KEY=<any long random string for the workshop>
```

---

## The auth security checklist (cheat sheet)

| Check | Why it matters | Where the skill covers it |
|-------|----------------|---------------------------|
| Passwords **hashed** (`werkzeug.security`) | A DB leak shouldn't reveal passwords | checklist §7 Secrets |
| **Access control** on every owner-only route, server-side | Hidden buttons aren't security | checklist §6 IDOR |
| One-vote enforced by a **DB unique constraint** | UI checks are bypassable | checklist §1 + §6 |
| Session **cookie flags** (HTTPOnly/SameSite) | Defends the login cookie | checklist §6/§8 |
| **`SECRET_KEY`** from env | Forgeable sessions if it leaks/defaults | checklist §7 |
| No **user enumeration** in error text | Don't help attackers map accounts | checklist §8 |

---

## What to notice

- **Auth multiplies the attack surface.** The same skill that found XSS in poll options now
  finds auth bypass and IDOR — the loop scales with complexity.
- **Server-side is the only side that counts.** Hiding the delete button is UX; the
  ownership check on the route is security.
- You reused the **exact same agents and skills** — no new setup — to add the most
  security-sensitive feature in the workshop.
