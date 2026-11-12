# Usage observability — measurements, not a token-spending agent

**Status:** OPTIONAL local collection tooling and methodology protocol; not installed into any PRODUCT repo and not proven on real Codex Desktop usage. This methodology GitHub repo contains no user's token records.

## Objective / sources

Reduce tokens, credits, repeated work and human handoffs **per verified customer outcome**, not simply per chat. Compare similar task classes, actual quality and model/tool settings. Don't optimize by deleting tests or shortening critical context.

Start with provider-native measurements: where available, ChatGPT Desktop **Settings → Usage & billing** shows Work/Codex usage by period, model, reasoning and speed, sometimes by chat, and history split by cached/uncached input and output. The user can manually transcribe relevant numbers; availability and billing units depend on plan/workspace and can be incomplete for subagents/background actions. Check current UI rather than assuming all metrics exist. ChatGPT Web may not expose exact per-turn tokens to this methodology. For API-powered workflows, usage response fields can give actual input/output/cached tokens; that does **not** grant access to subscription ChatGPT chat billing. In the Codex CLI, /status can sometimes reveal session context/limits; whether it shows exportable usage depends on version. Local Codex JSONL rollouts are **private conversation traces**, may change schema and may lack token events; NEVER ask the agent to inspect/print all rollouts or upload them.

Separate **observed** values from **estimates**. Never represent plan credits/allowance as dollars or API billable tokens. Cached input is a subset of input; don't add twice. Period-wide snapshots and per-task records can overlap; **never add them together**. Missing value is UNKNOWN, not zero. A high raw token count alone is not a diagnosis: tool execution, reasoning, retries and repeated context may all matter.

## Minimal task record

One small JSONL record **per task + surface** (Web/Codex/Work/API), or a clearly labeled separate **period snapshot**. A task record can contain only:
- random or non-identifying `id`; date, `task_id` from Product Goal Graph, `surface` and `source`, `measurement=observed|estimate`
- optional `model` / `effort`; `input_tokens`, `cached_input_tokens`, `output_tokens` if actually displayed; `credits` if actually displayed; `minutes`, `retries`, `handoffs` if actually measured
- `result=ACCEPTED|REWORK|BLOCKED|NOT_VERIFIED|NA` grounded in **Web/customer verification**, not Codex's DONE report
- for broad UI usage summaries use `scope=period` and `period` label, not a fake task-level record.

Do not collect full messages, code, prompts, secret keys, file bodies, private customer names, raw transcripts, system prompts, API response content, screenshots with user data or telemetry without permission. Token counts can reveal activity patterns; keep local and private. Store in a user-approved, gitignored location such as `.ai-handoff/usage/usage.jsonl` **in the PRODUCT repo** after explicit allowlist/bootstrap approval. `.gitignore` may need its own separately approved change. Do not auto-commit or push usage records, even to a private repository. Handoff to Web by **explicitly attaching only the summary**; uploaded metrics become available only to the recipient chat after user action.

## Optional bundled offline script (Python standard library only)

`tools/usage_report.py` does **not** tap Codex/ChatGPT APIs, read sessions, monitor tokens in the background, install plugins or access the network. It simply accepts supplied measurements and creates a short non-sensitive report:

```sh
python tools/usage_report.py add --file /path/to/private/usage.jsonl --id obs-001 --surface codex --scope task --task-id T-42 --source ui-chat --result ACCEPTED --credits 1.3 --minutes 8 --retries 1 --handoffs 1
python tools/usage_report.py report --file /path/to/private/usage.jsonl --out /path/to/private/usage-summary.md
```

If input/output token counts are visible, add `--input-tokens`, `--cached-input-tokens` and `--output-tokens`. For a usage period instead of a task, use `--scope period --period 2026-11-week2`, avoid `--task-id`, and report aggregate separately. Source names `ui-chat`, `ui-period`, `codex-status`, `api-usage`, `other` are provenance labels **not API integrations**. A task status may be UNKNOWN/NOT_VERIFIED until independent review.

Give the user the exported `usage-summary.md` after privacy review, ideally along with redacted task outcome references or a short description of known failure classes. In Web, analyze by surface, task type, model/effort and actual outcomes; identify likely wasted retries, repetitive context or overpowered modes as **hypotheses**, not facts; recommend *one* bounded controlled experiment and compare on equivalent tasks. Route any approved methodological change through RATIONALE, TEST_CASES and a real pilot. Do not change the user's account model, subscriptions, agents or project files based solely on token statistics.

## Recommended progression

1. **Week 1, no automation:** inspect native 7D/30D usage; collect a few representative task + surface entries with observed data and real acceptance status.
2. **Pilot:** run the local script on synthetic/sample input, then on privacy-reviewed task entries. Compare usage per accepted outcome including rework/handoffs; note missing telemetry.
3. **Only if collection effort is a proven bottleneck:** consider an explicitly approved offline parser of *just* numeric usage events from Codex session logs or supported API trace/export, with version-specific schema validation, a canary test and no raw text capture. Never grant a third-party telemetry SaaS or agent access to conversation history just to save minutes.

## Guardrails

- Read-only reporting must not mutate PRODUCT data. The `add` command writes **only the explicitly provided ledger path** after task-scoped authorization.
- Don't equate a reduction in tokens/credits with productivity if acceptance quality drops.
- Do not infer ChatGPT Web per-request token counts from visible message length; cached and reasoning tokens make that incorrect.
- Logs may be incomplete or lag. Report source, observed vs estimated status, coverage and limitations; don't backfill missing values as zeros.
