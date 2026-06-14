# Avengers Agents

Private audit-first coding agents for Claude Code and local development workflows.

Avengers Agents is a personal agent squad built around a simple rule: understand the real code path before changing anything. It is designed for repo audits, scoped fixes, debugging, review, testing, and safe git handoff.

> Private use only. This repository uses Avengers character names as a local naming scheme and is not intended for public redistribution or marketplace publishing.

## What This Gives You

- Read-only audits before implementation.
- Plans before non-trivial edits.
- Scoped fixes that preserve unrelated local changes.
- Specialist agents for frontend, backend, data, debugging, security, review, testing, and git.
- Validation scripts to catch broken plugin wiring.
- A Claude Code-style plugin bundle under `plugins/avengers`.
- A Codex-compatible local scaffold manifest under `.codex-plugin`.

## Agent Squad

| Agent | Role |
|---|---|
| Captain America | Main orchestrator, planning, coordinates agents |
| Iron Man | Implementation, architecture, automation, complex engineering |
| Spider-Man | UI/UX, frontend, user flows |
| Doctor Strange | Deep debugging, unusual edge cases, hard investigations |
| Black Widow | Security review, suspicious audit, auth and data leak checks |
| Hawkeye | Code review, precise file and line findings |
| Hulk | Stress testing, edge cases, performance pressure |
| Ant-Man | Small scoped fixes, surgical changes |
| Black Panther | Data integrity, backend reliability, defensive design |
| Nick Fury | Git, release coordination, staged diff safety, final checklist |

## Commands

| Command | Purpose |
|---|---|
| `/avengers:audit` | Read-only repo audit and runtime path trace |
| `/avengers:plan` | Create an implementation plan before editing |
| `/avengers:fix` | Implement an approved scoped change |
| `/avengers:debug` | Root-cause debugging with approval before fixes |
| `/avengers:review` | Code review and security-risk pass |
| `/avengers:test` | Verification, tests, stress, and edge checks |
| `/avengers:commit` | Staged diff review and safe commit workflow |
| `/avengers:init` | Create project context for this workflow |

## Default Workflow

1. Captain America receives the mission.
2. The active runtime path is traced before conclusions.
3. A plan is written or presented for non-trivial changes.
4. The correct specialist implements only the approved scope.
5. Hawkeye reviews the change.
6. Black Widow checks security when auth, user data, file IO, shell, SQL, or permissions are involved.
7. Hulk verifies tests, smoke checks, stress cases, and failure paths when relevant.
8. Nick Fury handles staged diff, commit, push, and release coordination only when asked.

## Local Claude Code Usage

Run Claude Code with the plugin loaded directly from this repository:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/avengers-agents/plugins/avengers
```

Example prompts:

```text
/avengers:audit why this admin route redirects
/avengers:plan add a manual passkey gate
/avengers:debug crash after submit
/avengers:review staged changes
/avengers:commit latest fix
```

## Repository Structure

```text
avengers-agents/
├── .claude-plugin/
│   └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── plugins/
│   └── avengers/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── agents/
│       ├── commands/
│       ├── knowledge/
│       └── skills/
├── scripts/
│   └── validate_avengers.py
├── skills/
│   └── avengers-agents/
│       └── SKILL.md
├── CLAUDE.md
└── README.md
```

## Validation

Run the local structure validator:

```bash
python3 scripts/validate_avengers.py
```

Expected result:

```text
OK: Avengers Agents structure is valid
```

The validator checks:

- all 10 agent files exist;
- all 8 command files exist;
- all required skills and knowledge files exist;
- skill references in agent frontmatter resolve;
- Claude plugin versions match;
- upstream Transformers repo identifiers are not present.

## Git Safety Rules

Nick Fury owns git work. The expected behavior is:

- start with `git status --short --branch`;
- inspect staged files with `git diff --cached --name-status`;
- inspect the actual staged diff before commit;
- never assume untracked files are included;
- never use `git add .` unless explicitly approved;
- never force-push, amend, delete branches, or publish without explicit approval.

## Development Notes

- Keep the plugin private/local.
- Keep generated task state under `.avengers/` or `.claude/avengers/`.
- Keep `.avengers/.temp/` out of git.
- Update both Claude plugin version files together:
  - `.claude-plugin/marketplace.json`
  - `plugins/avengers/.claude-plugin/plugin.json`
- Run validation before committing prompt or metadata changes.
