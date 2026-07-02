import json
import re

# 1. Structured CQ Object requested by user
structured_cq = {
  "chapter": "Accounting 2nd Paper Chapter 2",
  "question_id": "acc2_ch2_cq1_college",
  "stimulus": "Achhia, Sonia, and Samia are three partners in a partnership business. They share the profits and losses of the business in the ratio of 3:2:1 respectively. On January 1, 2022, their capitals were Tk. 80,000, Tk. 60,000, and Tk. 50,000 respectively. According to the agreement, 10% interest per annum is to be charged on the partners' capital and drawings. Sonia will get a salary of Tk. 1,500 per month for participating in the management of the business. In the middle of that year, Samia provided a loan of Tk. 10,000 to the business. For personal use, Achhia withdrew Tk. 600 in cash at the beginning of each month, Sonia Tk. 500 in the middle of each month, and Samia Tk. 400 at the end of each month. In addition to cash withdrawals, Achhia also withdrew goods worth Tk. 2,500 which was not recorded in the books. Before making the above adjustments but after debiting Sonia's salary, the net profit of the business for the year ended December 31, 2022, amounted to Tk. 65,150.<br><strong>Notre Dame College - 2026</strong>",
  "requirements": {
    "a": "Determine the amount of interest on partners' drawings.",
    "b": "Prepare the partners' Profit and Loss Appropriation Account for the year ended.",
    "c": "Prepare the Capital Accounts of Achhia and Sonia. [Share of profit Achhia Tk. 24,630 and Sonia Tk. 16,420]",
    "d": ""
  },
  "solutions": {
    "a": "<p><strong>Calculation of the amount of interest on partners' drawings:</strong><br>Interest on Achhia's drawings = 600 &times; 10% &times; 6.5 = Tk. 390<br>Interest on Sonia's drawings = 500 &times; 10% &times; 6 = Tk. 300<br>Interest on Samia's drawings = 400 &times; 10% &times; 5.5 = Tk. 220</p><p><strong>Answer:</strong> Interest on drawings: Achhia Tk. 390; Sonia Tk. 300 and Samia Tk. 220.</p>",
    "b": "<div style=\"text-align: center;\"><p><strong>Achhia, Sonia, and Samia<br>Profit and Loss Appropriation Account<br>For the year ended December 31, 2022</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"2\" style=\"text-align: left;\">Debit</th><th colspan=\"2\" style=\"text-align: right;\">Credit</th></tr><tr><th>Particulars</th><th>Tk.</th><th>Particulars</th><th>Tk.</th></tr><tr><td><strong>Partners' Capital A/c:</strong><br>(Interest on Capital)<br>Achhia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8,000<br>Sonia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6,000<br>Samia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>5,000</u></td><td style=\"vertical-align: bottom;\">19,000</td><td><strong>Profit and Loss A/c:</strong><br>Net Profit</td><td style=\"vertical-align: top;\">65,150</td></tr><tr><td><strong>Samia's Loan A/c:</strong><br>Interest on Loan</td><td style=\"vertical-align: bottom;\">300</td><td><strong>Partners' Capital A/c:</strong><br>(Interest on Drawings)<br>Achhia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 390<br>Sonia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 300<br>Samia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>220</u></td><td style=\"vertical-align: bottom;\">910</td></tr><tr><td><strong>Partners' Capital A/c:</strong><br>(Share of Profit)<br>Achhia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 24,630<br>Sonia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16,420<br>Samia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>8,210</u></td><td style=\"vertical-align: bottom;\">49,260</td><td><strong>Achhia's Capital A/c:</strong><br>Drawings of Goods</td><td style=\"vertical-align: top;\">2,500</td></tr><tr><td></td><td><strong><u>68,560</u></strong></td><td></td><td><strong><u>68,560</u></strong></td></tr></table></div><p><strong>Answer:</strong> Share of Profit: Achhia Tk. 24,630; Sonia Tk. 16,420; Samia Tk. 8,210.</p>",
    "c": "<div style=\"text-align: center;\"><p><strong>Partners' Capital Account</strong></p></div><div class=\"table-responsive overflow-x-auto\"><table><tr><th colspan=\"4\" style=\"text-align: left;\">Debit</th><th colspan=\"4\" style=\"text-align: right;\">Credit</th></tr><tr><th>Date</th><th>Particulars</th><th>Achhia (Tk.)</th><th>Sonia (Tk.)</th><th>Date</th><th>Particulars</th><th>Achhia (Tk.)</th><th>Sonia (Tk.)</th></tr><tr><td>2022<br>Dec 31</td><td>Drawings A/c</td><td>7,200</td><td>6,000</td><td>2022<br>Jan 1</td><td>Balance b/d</td><td>80,000</td><td>60,000</td></tr><tr><td>\" 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Drawings</td><td>390</td><td>300</td><td>Dec 31</td><td><strong>Profit &amp; Loss App. A/c:</strong><br>Interest on Capital</td><td>8,000</td><td>6,000</td></tr><tr><td></td><td>Goods Drawings</td><td>2,500</td><td></td><td></td><td>Share of Profit</td><td>24,630</td><td>16,420</td></tr><tr><td>\" 31</td><td>Balance c/d</td><td>1,02,540</td><td>94,120</td><td></td><td>Salary</td><td></td><td>18,000</td></tr><tr><td></td><td></td><td><strong><u>1,12,630</u></strong></td><td><strong><u>1,00,420</u></strong></td><td></td><td></td><td><strong><u>1,12,630</u></strong></td><td><strong><u>1,00,420</u></strong></td></tr><tr><td></td><td></td><td></td><td></td><td>2023<br>Jan 1</td><td>Balance b/d</td><td>1,02,540</td><td>94,120</td></tr></table></div>",
    "d": ""
  },
  "tables": []
}

