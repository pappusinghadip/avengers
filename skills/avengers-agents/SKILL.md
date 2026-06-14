---
name: avengers-agents
description: Private Avengers agent workflow for audit-first repo work, scoped fixes, review, testing, and git safety.
---

# Avengers Agents

Use this workflow when you want an audit-first development pass, natural Avengers routing, or a Claude Code plugin update.

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
5. Use `/avengers:research`, `/avengers:explain`, or `/avengers:brainstorm` before planning when the problem is unclear.
6. Plan non-trivial changes when working manually.
7. Delegate scoped implementation to the right specialist.
8. Review with Hawkeye and security-check with Black Widow when relevant.
9. Verify with Hulk using unit/component, integration, end-to-end/user-flow, and security angles when relevant.
10. Use Nick Fury for staged diff, commit, PR, and release checks.
11. Use JARVIS for `.avengers/reports/`, `.avengers/memory/`, and artifact housekeeping.

## Natural Routing

Claude Code can route direct named requests:

```text
captain america, build a search bar
hulk, test the auth flow
nick fury, prepare the commit
```
