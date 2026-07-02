import csv

file_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'

def get_rows(path, indices):
    result = {}
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, row in enumerate(reader, start=2):
            if i in indices:
                result[i] = row
    return header, result

targets = [25, 26, 128, 137]
header, rows = get_rows(file_path, targets)

def compare(id1, id2):
    r1 = rows[id1]
    r2 = rows[id2]
    print(f"\nComparing Row {id1} vs Row {id2}:")
    diffs = []
    for i, (h, v1, v2) in enumerate(zip(header, r1, r2)):
        if v1 != v2:
            diffs.append(f"  Col '{h}': '{v1}' != '{v2}'")
    
    if not diffs:
        print("  RESULT: EXACT DUPLICATE (Full Row)")
    else:
        print("  DIFFERENCES FOUND:")
        for d in diffs:
            print(d)

compare(25, 26)
compare(128, 137)
