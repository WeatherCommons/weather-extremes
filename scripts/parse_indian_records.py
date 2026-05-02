#!/usr/bin/env python3
"""Parse indian_records.html and emit per-year Record Events CSVs."""
import re
import sys
from collections import defaultdict
from pathlib import Path

HTML = Path("indian_records.html").read_text()
OUT_DIR = Path("src/data/records")

MONTH_NUM = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}
MONTH_ABBR = {abbr: num for abbr, num in zip(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    range(1, 13)
)}

HEADER = "Date,City,Lat,Lon,Country,Metric,Type,Value,Prev,Prev Date,Scope,Since,Elevation,WMO"


def map_record_type(s):
    """Return (metric, type, scope) for a record-type string."""
    s = s.strip().lower()
    all_time = s.startswith("all time")
    base = s.replace("all time", "").strip()
    scope = "Year" if all_time else "Month"
    if base == "max":
        return "Max Temp", "High", scope
    if base == "min":
        return "Min Temp", "Low", scope
    if base == "high min":
        return "Min Temp", "High", scope
    if base == "low max":
        return "Max Temp", "Low", scope
    if base in ("24 hr rainfall", "24 hr  rainfall"):
        return "Rain", "24hrs", scope
    if base == "monthly rainfall":
        return "Rain", "Month total", scope
    return "Unknown", base, scope


def strip_units(v):
    """Pull a number out of '6.5C', '65mm', etc."""
    m = re.search(r"-?\d+(?:\.\d+)?", v)
    return m.group(0) if m else ""


def parse_old_record(s):
    """'7.2C on 30/4/2023' -> ('7.2', '2023-04-30')."""
    s = s.strip()
    if not s:
        return "", ""
    m = re.match(r"\s*(-?\d+(?:\.\d+)?)\s*\w*\s*on\s*(\d{1,2})/(\d{1,2})/(\d{4})", s, re.I)
    if m:
        val, d, mo, y = m.groups()
        return val, f"{y}-{int(mo):02d}-{int(d):02d}"
    # fallback: just extract numeric value
    return strip_units(s), ""


def cells_from_row(row_html):
    """Extract cell text from a <tr>...</tr> chunk."""
    cells = re.findall(r"<td[^>]*>(.*?)</td>", row_html, re.S)
    return [re.sub(r"<[^>]+>", "", c).replace("&amp;", "&").strip() for c in cells]


# Locate each "Month YYYY" marker and the following table.
section_re = re.compile(
    r"<p>(?:&nbsp;|\s)*("
    r"January|February|March|April|May|June|July|August|September|October|November|December"
    r")\s+(\d{4})",
)
table_re = re.compile(r'<table class="wikitable">(.*?)</table>', re.S)
row_re = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)

records_by_year = defaultdict(list)
warnings = []

# Find sections (month, year, html-position) and the table immediately after each.
sections = [(m.group(1), int(m.group(2)), m.end()) for m in section_re.finditer(HTML)]

for month_name, year, start in sections:
    # The first table after this position is the section's table.
    t = table_re.search(HTML, start)
    if not t:
        continue
    rows = row_re.findall(t.group(1))
    # First row is the header.
    for r in rows[1:]:
        c = cells_from_row(r)
        if len(c) < 9:
            continue
        date_raw, wmo, since_yr, station, _state, elev, rec_type, value, old = c[:9]

        # Date: "02-Apr" -> "YYYY-MM-DD" using the section's year.
        dm = re.match(r"(\d{1,2})-([A-Za-z]+)", date_raw)
        if not dm:
            warnings.append(f"bad date {date_raw!r} in {month_name} {year}")
            continue
        day = int(dm.group(1))
        mo_abbr = dm.group(2)[:3].title()
        if mo_abbr not in MONTH_ABBR:
            warnings.append(f"bad month abbr {dm.group(2)!r} in {month_name} {year}")
            continue
        mo = MONTH_ABBR[mo_abbr]
        date_iso = f"{year}-{mo:02d}-{day:02d}"

        metric, type_, scope = map_record_type(rec_type)
        if metric == "Unknown":
            warnings.append(f"unknown type {rec_type!r} in {month_name} {year} for {station}")

        prev_val, prev_date = parse_old_record(old)
        elev_clean = elev.replace(",", "").strip()
        since_clean = since_yr.strip()
        since_iso = f"{since_clean}-01-01" if re.fullmatch(r"\d{4}", since_clean) else ""

        records_by_year[year].append([
            date_iso,
            station,
            "",   # Lat
            "",   # Lon
            "India",
            metric,
            type_,
            strip_units(value),
            prev_val,
            prev_date,
            scope,
            since_iso,
            elev_clean,
            wmo.strip(),
        ])

# Write per-year CSVs (sort rows by date desc, like the HTML).
for year, rows in records_by_year.items():
    rows.sort(key=lambda r: r[0], reverse=True)
    path = OUT_DIR / str(year) / "India.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        f.write(HEADER + "\n")
        for r in rows:
            f.write(",".join(r) + "\n")
    print(f"wrote {len(rows)} rows -> {path}")

if warnings:
    print(f"\n{len(warnings)} warnings:", file=sys.stderr)
    for w in warnings[:20]:
        print(f"  - {w}", file=sys.stderr)
    if len(warnings) > 20:
        print(f"  ... ({len(warnings) - 20} more)", file=sys.stderr)
