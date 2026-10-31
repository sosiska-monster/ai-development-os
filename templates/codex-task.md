# Codex Task Prompt (template)

Use a compact version for small tasks. This is a **template**, not an instruction to configure Codex before the user approves an actual project's environment.

```text
TASK: <ID — title>
SIZE/RISK: <S/M/L, LOW/MODERATE/HIGH>

GOAL: <one verifiable outcome>
CONTEXT: <relevant references; discover unknown paths in scoped area>
IN SCOPE: <allowed changes>
OUT OF SCOPE: <explicit exclusions>
CONSTRAINTS: <approved architecture, security, dependencies>
ACCEPTANCE: <objective user-facing behavior and invariants>
PLAN-FIRST: <yes for large/high-risk; provide affected areas and STOP for approval>
VERIFY: <project fast check + task-specific tests, or explain why unavailable>
GIT: <approved branch/checkpoint/commit policy; respect uncommitted changes>
MEMORY: <which docs might need evidence-based updates>
STOP WHEN: <scope expansion, new unapproved deps, destructive operation, core contract change>
REPORT: <follow agreed Codex Evidence Report; explanations in Russian, preserve relevant raw outputs>
```
