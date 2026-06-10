#!/usr/bin/env python3
"""Scaffold a blank, pre-sectioned PRD into a project folder.

Usage:
    python .agents/skills/prd-expander/scripts/new_prd.py "pantry tracker with expiry alerts"
    python .agents/skills/prd-expander/scripts/new_prd.py "makan group vote" --dir projects/makan-vote

This only creates the file with the six sections stubbed — you still do the thinking.
It will NOT overwrite an existing PRD.md (so you can't lose work by re-running it).
"""

import argparse
import re
import sys
from pathlib import Path

TEMPLATE = """# PRD: {title}

## 1. Summary
[One sentence: what we are building and for whom.]

## 2. User stories
- As a [who], I want to [what], so that [why].
- As a [who], I want to [what], so that [why].
- As a [who], I want to [what], so that [why].

## 3. Functional requirements
- [Concrete behaviour 1]
- [Concrete behaviour 2]
- [Data persists across a restart (SQLite).]

## 4. Data model
**[Entity]**
| Field | Type | Rule |
|-------|------|------|
| id | integer | auto, primary key |
| [field] | [type] | [required? length? range?] |

## 5. Out of scope
- [Something you are deliberately NOT building.]

## 6. Acceptance checks
- [ ] [A click/test that proves a core behaviour works.]
- [ ] [Bad input is rejected with a friendly message.]
- [ ] [Restarting keeps the data.]

## 7. Open questions (for the human)
- [ ] [Anything you had to guess — ask before building.]
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "app"


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a blank PRD.")
    parser.add_argument("request", help="one-line feature request, e.g. 'pantry tracker'")
    parser.add_argument(
        "--dir",
        default=None,
        help="target project dir (default: projects/<slug-of-request>)",
    )
    args = parser.parse_args()

    target_dir = Path(args.dir) if args.dir else Path("projects") / slugify(args.request)
    target_dir.mkdir(parents=True, exist_ok=True)
    prd_path = target_dir / "PRD.md"

    if prd_path.exists():
        print(f"Refusing to overwrite existing {prd_path}. Edit it directly.", file=sys.stderr)
        return 1

    prd_path.write_text(TEMPLATE.format(title=args.request.strip().title()), encoding="utf-8")
    print(f"Wrote {prd_path}")
    print("Now fill in every [bracketed] part, then ask the human to confirm before building.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
