import json
import re

file_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Transcribed and Translated Questions from the image
new_full_cq = [
    {
        "id": "b01",
        "stem": "<p>Alfa Company Ltd. purchased a machine on January 1, 2020, for 1,80,000 TK and incurred 5,000 TK and 15,000 TK for its transportation and installation respectively. The estimated useful life of the machine is 10 years, and its salvage value at the end of its life is estimated to be 20,000 TK. The company decided to charge depreciation at a rate of 10% using the straight-line method and close its accounts on December 31 each year.</p>",
        "meta": "Dhaka Board · 2024",
        "type": "board",
        "questions": [
            {
                "label": "a",
                "text": "Determine the depreciable cost and annual depreciation of the machine.",
                "answer": "<div class='text-sm space-y-1'><p><strong>Depreciable Cost:</strong> (1,80,000 + 5,000 + 15,000) - 20,000 = <strong>1,80,000 TK</strong></p><p><strong>Annual Depreciation:</strong> 2,00,000 × 10% = <strong>20,000 TK</strong></p></div>"
            },
            {
                "label": "b",
                "text": "Prepare the journal entries related to machine purchase and depreciation for the first three years.",
                "answer": "<div class='text-xs space-y-1'><p>1. <strong>Jan 1:</strong> Machinery A/C Dr 2,00,000; Cash A/C Cr 2,00,000</p><p>2. <strong>Dec 31:</strong> Depreciation Expense Dr 20,000; Accumulated Depreciation Cr 20,000</p><p>3. <strong>Dec 31:</strong> Income Summary Dr 20,000; Depreciation Expense Cr 20,000</p><p class='italic'>(Note: Repeat depreciation journals for years 2 and 3)</p></div>"
            },
            {
                "label": "c",
                "text": "Prepare the Machine Account and Depreciation Account (for the first three years).",
                "answer": "<div class='text-xs space-y-2'><p><strong>Machine Account:</strong> Constant balance of 2,00,000 TK (Debit) for all 3 years.</p><p><strong>Depreciation Account:</strong> Debited with 20,000 TK (Acc. Dep) and Credited with 20,000 TK (Income Summary) each year, closing with zero balance.</p></div>"
            }
        ]
    },
    {
        "id": "b02",
        "stem": "<p>Mr. Jamal started a service-oriented business on January 1, 2022. On December 31, his trial balance was as follows: Cash 1,20,000 TK; Supplies 20,000 TK; Insurance Expense 20,000 TK; Fixed Assets 3,50,000 TK; Capital 1,50,000 TK; Unearned Service Revenue 64,000 TK; Service Revenue 1,53,000 TK; Accounts Payable 20,000 TK.</p><p><strong>Other Information:</strong></p><ul class='list-disc ml-6 mt-2'><li>Service provided for 10,000 TK which has not been recorded.</li><li>Supplies used 5,000 TK.</li><li>Insurance expense unexpired 15,000 TK.</li><li>Charge 10% depreciation on fixed assets.</li></ul>",
        "meta": "Rajshahi Board · 2023",
        "type": "board",
        "questions": [
            {
                "label": "a",
                "text": "Determine the amount of total service revenue.",
                "answer": "<div class='text-sm font-medium'>Total Revenue = 1,53,000 + 10,000 = <strong>1,63,000 TK</strong></div>"
            },
            {
                "label": "b",
                "text": "Provide the necessary adjusting entries.",
                "answer": "<div class='text-xs space-y-1'><p>1. A/R Dr 10,000; Service Revenue Cr 10,000</p><p>2. Supplies Expense Dr 5,000; Supplies Cr 5,000</p><p>3. Prepaid Insurance Dr 15,000; Insurance Expense Cr 15,000</p><p>4. Depreciation Expense Dr 35,000; Accumulated Depreciation Cr 35,000</p></div>"
            },
            {
                "label": "c",
                "text": "Prepare a 10-column worksheet.",
                "answer": "<div class='text-sm'>The worksheet will adjust the trial balance using the entries in part (b). Net Income = Total Revenue (1,63,000) - Expenses (Insurance 5,000 + Supplies 5,000 + Depreciation 35,000) = 1,18,000 TK.</div>"
            }
        ]
    },
    {
        "id": "b03",
        "stem": "<p>On January 1, 2018, the following information was found in Arpita Company's statement of financial position: Allowance for Bad Debts 2,000 TK; Accounts Receivable 24,000 TK.</p><p><strong>Transactions in 2018:</strong></p><ul class='list-disc ml-6 mt-2'><li>Credit Sales: 80,000 TK.</li><li>Collection from Accounts Receivable: 70,000 TK.</li><li>Bad debts to be written off: 2,500 TK.</li><li>New Allowance for Bad Debts: 5,000 TK.</li></ul>",
        "meta": "Chittagong Board · 2019",
        "type": "board",
        "questions": [
            {
                "label": "a",
                "text": "Determine the amount of bad debt expense for the year 2018.",
                "answer": "<div class='text-sm font-medium'>Bad Debt Expense = 2,500 (written off) + 5,000 (New) - 2,000 (Old) = <strong>5,500 TK</strong></div>"
            },
            {
                "label": "b",
                "text": "Give the journal entries for the above transactions.",
                "answer": "<div class='text-xs space-y-1'><p>1. A/R Dr 80,000; Sales Cr 80,000</p><p>2. Cash Dr 70,000; A/R Cr 70,000</p><p>3. Allowance for Bad Debts Dr 2,500; A/R Cr 2,500</p><p>4. Bad Debt Expense Dr 5,500; Allowance for Bad Debts Cr 5,500</p></div>"
            },
            {
                "label": "c",
                "text": "Prepare the Allowance for Bad Debts Account and Accounts Receivable Account.",
                "answer": "<div class='text-xs space-y-2'><p><strong>Allowance for Bad Debts:</strong> Balance b/d 2,000 (Cr); Debit: A/R 2,500; Credit: Bad Debt Exp 5,500; Balance c/d 5,000 (Cr).</p><p><strong>Accounts Receivable:</strong> Balance b/d 24,000; Debit: Sales 80,000; Credit: Cash 70,000, Allowance 2,500; Balance c/d 31,500.</p></div>"
            }
        ]
    }
]

