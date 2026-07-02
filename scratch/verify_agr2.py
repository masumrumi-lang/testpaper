import csv
import re

print("=" * 60)
print("PART 1: Inspect Skipped Row 31")
print("=" * 60)

with open(r'c:\Users\BMTF\.antigravity\testpaper\Agri2_all_ch_mcq - Sheet1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

row = rows[29]  # Row 31 = 0-indexed 29 (header is row 0, data starts row 1)
print(f"Chapter: {row['Chapter']}")
print(f"Question: {row['Question'][:150]}")
print(f"Option A: {row['Option A']}")
print(f"Option B: {row['Option B']}")
print(f"Option C: {row['Option C']}")
print(f"Option D: {row['Option D']}")
print(f"Correct Answer: [{row['Correct Answer']}]")

print()
print("=" * 60)
print("PART 2: Verify agr2 block in data.js")
print("=" * 60)

with open(r'c:\Users\BMTF\.antigravity\testpaper\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check agr2 key exists
if 'agr2' in content:
    print("[OK] agr2 key found in data.js")
else:
    print("[FAIL] agr2 key NOT found!")

# Count MCQs in agr2 block
agr2_start = content.find('"agr2"')
if agr2_start == -1:
    agr2_start = content.find('agr2:')
if agr2_start == -1:
    agr2_start = content.find("'agr2'")

print(f"  agr2 block starts at char index: {agr2_start}")

# Find the agr2 block boundaries
# Look for next top-level key after agr2
rest = content[agr2_start:]
# Find all "id": NNNN patterns in the agr2 block
# We need to find where agr2 ends - look for the next subject key
subject_keys = ['bnbs1', 'bnbs2', 'acc1', 'acc2', 'fin1', 'fin2', 'ict', 'agr1']
agr2_end = len(content)
for key in subject_keys:
    for pattern in [f'"{key}"', f"'{key}'"]:
        idx = content.find(pattern, agr2_start + 10)
        if idx != -1 and idx < agr2_end:
            agr2_end = idx

agr2_block = content[agr2_start:agr2_end]
ids_in_block = re.findall(r'"id"\s*:\s*(\d+)', agr2_block)
print(f"  Total MCQs in agr2 block: {len(ids_in_block)}")

if ids_in_block:
    int_ids = [int(x) for x in ids_in_block]
    print(f"  ID range: {min(int_ids)} - {max(int_ids)}")

# Count per chapter
chapters_found = re.findall(r'"chapter"\s*:\s*"(\d+)"', agr2_block)
from collections import Counter
ch_counts = Counter(chapters_found)
print(f"  Chapters found: {sorted(ch_counts.keys())}")
for ch in sorted(ch_counts.keys()):
    print(f"    Chapter {ch}: {ch_counts[ch]} MCQs")

# Check total
total_in_block = len(ids_in_block)
print(f"\n  Expected: 217 MCQs (218 rows - 1 skipped)")
print(f"  Actual:   {total_in_block} MCQs")
if total_in_block == 217:
    print("  [OK] Count matches!")
else:
    print(f"  [WARNING] Count mismatch! Difference: {total_in_block - 217}")

# Verify no syntax issues by checking data.js can be loaded
print()
print("=" * 60)
print("PART 3: Syntax check")
print("=" * 60)
import subprocess
result = subprocess.run(['node', '-c', r'c:\Users\BMTF\.antigravity\testpaper\data.js'], capture_output=True, text=True)
if result.returncode == 0:
    print("[OK] data.js syntax is valid")
else:
    print(f"[FAIL] Syntax error: {result.stderr}")

# Check no duplicate keys
print()
print("=" * 60)
print("PART 4: Check for duplicate subject keys")
print("=" * 60)
all_keys = re.findall(r'"(agr2)"', content)
print(f"  Occurrences of 'agr2' as key: {len(all_keys)}")
if len(all_keys) == 1:
    print("  [OK] No duplicate agr2 keys")
else:
    print("  [WARNING] Multiple agr2 keys found!")

# Verify options always have exactly 4
print()
print("=" * 60)
print("PART 5: Verify all MCQs have 4 options")
print("=" * 60)
options_pattern = re.findall(r'"options"\s*:\s*\[(.*?)\]', agr2_block, re.DOTALL)
bad_options = 0
for i, opt_block in enumerate(options_pattern):
    opt_count = opt_block.count('"text"')
    if opt_count != 4:
        print(f"  [WARNING] MCQ index {i}: has {opt_count} options instead of 4")
        bad_options += 1
if bad_options == 0:
    print(f"  [OK] All {len(options_pattern)} MCQs have exactly 4 options")

print()
print("=" * 60)
print("VERIFICATION COMPLETE")
print("=" * 60)
