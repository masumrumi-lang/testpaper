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

def main():
    print("Reading raw file...")
    raw = INPUT.read_text(encoding="utf-8")
    
    # Identify row boundaries. Every row starts with either "2019,", "2018,", "2017," etc.
    # We will split by a regex that matches the start of a year column for these rows.
    # Or just use a simple regex to find the start of each row.
    
    # We can split by year at the start of a line
    lines = raw.split("\n")
    rows = []
    current_row = ""
    for line in lines:
        # Check if line starts with a year, e.g. "2019,Accounting"
        if re.match(r"^(201[0-9]|202[0-9]),", line):
            if current_row:
                rows.append(current_row)
            current_row = line
        else:
            current_row += "\n" + line
    if current_row:
        rows.append(current_row)
        
    print(f"Detected {len(rows)} data rows based on year headers.")
    
    # Now we just need to parse each string into columns. We will just use the python built-in csv module 
    # but ONLY on the single row strings. This prevents the whole file from hanging.
    import csv
    import io
    
    cleaned = []
    for r in rows:
        # Some rows might have unclosed quotes at the end, so we append a quote if there's an odd number
        if r.count('"') % 2 != 0:
            r += '"'
            
        reader = csv.reader(io.StringIO(r))
        try:
            cols = next(reader)
        except Exception as e:
            print(f"Error parsing row: {r[:100]}")
            continue
            
        # Pad columns
        cols += [""] * (12 - len(cols))
        cols = cols[:12]
        
        # Clean each column
        clean_cols = []
        for c in cols:
            # Strip simple markdown and latex
            c = c.replace("**", "").replace("__", "").replace("`", "").replace("$", "")
            # Convert multi-line to single line
            c_lines = [line.strip() for line in c.split("\n") if line.strip()]
            c = " // ".join(c_lines)
            c = re.sub(r"[ \t]{2,}", " ", c).strip()
            clean_cols.append(c)
            
        cleaned.append(dict(zip(COLUMNS, clean_cols)))
        
    print("Writing output...")
    with OUTPUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(cleaned)
        
    print("Done!")

if __name__ == "__main__":
    main()
