import json
import re

# 1. Structured CQ Object requested by user
structured_cq = {
  "chapter": "Accounting 2nd Paper Chapter 2",
  "question_id": "acc2_ch2_cq4_college",
  "stimulus": "P, Q, and R are three partners in a partnership business. On January 1, 2024, their account balances were as follows:<br><br>P's Capital - Tk. 1,80,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; P's Current Account - 20,000 (Cr)<br>Q's Capital - Tk. 1,50,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Q's Current Account - 8,000 (Dr)<br>R's Capital - Tk. 1,30,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; R's Current Account - 12,000 (Cr)<br><br>According to the partnership agreement, interest on capital is to be provided at 6%. On July 1, 2024, R provided Tk. 20,000 as a loan to the business. Q will get a salary of Tk. 500 per month for his full-time work in the business. After debiting the salary amount, the net income of the business on December 31, 2024, was Tk. 55,240.<br><strong>Ideal School and College, Motijheel - 2026</strong>",
  "requirements": {
    "a": "Determine the amount of Q's annual salary.",
    "b": "Prepare Profit and Loss Appropriation Account.",
    "c": "Prepare the Partners' Current Account.",
    "d": ""
  },
  "solutions": {
    "a": "<p><strong>Answer:</strong> Q's annual salary = 500 &times; 12 = Tk. 6,000</p>",
    "b": "<div class=\"text-center\"><p><strong>P, Q, and R<br>Profit and Loss Appropriation Account<br>For the year ended December 31, 2024</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"3\" style=\"text-align: left;\">Debit</th><th colspan=\"3\" style=\"text-align: right;\">Credit</th></tr><tr><th>Particulars</th><th>Tk.</th><th>Tk.</th><th>Particulars</th><th>Tk.</th><th>Tk.</th></tr><tr><td><strong>Partners' Current Account: (Interest on Capital)</strong><br>P<br>Q<br>R</td><td style=\"vertical-align: bottom;\">10,800<br>9,000<br><u>7,800</u></td><td style=\"vertical-align: bottom;\">27,600</td><td><strong>Profit and Loss Account:</strong><br>(Net Profit transferred)</td><td></td><td style=\"vertical-align: top;\">55,240</td></tr><tr><td><strong>R's Loan Account:</strong> (Interest on Loan)</td><td></td><td style=\"vertical-align: bottom;\">600</td><td></td><td></td><td></td></tr><tr><td><strong>Partners' Current Account: (Share of Profit)</strong><br>P<br>Q<br>R</td><td style=\"vertical-align: bottom;\">9,013<br>9,013<br><u>9,014</u></td><td style=\"vertical-align: bottom;\">27,040</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td><strong><u>55,240</u></strong></td><td></td><td></td><td><strong><u>55,240</u></strong></td></tr></table></div>",
    "c": "<div class=\"text-center\"><p><strong>Partners' Current Account</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"6\" style=\"text-align: left;\">Debit</th><th colspan=\"6\" style=\"text-align: right;\">Credit</th></tr><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>P (Tk.)</th><th>Q (Tk.)</th><th>R (Tk.)</th><th>Date</th><th>Particulars</th><th>J.F.</th><th>P (Tk.)</th><th>Q (Tk.)</th><th>R (Tk.)</th></tr><tr><td>2024<br>Jan. 1</td><td>Balance b/d</td><td></td><td></td><td>8,000</td><td></td><td>2024<br>Jan. 1</td><td>Balance b/d</td><td></td><td>20,000</td><td></td><td>12,000</td></tr><tr><td>Dec. 31</td><td>Balance c/d</td><td></td><td>39,813</td><td>16,013</td><td>28,814</td><td>Dec. 31</td><td><strong>Profit &amp; Loss A/c:</strong><br>Salary</td><td></td><td></td><td>6,000</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Dec. 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Capital</td><td></td><td>10,800</td><td>9,000</td><td>7,800</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Share of Profit</td><td></td><td>9,013</td><td>9,013</td><td>9,014</td></tr><tr><td></td><td></td><td></td><td><strong><u>39,813</u></strong></td><td><strong><u>24,013</u></strong></td><td><strong><u>28,814</u></strong></td><td></td><td></td><td></td><td><strong><u>39,813</u></strong></td><td><strong><u>24,013</u></strong></td><td><strong><u>28,814</u></strong></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>2025<br>Jan. 1</td><td>Balance b/d</td><td></td><td>39,813</td><td>16,013</td><td>28,814</td></tr></table></div>",
    "d": ""
  },
  "tables": []
}

