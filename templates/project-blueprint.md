# Project Blueprint / Environment Profile (adaptively sized)

Do not invent a detailed Blueprint for a three-line fix. Use for a product/new architecture or material refactor after requirement discovery; distinguish planning from actual installation.

## Product and source of truth
- Client goal, audience, raw specification location and privacy restrictions
- Confirmed requirements IDs / remaining AMBIGUOUS or BLOCKED questions
- MVP, critical Given/When/Then acceptance behaviors

## Product Assurance Profile — required decisions, minimal text

The product's **quality/assurance target** is independent of the current task's FAST / STANDARD / CONTROLLED mode. Agree on a lightweight profile before choosing how much architecture, testing and operational setup is needed.

- **Intended use and lifespan:** disposable exploration, demo, internal utility, MVP, enduring customer-facing service, or higher-consequence system.
- **Provisional assurance level:** PROTOTYPE / MVP / PRODUCTION / CRITICAL (labels are starting points, not automatic guarantees). State the *reason and explicit user approval*, and revisit when the product's audience or deployment changes.
- **Consequences and constraints:** users, real vs synthetic data, security/privacy, regulatory or contractual obligations, reliability/recovery targets, performance, support team, budget/deadline, migration and deployment environment.
- **Definition of Done:** minimum meaningful functional, automated/manual verification, security, maintainability, observability, deployment and recovery expectations. State which are intentionally out of scope and what triggers reevaluation.
- **Debt boundary:** temporary shortcuts allowed only where the consequences are acceptable; mark removal conditions. Production and sensitive data controls are **never waived simply because the project is called a prototype**.
- **Evidence:** project-specific checks and observed readiness, not a generic declaration of "production quality."

This profile informs the architecture and project environment; it does **not** require a new permanent file. For a small product, keep it as a short section in PROJECT/Blueprint.

**Simplicity-first design:** start with the existing architecture or the smallest understandable deployable design that satisfies confirmed requirements and the approved assurance profile. Explicitly name the components **not introduced** and the concrete conditions that would justify adding them. Avoid speculative microservices, queues, extra layers, dependencies or enterprise infrastructure. Reuse/modify/remove before adding abstractions; simplicity never waives necessary security, data integrity or verification.

**Composable MVP path (when relevant):** prefer proven ready-made modules/services to custom-built subsystems for early demand validation. List only major external dependencies and constraints, the smallest real-user launch checks (data, security, deployment/recovery), and the observed signal that would justify replacing or strengthening each component. Evolve one bounded module at a time; do not build speculative plugin architecture.

## Chat Register (short optional section in the PRODUCT PROJECT.md)

Keep only the named Web/Codex chats actually used or explicitly planned:
`EXACT CHAT NAME | ChatGPT Web / Codex Desktop | responsibility/boundary | PROPOSED / ACTIVE / PAUSED / ARCHIVED | approved Git branch/worktree or N/A | last verified checkpoint`.
ChatGPT Web routes every handoff to the **exact registered/proposed chat name** and can propose a new chat with starter context; it must not claim to create the chat or remember unshared other chats. A failed experiment is ARCHIVED, not merged into main. Store this map in existing PROJECT.md or its maintained ChatGPT Project source; do not change main merely to track a running experiment. No separate registry file required.

## Product Goal Graph (minimal single source of truth)

- **ROOT G0:** customer's desired finished product + confirmed end-to-end acceptance and explicit exclusions, in existing PROJECT.md/requirements.
- **Outcome tree:** stable parent IDs, must-have vs optional/deferred sub-results; each leaf is a bounded testable task. Preserve requirement IDs and concrete acceptance. Do not infer unknown product features.
- **Dependency DAG:** separately record `DEPENDS_ON` edges; check cycles and distinguish technical dependencies from parent-child composition. No invented file dependencies before repository recon.
- **Durable state:** keep task-node and edge rows in existing product TODO.md (or agreed equivalent), e.g. `ID | PARENT | REQ | ACCEPTANCE | DEPENDS_ON | STATUS | EVIDENCE`; Mermaid is a generated view only. Detail nearest few leaves, not full speculative implementation.
- **READY / VERIFIED / ACCEPTED:** only dispatch a leaf with prerequisites/critical decisions satisfied; verify code/test evidence before accepting; root requires integrated end-to-end product check and relevant customer signoff, not merely closed leaf tasks.

