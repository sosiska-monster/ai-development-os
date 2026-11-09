# Requirements — customer intent, SDD, traceability

Use for a new specification, substantial requirement ambiguity or change request. Skip a separate ledger for trivial changes where the requirement is self-evident; never erase an existing confirmed baseline.

## Discover what the client means

- Preserve the original wording, source, date and confidentiality restrictions **in the authorized product workspace** (not in this public methodology library). Check whether sharing customer data with external AI services is permitted.
- Separate desired outcomes from a customer's suggested implementation. Distinguish client confirmation from developer recommendation or user technical approval.
- Use CONFIRMED, ASSUMED, AMBIGUOUS, CONFLICTING, MISSING, PROPOSED, DEFERRED; when replaced use SUPERSEDED with a link to the replacement.
- Ask the few questions that affect critical user journeys, acceptance, architecture, security, deadlines and cost. Offer reversible assumptions for nonblocking unknowns.
- Use Given/When/Then, examples or typed contracts only when they make behavior verifiable. Never mandate a schema tool merely because a methodology recommends one.

## Constructive challenge before implementation

ChatGPT Web must not reflexively agree with the user's suggested technical implementation. First separate **what the customer needs** (confirmed outcome/acceptance) from **how the user proposes to build it** (technical hypothesis). If a proposal conflicts with the specification, real constraints or evidence, or causes needless complexity, say so respectfully and concretely: **issue → supporting fact or explicit uncertainty → consequence → smaller viable alternative → user decision needed**. Prefer a short argument, not a mandatory decision memo. If the approach is reasonable, accept it; no performative criticism.

Do not unilaterally rewrite customer-confirmed behavior, claim customer approval from a developer's preference, or start Codex implementation while a material conflict remains unresolved. For reversible, low-risk alternatives, recommend a default and ask only for consequential decisions.

## Determine the intended quality bar before overengineering

Ask what the product is **for**, how long it must live, who will actually use it, whether data are real/sensitive, what failures cost, what maintenance and recovery are expected, and the deadline/budget. Propose a lightweight Product Assurance Profile (PROTOTYPE / MVP / PRODUCTION / CRITICAL as adaptable labels), its Definition of Done and important deliberate exclusions. Obtain the user's approval; don't silently treat a quick demo as a production platform or a production promise as permission for needless enterprise complexity. Baseline safety and contractual obligations remain even for throwaway experiments. Revisit the profile if the product's real audience, data or deployment changes.

## Persistent requirement ledger

For nontrivial product work create or adapt `docs/ai/REQUIREMENTS.md` (template `templates/requirements-ledger.md`), anchored to the client's original text/source and linked to current tasks and tests.

Each entry: stable ID, requirement/acceptance, source, status, approving authority, implementation task(s), evidence (test/PR/commit). Mark verification separate from approval.

**Authority:** only authorized customer communication can establish customer CONFIRMED; the user can approve implementation decisions but must not be presented as the customer's approval. Codex can propose/record verification evidence, not upgrade a business requirement to CONFIRMED.

## Critical Decision Gate — semantic choices belong to Web/user, not Codex

During requirements, architecture and **before any irreversible or expensive execution**, Web identifies missing parameters that materially determine **what the product means, how it is evaluated or what data are changed**. Examples: ML training/validation/test split, class balancing or sample weights, leakage boundaries, evaluation metric and success threshold, data retention, authorization rules and public contract behavior. These are **product/methodological decisions**, not ordinary coding defaults. A safe implementation choice (variable name, formatting, localized refactor) can stay with Codex; do not seek human approval for every trivial setting.

**For ML dataset partitioning, explicitly settle before the training run:**
- What counts as an independent unit: sample/record, person, source, session, image/video family, timestamp, or other real-world group? What would constitute duplication/leakage?
- Which strategy fits the product: shuffled/random, label-stratified, group-aware, chronological/time-based, or cross-validation? **80/10/10 is an example, not a default mandate**; document the reasoning and feasibility, especially for small/imbalanced datasets.
- Approved **train / validation / final test** proportions or counts, expected rounded counts, dataset identity/version, random seed or deterministic temporal cutoffs. Ensure disjoint partitions; fit preprocessing/feature selection/augmentation only on training data as applicable, and keep final test data from model selection/tuning.
- Agreed evaluation metrics, test holdout policy and acceptance threshold. Class weights and split proportions are **different decisions**; do not conflate them.

**Decision flow:** Web reports `DECISION REQUIRED: <missing variable> | options/trade-offs | recommended value/strategy (PROPOSED) | user approval`. Codex receives `DECISION LOCK: <approved values + authority/source>`, with permitted variation only if expressly bounded. If a critical decision is missing, ambiguous or incompatible with actual data, Codex responds `BLOCKED — CRITICAL DECISION MISSING` **before changing the split, fitting a model, exporting results or spending a long training run**; it may do an explicitly approved read-only inventory to collect counts. A preset in a library, a guess in generated code, a previous model result or a "usual 80/10/10" suggestion is **not approval**. User may explicitly delegate a bounded choice to Web after evaluating trade-offs; record the choice.

**Verification contract for a split task:** inspect actual output counts/ratios, their sum against the dataset, no train/val/test item overlap or relevant group leakage, sufficient examples per important label where feasible, reproducibility and saved split/config/version. Do not fabricate passing checks from the intended configuration. If a run used an unapproved split, mark its reported metrics as **NOT COMPARABLE / NEEDS REVIEW** until the real split and evaluation process are audited; do not silently overwrite checkpoints, data or artifacts. Repair/retrain only after a new approved scoped task.

## Dynamic routing and readiness

Small low-risk correction may proceed FAST with concise acceptance. Significant new behavior or uncertainty becomes STANDARD; access-control, critical data, migration or public contract change becomes CONTROLLED with relevant approvals. No need to block architecture work for every small open question; record unresolved blockers and their consequences.

Requirement readiness: client goal and MVP boundary clear, essential behaviors testable, critical conflicts resolved or explicitly marked BLOCKED. Record missing information, never silently invent it.

## Change request / Spec Pivot

1. Compare requested behavior against **previous confirmed baseline** from the ledger; identify affected IDs, tasks, tests, public contracts and data.
2. Preserve original requirement as SUPERSEDED when replaced; add new ID/source/authority. Never overwrite history as if client always requested the new behavior.
3. Evaluate migration, security, cost and release impact; update Blueprint, TODO/Decision, AGENTS pointers **only when relevant**.
4. Reassess task mode dynamically; stop in-flight implementation when its acceptance is now wrong or a new high-risk effect is discovered.
5. Resume only against approved revised acceptance criteria, with regression checks and a safe checkpoint.
