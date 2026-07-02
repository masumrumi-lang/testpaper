with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact block by locating id: "b1"
start_marker = '{\n        id: "b1",'
end_marker_search = "    },\n    {"  # end of CQ block followed by next CQ

start_idx = content.find(start_marker)
if start_idx < 0:
    # try with \r\n
    start_marker = '{\r\n        id: "b1",'
    end_marker_search = "    },\r\n    {"
    start_idx = content.find(start_marker)

print(f"Start index: {start_idx}")

if start_idx >= 0:
    # Find the closing of this CQ object: look for the pattern "    }\n" after "]\n    }\n"
    # We need to find "]\n    }" which closes the questions array and then the CQ object
    search_from = start_idx
    
    # Find the end of this specific CQ block
    # The pattern is:  ]\r\n    }\r\n or ]\n    }\n
    # followed by either a comma+next CQ or end of array
    
    # Let's extract the block character by character by tracking braces
    brace_depth = 0
    i = start_idx
    block_end = -1
    while i < len(content):
        if content[i] == '{':
            brace_depth += 1
        elif content[i] == '}':
            brace_depth -= 1
            if brace_depth == 0:
                block_end = i + 1
                break
        i += 1
    
    if block_end > 0:
        old_block = content[start_idx:block_end]
        print(f"Found block from {start_idx} to {block_end} ({len(old_block)} chars)")
        print(f"First 100 chars: {repr(old_block[:100])}")
        print(f"Last 100 chars: {repr(old_block[-100:])}")
        
        # Now build the replacement
        NEW = """{
        id: "b1",
        stem: "<p>On April 1, 2024, Mr. Abir started a repair business with cash of Tk 20,800 and equipment worth Tk 10,200. The following transactions were completed during the month:</p><ul class='list-disc ml-6 mt-2 space-y-1 text-sm'><li>April 2: Paid rent for two months, Tk 6,000.</li><li>April 3: Provided repair services: Cash Tk 19,800; on credit Tk 2,400.</li><li>April 6: Purchased supplies on credit, Tk 1,500.</li><li>April 9: Billed for repair services provided, Tk 2,000.</li><li>April 15: The owner withdrew Tk 2,000 from the business for personal use.</li><li>April 22: Received Tk 1,500 from accounts receivable.</li><li>April 25: Paid Tk 300 for entertainment expenses.</li><li>April 30: Supplies used during the month, Tk 800.</li></ul>",
        meta: "Rajshahi Board - 2025",
        type: "board",
        questions: [
            {
                label: "a",
                text: "Determine the amount of Accounts Receivable at the end of the month.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'><strong>Determination of Accounts Receivable at the End of the Month</strong></p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><tbody><tr><td class='border border-gray-300 p-1 text-left pl-4'>April 3: Repair services provided on credit</td><td class='border border-gray-300 p-1 text-right'>Tk. 2,400</td></tr><tr><td class='border border-gray-300 p-1 text-left pl-4'>April 9: Billed for repair services</td><td class='border border-gray-300 p-1 text-right'>Tk. 2,000</td></tr><tr class='bg-gray-50'><td class='border border-gray-300 p-1 text-left pl-4 font-semibold'>Total Receivable</td><td class='border border-gray-300 p-1 text-right font-semibold'>Tk. 4,400</td></tr><tr><td class='border border-gray-300 p-1 text-left pl-4'>April 22: Less: Received from Accounts Receivable</td><td class='border border-gray-300 p-1 text-right'>(Tk. 1,500)</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1 text-left pl-4'>Ending Accounts Receivable</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>Tk. 2,900</td></tr></tbody></table></div></div>"
            },
            {
                label: "b",
                text: "Show the classification of accounts for the transactions dated 2, 6, 15, and 30 according to the modern method.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Classification of Accounts (Modern Method)</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left'>Date</th><th class='border border-gray-300 p-1 text-left'>Related Accounts</th><th class='border border-gray-300 p-1 text-center'>Account Category</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1 align-top' rowspan='2'>April 2</td><td class='border border-gray-300 p-1'>Prepaid Rent A/C</td><td class='border border-gray-300 p-1 text-center'>Asset</td></tr><tr><td class='border border-gray-300 p-1'>Cash A/C</td><td class='border border-gray-300 p-1 text-center'>Asset</td></tr><tr><td class='border border-gray-300 p-1 align-top' rowspan='2'>April 6</td><td class='border border-gray-300 p-1'>Supplies A/C</td><td class='border border-gray-300 p-1 text-center'>Asset</td></tr><tr><td class='border border-gray-300 p-1'>Accounts Payable A/C</td><td class='border border-gray-300 p-1 text-center'>Liability</td></tr><tr><td class='border border-gray-300 p-1 align-top' rowspan='2'>April 15</td><td class='border border-gray-300 p-1'>Drawings A/C</td><td class='border border-gray-300 p-1 text-center'>Owner&apos;s Equity</td></tr><tr><td class='border border-gray-300 p-1'>Cash A/C</td><td class='border border-gray-300 p-1 text-center'>Asset</td></tr><tr><td class='border border-gray-300 p-1 align-top' rowspan='2'>April 30</td><td class='border border-gray-300 p-1'>Supplies Expense A/C</td><td class='border border-gray-300 p-1 text-center'>Expense</td></tr><tr><td class='border border-gray-300 p-1'>Supplies A/C</td><td class='border border-gray-300 p-1 text-center'>Asset</td></tr></tbody></table></div></div>"
            },
            {
                label: "c",
                text: "Show the impact of the transactions dated 1, 2, 3, 22, and 25 on the accounting equation using a tabular sheet.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Impact on Accounting Equation (Tabular Sheet)</p><p class='text-center text-[10px] text-gray-500'>Assets = Liabilities + Owner&apos;s Equity</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left'>Date (2024)</th><th class='border border-gray-300 p-1 text-right'>Cash (Tk)</th><th class='border border-gray-300 p-1 text-right'>Equipment (Tk)</th><th class='border border-gray-300 p-1 text-right'>Prepaid Rent (Tk)</th><th class='border border-gray-300 p-1 text-right'>A/R (Tk)</th><th class='border border-gray-300 p-1 text-center'>=</th><th class='border border-gray-300 p-1 text-right'>A/P (Tk)</th><th class='border border-gray-300 p-1 text-center'>+</th><th class='border border-gray-300 p-1 text-right'>Capital (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>April 1</td><td class='border border-gray-300 p-1 text-right'>20,800</td><td class='border border-gray-300 p-1 text-right'>10,200</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>31,000</td></tr><tr><td class='border border-gray-300 p-1'>April 2</td><td class='border border-gray-300 p-1 text-right'>(6,000)</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>6,000</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'></td></tr><tr><td class='border border-gray-300 p-1'>April 3</td><td class='border border-gray-300 p-1 text-right'>19,800</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>2,400</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>22,200</td></tr><tr><td class='border border-gray-300 p-1'>April 22</td><td class='border border-gray-300 p-1 text-right'>1,500</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'>(1,500)</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'></td></tr><tr><td class='border border-gray-300 p-1'>April 25</td><td class='border border-gray-300 p-1 text-right'>(300)</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right'>(300)</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1'>Total</td><td class='border border-gray-300 p-1 text-right'>35,800</td><td class='border border-gray-300 p-1 text-right'>10,200</td><td class='border border-gray-300 p-1 text-right'>6,000</td><td class='border border-gray-300 p-1 text-right'>900</td><td class='border border-gray-300 p-1 text-center'>=</td><td class='border border-gray-300 p-1 text-right'></td><td class='border border-gray-300 p-1 text-center'>+</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>52,900</td></tr></tbody></table></div><p class='text-[10px] text-gray-500 italic mt-1'>Final Balance: Total Assets (Tk 52,900) = Total Equity (Tk 52,900)</p></div>"
            }
        ]
    }"""
        
        new_content = content[:start_idx] + NEW + content[block_end:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("SUCCESS: acc1_ch1_cq1 (Rajshahi Board 2025 - Mr. Abir) updated in data.js")
        
        # Verify
        v1 = new_content.count('Rajshahi Board - 2025')
        v2 = new_content.count('Ending Accounts Receivable')
        v3 = new_content.count('52,900')
        print(f"Verification - 'Rajshahi Board - 2025': {v1}")
        print(f"Verification - 'Ending Accounts Receivable': {v2}")
        print(f"Verification - '52,900' (final balance): {v3}")
    else:
        print("ERROR: Could not find end of CQ block")
else:
    print("ERROR: Could not find id: b1 in data.js")
