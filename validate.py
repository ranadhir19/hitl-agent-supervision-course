#!/usr/bin/env python3
"""Repo harness for hitl-agent-supervision-course.

Checks the delivered structure, not sidecar claims:
  1. Required top-level files exist and are non-empty.
  2. Every topic in CURRICULUM.md appears exactly once, in order —
     the full 30-topic sequence HITL 1.01 .. HITL 10.02.
  3. LICENSE is the MIT licence.
  4. Every capstone brief carries the required sections
     (setting, brief, deliverables, rubric, injected failures).
  5. No placeholder markers left in shipped markdown.

Exit 0 = green. Run before every push.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


for name in ["README.md", "LICENSE", "CURRICULUM.md", "BENCHMARK.md"]:
    p = ROOT / name
    check(p.exists() and p.stat().st_size > 0, f"missing or empty: {name}")

licence = (ROOT / "LICENSE").read_text(encoding="utf-8")
check("MIT License" in licence, "LICENSE: not the MIT licence")
check("Permission is hereby granted" in licence,
      "LICENSE: missing the MIT permission grant")

curr = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
found = [(int(m), int(t)) for m, t in re.findall(r"HITL (\d+)\.(\d\d)", curr)]
topic_counts = {1: 3, 2: 3, 3: 4, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 2}
expected = [(m, t) for m in sorted(topic_counts)
            for t in range(1, topic_counts[m] + 1)]
check(found == expected,
      f"CURRICULUM.md topic sequence mismatch: expected {len(expected)} "
      f"topics in order, found {len(found)}")
check(len(set(found)) == len(found), "duplicate topics in CURRICULUM.md")

cap_dir = ROOT / "capstones"
briefs = sorted(cap_dir.glob("0*.md"))
check(len(briefs) == 4, f"expected 4 capstone briefs, found {len(briefs)}")
for b in briefs:
    text = b.read_text(encoding="utf-8").lower()
    for section in ["setting", "brief", "deliverables", "rubric"]:
        check(section in text, f"{b.name}: missing section '{section}'")
    check("injected failures" in text,
          f"{b.name}: no injected failures section")

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    check("TODO-PLACEHOLDER" not in text, f"{md.relative_to(ROOT)}: placeholder left")

if failures:
    print("VALIDATE: FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"VALIDATE: PASS ({len(found)} topics, {len(briefs)} capstones)")