# Locate acc1 section
acc1_match = re.search(r'["\']acc1["\']:\s*\{', content)
if not acc1_match:
    print("Could not find acc1")
    exit(1)
acc1_start = acc1_match.start()

# Locate Chapter 6 in acc1
ch6_match = re.search(r'["\']6["\']:\s*\{', content[acc1_start:])
if not ch6_match:
    print("Could not find Chapter 6 in acc1")
    exit(1)
ch6_start = acc1_start + ch6_match.start()

# Find the end of Chapter 6 (start of Chapter 7)
ch7_match = re.search(r'["\']7["\']:\s*\{', content[ch6_start:])
if not ch7_match:
    print("Could not find Chapter 7 in acc1")
    exit(1)
ch6_end = ch6_start + ch7_match.start()

# Extract the existing mcqData from Chapter 6
# We need to find the block between ch6_start and ch6_end that is mcqData
mcq_match = re.search(r'mcqData:\s*\[(.*?)\n\s*\]\s*,', content[ch6_start:ch6_end], re.DOTALL)
if not mcq_match:
    print("Could not find mcqData in Chapter 6")
    exit(1)
mcq_content = mcq_match.group(1)

# Reconstruct the clean Chapter 6 block
full_cq_json = json.dumps(new_full_cq, indent=8, ensure_ascii=False).replace('\n', '\n    ')

clean_ch6 = f'''"6": {{
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 6 : Accounting for Receivables (Out of Short Syllabus)",
            mcqData: [{mcq_content}
            ],
            shortCQData: [],
            fullCQData: {full_cq_json}
        }},
        '''

# Replace the corrupted block
new_content = content[:ch6_start] + clean_ch6 + content[ch6_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully cleaned up and replaced Chapter 6")
