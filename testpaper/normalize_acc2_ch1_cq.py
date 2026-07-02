import pathlib
import re

DATA_JS = pathlib.Path("data.js")


def normalize_answer_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace(" -> ", " = ")
    text = text.replace("->", " = ")
    text = re.sub(r"\s+x\s+", " × ", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<=\d)\s*x\s*(?=\d|[A-Za-z(])", " × ", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<=[)\dA-Za-z])x(?=\d)", "×", text, flags=re.IGNORECASE)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s*\n\s*", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def replace_answer_block(match: re.Match) -> str:
    prefix = match.group(1)
    answer = match.group(2)
    return prefix + normalize_answer_text(answer)


def main():
    text = DATA_JS.read_text(encoding="utf-8")
    start = text.index('"1": {\n            "subjectName": "Accounting 2nd Paper"')
    end = text.index('"2": {', start)
    chapter = text[start:end]

    pattern = re.compile(r'("id": "acc2_ch1_cq\d+".*?"answer": ")(.*?)(?=")', re.S)
    new_chapter = pattern.sub(replace_answer_block, chapter)

    if new_chapter == chapter:
        print("No chapter-1 answer changes needed.")
        return

    new_text = text[:start] + new_chapter + text[end:]
    DATA_JS.write_text(new_text, encoding="utf-8")
    print("Normalized ACC2 chapter 1 CQ answers.")


if __name__ == "__main__":
    main()
