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

## One-task checkpoint and clean-context rotation

**Default:** finish only one explicitly authorized task and its necessary substeps. Return brief DONE/PARTIAL/BLOCKED, what changed and why, diff/check results and risks. End EVERY task report with **NEW CHAT: YES/NO + a concrete reason** and **STOP**. When DONE and the next work is a separate task, default **YES** and explicitly tell the user to open a fresh Codex chat. For PARTIAL/BLOCKED, prefer **NO** if resuming the same task in context is safer; if switching is needed, summarize verified worktree/check status first. Do not assert that a new chat was actually opened. Stop before the next independent task. A TODO, roadmap, suggested NEXT or active Goal is not permission to continue. If blocked, preserve dirty worktree and request an explicit direction.

**Across independent tasks:** when previous logs, retries or old hypotheses are cluttering the thread, recommend that the **user open a fresh Codex chat** in the same verified repository/worktree. The next chat reads AGENTS → current PROJECT/TODO → only task-relevant requirements and decisions. Do not copy the transcript. Previous chats remain available for reference. For an unfinished difficult task, native compaction (when actually available) may reduce history without dropping active task context; it is **not** a clean slate. Forking from old history may inherit that history. Text instructions cannot themselves clear chats or force new threads.

**Handoff:** update only *verified durable project facts* in existing PROJECT/TODO or their configured equivalents. Keep a short status in chat: task/result, Git branch/HEAD or UNKNOWN and dirty/untracked state, last check and actual exit or NOT RUN, blockers/approvals and next proposed action. Use a full Status Pack only for complex unresolved transfers. Do not create a fresh memory/handoff file per task. Never clear local .codex data, caches, chat history, checkpoints or user files in the name of "context hygiene". Never claim measured context usage without actual observation.

## Failure circuit breaker

Repeated no-progress attempts or expanding scope → **pause, don't destructively revert**. Capture command/output, diff, why hypotheses failed, current worktree and LAST GOOD; offer LOCAL FIX / REVERT (explicitly scoped and approved) / NEW BRANCH / REDESIGN. Two unsuccessful cycles is a diagnostic trigger, not a universal hard number. Preserve unrelated human edits and failed branch if useful.

Git checkpoints do not restore production data, external network effects or deleted third-party resources.
