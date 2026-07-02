import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

print("=== POST-INJECTION VERIFICATION ===\n")

# 1. Read data.js
with open(data_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Extract fin2 block
start_idx = content.find('"fin2":')
if start_idx == -1:
    print("[FAIL] Could not find 'fin2' block in data.js")
    sys.exit(1)

brace_count = 0
found_first_brace = False
end_idx = -1
for i in range(start_idx, len(content)):
    char = content[i]
    if char == '{':
        brace_count += 1
        found_first_brace = True
    elif char == '}':
        brace_count -= 1
        if found_first_brace and brace_count == 0:
            end_idx = i + 1
            break

if end_idx == -1:
    print("[FAIL] Could not find matching end brace for fin2")
    sys.exit(1)

fin2_block_str = content[start_idx:end_idx]
json_str = fin2_block_str.split(':', 1)[1].strip()

try:
    fin2_data = json.loads(json_str)
    print("[OK] fin2 block parsed successfully as valid JSON.")
except Exception as e:
    print(f"[FAIL] Could not parse fin2 block as JSON: {e}")
    sys.exit(1)

# 3. Check all expected chapters exist
expected_chapters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
existing_chapters = list(fin2_data.keys())
print(f"\n[INFO] Chapters found: {sorted(existing_chapters, key=int)}")

missing = [ch for ch in expected_chapters if ch not in existing_chapters]
if missing:
    print(f"[FAIL] Missing chapters: {missing}")
else:
    print("[OK] All 14 chapters present!")

# 4. Print per-chapter stats
print("\n--- PER-CHAPTER STATS ---")
total_full_cqs = 0
total_short_cqs = 0
new_chapters = ['3', '5', '7', '8', '12', '13', '14']
old_chapters = ['1', '2', '4', '6', '9', '10', '11']

for ch_num in sorted(fin2_data.keys(), key=int):
    ch_data = fin2_data[ch_num]
    tag = " [NEW]" if ch_num in new_chapters else " [EXISTING]"
    mcq_count = len(ch_data.get('mcqData', []))
    short_count = len(ch_data.get('shortCQData', []))
    full_count = len(ch_data.get('fullCQData', []))
    total_full_cqs += full_count
    total_short_cqs += short_count
    print(f"  Chapter {ch_num:>2}{tag}: mcq={mcq_count}, shortCQ={short_count}, fullCQ={full_count}  -- {ch_data.get('chapterName')}")

print(f"\nTotal full CQs: {total_full_cqs}")
print(f"Total short CQs: {total_short_cqs}")

# 5. Verify new chapters have expected CQ counts
new_full_cq_total = sum(len(fin2_data[ch].get('fullCQData', [])) for ch in new_chapters)
print(f"\n[INFO] New chapters total fullCQ count: {new_full_cq_total}")
if new_full_cq_total == 95:
    print("[OK] New chapters CQ count matches expected 95 from CSV!")
else:
    print(f"[WARN] Expected 95 new CQs from CSV, got {new_full_cq_total}")

# 6. Verify old chapters are untouched (spot-check IDs)
print("\n--- SPOT-CHECK EXISTING CHAPTERS ---")
spot_checks = {
    "1": "fin2-ch1-cq-071",
    "2": "fin2-ch2-cq-001",
    "4": "fin2-ch4-cq-050",
    "6": "fin2-ch6-cq-001",
    "9": "fin2-ch9-cq-095",
    "10": "fin2-ch10-cq-139",
    "11": "fin2-ch11-cq-041"
}
for ch_num, expected_id in spot_checks.items():
    full_cqs = fin2_data[ch_num].get('fullCQData', [])
    ids = [cq['id'] for cq in full_cqs]
    if expected_id in ids:
        print(f"  [OK] Chapter {ch_num}: Found expected ID {expected_id}")
    else:
        print(f"  [FAIL] Chapter {ch_num}: Expected ID {expected_id} NOT FOUND!")

# 7. Spot-check new chapters
print("\n--- SPOT-CHECK NEW CHAPTERS ---")
for ch_num in new_chapters:
    full_cqs = fin2_data[ch_num].get('fullCQData', [])
    if full_cqs:
        first_id = full_cqs[0]['id']
        last_id = full_cqs[-1]['id']
        first_stem_preview = full_cqs[0].get('stem', '')[:80]
        print(f"  [OK] Chapter {ch_num}: {len(full_cqs)} CQs, first={first_id}, last={last_id}")
        print(f"        First stem: {first_stem_preview}...")
    else:
        print(f"  [FAIL] Chapter {ch_num}: No fullCQData found!")

print("\n=== VERIFICATION COMPLETE ===")