with open('extracted_cq4.json', 'w', encoding='utf-8') as f:
    json.dump(structured_cq, f, indent=2, ensure_ascii=False)

# 2. Convert to application schema and inject into data.js
new_cq_app_schema = {
    "id": "acc2_ch2_cq4_college",
    "stem": "<p>P, Q, and R are three partners in a partnership business. On January 1, 2024, their account balances were as follows:</p><p>P's Capital - Tk. 1,80,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; P's Current Account - 20,000 (Cr)<br>Q's Capital - Tk. 1,50,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Q's Current Account - 8,000 (Dr)<br>R's Capital - Tk. 1,30,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; R's Current Account - 12,000 (Cr)</p><p>According to the partnership agreement, interest on capital is to be provided at 6%. On July 1, 2024, R provided Tk. 20,000 as a loan to the business. Q will get a salary of Tk. 500 per month for his full-time work in the business. After debiting the salary amount, the net income of the business on December 31, 2024, was Tk. 55,240.</p><p>Ideal School and College, Motijheel · 2026</p>",
    "meta": "Ideal School and College, Motijheel · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of Q's annual salary.",
            "answer": structured_cq["solutions"]["a"]
        },
        {
            "label": "b",
            "text": "Prepare Profit and Loss Appropriation Account.",
            "answer": structured_cq["solutions"]["b"]
        },
        {
            "label": "c",
            "text": "Prepare the Partners' Current Account.",
            "answer": structured_cq["solutions"]["c"]
        }
    ]
}

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the chapter
target_chapter = '"chapterName": "Chapter 2 : Partnership Business Accounts",'
idx = content.find(target_chapter)

if idx == -1:
    print("Error: Chapter not found")
else:
    cq_idx = content.find('"fullCQData": [', idx)
    if cq_idx == -1:
        print("Error: fullCQData not found")
    else:
        # Find the end of the fullCQData array for this chapter
        bracket_count = 0
        in_string = False
        escape = False
        start_search = cq_idx + len('"fullCQData": [')
        
        close_idx = -1
        for i in range(start_search, len(content)):
            char = content[i]
            if in_string:
                if escape:
                    escape = False
                elif char == '\\':
                    escape = True
                elif char == '"':
                    in_string = False
            else:
                if char == '"':
                    in_string = True
                elif char == '[' or char == '{':
                    bracket_count += 1
                elif char == ']' or char == '}':
                    bracket_count -= 1
                    if bracket_count < 0: # This means we hit the closing bracket of the array
                        close_idx = i
                        break
        
        if close_idx == -1:
            print("Error: Closing bracket for fullCQData not found")
        else:
            inner_content = content[start_search:close_idx].strip()
            
            json_str = json.dumps(new_cq_app_schema, indent=4, ensure_ascii=False)
            lines = json_str.split('\n')
            indented_lines = ['                ' + line for line in lines]
            formatted_json = '\n'.join(indented_lines)
            
            if inner_content == "":
                new_val = '\n' + formatted_json + '\n            '
                new_content = content[:start_search] + new_val + content[close_idx:]
            else:
                last_brace_idx = content.rfind('}', start_search, close_idx)
                if last_brace_idx != -1:
                    new_val = ',\n' + formatted_json
                    new_content = content[:last_brace_idx+1] + new_val + content[last_brace_idx+1:]
                else:
                    new_val = formatted_json
                    new_content = content[:close_idx] + new_val + content[close_idx:]
            
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully injected into data.js")
