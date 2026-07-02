import os
import subprocess
import re

data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

def verify():
    print("--- POST-INJECTION VERIFICATION ---")
    
    # 1. Syntax Check
    try:
        subprocess.run(['node', '-c', data_js_path], check=True, capture_output=True, text=True)
        print("[OK] Syntax validation passed.")
    except Exception as e:
        print(f"[FAIL] Syntax error: {e}")
        return

    # 2. Row Count
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the fin2 section
    match = re.search(r'"fin2":\s*(\{.*?\n\s+\}),', content, re.DOTALL)
    if not match:
        print("[FAIL] Could not find 'fin2' block in data.js")
        return
    
    fin2_str = match.group(1)
    
    # Count occurrences of "id": "fin2-ch"
    id_count = len(re.findall(r'"id": "fin2-ch\d+-cq-\d+"', fin2_str))
    print(f"[INFO] Found {id_count} full CQ records in fin2.")
    if id_count == 191:
        print("[OK] Injected row count matches CSV row count.")
    else:
        print(f"[FAIL] Row count mismatch: Expected 191, got {id_count}")

    # 3. Random Sampling
    sample_ids = ["fin2-ch2-cq-001", "fin2-ch4-cq-052", "fin2-ch9-cq-120", "fin2-ch10-cq-150"]
    print("\n--- RANDOM SAMPLING ---")
    for sid in sample_ids:
        if sid in content:
            print(f"[OK] {sid} exists in data.js")
            # Extract a bit of context
            idx = content.find(sid)
            print(f"Sample snippet for {sid}:\n{content[idx:idx+200]}...")
        else:
            print(f"[FAIL] {sid} MISSING from data.js")

verify()
