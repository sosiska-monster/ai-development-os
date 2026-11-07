# Project memory records — example formats, not compulsory file count

Store in the real product repository, not in this library. Preserve established case-sensitive names and existing documentation. An empty tiny project may combine files when their ownership/status remains explicit.

## PROJECT.md — current verified passport

Purpose, stack, current module map, active interfaces, constraints, documentation links, verification command. Keep concise (suggested up to ~200 lines). Avoid duplicating current task status if TODO already owns it. Document current observation, not a speculative design.

## TODO.md — operational task truth

```md
## IN PROGRESS
- T-031 | goal | acceptance REQ-021 | branch/base SHA | next
## BLOCKED / NEXT
- ...
## LAST GOOD
- SHA: <verified commit> | verify command / result / date
## DONE
- T-028 | commit/PR: ... (archive old records)
```

## Bugs.md — defect history

```md
### B-017 — <observable symptom>
Status: OPEN | RESOLVED | STALE
Reproduction / environment: ...
Cause: HYPOTHESIS | CONFIRMED (with evidence, version and link)
Fix / verification / commit: ...
Revisit when: ...
```

## Gotchas.md — reusable, checked pitfall

```md
### G-004 — <pitfall, not a generic command>
Status: PROPOSED | ACTIVE | STALE | OBSOLETE
Scope / affected code or dependency version: ...
Evidence and last verified SHA/version: ...
Safe procedure / caveat: ...
REVISIT_WHEN: <specific version, dependency, module, date or condition>
Linked bug/decision: ...
```

## Decision.md — user-approved choices, not hidden AI policy

```md
### D-006 — <decision>
Status: PROPOSED | APPROVED | STALE | SUPERSEDED | REJECTED
Approval evidence (required for APPROVED): <user/date/context>
Context, reason, rejected alternatives, constraints: ...
Verified against / affected files or versions: ...
REVISIT_WHEN: <specific condition; may be event-based>
Replacement reference when SUPERSEDED: ...
```

**Staleness policy:** If a revisit condition occurred, flag PENDING REVIEW / STALE; don't automatically erase a past decision or assume auto-detection. Never load stale notes as present-tense instructions. Code and tests establish observed implementation; client-confirmed requirements establish desired behavior.

## WordStyle.md

Portable personal writing and working preferences, **outside customer repo** unless the user approves. Update from user direction, not Codex speculation. Read only when the task benefits (e.g., authored messages/UI copy), not as a compulsory startup file.
