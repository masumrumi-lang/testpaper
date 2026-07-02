import re
import sys
from pathlib import Path

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

BASE = Path(r"c:\Users\BMTF\.antigravity\testpaper")
INPUT = BASE / "Acc2_ch1_cq - Sheet1.csv"
OUTPUT = BASE / "Acc2_ch1_cq_clean.csv"

COLUMNS = [
    "Year", "Subject", "Chapter", "Level", "Category", "Stem",
    "Question_A", "Question_B", "Question_C",
    "Ans_A", "Ans_B", "Ans_C",
]

def main():
    print("Reading raw file...", flush=True)
    raw = INPUT.read_text(encoding="utf-8")
    
    print("File read successfully. Length:", len(raw), flush=True)
    
    lines = raw.split("\n")
    print("Number of lines:", len(lines), flush=True)
    
    rows = []
    current_row = ""
    for line in lines:
        if line.startswith("20") and len(line) > 5 and line[4] == ",":
            if current_row:
                rows.append(current_row)
            current_row = line
        elif line.startswith("Year,Subject"):
            if current_row:
                rows.append(current_row)
            current_row = line
        else:
            current_row += "\n" + line
    if current_row:
        rows.append(current_row)
        
    print(f"Detected {len(rows)} data rows.", flush=True)
    
    # Fast manual parsing
    out_rows = []
    out_rows.append(",".join(f'"{c}"' for c in COLUMNS))
    
    for idx, r in enumerate(rows):
        if idx == 0: continue
        
        # fix odd quotes
        if r.count('"') % 2 != 0:
            r += '"'
            
        # Parse fields
        fields = []
        current = ""
        in_quotes = False
        i = 0
        while i < len(r):
            c = r[i]
            if c == '"':
                if in_quotes and i + 1 < len(r) and r[i+1] == '"':
                    current += '"'
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif c == ',' and not in_quotes:
                fields.append(current)
                current = ""
            else:
                current += c
            i += 1
        fields.append(current)
        
        while len(fields) < 12:
            fields.append("")
            
        clean_cols = []
        for c in fields[:12]:
            # Clean each field without complex regex
            c = c.replace("**", "").replace("__", "").replace("`", "").replace("$", "")
            lines = c.split('\n')
            parts = []
            for l in lines:
                ls = l.strip()
                if not ls: continue
                # if separator skip
                if not ls.replace('-', '').replace('=', '').replace('|', '').replace(':', '').replace(' ', ''):
                    continue
                # handle pipe
                if '|' in ls:
                    ls = " | ".join(x.strip() for x in ls.split('|') if x.strip())
                parts.append(ls)
            c = " // ".join(parts)
            # trim spaces
            while "  " in c:
                c = c.replace("  ", " ")
            clean_cols.append(c)
            
        # Write clean string
        escaped_row = []
        for c in clean_cols:
            escaped_row.append('"' + c.replace('"', '""') + '"')
        out_rows.append(",".join(escaped_row))
        
    print("Writing output...", flush=True)
    OUTPUT.write_text("\n".join(out_rows), encoding="utf-8")
    print("Done! Clean CSV created successfully.", flush=True)

if __name__ == "__main__":
    print("Starting fast clean script...", flush=True)
    try:
        main()
    except Exception as e:
        print("ERROR:", e, flush=True)
