# CLAUDE.md

This repository defines a private Claude Code-style plugin named Avengers Agents.

## Architecture

- `plugins/avengers/agents/`: 10 public agent definitions plus internal JARVIS support.
- `plugins/avengers/commands/`: slash command prompts.
- `plugins/avengers/hooks/`: session-start context injection.
- `plugins/avengers/skills/`: reusable workflow skills.
- `plugins/avengers/knowledge/`: shared rules used by skills and agents.
- `.claude-plugin/marketplace.json`: Claude plugin marketplace metadata.
- `.codex-plugin/plugin.json`: local Codex plugin manifest.

## Rules

- Captain America coordinates and plans. He does not directly edit source code.
- JARVIS owns activity logs, memory writes, reports, and artifact housekeeping only.
- Nick Fury owns git and release checks. He does not use broad staging commands.
- Hawkeye, Black Widow, and Hulk are read-only reviewers/testers.
- Source edits go through Iron Man, Spider-Man, Doctor Strange, Ant-Man, or Black Panther after approval.
- Audit and runtime-path tracing come before edits.
- Never use `git add .` in generated/noisy worktrees.
- Keep generated workflow state under `.avengers/` or `.claude/avengers/`.
- Prefer natural routing skills for named requests: `captain america`, `hulk`, and `nick fury`.
- Keep `.avengers/.temp/` ignored before writing lifecycle artifacts.
