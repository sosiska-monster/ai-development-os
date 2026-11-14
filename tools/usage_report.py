#!/usr/bin/env python3
"""Offline, metadata-only usage ledger for AI Development OS.

Never reads Codex transcripts, sessions, account APIs, credentials or the network.
Writes ONLY explicit --file / --out paths; no background monitoring.
"""
import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SURFACES = ("web", "codex", "work", "api", "other")
SOURCES = ("ui-chat", "ui-period", "codex-status", "api-usage", "other")
RESULTS = ("ACCEPTED", "REWORK", "BLOCKED", "NOT_VERIFIED", "NA")
NUMERIC = ("input_tokens", "cached_input_tokens", "output_tokens",
           "credits", "minutes", "retries", "handoffs")
FIELDS = {"id", "date", "scope", "surface", "source", "measurement",
          "task_id", "period", "result", "model", "effort", *NUMERIC}


def check(record):
    if not isinstance(record, dict):
        raise ValueError("usage record must be a JSON object")
    unknown = set(record) - FIELDS
    if unknown:
        raise ValueError("unrecognized usage fields: " + ", ".join(sorted(unknown)))
    for key in ("id", "date", "scope", "surface", "source", "measurement"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError("missing or invalid required field: " + key)
    for key in ("task_id", "period", "model", "effort"):
        value = record.get(key)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("invalid optional field: " + key)
    if record["scope"] == "task":
        if not record.get("task_id") or record.get("period") is not None:
            raise ValueError("task scope needs task_id, not period")
    elif record["scope"] == "period":
        if not record.get("period") or record.get("task_id") is not None:
            raise ValueError("period scope needs period, not task_id")
    else:
        raise ValueError("scope must be task/period")
    if record["surface"] not in SURFACES or record["source"] not in SOURCES:
        raise ValueError("invalid surface/source")
    if record["measurement"] not in ("observed", "estimate"):
        raise ValueError("measurement must be observed/estimate")
    if record.get("result", "NA") not in RESULTS:
        raise ValueError("invalid result")
    try:
        datetime.fromisoformat(record["date"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid ISO date") from exc
    for key in NUMERIC:
        v = record.get(key)
        if v is None:
            continue
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise ValueError(key + " must be a nonnegative number")
        if isinstance(v, float) and not math.isfinite(v):
            raise ValueError(key + " must be finite")
        if v < 0:
            raise ValueError(key + " must be nonnegative")
        if key not in ("credits", "minutes") and not isinstance(v, int):
            raise ValueError(key + " must be an integer")
    if (record.get("cached_input_tokens") is not None
        and record.get("input_tokens") is not None
        and record["cached_input_tokens"] > record["input_tokens"]):
        raise ValueError("cached_input_tokens is included in input_tokens")
    return record

def read(path):
    records, ids, pairs = [], set(), set()
    for lineno, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            r = check(json.loads(line, parse_constant=lambda value: (_ for _ in ()).throw(ValueError("non-finite JSON number: " + value))))
            if r["id"] in ids:
                raise ValueError("duplicate record id")
            ids.add(r["id"])
            if r["scope"] == "task":
                pair = (r["task_id"], r["surface"])
                if pair in pairs:
                    raise ValueError("duplicate task/surface; cumulative measurements cannot be added")
                pairs.add(pair)
            records.append(r)
        except (ValueError, json.JSONDecodeError) as exc:
            raise ValueError("line {}: {}".format(lineno, exc)) from exc
    return records


def display(value, digits=0):
    return "UNKNOWN" if value is None else format(value, ",.{}f".format(digits)).replace(",", " ")


def cell(value):
    """Render an untrusted optional metadata value as one safe Markdown cell."""
    if value is None or value == "":
        return "UNKNOWN"
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def report(records):
    task = [r for r in records if r["scope"] == "task"]
    period = [r for r in records if r["scope"] == "period"]
    ids = {r["task_id"] for r in task}
    lines = [
        "# AI Development OS — usage summary",
        "",
        "Metadata only. No content from chats, raw logs, API keys or repository files.",
        "Observed counts are not necessarily complete billing records. Missing means UNKNOWN, not zero.",
        "Cached input is part of input; do not add it again. Credits are not dollars.",
        "Period snapshots can overlap task measurements and are NEVER added to them.",
        "",
        "Task/surface records: {}; distinct tasks: {}; period snapshots: {}.".format(
            len(task), len(ids), len(period)),
        "",
        "## By surface (observed values, with reporting coverage)",
        "",
        "| Surface | Rows | Input tokens | Cached input | Output tokens | Credits |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for surface in sorted({r["surface"] for r in task}):
        rows = [r for r in task if r["surface"] == surface]
        def total(key, digits=0):
            observed = [r[key] for r in rows
                        if r["measurement"] == "observed" and r.get(key) is not None]
            return "{} ({}/{})".format(display(sum(observed), digits), len(observed), len(rows)) if observed else "UNKNOWN (0/{})".format(len(rows))
        lines.append("| {} | {} | {} | {} | {} | {} |".format(
            surface, len(rows), total("input_tokens"),
            total("cached_input_tokens"), total("output_tokens"), total("credits", 3)))
    if not task:
        lines.append("| None | 0 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |")
    lines.extend(["", "## Task observations", "",
        "| Task | Surface | Model | Effort | Source | Measurement | Result | Input+output* | Credits | Retries | Handoffs | Minutes |",
        "|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|"])
    for r in sorted(task, key=lambda x: (x["task_id"], x["surface"])):
        a, b = r.get("input_tokens"), r.get("output_tokens")
        count = a+b if r["measurement"] == "observed" and a is not None and b is not None else None
        credit = r.get("credits") if r["measurement"] == "observed" else None
        lines.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            cell(r["task_id"]), r["surface"], cell(r.get("model")),
            cell(r.get("effort")), r["source"], r["measurement"],
            r.get("result", "NA"), display(count), display(credit, 3),
            display(r.get("retries")), display(r.get("handoffs")),
            display(r.get("minutes"), 1)))
    statuses = defaultdict(set)
    for r in task:
        if r.get("result", "NA") != "NA":
            statuses[r["task_id"]].add(r["result"])
    accepted = sum(1 for s in statuses.values() if s == {"ACCEPTED"})
    inconsistent = sum(1 for s in statuses.values() if len(s) > 1)
    lines.extend(["", "*Input already includes cached tokens. Different surfaces may have different billing coverage.*",
        "", "## Quality and limitations", "",
        "- Unambiguously ACCEPTED tasks: {}/{}.".format(accepted, len(ids)),
        "- Tasks with conflicting labels: {}.".format(inconsistent),
        "- Estimated task records excluded from observed totals: {}.".format(
            sum(r["measurement"] == "estimate" for r in task)),
        "- Task rows without complete observed input+output: {}.".format(
            sum(r["measurement"] != "observed" or
                r.get("input_tokens") is None or r.get("output_tokens") is None for r in task)),
    ])
    if period:
        lines.extend(["", "## Period snapshots (separate, not summed)", ""])
        for r in period:
            lines.append("- {} / {} / {}: credits {}, input {}, output {}, {}.".format(
                r["period"], r["surface"], r["source"],
                display(r.get("credits"), 3), display(r.get("input_tokens")),
                display(r.get("output_tokens")), r["measurement"]))
    lines.extend(["", "## Interpretation rules", "",
        "- Compare only similar tasks and accepted outcomes before proposing a model/effort change.",
        "- Investigate retries, excessive context and handoffs as hypotheses, not proven causes.",
        "- Change one variable in an approved pilot; compare real success, rework and measured usage.",
        "- Do not upload raw conversation transcripts or optimize away required checks.", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("add", help="append one explicitly supplied usage observation")
    a.add_argument("--file", required=True)
    a.add_argument("--id", required=True)
    a.add_argument("--date", default=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    a.add_argument("--scope", choices=("task", "period"), default="task")
    a.add_argument("--surface", choices=SURFACES, required=True)
    a.add_argument("--source", choices=SOURCES, required=True)
    a.add_argument("--measurement", choices=("observed", "estimate"), default="observed")
    a.add_argument("--task-id")
    a.add_argument("--period")
    a.add_argument("--result", choices=RESULTS, default="NA")
    a.add_argument("--model")
    a.add_argument("--effort")
    for field in NUMERIC:
        a.add_argument("--" + field.replace("_", "-"),
                       type=float if field in ("credits", "minutes") else int)
    p = sub.add_parser("report", help="summarize the private ledger without network")
    p.add_argument("--file", required=True)
    p.add_argument("--out", help="optional explicit Markdown output path")
    args = parser.parse_args()
    try:
        if args.command == "add":
            d = {k: v for k, v in vars(args).items()
                 if k not in ("command", "file") and v is not None}
            check(d)
            dest = Path(args.file)
            if dest.exists():
                existing = read(dest)
                if any(r["id"] == d["id"] or (
                        r["scope"] == d["scope"] == "task"
                        and r["task_id"] == d["task_id"]
                        and r["surface"] == d["surface"]) for r in existing):
                    raise ValueError("duplicate id or task/surface")
            dest.parent.mkdir(parents=True, exist_ok=True)
            # A valid last JSONL record may lack a final newline; protect it before appending.
            newline_needed = False
            if dest.exists() and dest.stat().st_size:
                with dest.open("rb") as source:
                    source.seek(-1, 2)
                    newline_needed = source.read(1) != b"\n"
            with dest.open("ab") as out:
                if newline_needed:
                    out.write(b"\n")
                out.write((json.dumps(d, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n").encode("utf-8"))
            print("Added record {}".format(d["id"]))
        else:
            result = report(read(args.file))
            if args.out:
                source, target = Path(args.file), Path(args.out)
                if (source.resolve() == target.resolve()
                    or (target.exists() and source.samefile(target))):
                    raise ValueError("report output must not overwrite the input journal")
                target.write_text(result, encoding="utf-8")
                print("Created {}".format(args.out))
            else:
                print(result)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
