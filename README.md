# Avengers Agents

Private local coding agents for an audit-first workflow.

This plugin is for private/local use. It uses Avengers character names as a personal naming scheme and is not intended for public redistribution.

## Workflow

1. Audit the real runtime path before conclusions.
2. Write or present a plan before edits.
3. Keep code changes scoped to the approved area.
4. Preserve unrelated local edits.
5. Verify behavior and staged file boundaries before commit.

## Agent Squad

| Agent | Role |
|---|---|
| Captain America | Main orchestrator, planning, coordinates agents |
| Iron Man | Implementation, architecture, automation, complex engineering |
| Spider-Man | UI/UX, frontend, user flows |
| Doctor Strange | Deep debugging, weird edge cases, hard investigations |
| Black Widow | Security review, suspicious audit, auth/data leak checks |
| Hawkeye | Code review, precise file/line findings |
| Hulk | Stress testing, breaking things, performance pressure |
| Ant-Man | Small scoped fixes, surgical changes |
| Black Panther | Data integrity, backend reliability, defensive design |
| Nick Fury | Git, release coordination, final checklist |

## Commands

| Command | Purpose |
|---|---|
| `/avengers:audit` | Read-only repo audit and runtime path trace |
| `/avengers:plan` | Plan a change before implementation |
| `/avengers:fix` | Implement an approved scoped change |
| `/avengers:debug` | Root-cause debugging with approval before fixes |
| `/avengers:review` | Code review and security-risk pass |
| `/avengers:test` | Verification, tests, stress and edge checks |
| `/avengers:commit` | Staged diff review and safe commit workflow |
| `/avengers:init` | Create project context for this workflow |

## Local Claude Code Test

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/avengers-agents/plugins/avengers
```

## Validate

```bash
python3 /Users/pappusingha/Documents/MyAgent/avengers-agents/scripts/validate_avengers.py
```
