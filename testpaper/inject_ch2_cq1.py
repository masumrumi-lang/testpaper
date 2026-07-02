import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Target: Chapter 2's empty fullCQData into Chapter 3 boundary
OLD = '''            shortCQData: [],
            fullCQData: []
        },
        "3": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 3 : Bank Reconciliation Statement",'''

NEW = '''            shortCQData: [],
            fullCQData: [
{
    id: 1,
    stem: "<p>The following transactions occurred in Mr. Habib's business in July 2024:</p><ul class='list-disc ml-6 mt-2 space-y-1 text-sm'><li>July 1: Started business with cash Tk 2,00,000, office equipment Tk 50,000, and a bank loan of Tk 40,000.</li><li>July 10: Provided services to a client for Tk 40,000, receiving Tk 30,000 in cash.</li><li>July 12: Purchased supplies for cash Tk 10,000.</li><li>July 15: Paid rent for two months, Tk 10,000.</li><li>July 24: Withdrew Tk 15,000 from the bank.</li><li>July 28: Paid half of the bank loan amount.</li><li>July 30: Supplies used amounted to Tk 6,000.</li><li>July 31: Paid monthly salary Tk 10,000.</li></ul>",
    meta: "Dhaka Board - 2025",
    type: "board",
    questions: [
        {
            label: "a",
            text: "Determine Mr. Habib's opening capital.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'><strong>Determination of Opening Capital</strong></p><p class='text-xs text-gray-500 italic text-center'>Opening Capital = Opening Assets &minus; Opening Liabilities</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left'>Particulars</th><th class='border border-gray-300 p-1 text-right'>Tk.</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1 pl-4 font-semibold' colspan='2'>Opening Assets:</td></tr><tr><td class='border border-gray-300 p-1 pl-8'>Cash</td><td class='border border-gray-300 p-1 text-right'>2,00,000</td></tr><tr><td class='border border-gray-300 p-1 pl-8'>Office Equipment</td><td class='border border-gray-300 p-1 text-right'>50,000</td></tr><tr><td class='border border-gray-300 p-1 pl-8'>Bank Balance (from loan deposited)</td><td class='border border-gray-300 p-1 text-right border-b border-gray-400'>40,000</td></tr><tr class='bg-gray-50'><td class='border border-gray-300 p-1 pl-4 font-semibold'>Total Opening Assets</td><td class='border border-gray-300 p-1 text-right font-semibold'>2,90,000</td></tr><tr><td class='border border-gray-300 p-1 pl-4 font-semibold' colspan='2'>Less: Opening Liabilities:</td></tr><tr><td class='border border-gray-300 p-1 pl-8'>Bank Loan</td><td class='border border-gray-300 p-1 text-right border-b border-gray-400'>40,000</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1 pl-4'>Opening Capital (2,90,000 &minus; 40,000)</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>Tk. 2,50,000</td></tr></tbody></table></div></div>"
        },
        {
            label: "b",
            text: "Show the impact of the transactions dated July 1, 10, 12, and 30 on the accounting equation in a tabular format.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Impact on Accounting Equation (A = L + OE)</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left' rowspan='2'>Date</th><th class='border border-gray-300 p-1 text-center' colspan='5'>Assets</th><th class='border border-gray-300 p-1 text-center'>=</th><th class='border border-gray-300 p-1 text-center'>Liabilities</th><th class='border border-gray-300 p-1 text-center'>+</th><th class='border border-gray-300 p-1 text-center'>Owner&rsquo;s Equity</th></tr><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-right'>Cash</th><th class='border border-gray-300 p-1 text-right'>Office Equip.</th><th class='border border-gray-300 p-1 text-right'>Bank</th><th class='border border-gray-300 p-1 text-right'>Accounts Receivable</th><th class='border border-gray-300 p-1 text-right'>Supplies</th><th class='border border-gray-300 p-1 text-center'>=</th><th class='border border-gray-300 p-1 text-right'>Bank Loan</th><th class='border border-gray-300 p-1 text-center'>+</th><th class='border border-gray-300 p-1 text-right'>Capital</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>July 1</td><td class='border border-gray-300 p-1 text-right'>2,00,000</td><td class='border border-gray-300 p-1 text-right'>50,000</td><td class='border border-gray-300 p-1 text-right'>40,000</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'>40,000</td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>2,50,000</td></tr><tr><td class='border border-gray-300 p-1'>July 10</td><td class='border border-gray-300 p-1 text-right'>30,000</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>40,000</td></tr><tr><td class='border border-gray-300 p-1'>July 12</td><td class='border border-gray-300 p-1 text-right'>(10,000)</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td></tr><tr><td class='border border-gray-300 p-1'>July 30</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-right'>(6,000)</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'>&mdash;</td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>(6,000)</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1'>Total</td><td class='border border-gray-300 p-1 text-right'>2,20,000</td><td class='border border-gray-300 p-1 text-right'>50,000</td><td class='border border-gray-300 p-1 text-right'>80,000</td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-right'>4,000</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'>40,000</td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>3,24,000</td></tr></tbody></table></div><p class='text-[10px] text-gray-500 italic mt-1'>*Total Assets: 2,20,000 + 50,000 + 80,000 + 10,000 + 4,000 = Tk. 3,64,000 = Total L + OE: 40,000 + 3,24,000 = Tk. 3,64,000 (Balanced)</p></div>"
        },
        {
            label: "c",
            text: "Provide journal entries for the transactions dated July 15, 24, 28, and 31.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Journal Entries of Mr. Habib</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left'>Date</th><th class='border border-gray-300 p-1 text-left'>Account Titles &amp; Explanations</th><th class='border border-gray-300 p-1'>L.F.</th><th class='border border-gray-300 p-1 text-right'>Debit (Tk)</th><th class='border border-gray-300 p-1 text-right'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1 align-top'>2024<br>July 15</td><td class='border border-gray-300 p-1 text-left'>Prepaid Rent A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Cash A/C<br><em class='text-[10px] text-gray-500'>(Being prepaid rent paid for two months)</em></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right align-top'>10,000</td><td class='border border-gray-300 p-1 text-right align-top'><br>10,000</td></tr><tr><td class='border border-gray-300 p-1 align-top'>&quot; 24</td><td class='border border-gray-300 p-1 text-left'>Cash A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class='text-[10px] text-gray-500'>(Being cash withdrawn from bank)</em></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right align-top'>15,000</td><td class='border border-gray-300 p-1 text-right align-top'><br>15,000</td></tr><tr><td class='border border-gray-300 p-1 align-top'>&quot; 28</td><td class='border border-gray-300 p-1 text-left'>Bank Loan A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class='text-[10px] text-gray-500'>(Being half of the bank loan repaid: 40,000 &divide; 2 = 20,000)</em></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right align-top'>20,000</td><td class='border border-gray-300 p-1 text-right align-top'><br>20,000</td></tr><tr><td class='border border-gray-300 p-1 align-top'>&quot; 31</td><td class='border border-gray-300 p-1 text-left'>Salary Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Cash A/C<br><em class='text-[10px] text-gray-500'>(Being monthly salary paid)</em></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right align-top'>10,000</td><td class='border border-gray-300 p-1 text-right align-top'><br>10,000</td></tr></tbody></table></div></div>"
        }
    ]
}
            ]
        },
        "3": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 3 : Bank Reconciliation Statement",'''

# Count occurrences first
count = content.count(OLD)
print(f"Occurrences of target string: {count}")

if count == 1:
    new_content = content.replace(OLD, NEW, 1)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: acc1_ch2_cq1 (Mr. Habib - Dhaka Board 2025) injected into data.js")
    
    # Verify
    verify_count = new_content.count('Habib')
    print(f"Verification - 'Habib' occurrences in data.js: {verify_count}")
else:
    print("ERROR: Target string not found or found multiple times. Aborting.")
