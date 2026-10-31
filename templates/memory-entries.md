# Project Memory Records — Examples

These are **project-level** files, NOT stored in the methodology repository. Adapt filenames to actual established capitalization; avoid duplicated files differing only by case.

## PROJECT.md

Passport <= 200 lines: product, purpose, current stage, stack, main modules, critical constraints, commands, map of documentation. Link to details rather than copying logs or entire decisions.

## TODO.md

```md
## IN PROGRESS
- T-031 | <goal> | owner/branch: ... | done when: ... | next: ...
## NEXT
- ...
## BLOCKED
- ...
## DONE (archive older entries)
- T-029 | ... | commit/PR: ...
```

## Bugs.md

```md
### B-017 — <symptom>
Status: OPEN | RESOLVED
Reproduction: ...
Cause: HYPOTHESIS | CONFIRMED (evidence: command/log/commit)
Fix: ...
Verification: ...
Commit: ...
```

## Gotchas.md

```md
### G-004 — <pitfall>
When: ...
Avoid: ...
Why: ... (evidence)
Safe procedure: ...
Linked: B-... / D-...
Status: ACTIVE | OBSOLETE
```

## Decision.md

```md
### D-006 — <decision>
Status: PROPOSED | APPROVED | SUPERSEDED | REJECTED
Approval: <user confirmation / reference; required for APPROVED>
Context: ...
Decision: ...
Rationale: ...
Alternatives rejected: ...
Revisit when: ...
```

## WordStyle.md

Personal communication, writing and engineering preferences. Store outside client repositories unless explicitly agreed. Update only from user preferences, not AI guesses.
