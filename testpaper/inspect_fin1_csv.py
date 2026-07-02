import csv

def inspect_csv():
    csv_file = 'c:/Users/BMTF/.antigravity/testpaper/Fin1_ch_1_3_cq - Sheet1.csv'
    output = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            output.append(f"Fieldnames: {fieldnames}")
            
            chapters = {}
            for row in reader:
                ch = row.get('Chapter', '').strip()
                chapters[ch] = chapters.get(ch, 0) + 1
                
            output.append("Chapters and row counts:")
            for ch, count in sorted(chapters.items()):
                output.append(f"  Chapter {ch}: {count} rows")
    except Exception as e:
        output.append(f"Error: {e}")

    with open('c:/Users/BMTF/.antigravity/testpaper/inspect_output.txt', 'w', encoding='utf-8') as out_f:
        out_f.write("\n".join(output))

if __name__ == '__main__':
    inspect_csv()
