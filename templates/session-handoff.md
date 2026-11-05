# Session Handoff / ChatGPT Status Pack

A status pack summarizes *verified current state*, not a memory of everything said. For ordinary one-task handoffs, **do not create a file**: finish with a concise chat report, update only durable facts in existing PROJECT/TODO when necessary, then STOP. For a new independent task, user may open a fresh Codex chat in the same verified repo; it reads AGENTS → PROJECT/TODO → relevant requirements. A new chat is not an automatic effect of these instructions; compaction is only a continuation aid, not an empty context. A NEXT suggestion does not authorize work.

**Lightweight report (default for small tasks, no new document):**

```text
STATUS: DONE / PARTIAL / BLOCKED
WHAT / WHY: <1–2 sentences>
PATHS: <main changes and scope>
CHECKS: <actual command + exit code or NOT RUN>
RISKS / BLOCKERS: <NONE or concrete fact>
NEW CHAT: YES / NO — <clear reason; YES by default after DONE for a separate next task>
NEXT: <suggest one next task; ask user; STOP>
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
