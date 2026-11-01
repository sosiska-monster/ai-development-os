# Requirements — customer intent, SDD, traceability

Use for a new specification, substantial requirement ambiguity or change request. Skip a separate ledger for trivial changes where the requirement is self-evident; never erase an existing confirmed baseline.

## Discover what the client means

- Preserve the original wording, source, date and confidentiality restrictions **in the authorized product workspace** (not in this public methodology library). Check whether sharing customer data with external AI services is permitted.
- Separate desired outcomes from a customer's suggested implementation. Distinguish client confirmation from developer recommendation or user technical approval.
- Use CONFIRMED, ASSUMED, AMBIGUOUS, CONFLICTING, MISSING, PROPOSED, DEFERRED; when replaced use SUPERSEDED with a link to the replacement.
- Ask the few questions that affect critical user journeys, acceptance, architecture, security, deadlines and cost. Offer reversible assumptions for nonblocking unknowns.
- Use Given/When/Then, examples or typed contracts only when they make behavior verifiable. Never mandate a schema tool merely because a methodology recommends one.

## Persistent requirement ledger

For nontrivial product work create or adapt `docs/ai/REQUIREMENTS.md` (template `templates/requirements-ledger.md`), anchored to the client's original text/source and linked to current tasks and tests.

Each entry: stable ID, requirement/acceptance, source, status, approving authority, implementation task(s), evidence (test/PR/commit). Mark verification separate from approval.

**Authority:** only authorized customer communication can establish customer CONFIRMED; the user can approve implementation decisions but must not be presented as the customer's approval. Codex can propose/record verification evidence, not upgrade a business requirement to CONFIRMED.

## Dynamic routing and readiness

Small low-risk correction may proceed FAST with concise acceptance. Significant new behavior or uncertainty becomes STANDARD; access-control, critical data, migration or public contract change becomes CONTROLLED with relevant approvals. No need to block architecture work for every small open question; record unresolved blockers and their consequences.

Requirement readiness: client goal and MVP boundary clear, essential behaviors testable, critical conflicts resolved or explicitly marked BLOCKED. Record missing information, never silently invent it.

## Change request / Spec Pivot

1. Compare requested behavior against **previous confirmed baseline** from the ledger; identify affected IDs, tasks, tests, public contracts and data.
2. Preserve original requirement as SUPERSEDED when replaced; add new ID/source/authority. Never overwrite history as if client always requested the new behavior.
3. Evaluate migration, security, cost and release impact; update Blueprint, TODO/Decision, AGENTS pointers **only when relevant**.
4. Reassess task mode dynamically; stop in-flight implementation when its acceptance is now wrong or a new high-risk effect is discovered.
5. Resume only against approved revised acceptance criteria, with regression checks and a safe checkpoint.
