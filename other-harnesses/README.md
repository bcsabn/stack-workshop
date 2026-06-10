# Other Harnesses — Claude Code & Gemini CLI

The workshop targets **OpenAI Codex** (agents in `.codex/agents/*.toml`, skills in
`.agents/skills/`). This folder mirrors the **same two subagents and three skills** for the
other two popular agentic CLIs, so you can run the exact same workflow in:

- **Claude Code** (Anthropic)
- **Gemini CLI** (Google)

The **skills are identical** across all three tools — they follow the shared
[Agent Skills standard](https://agentskills.io) (`SKILL.md` + `reference/` + `scripts/`).
Only the **subagent file format** differs per tool, so that's the only thing this folder
re-expresses.

```
other-harnesses/
├── claude/
│   ├── .claude/agents/          coding-agent.md, frontend-design-agent.md   (Claude format)
│   └── .agents/skills/          prd-expander/, ui-mockup/, security-review/  (shared skills)
└── gemini/
    ├── .gemini/agents/          coding-agent.md, frontend-design-agent.md   (Gemini format)
    └── .agents/skills/          prd-expander/, ui-mockup/, security-review/  (shared skills)
```

---

## How to use a different harness in the workshop

The labs are tool-agnostic — the prompts are the same. Just copy the matching files into your
working folder (the `agents-and-skills/` workspace, or a fresh project), then drive the same
PRD → mockup → UI → backend → review loop.

### Claude Code

```bash
# from the agents-and-skills workspace (or your project root)
cp -R other-harnesses/claude/.claude  .
cp -R other-harnesses/claude/.agents  .      # skip if .agents/ already present
```

- **Agents** live in `.claude/agents/<name>.md` — Markdown with YAML frontmatter
  (`name`, `description`, `tools`, `model`). Invoke with the `/agents` picker or by asking
  Claude to "use the coding_agent subagent".
- **Skills** live in `.agents/skills/<name>/SKILL.md` and are auto-discovered by description.
- Adjust `model:` in each agent file to whatever you have access to (e.g. `sonnet`, `opus`).

### Gemini CLI

```bash
cp -R other-harnesses/gemini/.gemini  .
cp -R other-harnesses/gemini/.agents  .      # skip if .agents/ already present
```

- **Agents** live in `.gemini/agents/<name>.md` — Markdown with YAML frontmatter
  (`name`, `description`, `model`, `tools`). Tool names use Gemini's built-in tool IDs
  (`read_file`, `write_file`, `edit`, `glob`, `search_file_content`, `run_shell_command`).
- **Skills** live in `.agents/skills/<name>/SKILL.md`, same as everywhere.
- Adjust `model:` to a model you have access to (e.g. `gemini-2.5-pro`, `gemini-2.5-flash`).

---

## What's the same vs different

| Piece | Codex (default) | Claude Code | Gemini CLI |
|-------|-----------------|-------------|------------|
| Skills | `.agents/skills/*/SKILL.md` | **same files** | **same files** |
| Agent location | `.codex/agents/*.toml` | `.claude/agents/*.md` | `.gemini/agents/*.md` |
| Agent format | TOML, `developer_instructions` | MD + YAML frontmatter | MD + YAML frontmatter |
| Tool field | `sandbox_mode` | `tools:` (Claude tool names) | `tools:` (Gemini tool names) |
| Model field | `model_reasoning_effort` | `model:` | `model:` |
| House rules file | `AGENTS.md` | `AGENTS.md` (also reads CLAUDE.md) | `AGENTS.md` (also reads GEMINI.md) |

The **content** of every agent and skill is kept word-for-word in sync with the Codex
originals under `agents-and-skills/` — only the wrapper format changes.

> If you change an agent's instructions in one place, update the other two so they don't
> drift. The skills are copies of the same files — re-copy them if the originals change.
