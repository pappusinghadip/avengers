# Avengers Agents

Audit-first AI coding agents for Claude Code workflows.

Avengers Agents is a Claude Code-style plugin that gives you a small, opinionated squad of specialist agents for real software work: repo audits, scoped fixes, debugging, research, code review, verification, PR preparation, reporting, and git-safe delivery.

The workflow is simple:

1. Understand the real runtime path.
2. Plan before editing.
3. Make scoped changes.
4. Review and verify.
5. Commit only what was intended.

> Unofficial fan-themed project. This repository is not affiliated with, sponsored by, or endorsed by Marvel, Disney, or any related rights holder.

## Features

- Read-only audit command for tracing real code paths.
- Full gated feature lifecycle command for gather, research, plan, build, review plus test, and summary.
- Full gated bugfix lifecycle command for gather, investigate, fix plan, fix, verify, and summary.
- Planning command for implementation notes before edits.
- Research, explain, brainstorm, refactor, report, and PR commands.
- Scoped fix command for approved changes.
- Debug command for root-cause investigations.
- Review command with file and line findings.
- Test command for four-angle verification: unit/component, integration, E2E/user flow, and security.
- Commit command built around staged-diff safety.
- Project init command for generating local context.
- Natural routing skills for `captain america`, `hulk`, and `nick fury`.
- JARVIS internal support for activity logs, reports, memory, and artifact housekeeping.

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

Internal support:

| Agent | Role |
|---|---|
| JARVIS | Activity logging, reports, memory writes, artifact housekeeping |

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
/avengers:feature add passkey login
/avengers:bugfix users cannot log in after password reset
/avengers:research auth flow
/avengers:explain checkout module
/avengers:plan add passkey login
/avengers:review staged changes
```

You can also use natural routing in Claude Code:

```text
captain america, build a search bar
hulk, test the auth flow
nick fury, prepare the commit
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

Run a full feature lifecycle:

```text
/avengers:feature add a manual passkey check after password login
```

Run a full bugfix lifecycle:

```text
/avengers:bugfix login fails after password reset
```

Implement an approved scoped change:

```text
/avengers:fix implement the approved passkey plan
```

Review changed code:

```text
/avengers:review staged changes
```

Prepare a PR:

```text
/avengers:pr target main
```

Commit safely:

```text
/avengers:commit latest fix
```

## Commands

| Command | Purpose |
|---|---|
| `/avengers:audit` | Read-only repo audit and runtime path trace |
| `/avengers:brainstorm` | Compare options and tradeoffs before building |
| `/avengers:plan` | Create an implementation plan before editing |
| `/avengers:feature` | Gather -> research -> plan -> build -> review plus test -> summary |
| `/avengers:bugfix` | Gather -> investigate -> fix plan -> fix -> verify -> summary |
| `/avengers:fix` | Implement an approved scoped change |
| `/avengers:debug` | Root-cause debugging with approval before fixes |
| `/avengers:explain` | Layered codebase or feature explanation |
| `/avengers:research` | Deep read-only research from multiple angles |
| `/avengers:refactor` | Review-led refactoring with approval gate |
| `/avengers:review` | Code review and security-risk pass |
| `/avengers:test` | Four-angle verification, stress, and edge checks |
| `/avengers:commit` | Staged diff review and safe commit workflow |
| `/avengers:pr` | PR preparation with diff review and approval gate |
| `/avengers:report` | Activity summary from reports, memory, and artifacts |
| `/avengers:init` | Create project context for this workflow |

## Gated Lifecycles

Lifecycle state is written under `.avengers/.temp/`. If context is compacted or a terminal closes, restart by reading the task `status.md` and phase files. The commands check whether `.avengers/.temp/` is gitignored before writing artifacts.

### Feature Lifecycle

```text
/avengers:feature build a search bar

Phase 0  Gather         Requirements. Definition of done. Existing resources.
Phase 1  Research       Avengers explore the codebase from multiple angles in parallel.
          GATE          Confirm understanding before planning.
Phase 2  Plan           Architecture decisions, chunks, risks, and verification.
          GATE          Approve the plan before source edits.
Phase 3  Build          Avengers execute per the approved plan.
          GATE          Review what was built.
Phase 4  Review + Test  Hawkeye reviews. Black Widow audits sensitive paths. Hulk verifies from four angles.
          GATE          Decide which findings to fix, defer, or accept.
Phase 5  Summary        What was built, decisions made, test result, and reusable notes.
```

### Bugfix Lifecycle

```text
/avengers:bugfix users cannot log in after SSO

Phase 0  Gather         Bug details, logs, screenshots, impact, and timeline.
Phase 1  Investigate    Doctor Strange traces symptoms to root cause.
          GATE          Confirm the root cause before any fix is attempted.
Phase 2  Fix Plan       Proposed fix, blast radius, rollback, and verification.
          GATE          Approve the approach before source edits.
Phase 3  Fix            The right Avenger executes the fix.
          GATE          Review the fix.
Phase 4  Verify         Hawkeye reviews. Black Widow audits sensitive paths. Hulk confirms the bug is gone.
Phase 5  Summary        Root cause, fix, verification, and reusable decision rule.
```

JARVIS can log lifecycle output to `.avengers/reports/activity.log` and save reusable decision rules to `.avengers/memory/`.

## Recommended Workflow

### For New Features

```text
/avengers:feature build the new feature
/avengers:commit feature summary
```

### For Bugs

```text
/avengers:bugfix paste the error or describe the failing behavior
/avengers:commit bugfix summary
```

Use `/avengers:plan` plus `/avengers:fix` when you want to split the lifecycle manually. Use `/avengers:research`, `/avengers:explain`, or `/avengers:brainstorm` when you want understanding before any plan.

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
- JARVIS quietly handles `.avengers/` reports, memory, and activity logs.

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
│       ├── hooks/
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

- all 10 public agent files and internal JARVIS support agent exist;
- all command files exist;
- routing and shared-rule skills exist;
- hook files exist;
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
- never force-push, amend, delete branches, create PRs/releases, deploy, publish packages, or run `git push` without explicit approval for that exact remote action in the current task;
- approval to edit, test, or commit locally is not approval to push;
- before any approved push/publish, show the exact remote, branch, account if detectable, and command.

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
