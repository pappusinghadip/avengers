# Avengers Agents

Audit-first AI coding agents for Claude Code workflows.

Avengers Agents is a Claude Code-style plugin that gives you a small, opinionated squad of specialist agents for real software work: repo audits, scoped fixes, debugging, code review, verification, and git-safe delivery.

The workflow is simple:

1. Understand the real runtime path.
2. Plan before editing.
3. Make scoped changes.
4. Review and verify.
5. Commit only what was intended.

> Unofficial fan-themed project. This repository is not affiliated with, sponsored by, or endorsed by Marvel, Disney, or any related rights holder.

## Features

- Read-only audit command for tracing real code paths.
- Planning command for implementation notes before edits.
- Scoped fix command for approved changes.
- Debug command for root-cause investigations.
- Review command with file and line findings.
- Test command for verification, edge cases, and stress checks.
- Commit command built around staged-diff safety.
- Project init command for generating local context.

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

## Installation

### Option 1: Install From GitHub In Claude Code

After this repository is available on GitHub:

```bash
/plugin marketplace add pappusinghadip/avengers
/plugin install avengers@avengers-agents
```

Then use the slash commands:

```text
/avengers:audit explain the auth flow
/avengers:plan add passkey login
/avengers:review staged changes
```

### Option 2: Run Locally From A Clone

Clone the repository:

```bash
git clone git@github.com:pappusinghadip/avengers.git
cd avengers
```

Run Claude Code with the plugin directory:

```bash
claude --plugin-dir "$PWD/plugins/avengers"
```

For the current local workspace:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/avengers-agents/plugins/avengers
```

## Quick Start

Initialize project context in any repo:

```text
/avengers:init
```

Audit before making changes:

```text
/avengers:audit why does /admin redirect to login
```

Create a plan before implementation:

```text
/avengers:plan add a manual passkey check after password login
```

Implement an approved scoped change:

```text
/avengers:fix implement the approved passkey plan
```

Review changed code:

```text
/avengers:review staged changes
```

Commit safely:

```text
/avengers:commit latest fix
```

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

## Recommended Workflow

### For New Features

```text
/avengers:audit existing related feature
/avengers:plan build the new feature
/avengers:fix implement the approved plan
/avengers:review changed files
/avengers:test affected flow
/avengers:commit feature summary
```

### For Bugs

```text
/avengers:debug paste the error or describe the failing behavior
/avengers:plan propose the fix
/avengers:fix apply the approved fix
/avengers:test verify the original bug is gone
/avengers:review changed files
```

### For Git Handoff

```text
/avengers:review staged changes
/avengers:commit commit message or context
```

Nick Fury is intentionally staged-diff focused. The commit workflow should not use broad staging unless explicitly requested.

## How The Agents Route Work

- Captain America coordinates larger work.
- Iron Man handles complex implementation and automation.
- Spider-Man handles frontend and user-facing flows.
- Doctor Strange handles difficult debugging.
- Black Panther handles backend reliability, persistence, and data safety.
- Ant-Man handles tiny low-risk patches.
- Hawkeye reviews code.
- Black Widow reviews security-sensitive paths.
- Hulk verifies edge cases, stress cases, and regressions.
- Nick Fury handles git, release checks, and final commit hygiene.

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

Run the structure validator:

```bash
python3 scripts/validate_avengers.py
```

Expected output:

```text
OK: Avengers Agents structure is valid
```

The validator checks:

- all 10 agent files exist;
- all 8 command files exist;
- required skills and knowledge files exist;
- agent skill references resolve;
- Claude plugin versions match;
- upstream reference identifiers are not present.

## Development

When editing the plugin:

1. Update agent, command, skill, or knowledge files under `plugins/avengers`.
2. Run validation.
3. Test locally with `claude --plugin-dir "$PWD/plugins/avengers"`.
4. Commit only intentional files.

Useful commands:

```bash
python3 scripts/validate_avengers.py
git status --short --branch
git diff --cached --name-status
```

## Git Safety Rules

Nick Fury follows these rules:

- start with `git status --short --branch`;
- inspect staged files with `git diff --cached --name-status`;
- inspect the actual staged diff before commit;
- never assume untracked files are included;
- never use `git add .` unless explicitly approved;
- never force-push, amend, delete branches, or publish without explicit approval.

## Generated State

Generated workflow state should stay out of normal commits:

```text
.avengers/.temp/
.claude/avengers/.temp/
```

Project context and memory may be created by `/avengers:init` inside a target repo.

## Versioning

Keep these versions in sync:

- `.claude-plugin/marketplace.json`
- `plugins/avengers/.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`

Run validation after version or metadata changes.

## License

No open-source license has been added yet. Unless a `LICENSE` file is added, all rights are reserved by the repository owner.
