import json
import re

# 1. Structured CQ Object requested by user
structured_cq = {
  "chapter": "Accounting 2nd Paper Chapter 2",
  "question_id": "acc2_ch2_cq5_college",
  "stimulus": "Omar, Osman, and Oli are three partners in a partnership business. They share profit and loss in the ratio of 3:2:1 respectively. On January 1, 2025, their capitals were: Omar Tk. 6,80,000, Osman Tk. 4,80,000, and Oli Tk. 4,00,000. On July 1, Osman provided Tk. 1,60,000 as a loan to the business. Osman withdrew Tk. 60,000 in cash from the business on April 1. According to the agreement, Oli will get a salary of Tk. 8,000 per month for his full-time work. Oli withdraws his salary in cash. Omar will get a commission of 5% on the net profit of the business. Interest at 10% per annum is to be charged on the partners' capital, drawings, and loan. Omar and Osman jointly guaranteed Oli that Oli will receive at least Tk. 1,30,500 per year as his share of profit. After adjusting Oli's salary but before making other adjustments, the net profit of the business for the year ended December 31, 2025, amounted to Tk. 8,80,000.<br><strong>Dhaka Commerce College - 2026</strong>",
  "requirements": {
    "a": "Determine the amount of Omar's commission.",
    "b": "Prepare the Partners' Profit and Loss Appropriation Account assuming Omar's commission is Tk. 40,000.",
    "c": "Prepare the Capital Account for Omar and Osman. (Assuming divisible share of profit as Tk. 3,00,000 and Tk. 2,00,000 respectively)"
  },
  "solutions": {
    "a": "<p>Omar's commission = Net profit &times; 5% = (8,80,000 &times; 5%) = Tk. 44,000</p><p><strong>Answer:</strong> Omar's commission is Tk. 44,000.</p>",
    "b": "<div class=\"text-center\"><p><strong>Omar, Osman, and Oli<br>Profit and Loss Appropriation Account<br>For the year ended December 31, 2025</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"3\" style=\"text-align: left;\">Debit</th><th colspan=\"3\" style=\"text-align: right;\">Credit</th></tr><tr><th>Particulars</th><th>Tk.</th><th>Tk.</th><th>Particulars</th><th>Tk.</th><th>Tk.</th></tr><tr><td><strong>Partners' Capital Account: (Interest on Capital)</strong><br>Omar (6,80,000 &times; 10%)<br>Osman (4,80,000 &times; 10%)<br>Oli (4,00,000 &times; 10%)</td><td style=\"vertical-align: bottom;\">68,000<br>48,000<br><u>40,000</u></td><td style=\"vertical-align: bottom;\">1,56,000</td><td><strong>Income Statement:</strong> (Net Profit)</td><td></td><td style=\"vertical-align: top;\">8,80,000</td></tr><tr><td><strong>Omar's Capital Account:</strong><br>(Commission) (Given in question)</td><td></td><td style=\"vertical-align: bottom;\">40,000</td><td><strong>Osman's Capital Account: (Interest on Drawings)</strong><br>(60,000 &times; 10% &times; 9/12)</td><td></td><td style=\"vertical-align: bottom;\">4,500</td></tr><tr><td><strong>Osman's Loan Account:</strong><br>(Interest on Loan) (1,60,000 &times; 10% &times; 6/12)</td><td></td><td style=\"vertical-align: bottom;\">8,000</td><td></td><td></td><td></td></tr><tr><td><strong>Partners' Capital Account: (Share of Profit)</strong><br>Omar (6,80,500 &minus; 1,30,500) &times; 3/5<br>Osman (6,80,500 &minus; 1,30,500) &times; 2/5<br>Oli (Note)</td><td style=\"vertical-align: bottom;\">3,30,000<br>2,20,000<br><u>1,30,500</u></td><td style=\"vertical-align: bottom;\">6,80,500</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td><strong><u>8,84,500</u></strong></td><td></td><td></td><td><strong><u>8,84,500</u></strong></td></tr></table></div><p><strong>Answer:</strong> Divisible Share of Profit: Omar Tk. 3,30,000; Osman Tk. 2,20,000 and Oli Tk. 1,30,500.</p>",
    "c": "<div class=\"text-center\"><p><strong>Omar and Osman<br>Capital Account</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"4\" style=\"text-align: left;\">Debit</th><th colspan=\"4\" style=\"text-align: right;\">Credit</th></tr><tr><th>Date</th><th>Particulars</th><th>Omar (Tk.)</th><th>Osman (Tk.)</th><th>Date</th><th>Particulars</th><th>Omar (Tk.)</th><th>Osman (Tk.)</th></tr><tr><td>2025<br>Apr. 1</td><td>Drawings Account</td><td></td><td>60,000</td><td>2025<br>Jan. 1</td><td>Balance b/d</td><td>6,80,000</td><td>4,80,000</td></tr><tr><td>Dec. 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Drawings</td><td></td><td>4,500</td><td>Dec. 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Capital</td><td>68,000</td><td>48,000</td></tr><tr><td>Dec. 31</td><td>Balance c/d</td><td>10,92,000</td><td>6,63,500</td><td></td><td>Commission (from 'a')</td><td>44,000</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Share of Profit (Given in question)</td><td>3,00,000</td><td>2,00,000</td></tr><tr><td></td><td></td><td><strong><u>10,92,000</u></strong></td><td><strong><u>7,28,000</u></strong></td><td></td><td></td><td><strong><u>10,92,000</u></strong></td><td><strong><u>7,28,000</u></strong></td></tr><tr><td></td><td></td><td></td><td></td><td>2026<br>Jan. 1</td><td>Balance b/d</td><td>10,92,000</td><td>6,63,500</td></tr></table></div><p><strong>Answer:</strong> Closing capital balance: Omar Tk. 10,92,000 and Osman Tk. 6,63,500.</p>",
    "d": ""
  },
  "tables": []
}

