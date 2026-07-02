import csv
with open("c:/Users/BMTF/.antigravity/testpaper/Acc2_all_ch_mcq - Sheet1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # Let's find one row for chapter 2 and one for chapter 4
    rows = []
    for row in reader:
        if row['Chapter'] in ('2', '4') and len(rows) < 4:
            rows.append(row)
    
    for idx, r in enumerate(rows):
        print(f"--- Sample Row {idx} ---")
        for k, v in r.items():
            print(f"{k}: {repr(v)}")
