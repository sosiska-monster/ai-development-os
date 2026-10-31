# Codex AGENTS.md — Minimal Project Template

**Use only after adapting to the actual project.** Codex recognizes `AGENTS.md`; the files linked below are project conventions, not built-in Codex features. Inspect existing AGENTS.md and environment first.

```md
# Codex project instructions

## Start
Read this file, then docs/ai/PROJECT.md and the active entry in docs/ai/TODO.md.
Open other docs only when relevant.

## Verify
Fast check: `<project-specific command or documented fallback>`.
Full check: `<only if needed>`.
Report command, exit code and relevant verbatim output.

## Scope and integrity
Deliver only the agreed task. Report extra findings rather than silently fixing them.
Keep meaningful tests strict. Changes to expected behavior, skips, typing/lint configuration,
or new dependencies require documented justification and applicable approval.
Verify packages, versions, licenses and installed-version APIs. Include lockfile changes.

## Git
Respect pre-existing changes. Commit only scoped, verified work in an authorized branch.
No destructive reset, history rewrite, push, force operations or --no-verify without approval.

## Memory routing
On bugs, search docs/ai/Bugs.md and docs/ai/Gotchas.md first.
On architecture decisions, consult docs/ai/Decision.md and architecture docs if present.
Update TODO/PROJECT only with verified facts; propose evidence-linked Bugs/Gotchas entries.
Never mark a Decision APPROVED without explicit user approval.

## Reporting
Use the project Codex Evidence Report; use base-commit diff stats after commits.
Redact secrets. Stop for scope expansion or risky unknowns.
```
