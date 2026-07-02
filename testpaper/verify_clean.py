import csv
from pathlib import Path

BASE = Path(r"c:\Users\BMTF\.antigravity\testpaper")
OUT  = BASE / "verify_out.txt"
CSV  = BASE / "Acc2_ch1_cq_clean.csv"

lines = []
lines.append(f"exists: {CSV.exists()}")

if CSV.exists():
    lines.append(f"size_bytes: {CSV.stat().st_size}")
    with CSV.open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
    lines.append(f"rows: {len(rows)}")
    lines.append(f"cols: {reader.fieldnames}")

    # check for embedded newlines
    nl_rows = []
    bad_col_count = []
    for i, row in enumerate(rows):
        if len(row) != 12:
            bad_col_count.append(i + 2)
        for col, val in row.items():
            if "\n" in val or "\r" in val:
                nl_rows.append((i + 2, col))
                break

    lines.append(f"rows_with_embedded_newlines: {nl_rows[:10]}")
    lines.append(f"rows_with_wrong_col_count: {bad_col_count[:10]}")

    if rows:
        lines.append("--- Row1 Stem (first 300) ---")
        lines.append(rows[0]["Stem"][:300])
        lines.append("--- Row1 Ans_A (first 300) ---")
        lines.append(rows[0]["Ans_A"][:300])
else:
    lines.append("CLEAN CSV NOT FOUND - checking if original script ran:")
    orig = BASE / "clean_acc2_ch1_cq.py"
    lines.append(f"  script exists: {orig.exists()}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("Done - wrote", OUT)
