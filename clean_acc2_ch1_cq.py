"""
clean_acc2_ch1_cq.py (v3)
Robust cleaner for Acc2_ch1_cq
"""
import csv
import re
import sys
from pathlib import Path

BASE   = Path(r"c:\Users\BMTF\.antigravity\testpaper")
INPUT  = BASE / "Acc2_ch1_cq - Sheet1.csv"
OUTPUT = BASE / "Acc2_ch1_cq_clean.csv"

COLUMNS = [
    "Year", "Subject", "Chapter", "Level", "Category", "Stem",
    "Question_A", "Question_B", "Question_C",
    "Ans_A", "Ans_B", "Ans_C",
]

def is_separator(line: str) -> bool:
    core = re.sub(r"[-=|:\s]", "", line.strip())
    return len(line.strip()) > 0 and len(core) == 0

def simple_strip(text: str) -> str:
    # Remove basic markdown formatting without complex regex
    text = text.replace("**", "").replace("__", "")
    text = text.replace("`", "")
    # Remove simple latex tags
    text = text.replace("$", "")
    return text

def pipe_row(line: str) -> str:
    cells = [simple_strip(c.strip()) for c in line.split("|")]
    cells = [c for c in cells if c]
    return " | ".join(cells)

def cell_to_plain(raw: str) -> str:
    if not raw:
        return ""
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    parts = []
    for line in lines:
        s = line.strip()
        if not s or is_separator(s):
            continue
        part = pipe_row(s) if "|" in s else simple_strip(s)
        part = part.strip()
        if part:
            parts.append(part)
    result = " // ".join(parts)
    return re.sub(r"[ \t]{2,}", " ", result).strip()

def main():
    print(f"Reading from {INPUT.name}...")
    try:
        with INPUT.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            raw_rows = list(reader)
        print(f"Loaded {len(raw_rows)} rows.")

        cleaned = []
        for row in raw_rows:
            new_row = {col: cell_to_plain(row.get(col, "")) for col in COLUMNS}
            cleaned.append(new_row)

        with OUTPUT.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(cleaned)
        
        print(f"Successfully wrote {len(cleaned)} rows to {OUTPUT.name}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
