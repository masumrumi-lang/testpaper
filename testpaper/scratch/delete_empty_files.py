from pathlib import Path

root = Path(r"C:\Users\BMTF\.antigravity\testpaper")

deleted = 0

for file in root.rglob("*"):
    if file.is_file():
        # delete empty files
        if file.stat().st_size == 0:
            file.unlink()
            deleted += 1

print("Deleted empty files:", deleted)
