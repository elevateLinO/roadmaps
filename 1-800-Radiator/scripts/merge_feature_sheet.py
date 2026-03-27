#!/usr/bin/env python3
"""Fetch Features tab CSV and rewrite embedded JSON in feature-planning-timeline-infographic.html."""
import csv
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Optional

SHEET_EXPORT = (
    "https://docs.google.com/spreadsheets/d/19eZ2wcBNra2quFN4crZDs_4rcPuOdn-J1Jj9rWvE2Pc"
    "/export?format=csv&gid=108296775"
)
SHEET_EDIT = (
    "https://docs.google.com/spreadsheets/d/19eZ2wcBNra2quFN4crZDs_4rcPuOdn-J1Jj9rWvE2Pc"
    "/edit?gid=108296775"
)

VALUE_AREA_LABELS = [
    "Conversion & Acquisition",
    "Customer Experience",
    "Operational Efficiency",
    "Financial Visibility",
    "Technical Foundation",
    "Marketing Enablement",
    "Search & Discovery Authority",
]

GROUP_LEGEND = [
    {"id": "FG-01", "name": "Pre-Login Marketing & Authority"},
    {"id": "FG-02", "name": "Part Search & Discovery"},
    {"id": "FG-03", "name": "Cart, Ordering & Upsell"},
    {"id": "FG-04", "name": "Shop Dashboard & Account Management"},
    {"id": "FG-05", "name": "Delivery & Fulfillment Visibility"},
    {"id": "FG-06", "name": "Billing & Payments"},
    {"id": "FG-07", "name": "Marketing & Promotions Engine"},
    {"id": "FG-08", "name": "Internal Tools & Intelligence"},
    {"id": "FG-09", "name": "Platform & Infrastructure"},
]


def cell_on(v: str) -> bool:
    s = (v or "").strip().lower()
    return s in ("x", "✓", "1", "yes", "y", "true")


def parse_last_updated_unix(raw: str) -> Optional[int]:
    """Parse Last Updated cell: Unix seconds (or ms if > 1e12). Legacy non-numeric -> None."""
    s = (raw or "").strip()
    if not s or not s.isdigit():
        return None
    n = int(s)
    if n > 1_000_000_000_000:
        n = n // 1000
    return n


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    html_path = root / "feature-planning-timeline-infographic.html"
    raw = urllib.request.urlopen(SHEET_EXPORT, timeout=60).read().decode("utf-8")
    rows = list(csv.reader(raw.splitlines()))
    if not rows:
        sys.exit("empty csv")
    h = {name: i for i, name in enumerate(rows[0])}

    sheet_last_updated = ""
    for r in rows[1:]:
        if len(r) < len(rows[0]):
            r = r + [""] * (len(rows[0]) - len(r))
        fid = (r[h["Feature ID"]] or "").strip()
        if fid == "FG-01" and re.match(r"^FG-\d+$", fid):
            idx = h.get("Last Updated")
            if idx is not None and idx < len(r):
                sheet_last_updated = (r[idx] or "").strip()
            break
    if not sheet_last_updated and "Last Updated" in h:
        idx = h["Last Updated"]
        for r in rows[1:]:
            if len(r) <= idx:
                continue
            v = (r[idx] or "").strip()
            if v:
                sheet_last_updated = v
                break

    sheet_last_updated_unix = parse_last_updated_unix(sheet_last_updated)

    features = []
    for r in rows[1:]:
        if len(r) < len(rows[0]):
            r = r + [""] * (len(rows[0]) - len(r))
        fid = (r[h["Feature ID"]] or "").strip()
        if not re.match(r"^FG-\d+\.\d+$", fid):
            continue
        phase_s = (r[h["Phase"]] or "").strip()
        try:
            phase = float(phase_s) if phase_s else None
        except ValueError:
            phase = None
        if phase is None:
            continue
        dep = (r[h["Depends On"]] or "").strip()
        gid = (r[h["Feature Group ID"]] or "").strip()
        gname = (r[h["Feature Group"]] or "").strip()
        title = (r[h["Feature Idea"]] or "").strip()
        desc = (r[h["Descriptions"]] or "").strip()
        kpis = (r[h["KPIs"]] or "").strip()
        active_areas = []
        for lab in VALUE_AREA_LABELS:
            i = h.get(lab)
            if i is None:
                continue
            val = r[i] if i < len(r) else ""
            if cell_on(val):
                active_areas.append(lab)
        features.append(
            {
                "id": fid,
                "title": title,
                "phase": phase,
                "gid": gid,
                "groupName": gname,
                "dependsOn": dep,
                "description": desc,
                "kpis": kpis,
                "valueAreasActive": active_areas,
            }
        )

    data = {
        "title": "1-800-Radiator — Feature planning timeline",
        "subtitle": "Six aligned columns from 1.0 to 3.5 (half-step bands). Source: Feature Planning sheet (Google Sheets).",
        "axisTicks": [1, 1.5, 2, 2.5, 3, 3.5],
        "phaseColumnCount": 6,
        "groupLegend": GROUP_LEGEND,
        "valueAreaLabels": VALUE_AREA_LABELS,
        "sheetLastUpdatedUnix": sheet_last_updated_unix,
        "sheetExportUrl": SHEET_EXPORT,
        "sheetEditUrl": SHEET_EDIT,
        "features": features,
    }

    text = html_path.read_text(encoding="utf-8")
    new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_block = '<script id="data" type="application/json">' + new_json + "</script>"
    text2, n = re.subn(
        r'<script id="data" type="application/json">.*?</script>',
        new_block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if n != 1:
        sys.exit(f"replace failed: {n}")
    html_path.write_text(text2, encoding="utf-8")
    print(
        "OK",
        html_path,
        "features",
        len(features),
        "sheetLastUpdatedUnix",
        sheet_last_updated_unix,
    )


if __name__ == "__main__":
    main()
