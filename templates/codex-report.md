# Codex Evidence Report — Contract

Codex should report in Russian. Commands, exit codes and quoted log excerpts must remain unchanged. Never claim a check passed unless executed or independently verifiable. Redact secrets.

```text
TASK ID / GOAL:
RESULT: each acceptance criterion — DONE | NOT DONE | NOT VERIFIED

GIT:
  branch:
  base SHA (start of task):
  head SHA:
  git status --short: <literal output or EMPTY>
  change stat: <literal git diff --stat BASE...HEAD or equivalent>
  if single commit: <literal git show --stat --oneline HEAD>
  uncommitted changes: <separately stated>

CHANGED FILES: <added / modified / deleted / renamed, focused summary>
DEPENDENCIES: <added/removed/changed, lockfile effect, or NONE>
CHECKS:
  command: ... | exit: ... | PASS/FAIL/NOT RUN
  relevant raw excerpt: ...
  skipped checks and why: ...
TEST/CONFIG CHANGES: <test files, skip/xfail, lint/type configs, explanation>
SCOPE / SECURITY / ARCHITECTURE: <deviations and risks>
MEMORY: <actual files updated; proposed evidence-linked entries awaiting approval>
CONTEXT: <available metric or UNAVAILABLE>
NEXT ACTION: ...
```

**Important:** after a commit, `git diff --stat` without a base may be empty. Capture task-base vs HEAD (and separate uncommitted state) so changes remain visible. For high-risk files, include focused diffs in the follow-up, not automatically every giant log.
