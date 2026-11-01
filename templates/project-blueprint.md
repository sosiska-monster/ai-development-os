# Project Blueprint / Environment Profile (adaptively sized)

Do not invent a detailed Blueprint for a three-line fix. Use for a product/new architecture or material refactor after requirement discovery; distinguish planning from actual installation.

## Product and source of truth
- Client goal, audience, raw specification location and privacy restrictions
- Confirmed requirements IDs / remaining AMBIGUOUS or BLOCKED questions
- MVP, critical Given/When/Then acceptance behaviors

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
