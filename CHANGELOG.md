# CHANGELOG

## 0.2.0-draft — UNRELEASED / NOT PILOT-VALIDATED (2026-11-01)

- Product Goal Graph: customer-accepted finished product as root, intermediate required results, small Codex-ready task leaves, separate part-of and dependency DAG edges, requirement traceability and integrated root acceptance. Stored in existing project requirements/PROJECT + TODO; T65–T68 NOT RUN.
- Reference-first Codex → ChatGPT Web evidence handoff: final report indexes existing files/commits and test exits; optional narrow local `.ai-handoff/<TASK_ID>/` attachments or explicitly approved shared evidence. Do not imply local paths are Web-accessible or auto-upload/push data; T59–T64 NOT RUN.
- Critical Decision Gate: Web must approve consequential ML data split/stratification/grouping, dataset version, evaluation and model semantics before Codex runs training; add DECISION LOCK, explicit BLOCKED state, actual partition/leakage verification and preservation of suspect artifacts. 80/10/10 is illustrative only; tests T53–T58 NOT RUN.
- Explicit Web chat routing by exact, confirmed/proposed names (not YES/NO or generic current/new), plus a durable minimal chat register in product PROJECT or ChatGPT Project sources. Experimental model trials require approved isolated Git worktree/branch when they have side effects, verified Codex preflight, no mainline merge on failure, and approved safe cleanup. T47–T52 NOT RUN.
- Web-led experiment selection: proactively identify evidence-backed bottlenecks, compare no change/alternatives by expected value, risk and effort, and recommend one measurable pilot with baseline, success criterion and stop rule. Execution remains separately approved; no auto-install or claim of tested results. Scenarios T43–T46 NOT RUN.
- ChatGPT Web now recommends an explicit chat name, current stage, stay/new-chat decision, and Codex prompt destination; when proposing a new chat it supplies a verified-context starter prompt. No claim of automatic chat/UI switching; no extra mandatory chat-per-task ritual.
- Added an optional Russian `USER_GUIDE.md`: end-to-end requirements → MVP → implementation → testing → staging → hosting/production workflow; adaptive ChatGPT/Codex model routing and practical daily prompts. Documentation only; no production access, executed pilot or release claim.
- Dynamic two-way FAST / STANDARD / CONTROLLED task routing, risk-triggered escalation/de-escalation and low-risk direct Codex workflow.
- ChatGPT Project CORE as durable entry point; verified-on-demand GitHub module loading and explicit unknown-version behavior.
- Separate persistent requirements ledger template; change-request handling and authority distinction.
- Scope evidence covering commits, staged/unstaged and untracked files; Lite/Full reports, independent review guidance.
- Project-specific harness verification, baseline `verify`, safe brownfield recon, irreversible operations and production boundaries.
- Stale memory lifecycle and anti-poisoning rules; no destructive auto-revert on repeated failures.
- Expanded reproducible methodology test scenarios and rationale. All live tests **NOT RUN**.
- Adaptive model and reasoning-effort routing: use platform-native Default/auto when verified, otherwise recommend manual changes only when justified; no pretend UI automation; tests T21–T25 NOT RUN.
- Product Assurance Profile: adapt architecture, Definition of Done and verification to prototype/MVP/production/critical consequences, independently of dynamic FAST/STANDARD/CONTROLLED task risk; unrun scenarios T18–T20.
- Safe, scope-aware Hygiene Sweep between verified tasks/batches: remove obvious task-introduced waste, independently check diff/tests, protect dirty/untracked and high-risk artifacts; scenarios T26–T29 NOT RUN.
- One Task → concise Report with explicit NEW CHAT: YES/NO + reason → STOP for user direction; after DONE suggest a fresh Codex chat for next independent task by default; native compaction for unfinished same task. No forced UI reset, deletion of histories or per-task files; T30–T35 NOT RUN.
- ChatGPT Web is task dispatcher: one verifiable result per Codex prompt, separate READ CONTEXT and WRITE ALLOWLIST, STOP on expansion and actual diff review. T36–T38 NOT RUN.
- ChatGPT Web decomposes the approved MVP into small dependency-aware, reviewable vertical tasks; challenges conflicting/needlessly complex implementation proposals with a grounded simpler alternative. Single approved Codex task remains enforced; T39–T42 NOT RUN.
- Initially developed in draft PR #1; merging its documentation into `main` **does not release or pilot-validate 0.2.0-draft**. No stable `v0.2.0` tag or claim of technical enforcement.
- Added a minimal three-experiment pilot priority, independently runnable Git inspection commands for product repositories, and shorter non-essential CORE wording. Pilot results remain NOT RUN.

## 0.1.0 — Initial library baseline (2026-10-31)

- CORE/MANIFEST, six methodology modules and project templates, rationale and maintenance protocol.
- Initial GitHub commit: `9dfa6a8f0f547a89cf73b2e8411699b9766180b7`.
- Initial methodology was not empirically validated; no stable tag is asserted here.
