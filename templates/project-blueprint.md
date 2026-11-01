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

## Architecture proposal
- Recommended stack/versions (verified vs assumed)
- Main modules/data flow/trust boundaries
- Public contracts, migrations and main operational risks
- Simpler alternative, trade-off and revisit condition
- Explicitly excluded components, services, tools or features

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
