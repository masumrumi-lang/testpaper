import json
import re

# 1. Structured CQ Object requested by user
structured_cq = {
  "chapter": "Accounting 2nd Paper Chapter 2",
  "question_id": "acc2_ch2_cq3_college",
  "stimulus": "X, Y, and Z are three partners in a partnership business. Their profit-sharing ratio is 5:4:1. On January 1, 2025, their capitals were Tk. 3,60,000, Tk. 2,40,000, and Tk. 1,20,000 respectively. In the middle of the year, X provided Tk. 2,00,000 to the business as a loan. Each partner withdrew Tk. 4,000 in the middle of every month throughout the year. Y withdrew goods worth Tk. 6,000 which was not recorded in the books. According to the agreement, Z gets a salary of Tk. 4,000 per month from the business for rendering full-time service. Interest at 10% is to be charged on capital and drawings. X and Y jointly guaranteed Z that Z will get a share of profit of Tk. 60,000 every year excluding his interest on capital and salary. After debiting Z's salary but before making other adjustments, the profit of the business amounts to Tk. 3,60,000.<br><strong>RAJUK Uttara Model College, Dhaka - 2026</strong>",
  "requirements": {
    "a": "Determine the amount of interest on partners' drawings.",
    "b": "Prepare Profit and Loss Appropriation Account.",
    "c": "Prepare the Partners' Capital Account.",
    "d": ""
  },
  "solutions": {
    "a": "<p><strong>Calculation of the amount of interest on partners' drawings:</strong><br>X = (Monthly drawings &times; 10%) &times; 6 = (4,000 &times; 10%) &times; 6 = Tk. 2,400.<br>Y = (Monthly drawings &times; 10%) &times; 6 = (4,000 &times; 10%) &times; 6 = Tk. 2,400.<br>Z = (Monthly drawings &times; 10%) &times; 6 = (4,000 &times; 10%) &times; 6 = Tk. 2,400.</p>",
    "b": "<div class=\"text-center\"><p><strong>X, Y, and Z<br>Profit and Loss Appropriation Account<br>For the year ended December 31, 2025</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"3\" style=\"text-align: left;\">Debit</th><th colspan=\"3\" style=\"text-align: right;\">Credit</th></tr><tr><th>Particulars</th><th>Tk.</th><th>Tk.</th><th>Particulars</th><th>Tk.</th><th>Tk.</th></tr><tr><td><strong>Partners' Capital Account: (Interest on Capital)</strong><br>X<br>Y<br>Z</td><td style=\"vertical-align: bottom;\">36,000<br>24,000<br><u>12,000</u></td><td style=\"vertical-align: bottom;\">72,000</td><td><strong>Income Statement:</strong> (Net Profit)</td><td></td><td style=\"vertical-align: top;\">3,60,000</td></tr><tr><td><strong>X's Loan Account:</strong> (Interest on Loan)</td><td></td><td style=\"vertical-align: bottom;\">6,000</td><td><strong>Partners' Capital Account: (Interest on Drawings)</strong><br>X<br>Y<br>Z</td><td style=\"vertical-align: bottom;\">2,400<br>2,400<br><u>2,400</u></td><td style=\"vertical-align: bottom;\">7,200</td></tr><tr><td><strong>Partners' Capital Account: (Share of Profit)</strong><br>X<br>Y<br>Z</td><td style=\"vertical-align: bottom;\">1,30,667<br>1,04,533<br><u>60,000</u></td><td style=\"vertical-align: bottom;\">2,95,200</td><td><strong>Y's Capital Account:</strong> (Drawings of Goods)</td><td></td><td style=\"vertical-align: bottom;\">6,000</td></tr><tr><td></td><td></td><td><strong><u>3,73,200</u></strong></td><td></td><td></td><td><strong><u>3,73,200</u></strong></td></tr></table></div><p><strong>Note:</strong> According to the guarantee, Z's profit = Tk. 60,000<br>Therefore, X's profit = (2,95,200 - 60,000) &times; 5/9 = Tk. 1,30,667<br>And Y's profit = (2,95,200 - 60,000) &times; 4/9 = Tk. 1,04,533.</p>",
    "c": "<div class=\"text-center\"><p><strong>X, Y, and Z<br>Capital Account</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"5\" style=\"text-align: left;\">Debit</th><th colspan=\"5\" style=\"text-align: right;\">Credit</th></tr><tr><th>Date</th><th>Particulars</th><th>X (Tk.)</th><th>Y (Tk.)</th><th>Z (Tk.)</th><th>Date</th><th>Particulars</th><th>X (Tk.)</th><th>Y (Tk.)</th><th>Z (Tk.)</th></tr><tr><td>2025<br>Dec. 31</td><td>Drawings Account</td><td>48,000</td><td>48,000</td><td>48,000</td><td>2025<br>Jan. 1</td><td>Balance b/d</td><td>3,60,000</td><td>2,40,000</td><td>1,20,000</td></tr><tr><td>Dec. 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Drawings</td><td>2,400</td><td>2,400</td><td>2,400</td><td>Dec. 31</td><td><strong>Profit &amp; Loss A/c:</strong><br>Salary</td><td></td><td></td><td>48,000</td></tr><tr><td></td><td>Drawings of Goods</td><td></td><td>6,000</td><td></td><td>Dec. 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Capital</td><td>36,000</td><td>24,000</td><td>12,000</td></tr><tr><td>Dec. 31</td><td>Balance c/d</td><td>4,76,267</td><td>3,12,133</td><td>1,89,600</td><td></td><td>Share of Profit</td><td>1,30,667</td><td>1,04,533</td><td>60,000</td></tr><tr><td></td><td></td><td><strong><u>5,26,667</u></strong></td><td><strong><u>3,68,533</u></strong></td><td><strong><u>2,40,000</u></strong></td><td></td><td></td><td><strong><u>5,26,667</u></strong></td><td><strong><u>3,68,533</u></strong></td><td><strong><u>2,40,000</u></strong></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>2026<br>Jan. 1</td><td>Balance b/d</td><td>4,76,267</td><td>3,12,133</td><td>1,89,600</td></tr></table></div>",
    "d": ""
  },
  "tables": []
}