with open('extracted_cq5.json', 'w', encoding='utf-8') as f:
    json.dump(structured_cq, f, indent=2, ensure_ascii=False)

# 2. Convert to application schema and inject into data.js
new_cq_app_schema = {
    "id": "acc2_ch2_cq5_college",
    "stem": "<p>Omar, Osman, and Oli are three partners in a partnership business. They share profit and loss in the ratio of 3:2:1 respectively. On January 1, 2025, their capitals were: Omar Tk. 6,80,000, Osman Tk. 4,80,000, and Oli Tk. 4,00,000. On July 1, Osman provided Tk. 1,60,000 as a loan to the business. Osman withdrew Tk. 60,000 in cash from the business on April 1. According to the agreement, Oli will get a salary of Tk. 8,000 per month for his full-time work. Oli withdraws his salary in cash. Omar will get a commission of 5% on the net profit of the business. Interest at 10% per annum is to be charged on the partners' capital, drawings, and loan. Omar and Osman jointly guaranteed Oli that Oli will receive at least Tk. 1,30,500 per year as his share of profit. After adjusting Oli's salary but before making other adjustments, the net profit of the business for the year ended December 31, 2025, amounted to Tk. 8,80,000.</p><p>Dhaka Commerce College · 2026</p>",
    "meta": "Dhaka Commerce College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of Omar's commission.",
            "answer": structured_cq["solutions"]["a"]
        },
        {
            "label": "b",
            "text": "Prepare the Partners' Profit and Loss Appropriation Account assuming Omar's commission is Tk. 40,000.",
            "answer": structured_cq["solutions"]["b"]
        },
        {
            "label": "c",
            "text": "Prepare the Capital Account for Omar and Osman. (Assuming divisible share of profit as Tk. 3,00,000 and Tk. 2,00,000 respectively)",
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
