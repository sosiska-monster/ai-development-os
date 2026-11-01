# Delivery — dynamic routing, vertical slices and evidence

**When:** implementing or reviewing work. Read with the task's risk and actual project state, not as a ritual.

## Select an initial mode, then re-route continuously

| Mode | Entry indicators | Required minimum |
|---|---|---|
| **FAST** | Small, reversible, well-understood local change; no material contract, data, security, dependency or architectural effect; working verification already exists | Codex can execute directly; scoped diff, targeted check, Lite report and Git checkpoint when justified |
| **STANDARD** | Ordinary user-visible feature, moderate bug or moderate uncertainty | Short acceptance-based task, focused verification, changed-path review, Full report when warranted |
| **CONTROLLED** | Migration/deletion, production, security/auth, confidential data, payments, public API, high-cost or irreversible impact, large ambiguity, architectural change | Plan-first + user approval, risk/rollback plan, independent diff and relevant tests, Full report, no silent production action |

There is **no hard file-count threshold**. A one-line auth change can be CONTROLLED; a ten-file mechanical rename may be STANDARD. Choose the cheapest mode that still covers actual risk.

**Dynamic transition protocol:**
- Evaluate on task intake **and at every new fact**: unexpectedly changed files, critical contract, new dependency, failed checks without progress, data exposure, user changes scope.
- FAST → STANDARD/CONTROLLED or STANDARD → CONTROLLED: **stop scope-expanding work**, preserve current uncommitted state, report trigger, impact and options; obtain approval when permissions, risks or product contract change. A tool/AI may recommend escalation, not grant itself new authority.
- CONTROLLED → STANDARD/FAST or STANDARD → FAST: possible after the risk is resolved and scope is verified safe. Keep any risk-driven check already required; do not retroactively erase evidence or permission decisions.
- At any mode, use extra checks if a specific invariant demands them. Trigger does not automatically mandate a new meeting/document.
- For serial small edits, send a concise batch summary to ChatGPT periodically or before a dependent architectural decision; no unnecessary human clipboard loop on every button.

## Two independent dimensions: product assurance and task risk

Every task inherits the product's **approved assurance baseline** (documented in the Blueprint/PROJECT/Environment Profile), while FAST/STANDARD/CONTROLLED determines how carefully **this particular change** is handled. A FAST change in production still uses the baseline safety and quality checks applicable to the affected behavior; a prototype must use CONTROLLED when a task becomes sensitive, destructive or irreversible. Do not auto-promote every production task to CONTROLLED or turn every prototype task into FAST.

When a prototype becomes an externally used product, or a demo starts processing real data, reassess the project's assurance profile, tests, deployment and recovery readiness **before the increased exposure**. Such transitions are a product decision requiring appropriate user signoff; they are not a new mode or a fixed file-count threshold.

## Task contract

Use objective GOAL, current relevant context, IN/OUT OF SCOPE, optionally EXPECTED_DIFF_PATHS, acceptance criteria, verification, stop/escalation triggers and Git/memory policy. The path set may be **provisional** when the codebase is unknown; Codex must report discovery and request expansion for materially risky new areas. Legitimate tests/lockfiles can be approved additions, never silently exempt.

## Scope check — actual repository evidence

For each task use a base SHA and inspect:
- committed changes vs base (e.g. `git diff --name-status BASE..HEAD` for an ordinary linear task; choose correct merge-base semantics for PRs),
- staged/unstaged changes (`git diff --name-status`, `git diff --cached --name-status`),
- untracked files (`git ls-files --others --exclude-standard`),
- dirty pre-existing changes **separately**, so they are not falsely attributed to Codex.

Compare *all* effective task paths with approved scope. If outside scope, report MISMATCH, explain and seek approval; **never mark ACCEPT just because tests pass**. Path checks don't prove behavior, test integrity or freedom from secret leakage.

## Integrity and verification

- Test behavior from approved requirements; use risk-based test-first for critical invariants. Do not replace failing tests with skips, removed assertions, mocks or type/lint suppression to fake green results.
- Test changes can be legitimate when requirements change; disclose exact diff and approval/evidence. Scan configuration, dependency and lockfile modifications, too.
- A stable, fast project `verify` should exist **before ordinary feature work when practical**; for an empty repo the first environment setup may establish it. Record baseline SHA and baseline results; `verify-full` by risk.
- Repeat failures without progress → pause, diagnose and escalate; never automatically erase the worktree or run destructive restore.
- For product behavior review, prefer independently retrieved GitHub diff, CI results or user-inspected Codex diff. Command output authored by Codex alone is **not independent proof**.

## Reports and decisions

FAST/LOW uses the Lite evidence format. STANDARD generally Full if meaningful; CONTROLLED always Full with targeted diff, tests, and approval status. See `templates/codex-report.md`.

ChatGPT verdict: **ACCEPT / FIX / REWORK / INSUFFICIENT EVIDENCE**. If real artifacts are unavailable, do not assert verified success. A vertical slice is valuable user behavior, not volume of files.

Git checkpoint: logical verified commits, preserving unrelated/uncommitted work; no silent push, force, reset, cleaning or production operations. Use branch/worktree when it improves isolation, not as a universal ritual.
