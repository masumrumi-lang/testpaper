import csv
import io
import os

def clean_csv_content(content):
    # Standardize line endings to \r\n
    # Replace \r\n with just \n for consistent processing first
    content = content.replace("\r\n", "\n")
    # Replace any remaining \r with \n
    content = content.replace("\r", "\n")

    # Remove leading/trailing empty lines and reduce multiple empty lines to one
    lines = content.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line or (cleaned_lines and cleaned_lines[-1] != ""):  # Keep single empty lines if not consecutive
            cleaned_lines.append(stripped_line)
    
    # Ensure only one empty line if there were multiple between text
    final_cleaned_lines = []
    for line in cleaned_lines:
        if line == "" and final_cleaned_lines and final_cleaned_lines[-1] == "":
            continue
        final_cleaned_lines.append(line)

    # Re-join with \r\n
    return "\r\n".join(final_cleaned_lines).strip()

def process_csv_file(input_filepath, output_filepath):
    with open(input_filepath, 'r', newline="", encoding=\'utf-8\') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        rows = list(reader)

    processed_rows = []
    processed_rows.append(header) # Always include header
    for row in rows:
        processed_row = []
        for cell in row:
            processed_row.append(clean_csv_content(cell))
        processed_rows.append(processed_row)

    with open(output_filepath, 'w', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(processed_rows)

if __name__ == "__main__":
    input_csv_path = "BUS_2_CH4_CQ - Sheet1.csv"
    output_csv_path = "BUS_2_CH4_CQ - Sheet1_cleaned.csv"

    process_csv_file(input_csv_path, output_csv_path)

    # Replace the original file with the cleaned one
    os.replace(output_csv_path, input_csv_path)
    print(f"Successfully cleaned and updated {input_csv_path}")
