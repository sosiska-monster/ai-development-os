# Memory, context and intelligent recovery

**When:** a new session, contradictory or stale notes, repeated failures, changed requirements or recovery.

## Truth, authority and memory ownership

- **Requirements Ledger (customer authority):** approved *desired* behavior and its source; not merely Codex's implementation.
- **Actual repository state:** verified code, schemas, lockfiles and tests show current implementation; can be incorrect relative to requirements.
- **Project memory:** `PROJECT.md` (current passport), `TODO.md` (active status), `Bugs.md` (defect timeline), `Gotchas.md` (validated pitfalls), `Decision.md` (approval-controlled architecture), personal `WordStyle.md` (outside client repo). Optional file merges in tiny products must preserve distinct semantics.
- **Library memory:** `RATIONALE.md` explains the methodology, not a client's system.

Never promote hypotheses, stale logs or an AI report to normative project truth. A Code/Memory conflict requires inspection; a Code/Confirmed-Requirement conflict requires correction or an authorized change of requirement.

## Reads and writes

New Codex chat: `AGENTS.md` → current `PROJECT.md` + active `TODO.md` (or configured equivalents), then task-relevant `REQUIREMENTS.md`/Decision/Bugs/Gotchas. Don't read all histories every time.

Codex updates PROJECT/TODO only with verified facts. It proposes new Bug/Gotcha diagnoses as PROPOSED/HYPOTHESIS with reproduction, evidence, affected versions and `REVISIT_WHEN`. User reviews significant diagnoses. Decision APPROVED only on explicit consent; customer requirement CONFIRMED only with authorized confirmation.

For notes that contradict current code/dependency versions or trigger REVISIT_WHEN, mark **STALE/PENDING REVIEW** rather than deleting them or assuming they are wrong. Expired/stale material is historical context, not current instruction. Review and archive obsolete records, keeping linked history in Git.

## Context handoff

Before changing session, preserve the task's baseline SHA, branch, Git dirtiness, last verified `verify` result and checkpoint, next action, active requirements IDs and links, uncertain claims, approvals and remaining risks. A new chat can consult project facts instead of replaying the transcript. Don't claim actual context percentage without a measurement.

## Failure circuit breaker

Repeated no-progress attempts or expanding scope → **pause, don't destructively revert**. Capture command/output, diff, why hypotheses failed, current worktree and LAST GOOD; offer LOCAL FIX / REVERT (explicitly scoped and approved) / NEW BRANCH / REDESIGN. Two unsuccessful cycles is a diagnostic trigger, not a universal hard number. Preserve unrelated human edits and failed branch if useful.

Git checkpoints do not restore production data, external network effects or deleted third-party resources.