## Progressive preview/approval for underspecified user-facing features

For a vague UI requirement, Web first proposes a small, testable design/content concept with a text wireframe or optional visual preview, recommended choice and up to two meaningful alternatives. Mark UI layout, CTA and copy `PROPOSED`; approved business facts `CONFIRMED`; unknown prices/currency/billing terms `MISSING` rather than inventing them. User approves the coherent experience before Codex implementation. Store concise approved outcome and reference under the same product goal node/requirements; don't create a new permanent design document for every screen. Codex receives approved behavior, responsive layout and acceptance criteria. Trivial/established designs can skip separate review.

## Outcome-based verification and model evaluation (when relevant)

- **User-observed result:** one or more approved Given/When/Then journeys per meaningful goal node; for UI preview/mobile/CTA, for APIs/CLI direct invocation, for ML actual inference on relevant holdout. List tool/runtime needed and safe environment; `NOT RUN` when inaccessible.
- **Automated independent checks:** existing deterministic `verify`, PR CI if useful, test/config/scope integrity and real baseline; exact owner of CI/protected branch/permission controls and whether *observed*.
- **Model Evaluation Contract (ML/LLM only):** approved dataset/task/cases version, split/group/time/seed or rubric, baseline/model/prompt/code version, metrics/thresholds and critical slices, privacy and final holdout policy; require comparable verified evidence before promotion. Record in existing project decision/config, not mandatory separate document.
- **Feedback:** when a real failure occurs, create a minimal reproducible regression case tied to the goal node and observed environment; compare before/after verified results and manual effort. Don't mark a rule effective from text alone.

## Existing repository AS-IS / TO-BE (only for active products)

- Do **not** initialize a new repository or overwrite previously accepted requirements, project memory, worktrees and running services. Scope audit to whole architecture only when justified; otherwise to the affected subsystem.
- **AS-IS:** actual repo branch/HEAD/dirty/untracked, observed working journeys and known defects, module/dependency/contract map, current safety/test baseline (including UNKNOWN/NOT RUN), historical design constraints.
- **Confirmed debt:** code paths/symbols and verified effect, relevant user/goal impact, severity, why "keep as is" is inadequate. Separate hypotheses from evidence and cosmetic tastes.
- **Minimal TO-BE:** keep/reuse vs eliminate/replace; one scoped fix candidate, affected contracts/data/consumers, acceptance before/after and rollback needs; update existing goal graph without rewriting it.
- **Approval gate:** no refactor, tests that mutate state, dependency install, graph rewrites or Git publish during read-only discovery. Bootstrap/reconfiguration only if observed need and separately approved.

## Architecture proposal
- Recommended stack/versions (verified vs assumed)
- Main modules/data flow/trust boundaries
- Public contracts, migrations and main operational risks
- Simpler alternative, trade-off and revisit condition
- Explicitly excluded components, services, tools or features

## Adaptive model / reasoning policy (only when useful)

- Available ChatGPT and Codex model/effort options, native Default/auto behavior, usage limitations: VERIFIED / UNKNOWN.
- Initial choice: use a suitable efficient option; reserve higher capability/effort for materially difficult reasoning, not every task in a production project.
- Escalation: failed *verified* outcomes or genuinely novel complexity after improving context/prompt and splitting work; de-escalate after the hard part.
- Change actor: native router if observed, otherwise **user's model picker**; project instructions do not switch the interface.
- Compare results using verified quality, rework and actual time/usage if available. No unsupported provider claims or secret sharing.

## Codex Environment Profile
- Codex Desktop/CLI/Cloud actual setup and permission model
- Project `AGENTS.md` + memory/requirements routing
- Git branch/worktree/checkpoint/dirty-worktree policy
- `verify` and baseline status; relevant CI and security controls, evidence of working configuration
- Dynamic modes: FAST / STANDARD / CONTROLLED, risk triggers and approval rules
- Skills/MCP/subagents: included for specific demonstrated need or none
- Method library commit SHA/release marker and planned compatibility update

## Readiness and approval
- Requirements: READY / PARTIAL / BLOCKED
- Architecture: READY / PARTIAL / BLOCKED
- Environment: PLANNED / IMPLEMENTED / VERIFIED / BLOCKED
- Explicit user approval of architecture and environment, dated/contextual
- Separate user request for Codex Bootstrap; no assumed authorization
