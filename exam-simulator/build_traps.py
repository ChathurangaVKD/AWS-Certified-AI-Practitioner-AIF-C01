#!/usr/bin/env python3
"""Parse docs/EXAM-TRAP-SHEET.md into traps.js for the trap checklist page.

Every table row (and every "- [ ]" bullet) becomes one checkable trap.
Run from anywhere: python3 exam-simulator/build_traps.py
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "EXAM-TRAP-SHEET.md"
OUT = Path(__file__).resolve().parent / "traps.js"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


sections, sec, group, table_head = [], None, None, None
for raw in SRC.read_text(encoding="utf-8").splitlines():
    line = raw.rstrip()
    if line.startswith("## "):
        sec = {"title": line[3:].strip(), "groups": []}
        sections.append(sec)
        group, table_head = None, None
        continue
    if sec is None:
        continue
    if line.startswith("### "):
        group = {"title": line[4:].strip(), "items": []}
        sec["groups"].append(group)
        table_head = None
        continue
    if group is None:
        group = {"title": "", "items": []}
        sec["groups"].append(group)
    if line.startswith("|"):
        c = cells(line)
        if all(re.fullmatch(r":?-{2,}:?", x) for x in c if x):
            continue
        if table_head is None:
            table_head = c
            continue
        group["items"].append({"head": table_head, "cells": c})
    elif re.match(r"- \[ \] ", line):
        group["items"].append({"head": None, "cells": [line[6:].strip()]})
    elif not line.strip():
        table_head = None

out = []
for s in sections:
    groups = []
    for g in s["groups"]:
        if not g["items"]:
            continue
        items = []
        for i, it in enumerate(g["items"]):
            key = slug(s["title"]) + "/" + slug(g["title"]) + "/" + slug(it["cells"][0])[:60]
            items.append({"id": key, "head": it["head"], "cells": it["cells"]})
        groups.append({"title": g["title"], "items": items})
    if groups:
        out.append({"id": slug(s["title"]), "title": s["title"], "groups": groups})

total = sum(len(g["items"]) for s in out for g in s["groups"])
ids = [i["id"] for s in out for g in s["groups"] for i in g["items"]]
# Keep ids unique even if two rows share a first cell.
seen = {}
for s in out:
    for g in s["groups"]:
        for i in g["items"]:
            n = seen.get(i["id"], 0)
            seen[i["id"]] = n + 1
            if n:
                i["id"] += f"-{n + 1}"

OUT.write_text("window.TRAPS = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(out)} sections, {total} traps")
