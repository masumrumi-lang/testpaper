"""
clean_acc2_pandas.py
Robust cleaner using Pandas
"""
import sys
import re
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Pandas not installed. Trying to install...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

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
    text = text.replace("**", "").replace("__", "")
    text = text.replace("`", "")
    text = text.replace("$", "")
    return text

def pipe_row(line: str) -> str:
    cells = [simple_strip(c.strip()) for c in line.split("|")]
    cells = [c for c in cells if c]
    return " | ".join(cells)

def cell_to_plain(raw) -> str:
    if pd.isna(raw):
        return ""
    raw = str(raw)
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
    print("Reading CSV with Pandas...")
    df = pd.read_csv(INPUT, dtype=str)
    print(f"Loaded {len(df)} rows.")

    for col in COLUMNS:
        if col not in df.columns:
            df[col] = ""

    # Apply cleaning
    for col in COLUMNS:
        df[col] = df[col].apply(cell_to_plain)

    # Output only the specified columns
    out_df = df[COLUMNS]

    # Drop fully empty rows
    out_df = out_df.dropna(how='all')
    
    out_df.to_csv(OUTPUT, index=False, quoting=1) # 1 corresponds to csv.QUOTE_ALL
    print(f"Successfully wrote clean CSV to {OUTPUT.name}")

if __name__ == "__main__":
    main()
