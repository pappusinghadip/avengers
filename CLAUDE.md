# CLAUDE.md

This repository defines a private Claude Code-style plugin named Avengers Agents.

## Architecture

- `plugins/avengers/agents/`: 10 named agent definitions.
- `plugins/avengers/commands/`: slash command prompts.
- `plugins/avengers/skills/`: reusable workflow skills.
- `plugins/avengers/knowledge/`: shared rules used by skills and agents.
- `.claude-plugin/marketplace.json`: Claude plugin marketplace metadata.
- `.codex-plugin/plugin.json`: local Codex plugin manifest.

## Rules

- Captain America coordinates and plans. He does not directly edit source code.
- Nick Fury owns git and release checks. He does not use broad staging commands.
- Hawkeye, Black Widow, and Hulk are read-only reviewers/testers.
- Source edits go through Iron Man, Spider-Man, Doctor Strange, Ant-Man, or Black Panther after approval.
- Audit and runtime-path tracing come before edits.
- Never use `git add .` in generated/noisy worktrees.
- Keep generated workflow state under `.avengers/` or `.claude/avengers/`.
