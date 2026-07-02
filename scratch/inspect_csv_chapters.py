import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

chapters = set()
with open("c:/Users/BMTF/.antigravity/testpaper/Acc2_all_ch_mcq - Sheet1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        chapters.add(row['Chapter'])

print("Unique chapters in CSV:")
for c in sorted(chapters):
    print(repr(c))
