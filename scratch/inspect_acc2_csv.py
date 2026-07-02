import csv
with open("c:/Users/BMTF/.antigravity/testpaper/Acc2_all_ch_mcq - Sheet1.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for i in range(3):
        try:
            row = next(reader)
            print(f"Row {i}:", row)
        except StopIteration:
            break
