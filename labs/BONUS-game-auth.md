# Bonus Rapid — Bekantan Rooftop Run with Accounts (Auth + Multi-User Leaderboard)

**Goal:** turn the single-player Bekantan game into a **multi-user** game: players sign up,
log in, and their scores go to a **shared leaderboard** tied to their account. This is where
the game stops being pure frontend and grows a real (small) backend — and a brand-new
attack surface: **score submission you must not trust.**

> **Prerequisite:** finish `RAPID-game.md` first — you're extending that game.
> **Workspace:** open the **`agents-and-skills/`** folder. Build into `projects/game/`.

---

## What "multi-user" adds

- **Accounts:** username + password (hashed), log in / log out.
- **Per-user scores:** every run's score is saved against the logged-in user.
- **Global leaderboard:** top scores across all players, showing who's who.
- **"My best":** a logged-in player sees their personal high score.
- **The trust problem:** the score arrives from the browser, where the player controls
  everything. You can't fully stop cheating in a client-side game, but you **can** validate,
  rate-limit, and require login — and you must never trust the number blindly.

---

## Prompts (run in order)

1. **PRD the upgrade:**
   > Use the prd-expander skill on: "add accounts and a shared leaderboard to the bekantan
   > game — sign up, log in; save each run's score to the logged-in user; show a global top-10
   > and the player's personal best." Make the data model explicit and call out that the
   > submitted score is **untrusted input from the browser**. Confirm the PRD with me.

2. **Mockup the new screens:**
   > Use the ui-mockup skill to add sign-up, log-in, a leaderboard panel, and a "your best
   > score" badge to the game's UI in `projects/game/`. Include logged-in vs logged-out states
   > and the auth error states.

3. **Implement the UI:**
   > frontend_design_agent: add the sign-up / log-in / log-out UI and a leaderboard panel to
   > `projects/game/`. Keep the game itself one screen; show the player's name and best score
   > in the header when logged in. Escape every player name on the leaderboard (no XSS via
   > usernames).

4. **Build the backend (auth + scores):**
   > coding_agent: add to `projects/game/`:
   > - A users table; password hashing with `werkzeug.security`; Flask sessions; a
   >   `@login_required` decorator.
   > - A `scores` table (user_id, score, created_at) and a `POST /api/score` endpoint that
   >   **requires login** and saves the run's score.
   > - **Validate the submitted score server-side**: it's an integer, within a sane range,
   >   and reject anything absurd. Treat the value as untrusted browser input, not as truth.
   > - Basic anti-abuse: rate-limit how often one user can submit (e.g. one save per finished
   >   run / per N seconds).
   > - A `GET /api/leaderboard` (global top-10) and the player's personal best.
   > - A couple of pytest tests: login-required on `/api/score`, and a rejection test for a
   >   non-integer / out-of-range score.
   > Update the project's Docker files if needed so it runs with
   > `cd projects/game && docker compose up`.

5. **Security pass — focus on the trust boundary:**
   > Use the security-review skill on `projects/game/`. Run `scripts/scan.py` first, then walk
   > the checklist with these in focus:
   > - **Untrusted client input:** is the score validated (type + range) before storing? Is
   >   `/api/score` login-protected so anonymous/forged posts can't spam the board?
   > - **XSS via usernames** on the leaderboard — every name escaped?
   > - **SQL injection** on score/leaderboard queries — all parameterised?
   > - **Auth:** passwords hashed, session cookie flags set, `SECRET_KEY` from env?
   > - **IDOR:** can a user submit a score as another user, or read someone's private data?
   > Fix every finding and point at the lines.

---

## Run it

```bash
cd projects/game
docker compose up                     # then open http://localhost:5000
docker compose run --rm app pytest
```

Set a session secret in your `.env` (don't hardcode it):

```
SECRET_KEY=<any long random string for the workshop>
```

---

## The "you can't trust the client" lesson (cheat sheet)

The game runs in the player's browser, so the score is **untrusted input** — exactly like a
form field. You can't make a client-side score un-fakeable, but you reduce the damage:

| Defence | What it stops | Where the skill covers it |
|---------|---------------|---------------------------|
| **Require login** to submit | Anonymous board spam | checklist §6 access control |
| **Validate type + range** server-side | Garbage / absurd scores (`"9e99"`, negatives) | checklist §1 + §5 untrusted input |
| **Rate-limit** submissions | Flooding the leaderboard | checklist §1 (server-side enforcement) |
| **Escape usernames** on render | Stored XSS via a crafted name | checklist §3 XSS |
| **Parameterise** score/board SQL | SQL injection | checklist §2 |

> Honest framing for attendees: a determined cheater *can* still POST a fake (but valid)
> score, because the browser owns the game logic. The point of this lab is the **trust
> boundary** — the server treats every incoming number as a claim to be checked, never a fact.

---

## What to notice

- The game grew from **pure frontend to a real client/server trust boundary** — and the
  security questions changed accordingly.
- The **same agents and skills** handled auth, an API, and a leaderboard with no new setup.
- "Validate untrusted input" stopped being abstract: the score field *is* the attack.
