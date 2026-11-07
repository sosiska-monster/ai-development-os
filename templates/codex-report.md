# Codex evidence contract — Lite / Full

Report in Russian; don't invent tests, commands, Git outputs or repository state. **Codex-generated evidence is not independent verification** until reviewed against real files/diff/CI or a trusted external capture. Never include secrets or raw env dumps.

## User-facing summary at every task boundary

Prefer a **short Russian 6-line answer**: DONE/PARTIAL/BLOCKED; what changed and why; main paths; actual check + exit or NOT RUN; risks; **NEW CHAT: YES/NO (reason)**; next task only as a suggestion and **STOP for explicit user authorization**. If DONE, default to **NEW CHAT: YES — "Задача завершена. Перед следующей независимой задачей открой новый чат Codex"**. For PARTIAL/BLOCKED say whether to continue the same thread or switch with a minimal verified handoff. Never claim to have opened or reset a chat. Keep the underlying Lite/Full evidence accessible for review, but do not paste extensive logs into the main response unless needed for a risk decision. A proposed NEXT is not permission to begin it; blocked work remains intact. No separate report file per small task.

## Lite (FAST/LOW; concise)

```text
RESULT: <what changed + acceptance DONE / NOT VERIFIED>
PATHS: <actual task paths; scope MATCH / MISMATCH / NOT SCOPED>
VERIFY: <command, exit code, PASS / FAIL / NOT RUN + short verbatim output>
GIT: <branch, base/head or commit link; dirty/untracked status if any>
RISK / NEXT: <new risks, deviations or NONE; next step>
```

## Full (STANDARD when appropriate; always CONTROLLED)

```text
TASK / MODE & REASON / GOAL:
ACCEPTANCE: <each acceptance criterion DONE / NOT DONE / NOT VERIFIED>
GIT:
  branch, task base SHA, HEAD SHA, latest verified checkpoint:
  git status --short (verbatim, or EMPTY):
  committed delta vs task base (correct comparison for history):
  staged / unstaged / untracked (separately):
  pre-existing changes (if any):
CHANGED PATHS: <added, modified, removed, renamed; actual diff vs approved EXPECTED_DIFF_PATHS>
SCOPE MATCH: MATCH | MISMATCH | NOT SCOPED (approved exceptions identified)
CHECKS: <command | exit code | PASS/FAIL/NOT RUN; relevant verbatim excerpt; baseline if applicable>
TEST / QUALITY CONFIG CHANGES: <diff summary, test-weakening risk and approval>
DEPENDENCIES / LOCKFILES: <verified actual versions, changes or NONE>
SECURITY / DATA / CONTRACTS: <risk; required approvals; production not touched unless separately authorized>
MEMORY: <verified fact updates vs PROPOSED/STALE entries awaiting review>
EVIDENCE SOURCES: <GitHub commit/PR, Codex diff, CI job links, independently inspected artifacts; or NONE>
BLOCKERS / STOP REASON / NEXT ACTION:
```

Do not rely on bare `git diff --stat` after a commit: it can be empty. Also inspect staged, unstaged and untracked files; distinguish unrelated pre-existing user edits. Quote only necessary log excerpts and remove tokens/credentials.

## Hygiene checkpoint (optional concise line)

At natural task/batch completion, optionally include:
`HYGIENE: CLEAN | REMOVED <specific task-scoped waste; why; verification> | DEFERRED <candidate; approval/scope needed>`.

Treat untracked files and unrelated pre-existing changes as protected, not waste to delete. Do not count code removal or line-count reduction as success without preserved required behavior and actual checks. A hygiene change is part of the real diff and scope review, **not** an unreported side edit.

## Reviewer contract

- ChatGPT does not replace reviewing actual diff or tests with a plausible report.
- For material/high-risk changes, independently inspect relevant changed code and sensitive test/config/security files; CI is useful, not a proof of correctness.
- If diff or independently reliable source is missing, verdict **INSUFFICIENT EVIDENCE** rather than invented ACCEPT.
