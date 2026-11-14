# Session Handoff / ChatGPT Status Pack

A status pack summarizes *verified current state*, not a memory of everything said. For ordinary tasks, **do not create a file**: give a concise report, update durable facts in existing PROJECT/TODO only when necessary, and STOP before starting another independent task. Continue the same Codex chat by default. If a new chat is actually needed (independent review, unusable context or user choice), pass the minimal verified context; compaction is only a continuation aid. A NEXT suggestion does not authorize work.

**Lightweight report (default for small tasks, no new document):**

```text
STATUS: DONE / PARTIAL / BLOCKED
WHAT / WHY: <1–2 sentences>
PATHS: <main changes and scope>
CHECKS: <actual command + exit code or NOT RUN>
RISKS / BLOCKERS: <NONE or concrete fact>
NEXT: <optional next task suggestion; do not execute; STOP>
```

**Full Status Pack** only for significant unresolved transitions, missing context or high-risk handoffs. Before moving sessions ensure actual Git state, a last checked result and the next task are recorded. No silent requirement confirmations.

```text
AI DEVELOPMENT OS STATUS PACK
Product repo / Git URL:
Method library version / immutable SHA (verified or UNKNOWN):
Current operating mode + trigger to escalate/de-escalate:
Requirements source / active REQ IDs (link to actual REQUIREMENTS.md):
Architecture / approved Decision IDs:
Current task ID, acceptance / next vertical result:
Actual Git branch, base SHA, HEAD, dirty + untracked state:
LAST GOOD verified SHA / verify command, exit, date:
Changes since last chat (commit/PR links, scope and known risks):
Current PROJECT / TODO links:
Known PROPOSED or STALE memory not treated as fact:
Approvals / production boundary / blockers:
Next concrete action:
```

For a new Codex session load project AGENTS → current PROJECT/TODO → only task-relevant REQUIREMENTS/Decision/Bugs/Gotchas. Do not replay every log or upload customer secrets.
