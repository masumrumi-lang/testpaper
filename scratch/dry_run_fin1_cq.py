import csv
import json
import os
import sys

CSV_FILE = "Fin1_ch_1_3_4_6_8_9_cq - Sheet1.csv"
TARGET_CHAPTERS = ["1", "3", "4", "6", "8", "9"]

def sanitize(text):
    if not text:
        return ""
    # clean up newlines and strip whitespace
    return text.replace('\r\n', '\n').strip()

def process_content(text):
    if not text:
        return ""
    text = sanitize(text)
    # Default processing: convert newlines to <br> for HTML rendering
    # Double newlines as <br><br>
    text = text.replace("\n\n\n", "<br><br>")
    text = text.replace("\n\n", "<br><br>")
    text = text.replace("\n", "<br>")
    return text

def dry_run():
    if not os.path.exists(CSV_FILE):
        print(f"Error: CSV file not found: {CSV_FILE}")
        return

    chapter_data = {ch: {"full": [], "short": []} for ch in TARGET_CHAPTERS}

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            ch = row.get("Chapter", "").strip()
            if ch not in TARGET_CHAPTERS:
                continue

            stem = process_content(row.get("Stem", ""))
            meta = f"{row.get('Level', '-')} · {row.get('Year', '-')}"
            q_type = row.get('Category', 'board').strip().lower()

            # Build sub-questions list
            questions = []
            if row.get("Question_A"):
                questions.append({"label": "a", "text": process_content(row["Question_A"]), "answer": process_content(row.get("Ans_A", ""))})
            if row.get("Question_B"):
                questions.append({"label": "b", "text": process_content(row["Question_B"]), "answer": process_content(row.get("Ans_B", ""))})
            if row.get("Question_C"):
                questions.append({"label": "c", "text": process_content(row["Question_C"]), "answer": process_content(row.get("Ans_C", ""))})
            if row.get("Question_D"):
                questions.append({"label": "d", "text": process_content(row["Question_D"]), "answer": process_content(row.get("Ans_D", ""))})

            # Full CQ
            idx = len(chapter_data[ch]["full"]) + 1
            full_item = {
                "id": f"fin1-ch{ch}-cq-{idx:03d}",
                "stem": stem,
                "meta": meta,
                "type": q_type,
                "questions": questions
            }
            chapter_data[ch]["full"].append(full_item)

            # Short CQ (A and B parts)
            if row.get("Question_A"):
                chapter_data[ch]["short"].append({
                    "id": f"fin1-ch{ch}-short-a-{idx:03d}",
                    "text": process_content(row["Question_A"]),
                    "answer": process_content(row.get("Ans_A", "")),
                    "meta": meta,
                    "type": q_type
                })
            if row.get("Question_B"):
                chapter_data[ch]["short"].append({
                    "id": f"fin1-ch{ch}-short-b-{idx:03d}",
                    "text": process_content(row["Question_B"]),
                    "answer": process_content(row.get("Ans_B", "")),
                    "meta": meta,
                    "type": q_type
                })

    print("--- PARSED CQ COUNTS ---")
    for ch in TARGET_CHAPTERS:
        print(f"Chapter {ch}: {len(chapter_data[ch]['full'])} Full CQs, {len(chapter_data[ch]['short'])} Short CQs")

    print("\n--- SAMPLE PREVIEW FOR CHAPTER 1 (FIRST ITEM) ---")
    if chapter_data["1"]["full"]:
        print("FULL CQ:")
        print(json.dumps(chapter_data["1"]["full"][0], indent=2, ensure_ascii=False))
        print("\nSHORT CQ PART A:")
        print(json.dumps(chapter_data["1"]["short"][0], indent=2, ensure_ascii=False))
        print("\nSHORT CQ PART B:")
        print(json.dumps(chapter_data["1"]["short"][1], indent=2, ensure_ascii=False))

if __name__ == "__main__":
    dry_run()
