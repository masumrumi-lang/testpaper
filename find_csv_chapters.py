import csv
chapters = set()
with open('BUS1_CH7_CH8_CQ - Sheet1.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) > 2:
            chapters.add(row[2].strip())
print("Chapters in CSV:", chapters)
