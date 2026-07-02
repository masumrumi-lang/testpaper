import csv

def main():
    print("Opening file...")
    try:
        with open("Acc2_ch1_cq - Sheet1.csv", "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Read {len(content)} characters.")
            
        with open("Acc2_ch1_cq - Sheet1.csv", "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            print(f"Parsed {len(rows)} CSV rows.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
