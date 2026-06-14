# Workflow Rules

## Audit First

- Start from the real runtime path: entrypoint, route, caller, config, backend file, database key, or staged diff.
- Do not answer from filename similarity alone.
- If several files look relevant, trace the active caller before concluding.

## Plan Before Edits

- For non-trivial changes, present a short plan and wait for approval.
- Include scope, files likely touched, verification, and rollback risk.
- If the user asked for audit only, do not edit.

## Scope Discipline

- Preserve unrelated local edits.
- Search callers before changing public interfaces.
- Keep fixes narrow unless the user approves larger cleanup.
- Never hide uncertainty. Say what was verified and what is still assumed.

## Artifact Paths

- Project context: `.avengers/context/project.md`
- Temporary work: `.avengers/.temp/`
- Memory: `.avengers/memory/`
- Reports: `.avengers/reports/`

## Artifact Discipline

- Before creating `.avengers/.temp/` artifacts, check whether `.avengers/.temp/`, `.avengers/`, or equivalent is gitignored.
- If not ignored, ask before appending `.avengers/.temp/` to `.gitignore`.
- Every lifecycle artifact directory should have `status.md`.
- `status.md` should include phase, status, summary, next action, and gate state.
- On resume, read `status.md` before continuing.
- Specialists should write details to artifact files and return short summaries.

## Activity Logging

- Use JARVIS for `.avengers/reports/activity.log`.
- Log meaningful lifecycle, research, test, review, commit, and PR work.
- Do not log invented token counts or unverified file counts.
