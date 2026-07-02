import csv, os, sys

BASE = r"c:\Users\BMTF\.antigravity\testpaper"
OUT  = r"c:\Users\BMTF\.antigravity\testpaper\scratch\inspect_out.txt"

out = open(OUT, "w", encoding="utf-8")

# --- 1. CSV row count + first row preview ---
csv_path = os.path.join(BASE, "Acc2_ch1_cq - Sheet1.csv")
with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

out.write(f"CSV total rows: {len(rows)}\n")
out.write(f"Columns: {list(rows[0].keys())}\n\n")
out.write("=== ROW 1 FIELDS ===\n")
for k, v in rows[0].items():
    out.write(f"  {k}: {repr(v[:120])}\n")

out.write("\n=== ROW 1 STEM (full) ===\n")
out.write(rows[0].get("Stem", "") + "\n")

out.write("\n=== ROW 1 Ans_A (first 500 chars) ===\n")
out.write(rows[0].get("Ans_A", "")[:500] + "\n")

# --- 2. data.js acc2 structure ---
data_path = os.path.join(BASE, "data.js")
content = open(data_path, "r", encoding="utf-8").read()

idx = content.find('"acc2"')
out.write(f"\nacc2 found at char index: {idx}\n")
if idx >= 0:
    out.write("\n=== acc2 snippet (first 3000 chars) ===\n")
    out.write(content[idx: idx + 3000])

# Check for existing ch1 inside acc2
ch1_search = content.find('"1"', idx) if idx >= 0 else -1
out.write(f"\n\nFirst '\"1\"' after acc2 at: {ch1_search}\n")
if ch1_search >= 0:
    out.write(content[ch1_search: ch1_search + 1000])

out.close()
print("Done - wrote to", OUT)
