# Codex evidence contract — Lite / Full

Report in Russian; don't invent tests, commands, Git outputs or repository state. **Codex-generated evidence is not independent verification** until reviewed against real files/diff/CI or a trusted external capture. Never include secrets or raw env dumps.

## User-facing summary at every task boundary

Prefer a **short Russian answer**: DONE/PARTIAL/BLOCKED; result; actual changed paths and feature-scope check; verification command/exit or NOT RUN; risks; proposed next action and **STOP**. Continue in the same Codex chat by default; mention switching only if useful (lost context, independent review, user choice). Don't pretend to reset a chat or autonomously start the next task. Keep detailed Lite/Full evidence available without duplicating logs; no report file for trivial changes.

## File handoff to ChatGPT Web — reference first, one designated place if needed

**Default (every task):** do not generate a separate report file, copy source files, bundle huge logs or force the user to upload everything. The short final Russian report **is the index** of evidence, referring to existing source files, diffs, CI results, dataset summaries and any genuinely needed attachments by **exact relative path and branch/base/head SHA** (and a verified GitHub commit/PR link when one exists). Include a brief result, changed paths and real check+exit **inline** so the answer remains useful if Web cannot access an attachment. Distinguish `EVIDENCE: GITHUB ACCESSIBLE / LOCAL UPLOAD REQUIRED / CI LINK / NOT AVAILABLE`. A path to `C:\\...` or a local repository is **not** a Web-readable link; a committed but **not pushed** file is likewise unavailable through GitHub. Never claim access or upload without verifying it.

**When Web must inspect an actual output file not already accessible through an existing shared source:**
1. If the product's approved Environment Profile already names a handoff folder, use **that**. Otherwise propose `.ai-handoff/<TASK_ID>/` in the current **PRODUCT worktree** as the local, temporary, **gitignored by configured project policy**, single handoff destination. An explicit approved task `WRITE ALLOWLIST` must include the exact destination *before Codex creates/copies any file*; do not silently expand scope or edit `.gitignore` as an exception. Set up the folder/ignore only as a separately approved bootstrap/setup action if absent. Use collision-safe task identifiers; preserve preexisting files.
2. Put **only minimal, safe-to-share derivatives** there: short sanitized split statistics, a bounded test excerpt, a small relevant diff/report, a screenshot specifically needed for review. Keep originals in their original locations; never relocate/overwrite training data, checkpoints or test artifacts. No secrets, personal/customer records, full datasets, model weights, unredacted logs or huge generated binaries.
3. In the final reply list `HANDOFF FILES: <exact paths + purpose + size if useful>` and `TRANSFER: attach these files to ChatGPT Web → «confirmed destination», or mark destination PROPOSED` when manual cross-chat upload is required. Web may inspect uploaded content only after user attaches it; paths alone never prove access.
4. If user explicitly approves GitHub-based handoff, store only reviewed small non-sensitive evidence under `docs/ai/evidence/<TASK_ID>/` (or existing approved equivalent), **separately allowlist these files**, commit/push only with explicit authorization, and cite the verified immutable commit URL/ref. This is optional, not required for routine tasks. Never publish sensitive artifacts in the central AI Development OS methodology repo.
5. Old handoff bundles, ignored files and evidence directories are protected user/worktree material: **no automatic cleanup**. Cleanup requires review and user authorization, especially after a failed experiment. The handoff location inherits experimental branch/worktree isolation; never put experimental outputs in mainline just to share them.

Use one source of truth for each file. **Don't copy unchanged project source into a handoff folder just because Web wants to read it** if the same file is already reachable through an approved GitHub source. For a tiny FAST change, a verified Git reference and 5–6-line inline report normally suffice.

## Optional PR handoff and runtime evaluation — reference-first

For a task that has an **approved GitHub publication policy**, use the existing concise final report as the PR handoff:
```text
PRODUCT REPO / TASK / GOAL NODE: <verified>
BRANCH / BASE..HEAD / COMMIT SHA: <actual values>
PR URL / STATUS: <verified URL + open/draft, or NOT CREATED>
SCOPE: <changed paths and MATCH / MISMATCH>
CI: <required job name + GitHub URL + observed status, or NOT RUN / INACCESSIBLE>
RUNTIME ACCEPTANCE: <user journey / API / CLI / inference; environment; PASS/FAIL/NOT RUN/NOT APPLICABLE>
MODEL EVAL (if applicable): <dataset and eval version; baseline and candidate; actual metrics/slices; comparable?; artifact ref>
IN-TASK REPAIR: <short attempted fixes/checks or NONE; remaining risk>
WEB REVIEW ACCESS: <COMPLETE / PARTIAL / NOT VERIFIED; exact reviewed refs, not an assumption>
DESTINATION: ChatGPT Web → «<confirmed/proposed exact chat name>»
```
No separate report file for a trivial task. A CI badge is not evidence until the relevant job, commit SHA and status are actually inspected. A passing build alone cannot certify the UI or ML results. If Web only sees default branch or a truncated PR, label review INSUFFICIENT EVIDENCE and request minimal targeted artifacts. Never auto-push or merge main, and never publish sensitive training records or model weights. On repeated in-task failures don't conceal attempted fixes or claim success.

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
CHANGED PATHS: <added, modified, removed, renamed; actual changes within the approved feature/component; for CONTROLLED also check specified paths>
SCOPE MATCH: MATCH | MISMATCH | NOT SCOPED (actual diff within approved feature/component; CONTROLLED also compare exact paths; mention exceptions)
CHECKS: <command | exit code | PASS/FAIL/NOT RUN; relevant verbatim excerpt; baseline if applicable>
TEST / QUALITY CONFIG CHANGES: <diff summary, test-weakening risk and approval>
DEPENDENCIES / LOCKFILES: <verified actual versions, changes or NONE>
SECURITY / DATA / CONTRACTS: <risk; required approvals; production not touched unless separately authorized>
MEMORY: <verified fact updates vs PROPOSED/STALE entries awaiting review>
EVIDENCE SOURCES: <GitHub commit/PR, Codex diff, CI job links, independently inspected artifacts; or NONE>
HANDOFF FILES / ACCESS: <exact existing paths or NONE; GITHUB ACCESSIBLE / LOCAL UPLOAD REQUIRED / CI LINK / NOT AVAILABLE; verified destination Web chat name>
RUNTIME ACCEPTANCE / MODEL EVAL: <actual scenario and evidence, or NOT RUN/NOT APPLICABLE>
IN-TASK REPAIRS: <scope-safe fixes and reruns, or NONE; no silent changed success criteria>
PR / CI / WEB ACCESS: <verified refs/status or NOT AVAILABLE>
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
