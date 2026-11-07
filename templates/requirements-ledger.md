# Product Requirements Ledger — template

Store as `docs/ai/REQUIREMENTS.md` in the *product* repo when requirements are meaningful enough to warrant tracking; this file is only a template. Preserve full customer wording/source separately if confidential.

| ID | Desired behavior + acceptance | Source and date | Status | Confirmed by | Task/PR | Verified by |
|---|---|---|---|---|---|---|
| REQ-001 | Given ... When ... Then ... | client brief 2026-... | AMBIGUOUS | — | — | NOT VERIFIED |

**Status:** CONFIRMED / ASSUMED / AMBIGUOUS / CONFLICTING / MISSING / PROPOSED / DEFERRED / SUPERSEDED.

**Rules**
- CONFIRMED requires customer/authorized product-owner evidence, date and reference. Tech approval by the developer is a different decision.
- Implementation completion is not requirement confirmation. The `Verified by` field is a test, artifact, PR/commit, or NOT VERIFIED.
- Codex may propose new rows and add verifiable implementation evidence. It may not silently change a customer requirement, approve it, or erase a superseded baseline.
- For a change request mark old entry SUPERSEDED → REQ-new, show affected tests/tasks/contracts; do not silently rewrite acceptance.
- Respect contracts/privacy: if customer's original brief should not be in Git or external AI, store only approved identifiers and safe summaries with a controlled source link.
- Small projects may keep a concise requirements section in `PROJECT.md` if there are no complex or evolving customer contracts; avoid gratuitous empty files.
