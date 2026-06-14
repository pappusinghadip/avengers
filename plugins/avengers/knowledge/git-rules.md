# Git Rules

Use this for Nick Fury.

- Start with `git status --short --branch`.
- Inspect staged changes with `git diff --cached --name-status` and `git diff --cached`.
- Do not assume untracked files are included.
- Do not use `git add .` unless the user explicitly approves the full worktree.
- Preserve unrelated local edits.
- Never amend, force-push, delete branches, create PRs/releases, deploy, publish packages, or run `git push` without explicit user approval for that exact remote action in the current task.
- Approval to commit is not approval to push.
- Before an approved push or publish, show the remote, branch, account if detectable, exact command, and scope.
- After push/merge claims, verify the actual command result and current branch.
- For PR work, detect the platform from `git remote -v` before suggesting `gh`, `glab`, or manual PR steps.
- If `gh auth status` or another CLI account does not match the remote owner, warn before publishing.
