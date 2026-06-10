#!/usr/bin/env python3
"""Security *smell* detector for small Flask apps — a fast first pass.

This is NOT a judge. It greps for patterns that are OFTEN bugs, so you know where to look.
Every hit must be confirmed by reading the code. False positives are expected and fine.

Usage:
    python .agents/skills/security-review/scripts/scan.py projects/makan-vote
    python .agents/skills/security-review/scripts/scan.py app.py templates/

Exit code is 0 always (it's advisory). Pair it with the checklist in reference/checklist.md.
"""

import re
import sys
from pathlib import Path

# (label, severity, regex, which file extensions to check)
RULES = [
    ("Possible string-built SQL (use ? params)", "HIGH",
     re.compile(r"""(execute|executescript)\s*\(\s*[^?]*?(\+|%|f["']|\.format\()""", re.I),
     {".py"}),
    ("Jinja autoescape disabled on output", "HIGH",
     re.compile(r"\|\s*safe\b|Markup\s*\(|autoescape\s+false", re.I),
     {".html", ".jinja", ".j2", ".py"}),
    ("eval/exec on possibly-untrusted input", "HIGH",
     re.compile(r"\b(eval|exec)\s*\(", ),
     {".py"}),
    ("Hardcoded API key / token", "HIGH",
     re.compile(r"""(sk-[A-Za-z0-9_\-]{12,}|api_key\s*=\s*["'][^"']+["'])"""),
     {".py", ".html", ".js", ".toml", ".yml", ".yaml"}),
    ("Sequential id in route/redirect (possible IDOR)", "MED",
     re.compile(r"""(redirect|url_for)\([^)]*\b(id|poll_id|item_id)\b""", re.I),
     {".py"}),
    ("Flask debug mode on (don't ship it)", "MED",
     re.compile(r"debug\s*=\s*True|FLASK_DEBUG\s*[=:]\s*1"),
     {".py", ".yml", ".yaml", ".env"}),
    ("Reads request data without obvious validation nearby", "LOW",
     re.compile(r"request\.(form|args|json|values)\b"),
     {".py"}),
]

SKIP_DIRS = {".git", "__pycache__", "venv", ".venv", "node_modules"}
TEXT_EXTS = {".py", ".html", ".jinja", ".j2", ".js", ".toml", ".yml", ".yaml", ".env"}


def iter_files(targets):
    for t in targets:
        p = Path(t)
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and not (SKIP_DIRS & set(f.parts)) and f.suffix in TEXT_EXTS:
                    yield f


def main(argv):
    targets = argv or ["."]
    hits = 0
    for f in iter_files(targets):
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for n, line in enumerate(lines, 1):
            for label, sev, rx, exts in RULES:
                if f.suffix in exts and rx.search(line):
                    hits += 1
                    print(f"[{sev}] {f}:{n}  {label}")
                    print(f"        {line.strip()[:120]}")

    print()
    if hits:
        print(f"{hits} smell(s) to confirm by hand. Read each line, then apply "
              f"reference/checklist.md. Smells are not proof — verify before reporting.")
    else:
        print("No obvious smells. Still walk the checklist by hand — this tool only "
              "catches the easy patterns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
