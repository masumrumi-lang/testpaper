import re
import glob

files = sorted(glob.glob("fullCQ_board_part*.js"))
output = []
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        matches = re.finditer(r'id:\s*"(.*?)".*?meta:\s*"(.*?)"', content, re.DOTALL)
        for m in matches:
            output.append(f"{m.group(1)}: {m.group(2)}")

with open("id_meta_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))
