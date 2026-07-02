import csv
import json
import re

def bold_terms(text):
    if not text:
        return ""
    # Key management principles and famous theorists
    terms = [
        "Plan", "Organize", "Lead", "Control", 
        "Planning", "Organizing", "Leading", "Controlling",
        "Henri Fayol", "F.W. Taylor", "Henry Fayol", "Frederick Taylor",
        "Partnership", "Joint Stock Company", "Management Principles"
    ]
    for term in terms:
        # Case insensitive replacement with strong tag, but keeping original case in text if possible
        # Using a lambda to keep the original case of the matched text
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        text = pattern.sub(lambda m: f"<strong>{m.group(0)}</strong>", text)
    return text

def process_csv(file_path):
    chapters = {}
    
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chapter_str = row['Chapter'].strip()
            # Extract chapter number
            chapter_num = re.search(r'\d+', chapter_str)
            if chapter_num:
                chapter_id = chapter_num.group()
            else:
                chapter_id = "1" # Default
                
            if chapter_id not in chapters:
                chapters[chapter_id] = {
                    "subjectName": "Business Organization and Management",
                    "chapterName": chapter_str, 
                    "mcqData": []
                }
            
            # Map Year/Practice Question logic
            year = row['Year'].strip()
            level = row['Level'].strip()
            
            if year == "" or year == "-" or year.lower() == "n/a":
                meta_year = "Practice Question"
                q_type = "general practice"
            else:
                meta_year = year
                q_type = row['Category'].lower() if row['Category'] else "board"
            
            meta = f"{level} · {meta_year}"
            
            # Map Correct Answer (a-d to 0-3)
            ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
            correct_ans_str = row['Correct Answer'].lower().strip()
            # Handle numeric answers 1-4 just in case
            if correct_ans_str in ['1', '2', '3', '4']:
                correct_ans = int(correct_ans_str) - 1
            else:
                correct_ans = ans_map.get(correct_ans_str, 0)
            
            # Format Explanation
            explanation = bold_terms(row['Explanation'].strip())
            if explanation:
                # Add "Correct Answer" prefix if not present (optional, but looks good)
                options = [row['Option A'], row['Option B'], row['Option C'], row['Option D']]
                correct_text = options[correct_ans]
                if "Correct Answer" not in explanation:
                    explanation = f"<p>{explanation}</p><p class='mt-2'><strong>Correct Answer: {correct_text}</strong></p>"
                else:
                    explanation = f"<p>{explanation}</p>"
            
            # Construct MCQ object
            mcq = {
                "id": len(chapters[chapter_id]["mcqData"]) + 1,
                "text": f"<p>{row['Question'].strip()}</p>",
                "meta": meta,
                "type": q_type,
                "options": [
                    row['Option A'].strip(),
                    row['Option B'].strip(),
                    row['Option C'].strip(),
                    row['Option D'].strip()
                ],
                "correctAnswer": correct_ans,
                "explanation": explanation
            }
            
            chapters[chapter_id]["mcqData"].append(mcq)
            
    return chapters

if __name__ == "__main__":
    data = process_csv("B&M 1st Paper mcq - Sheet1.csv")
    
    # We will use "bus1" as the internal key in the JS file for simplicity, 
    # but the subjectName inside is "Business Organization and Management"
    with open("bus1_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Processing complete. {sum(len(c['mcqData']) for c in data.values())} questions processed.")
    print("Data saved to bus1_data.json")
