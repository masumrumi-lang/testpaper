import json

cq_obj = '''{
    id: 1,
    questionText: "Mr. Habib's business had the following transactions in July 2024:<br>July-1: Started business with cash 2,00,000 Tk, office equipment 50,000 Tk and a bank loan of 40,000 Tk.<br>July-10: Provided service of 40,000 Tk to a client and received 30,000 Tk.<br>July-12: Purchased supplies for cash 10,000 Tk.<br>July-15: Paid two months rent 10,000 Tk.<br>July-24: Withdrawn from bank 15,000 Tk.<br>July-28: Paid half of the bank loan.<br>July-30: Amount of used supplies is 6,000 Tk.<br>July-31: Monthly salary paid 10,000 Tk.",
    meta: "Dhaka Board - 2025",
    type: "board",
    questions: [
        {
            label: "a",
            text: "Determine Mr. Habib's opening capital.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Calculation of Opening Capital</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300 text-center'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Particulars</th><th class='border border-gray-300 p-1'>Amount (Tk)</th><th class='border border-gray-300 p-1'>Amount (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1 text-left pl-4'>Cash</td><td class='border border-gray-300 p-1 text-right'>2,00,000</td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1 text-left pl-4'>Office Equipment</td><td class='border border-gray-300 p-1 text-right border-b border-gray-400'>50,000</td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1 font-semibold text-center'>Opening Capital</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>2,50,000</td></tr></tbody></table></div><p class='text-[10px] text-gray-500 italic'>*Note: Bank loan is a liability, not part of owner's capital. Total cash on hand = 2,00,000 (Owner's) + 40,000 (Loan) = 2,40,000 Tk. But capital only includes owner's equity.</p></div>"
        },
        {
            label: "b",
            text: "Show the effect of transactions of July 1, 10, 12 and 30 on the accounting equation in a tabular format.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Effect on Accounting Equation (Tabular Format)</p><div class='overflow-x-auto'><table class='w-full text-[10px] border-collapse border border-gray-300 text-center'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1' rowspan='2'>Date (July)</th><th class='border border-gray-300 p-1' colspan='4'>Assets (A)</th><th class='border border-gray-300 p-1'>=</th><th class='border border-gray-300 p-1' colspan='2'>Liabilities (L) + Equity (E)</th><th class='border border-gray-300 p-1' rowspan='2'>Remarks</th></tr><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Cash</th><th class='border border-gray-300 p-1'>Office Eq.</th><th class='border border-gray-300 p-1'>Supplies</th><th class='border border-gray-300 p-1'>A/R</th><th class='border border-gray-300 p-1'>=</th><th class='border border-gray-300 p-1'>Bank Loan</th><th class='border border-gray-300 p-1'>Capital</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>1</td><td class='border border-gray-300 p-1 text-right'>2,40,000</td><td class='border border-gray-300 p-1 text-right'>50,000</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>40,000</td><td class='border border-gray-300 p-1 text-right'>2,50,000</td><td class='border border-gray-300 p-1 text-left'>Investment &amp; Loan</td></tr><tr><td class='border border-gray-300 p-1'>10</td><td class='border border-gray-300 p-1 text-right'>30,000</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>40,000</td><td class='border border-gray-300 p-1 text-left'>Service Rev</td></tr><tr><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>Bal</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>2,70,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>50,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'></td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>10,000</td><td class='border border-gray-300 p-1 bg-gray-50'></td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>40,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>2,90,000</td><td class='border border-gray-300 p-1 bg-gray-50'></td></tr><tr><td class='border border-gray-300 p-1'>12</td><td class='border border-gray-300 p-1 text-right'>(10,000)</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-left'></td></tr><tr><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>Bal</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>2,60,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>50,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>10,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>10,000</td><td class='border border-gray-300 p-1 bg-gray-50'></td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>40,000</td><td class='border border-gray-300 p-1 text-right font-semibold bg-gray-50'>2,90,000</td><td class='border border-gray-300 p-1 bg-gray-50'></td></tr><tr><td class='border border-gray-300 p-1'>30</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>(6,000)</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>(6,000)</td><td class='border border-gray-300 p-1 text-left'>Supplies Exp</td></tr><tr><td class='border border-gray-300 p-1 font-bold'>Total</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>2,60,000</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>50,000</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>4,000</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>10,000</td><td class='border border-gray-300 p-1 font-bold'>=</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>40,000</td><td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>2,84,000</td><td class='border border-gray-300 p-1'></td></tr></tbody></table></div></div>"
        },
        {
            label: "c",
            text: "Give journal entries for the transactions of July 15, 24, 28 and 31.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>General Journal</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300 text-center'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date (2024)</th><th class='border border-gray-300 p-1 text-left'>Account Titles &amp; Explanations</th><th class='border border-gray-300 p-1'>Ref.</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>July 15</td><td class='border border-gray-300 p-1 text-left pl-2'>Prepaid Rent A/C<br>&nbsp;&nbsp;Cash A/C<br><span class='text-[10px] italic text-gray-500'>(Paid two months rent in advance)</span></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-right'>10,000</td></tr><tr><td class='border border-gray-300 p-1'>July 24</td><td class='border border-gray-300 p-1 text-left pl-2'>Cash A/C<br>&nbsp;&nbsp;Bank A/C<br><span class='text-[10px] italic text-gray-500'>(Withdrawn from bank for business use)</span></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>15,000</td><td class='border border-gray-300 p-1 text-right'>15,000</td></tr><tr><td class='border border-gray-300 p-1'>July 28</td><td class='border border-gray-300 p-1 text-left pl-2'>Bank Loan A/C<br>&nbsp;&nbsp;Cash A/C<br><span class='text-[10px] italic text-gray-500'>(Paid half of bank loan)</span></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>20,000</td><td class='border border-gray-300 p-1 text-right'>20,000</td></tr><tr><td class='border border-gray-300 p-1'>July 31</td><td class='border border-gray-300 p-1 text-left pl-2'>Salary Exp A/C<br>&nbsp;&nbsp;Cash A/C<br><span class='text-[10px] italic text-gray-500'>(Paid monthly salary)</span></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>10,000</td><td class='border border-gray-300 p-1 text-right'>10,000</td></tr></tbody></table></div></div>"
        }
    ]
}'''

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
if start_idx != -1:
    ch2_idx = content.find('"2":', start_idx)
    if ch2_idx != -1:
        full_cq_idx = content.find('fullCQData: []', ch2_idx)
        if full_cq_idx != -1:
            # Replace empty array with our object in an array
            new_array_str = f"fullCQData: [\n{cq_obj}\n]"
            content = content[:full_cq_idx] + new_array_str + content[full_cq_idx + len('fullCQData: []'):]
            
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully inserted Chapter 2 CQ 1 into data.js!")
        else:
            print("fullCQData: [] not found exactly like that in Chapter 2. Let's find it flexibly.")
            full_cq_start = content.find('fullCQData:', ch2_idx)
            bracket_start = content.find('[', full_cq_start)
            bracket_end = content.find(']', bracket_start)
            if content[bracket_start+1:bracket_end].strip() == '':
                # It's an empty array with just whitespace
                new_array_str = f"[\n{cq_obj}\n]"
                content = content[:bracket_start] + new_array_str + content[bracket_end+1:]
                with open('data.js', 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Successfully inserted Chapter 2 CQ 1 into data.js (flexibly matched empty array)!")
            else:
                print("fullCQData in Chapter 2 is NOT empty. Contents:", content[bracket_start:bracket_end+1])
    else:
        print("Chapter 2 not found inside acc1")
else:
    print("acc1 not found")
