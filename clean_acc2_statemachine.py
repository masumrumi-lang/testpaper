import re
from pathlib import Path

BASE = Path(r"c:\Users\BMTF\.antigravity\testpaper")
INPUT = BASE / "Acc2_ch1_cq - Sheet1.csv"
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
    text = text.replace("**", "").replace("__", "").replace("`", "").replace("$", "")
    return text

def pipe_row(line: str) -> str:
    cells = [simple_strip(c.strip()) for c in line.split("|")]
    cells = [c for c in cells if c]
    return " | ".join(cells)

def cell_to_plain(raw: str) -> str:
    if not raw: return ""
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    parts = []
    for line in lines:
        s = line.strip()
        if not s or is_separator(s): continue
        part = pipe_row(s) if "|" in s else simple_strip(s)
        part = part.strip()
        if part: parts.append(part)
    result = " // ".join(parts)
    return re.sub(r"[ \t]{2,}", " ", result).strip()

def parse_csv_line(line: str) -> list:
    result = []
    current = ""
    in_quotes = False
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            if in_quotes and i + 1 < len(line) and line[i+1] == '"':
                current += '"'
                i += 1
            else:
                in_quotes = not in_quotes
        elif c == ',' and not in_quotes:
            result.append(current)
            current = ""
        else:
            current += c
        i += 1
    result.append(current)
    return result

def main():
    print("Reading raw file...")
    raw = INPUT.read_text(encoding="utf-8")
    
    lines = raw.split("\n")
    rows = []
    current_row = ""
    for line in lines:
        if re.match(r"^(201[0-9]|202[0-9]),", line) or re.match(r"^Year,Subject", line):
            if current_row:
                rows.append(current_row)
            current_row = line
        else:
            current_row += "\n" + line
    if current_row:
        rows.append(current_row)
        
    print(f"Detected {len(rows)} data rows.")
    
    cleaned = []
    for idx, r in enumerate(rows):
        if idx == 0: continue # Skip header
        if r.count('"') % 2 != 0:
            r += '"'
            
        cols = parse_csv_line(r)
        
        while len(cols) < 12:
            cols.append("")
            
        clean_cols = []
        for c in cols[:12]:
            clean_cols.append(cell_to_plain(c))
            
        cleaned.append(clean_cols)
        
    print("Writing output...")
    out_lines = []
    out_lines.append(",".join(f'"{c}"' for c in COLUMNS))
    for row in cleaned:
        escaped_row = []
        for c in row:
            escaped_row.append('"' + c.replace('"', '""') + '"')
        out_lines.append(",".join(escaped_row))
        
    OUTPUT.write_text("\n".join(out_lines), encoding="utf-8")
    print("Done! Clean CSV created successfully.")

if __name__ == "__main__":
    main()