with open('extracted_cq3.json', 'w', encoding='utf-8') as f:
    json.dump(structured_cq, f, indent=2, ensure_ascii=False)

# 2. Convert to application schema and inject into data.js
new_cq_app_schema = {
    "id": "acc2_ch2_cq3_college",
    "stem": "<p>X, Y, and Z are three partners in a partnership business. Their profit-sharing ratio is 5:4:1. On January 1, 2025, their capitals were Tk. 3,60,000, Tk. 2,40,000, and Tk. 1,20,000 respectively. In the middle of the year, X provided Tk. 2,00,000 to the business as a loan. Each partner withdrew Tk. 4,000 in the middle of every month throughout the year. Y withdrew goods worth Tk. 6,000 which was not recorded in the books. According to the agreement, Z gets a salary of Tk. 4,000 per month from the business for rendering full-time service. Interest at 10% is to be charged on capital and drawings. X and Y jointly guaranteed Z that Z will get a share of profit of Tk. 60,000 every year excluding his interest on capital and salary. After debiting Z's salary but before making other adjustments, the profit of the business amounts to Tk. 3,60,000.</p><p>RAJUK Uttara Model College, Dhaka · 2026</p>",
    "meta": "RAJUK Uttara Model College, Dhaka · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of interest on partners' drawings.",
            "answer": structured_cq["solutions"]["a"]
        },
        {
            "label": "b",
            "text": "Prepare Profit and Loss Appropriation Account.",
            "answer": structured_cq["solutions"]["b"]
        },
        {
            "label": "c",
            "text": "Prepare the Partners' Capital Account.",
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
