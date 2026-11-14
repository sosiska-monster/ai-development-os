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

## Optional Chat Register for parallel work

Continue the current Web/Codex chats by default. A Chat Register is **optional** and useful only when the user actually has several parallel workstreams, independent reviews or separate experimental chats. If needed, keep a short record in existing PROJECT.md or a maintained ChatGPT Project source: `CONFIRMED/PROPOSED CHAT NAME | SURFACE | PURPOSE | STATUS | BRANCH/WORKTREE | VERIFIED CHECKPOINT`. Don't create a new file or register for sequential work, or claim a chat exists without confirmation. A chat's name never proves Git branch/state.

At a **real cross-chat handoff**, use the confirmed destination or clearly mark the proposed name `PROPOSED`, with minimal verified context. If a separately created experiment chat ends, mark it `ARCHIVED` and return to the established development conversation; if the experiment was in the existing chat, record the outcome and simply continue there. When registry information is genuinely required but unavailable, mark it UNKNOWN rather than inventing details. No registry update after every task.

## One-task checkpoint, preserve useful context

**Default:** complete one explicitly authorized task and its necessary substeps; report DONE/PARTIAL/BLOCKED, meaningful changes, actual diff/check results and risks; **STOP before another independent task**. A TODO, suggested NEXT or active Goal is not authorization to continue. Preserve the worktree on failure and ask only about material blockers. No mandatory `NEW CHAT` field and no fresh-chat recommendation merely because the task is DONE.

**Across tasks:** continue the same Codex chat while its context remains useful. Switch only for an independent review/track, unusable or contaminated context, or the user's preference. For a real new chat, provide a minimal verified handoff and read AGENTS → current PROJECT/TODO → task-relevant requirements and decisions, not the full transcript. Native compaction may help a long ongoing conversation but is not a clean slate. Neither text instructions nor compaction can clear or create chat threads.

**Handoff:** update only *verified durable project facts* in existing PROJECT/TODO or their configured equivalents. Keep a short status in chat: task/result, Git branch/HEAD or UNKNOWN and dirty/untracked state, last check and actual exit or NOT RUN, blockers/approvals and next proposed action. Use a full Status Pack only for complex unresolved transfers. Do not create a fresh memory/handoff file per task. Never clear local .codex data, caches, chat history, checkpoints or user files in the name of "context hygiene". Never claim measured context usage without actual observation.

## Failure circuit breaker

Repeated no-progress attempts or expanding scope → **pause, don't destructively revert**. Capture command/output, diff, why hypotheses failed, current worktree and LAST GOOD; offer LOCAL FIX / REVERT (explicitly scoped and approved) / NEW BRANCH / REDESIGN. Two unsuccessful cycles is a diagnostic trigger, not a universal hard number. Preserve unrelated human edits and failed branch if useful.

Git checkpoints do not restore production data, external network effects or deleted third-party resources.
