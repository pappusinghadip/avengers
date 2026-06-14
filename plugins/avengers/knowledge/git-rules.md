# Git Rules

Use this for Nick Fury.

- Start with `git status --short --branch`.
- Inspect staged changes with `git diff --cached --name-status` and `git diff --cached`.
- Do not assume untracked files are included.
- Do not use `git add .` unless the user explicitly approves the full worktree.
- Preserve unrelated local edits.
- Never amend, force-push, delete branches, or publish without explicit user approval.
- After push/merge claims, verify the actual command result and current branch.