with open('extracted_cq.json', 'w', encoding='utf-8') as f:
    json.dump(structured_cq, f, indent=2, ensure_ascii=False)

# 2. Convert to application schema and inject into data.js
new_cq_app_schema = {
    "id": "acc2_ch2_cq1_college",
    "stem": "<p>Achhia, Sonia, and Samia are three partners in a partnership business. They share the profits and losses of the business in the ratio of 3:2:1 respectively. On January 1, 2022, their capitals were Tk. 80,000, Tk. 60,000, and Tk. 50,000 respectively. According to the agreement, 10% interest per annum is to be charged on the partners' capital and drawings. Sonia will get a salary of Tk. 1,500 per month for participating in the management of the business. In the middle of that year, Samia provided a loan of Tk. 10,000 to the business. For personal use, Achhia withdrew Tk. 600 in cash at the beginning of each month, Sonia Tk. 500 in the middle of each month, and Samia Tk. 400 at the end of each month. In addition to cash withdrawals, Achhia also withdrew goods worth Tk. 2,500 which was not recorded in the books. Before making the above adjustments but after debiting Sonia's salary, the net profit of the business for the year ended December 31, 2022, amounted to Tk. 65,150.</p><p>Notre Dame College · 2026</p>",
    "meta": "Notre Dame College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of interest on partners' drawings.",
            "answer": structured_cq["solutions"]["a"]
        },
        {
            "label": "b",
            "text": "Prepare the partners' Profit and Loss Appropriation Account for the year ended.",
            "answer": structured_cq["solutions"]["b"]
        },
        {
            "label": "c",
            "text": "Prepare the Capital Accounts of Achhia and Sonia. [Share of profit Achhia Tk. 24,630 and Sonia Tk. 16,420]",
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
        # We need to find the matching closing bracket
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
            # We want to insert the new CQ at the end of the array.
            # Find the last element by looking backward from close_idx
            # Wait, easier way: just insert right before close_idx with a comma
            
            # Check if the array is empty
            inner_content = content[start_search:close_idx].strip()
            
            json_str = json.dumps(new_cq_app_schema, indent=4, ensure_ascii=False)
            lines = json_str.split('\n')
            indented_lines = ['                ' + line for line in lines]
            formatted_json = '\n'.join(indented_lines)
            
            if inner_content == "":
                new_val = '\n' + formatted_json + '\n            '
                new_content = content[:start_search] + new_val + content[close_idx:]
            else:
                # Find the last closing brace of the last object
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
