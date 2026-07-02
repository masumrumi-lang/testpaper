import csv
import json
import re
from pathlib import Path

INPUT_CSV = Path("Acc2_ch1_cq - Sheet1.csv")
DATA_JS = Path("data.js")
CHAPTER_ID = "1"
SUBJECT_NAME = "Accounting 2nd Paper"
CHAPTER_NAME = "Chapter 1 : Accounts of Not-for-Profit Organizations"
ACC2_KEY = "acc2"


def normalize_text(text: str) -> str:
    if not text:
        return ""
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def to_html(text: str) -> str:
    return normalize_text(text).replace("\n", "<br>")


def build_chapter():
    with INPUT_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    cq_data = []
    for idx, row in enumerate(rows, start=1):
        questions = []
        for label in ["a", "b", "c"]:
            q_text = normalize_text(row.get(f"Question_{label.upper()}", ""))
            a_text = to_html(row.get(f"Ans_{label.upper()}", ""))
            if q_text:
                questions.append(
                    {
                        "label": label,
                        "text": q_text,
                        "answer": a_text,
                    }
                )

        cq_data.append(
            {
                "id": f"acc2_ch1_cq{idx}",
                "stem": to_html(row.get("Stem", "")),
                "meta": f"{normalize_text(row.get('Level', ''))} · {normalize_text(row.get('Year', ''))}",
                "type": normalize_text(row.get("Category", "")).lower() or "board",
                "questions": questions,
            }
        )

    return {
        CHAPTER_ID: {
            "subjectName": SUBJECT_NAME,
            "chapterName": CHAPTER_NAME,
            "mcqData": [],
            "cqData": cq_data,
        }
    }


def replace_or_insert_chapter(data_js_text: str, chapter_json: str) -> str:
    acc2_match = re.search(r'"acc2"\s*:\s*\{', data_js_text)
    if not acc2_match:
        raise RuntimeError("acc2 section not found in data.js")

    acc2_start = acc2_match.start()
    brace_start = data_js_text.find("{", acc2_match.end() - 1)
    if brace_start == -1:
        raise RuntimeError("acc2 opening brace not found")

    insert_match = re.search(r'\n(\s*)"2"\s*:\s*\{', data_js_text[brace_start:])
    if insert_match:
        insert_pos = brace_start + insert_match.start(0) + 1
        return data_js_text[:insert_pos] + chapter_json + ",\n" + data_js_text[insert_pos:]

    # If chapter 1 already exists, replace it.
    chapter_match = re.search(r'\n(\s*)"1"\s*:\s*\{', data_js_text[brace_start:])
    if chapter_match:
        start = brace_start + chapter_match.start(0) + 1
        depth = 0
        end = None
        for i in range(start, len(data_js_text)):
            if data_js_text[i] == "{":
                depth += 1
            elif data_js_text[i] == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError("Could not locate end of existing chapter 1 block")
        return data_js_text[:start] + chapter_json + data_js_text[end:]

    # Fallback: insert at the beginning of acc2 object contents.
    insert_pos = brace_start + 1
    while insert_pos < len(data_js_text) and data_js_text[insert_pos] in " \t\r\n":
        insert_pos += 1
    return data_js_text[:insert_pos] + chapter_json + ",\n" + data_js_text[insert_pos:]


def main():
    chapter_obj = build_chapter()
    chapter_json = json.dumps(chapter_obj, indent=4, ensure_ascii=False)
    chapter_json = chapter_json.strip()[1:-1].strip()
    chapter_json = "    " + chapter_json.replace("\n", "\n    ")

    data_js_text = DATA_JS.read_text(encoding="utf-8")
    new_text = replace_or_insert_chapter(data_js_text, chapter_json)
    DATA_JS.write_text(new_text, encoding="utf-8")

    print(f"Injected ACC2 chapter {CHAPTER_ID} CQ data from {INPUT_CSV.name}.")


if __name__ == "__main__":
    main()
