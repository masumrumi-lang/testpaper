import csv
from pathlib import Path

INPUT = Path('BUS_2_CH1_CQ - ch1.csv')
OUTPUT = Path('BUS_2_CH1_CQ - ch1.cleaned.csv')

PLACEHOLDER_QUESTIONS = {
    'A': 'Question A is missing from the original row; placeholder inserted.',
    'B': 'Question B is missing from the original row; placeholder inserted.',
    'C': 'Question C is missing from the original row; placeholder inserted.',
    'D': 'Question D is missing from the original row; placeholder inserted.',
}

PLACEHOLDER_ANSWERS = {
    'A': 'Answer A is missing from the original row; placeholder inserted.',
    'B': 'Answer B is missing from the original row; placeholder inserted.',
    'C': 'Answer C is missing from the original row; placeholder inserted.',
    'D': 'Answer D is missing from the original row; placeholder inserted.',
}

MESSAGE_MISSING_LEVEL = 'LEVEL missing due to row misalignment; placeholder inserted.'
MESSAGE_MISSING_CATEGORY = 'CATEGORY missing due to row misalignment; placeholder inserted.'
MESSAGE_MISSING_STEM = 'STEM missing due to row misalignment; placeholder inserted.'


def is_shifted_left_by_four(row):
    if len(row) != 14:
        return False
    return (
        row[6] and row[7] and row[8] and row[9] and row[10]
        and not row[11] and not row[12] and not row[13]
    )


def is_missing_questions(row):
    if len(row) != 14:
        return False
    return all(not row[i] for i in range(6, 10)) and any(row[i] for i in range(10, 14))


def fix_row(row, row_no, changes):
    if len(row) != 14:
        row = (row + [''] * 14)[:14]

    if is_missing_questions(row):
        for idx, part in enumerate(['A', 'B', 'C', 'D'], start=6):
            if not row[idx]:
                row[idx] = PLACEHOLDER_QUESTIONS[chr(64 + idx - 5)]
        changes.append((row_no, 'fill_missing_questions'))
        return row

    if is_shifted_left_by_four(row):
        restored = [row[0], row[1], row[2], MESSAGE_MISSING_LEVEL, MESSAGE_MISSING_CATEGORY, MESSAGE_MISSING_STEM]
        restored.extend(row[3:7])  # questions originally shifted into Level..Question_A
        restored.extend(row[7:11])  # answers originally shifted into Question_B..Ans_C
        while len(restored) < 14:
            restored.append('')
        if len(restored) > 14:
            restored = restored[:14]
        changes.append((row_no, 'realign_shifted'))
        return restored

    if not row[13] and row[9] and row[10] and row[11] and row[12] and row[6] and row[7] and row[8] and row[9]:
        row[13] = PLACEHOLDER_ANSWERS['D']
        changes.append((row_no, 'fill_missing_ans_d'))
        return row

    return row


def main():
    changes = []
    with INPUT.open('r', encoding='utf-8', newline='') as fin, OUTPUT.open('w', encoding='utf-8', newline='') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        for i, row in enumerate(reader, start=1):
            if i == 1:
                writer.writerow(row)
                continue
            fixed = fix_row(row, i, changes)
            writer.writerow(fixed)

    if changes:
        print('Repaired rows:')
        for row_no, reason in changes:
            print(f'  row {row_no}: {reason}')
    else:
        print('No repairs needed.')


if __name__ == '__main__':
    main()
