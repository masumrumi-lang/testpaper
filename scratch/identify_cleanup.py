import os
from pathlib import Path

root = Path(r"C:\Users\BMTF\.antigravity\testpaper")

categories = {
    "safe_to_clean": [],
    "keep": [],
    "do_not_touch": []
}

# Define rule lists/patterns
def categorize_file(path: Path):
    rel_path = path.relative_to(root)
    parts = rel_path.parts
    
    # 🔴 Do NOT touch blindly
    if ".git" in parts or ".vs" in parts or ".venv" in parts or "workspace metadata" in parts:
        return "do_not_touch"
    
    if path.is_dir():
        return None

    # Check safe to clean patterns
    # bak files, backup files, pycache files, txt output files, temporary js test files
    name = path.name.lower()
    suffix = path.suffix.lower()
    
    if (
        suffix in [".bak", ".tmp", ".log", ".cache", ".pyc"] or
        "backup" in name or
        name.endswith(".bak") or
        name in ["run_output.txt", "ch1_out.txt", "qc_report.txt", "expansion_report.txt", "metadata_fix_report.txt", "audit_discrepancy_report.txt", "test.json"] or
        (suffix == ".txt" and (name.startswith("cq") and "out" in name or name.endswith("full.txt"))) or
        name in ["data_write_test.js", "data_test_write.js"] or
        "__pycache__" in parts
    ):
        return "safe_to_clean"
        
    # 🟡 Keep
    if suffix in [".py", ".ipynb", ".csv", ".json", ".html", ".js", ".css", ".docx"]:
        return "keep"
        
    # Default fallback
    return "do_not_touch"

total_size_cleanable = 0
for p in root.rglob("*"):
    cat = categorize_file(p)
    if cat:
        size = p.stat().st_size if p.is_file() else 0
        categories[cat].append((p, size))
        if cat == "safe_to_clean":
            total_size_cleanable += size

print("=== SAFE TO CLEAN ===")
for p, size in sorted(categories["safe_to_clean"], key=lambda x: x[1], reverse=True):
    print(f"{p.relative_to(root)} ({size / 1024:.2f} KB)")
print(f"Total cleanable size: {total_size_cleanable / 1024 / 1024:.2f} MB")
