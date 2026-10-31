# Project Blueprint — Approval Template

```text
PRODUCT: <problem, users, outcome>
SCOPE: <confirmed v1, intentionally excluded>
REQUIREMENTS: <confirmed IDs, open assumptions, blocked questions>
TECHNICAL DECISIONS: <recommended stack & architecture, counterargument, revisit condition>
ARCHITECTURE: <modules, boundaries, data, contracts, risks>
ENVIRONMENT PROFILE:
  Codex interface: <desktop / CLI / cloud etc>
  AGENTS.md: <scope/location>
  Verify/verify-full: <commands or planned setup>
  Git: <branches, commits, checkpoints, restoration>
  Memory: <paths and writing policy>
  Context/session: <handoff policy>
  Dependencies: <approval/verification>
  Safety: <permissions>
  Skills/MCP/Subagents: <selected and excluded>
  Hygiene: <generated files, storage, cleanup>
RISKS & OPEN QUESTIONS:
FIRST VERTICAL SLICE: <one verifiable value outcome>
READINESS: Requirements <READY/PARTIAL/BLOCKED>; Architecture <...>; Environment <...>
USER DECISION REQUESTED: approve / propose changes
```

Approval is not a promise that project-specific tools have been installed. Codex validates and implements the approved Environment Profile later.
