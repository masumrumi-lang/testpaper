import csv
import json

csv_path = 'fin1_ch3_cq - Sheet1.csv'
try:
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)
        
    result = {
        "headers": headers,
        "row_count": len(rows),
        "sample_row": rows[0] if rows else None
    }
    
    with open('csv_headers.txt', 'w', encoding='utf-8') as out:
        json.dump(result, out, indent=4)
    print("Successfully inspected CSV.")
except Exception as e:
    with open('csv_headers.txt', 'w', encoding='utf-8') as out:
        out.write(f"Error: {str(e)}")
