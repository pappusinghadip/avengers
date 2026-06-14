# Build Patterns

Use this for Captain America and implementation agents.

## Decomposition

Parallelize only when chunks are genuinely independent:

- UI and backend can run in parallel if they touch separate files and share a clear contract.
- Multiple unrelated bug fixes can run in parallel.
- Research angles can run in parallel.

Sequence work when there is a dependency:

- Schema or model change before API/UI updates.
- Shared interface change before callers.
- Config or generated code before build verification.
- Same file edits should usually be owned by one agent.

## Agent Selection

| Work | Agent |
|---|---|
| Architecture, services, automation, complex implementation | Iron Man |
| UI, UX, frontend flows, responsive behavior | Spider-Man |
| Root-cause debugging and strange failures | Doctor Strange |
| Small safe patch | Ant-Man |
| Data, persistence, migrations, caches, backend invariants | Black Panther |
| Security review | Black Widow |
| Code review | Hawkeye |
| Stress, edge, performance, regression verification | Hulk |
| Git, PR, release, staged diff safety | Nick Fury |

## Conflict Resolution

1. Stop if two agents need to edit the same file.
2. Assign one owner for that file.
3. Re-read the final diff before review.
4. If a change grew beyond approved scope, ask the user.

## Build Output Discipline

Each builder reports:

- files changed;
- decisions made;
- assumptions;
- verification run or skipped;
- remaining risk.
