---
name: avengers-agents
description: Private Avengers agent workflow for audit-first repo work, scoped fixes, review, testing, and git safety.
---

# Avengers Agents

Use this workflow when you want an audit-first development pass.

## Local Claude Plugin

The Claude Code-style plugin lives at:

`plugins/avengers/`

Run locally with:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/avengers-agents/plugins/avengers
```

## Default Flow

1. Captain America coordinates.
2. Audit the real runtime path before edits.
3. Use `/avengers:feature` for the full feature lifecycle.
4. Use `/avengers:bugfix` for the full bugfix lifecycle.
5. Plan non-trivial changes when working manually.
6. Delegate scoped implementation to the right specialist.
7. Review with Hawkeye and security-check with Black Widow when relevant.
8. Verify with Hulk or repo-native tests.
9. Use Nick Fury for staged diff, commit, and release checks.
