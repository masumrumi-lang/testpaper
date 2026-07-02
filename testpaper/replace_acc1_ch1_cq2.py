
import sys

# Define the old block to match exactly
OLD_BLOCK = """    {
        id: "b2",
        stem: "<p>Mr. Jewel is a barrister. On January 1, 2024, he sold his personal savings certificate for 5,00,000 Taka and invested 3,00,000 Taka from it to start a law practice. His transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Rented an office for 20,000 Taka per month and paid two months' rent in advance.</li><li>Jan. 2: Appointed an office assistant at a monthly salary of 10,000 Taka.</li><li>Jan. 6: Provided legal services to a client worth 75,000 Taka and received 50,000 Taka in cash.</li><li>Jan. 20: Received 20,000 Taka in advance from another client for a legal service contract.</li><li>Jan. 25: Provided 10,000 Taka worth of service against the advance received.</li><li>Jan. 31: Paid January salary to the assistant and recorded one month's rent as an expense.</li></ul>",
        meta: "Chittagong · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of service revenue for Mr. Jewel in January.", 
                answer: "<div class='text-sm font-medium'>Revenue = 75,000 (Jan 6) + 10,000 (Jan 25) = <strong>85,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the above transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Total Equation (A = L + OE) = <strong>3,55,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for Mr. Jewel for the month of January.", 
                answer: "<div class='text-sm space-y-1'><p>Service Income: 85,000</p><p>(-) Salary Exp: (10,000)</p><p>(-) Rent Exp: (20,000)</p><p><strong>Net Profit = 55,000 Taka</strong></p></div>" 
            }
        ]
    },"""

# Define the new block with rich HTML
NEW_BLOCK = """    {
        id: "b2",
        stem: "<p><b>Chittagong Board 2025</b></p><p>Mr. Jewel is a barrister. On January 1, 2024, he sold his personal savings certificate for Tk 5,00,000 and started a legal business with Tk 3,00,000 from that amount. His transactions for the month of January were as follows:</p><ul class='list-disc ml-6 mt-2 space-y-1 text-sm'><li>Jan 1: Rented an office room at a monthly rent of Tk 20,000 and paid 2 months' rent in advance.</li><li>Jan 2: Appointed an office assistant at a monthly salary of Tk 10,000.</li><li>Jan 6: Provided legal services to a client for Tk 75,000; received Tk 50,000 in cash.</li><li>Jan 20: Received an advance of Tk 20,000 from another client for a legal service contract.</li><li>Jan 25: Provided legal services worth Tk 10,000 against the advance received earlier.</li><li>Jan 31: Paid the office assistant's salary for January and recorded one month's office rent as an expense.</li></ul>",
        meta: "Chittagong Board - 2025",
        type: "board",
        questions: [
            {
                label: "a",
                text: "Determine the total amount of service revenue for Mr. Jewel's legal business for the month of January.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'><strong>Total Service Revenue for January</strong></p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Particulars</th><th class='border border-gray-300 p-1 text-right'>Amount (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>Jan 6</td><td class='border border-gray-300 p-1'>Legal Services (Cash and Credit) provided</td><td class='border border-gray-300 p-1 text-right'>75,000</td></tr><tr><td class='border border-gray-300 p-1'>Jan 25</td><td class='border border-gray-300 p-1'>Earned portion of service revenue from advance</td><td class='border border-gray-300 p-1 text-right'>10,000</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1' colspan='2'>Total Service Revenue</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>85,000</td></tr></tbody></table></div></div>"
            },
            {
                label: "b",
                text: "Show the impact of the above transactions on the accounting equation using a tabular sheet.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'><strong>Impact on Accounting Equation (Tabular Sheet)</strong></p><div class='overflow-x-auto'><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Cash (Tk)</th><th class='border border-gray-300 p-1'>P. Rent</th><th class='border border-gray-300 p-1'>A/R</th><th class='border border-gray-300 p-1'>=</th><th class='border border-gray-300 p-1'>Unearned</th><th class='border border-gray-300 p-1'>+</th><th class='border border-gray-300 p-1'>Capital</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>Jan 1</td><td class='border border-gray-300 p-1'>3,00,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>3,00,000</td></tr><tr><td class='border border-gray-300 p-1'>Jan 1</td><td class='border border-gray-300 p-1'>(40,000)</td><td class='border border-gray-300 p-1'>40,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1'>Jan 6</td><td class='border border-gray-300 p-1'>50,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>25,000</td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>75,000</td></tr><tr><td class='border border-gray-300 p-1'>Jan 20</td><td class='border border-gray-300 p-1'>20,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'>20,000</td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1'>Jan 25</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'>(10,000)</td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>10,000</td></tr><tr><td class='border border-gray-300 p-1'>Jan 31</td><td class='border border-gray-300 p-1'>(10,000)</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>(10,000)</td></tr><tr><td class='border border-gray-300 p-1'>Jan 31</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>(20,000)</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>(20,000)</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1'>Total</td><td class='border border-gray-300 p-1'>3,20,000</td><td class='border border-gray-300 p-1'>20,000</td><td class='border border-gray-300 p-1'>25,000</td><td class='border border-gray-300 p-1'>=</td><td class='border border-gray-300 p-1'>10,000</td><td class='border border-gray-300 p-1'>+</td><td class='border border-gray-300 p-1'>3,55,000</td></tr></tbody></table></div><p class='text-center text-[10px] mt-1'>Final Balance: Total Assets (3,65,000) = Liabilities + Equity (3,65,000)</p></div>"
            },
            {
                label: "c",
                text: "Prepare an Income Statement for Mr. Jewel for the month of January.",
                answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'><strong>Income Statement (For the month ended January 31, 2024)</strong></p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Particulars</th><th class='border border-gray-300 p-1 text-right'>Details (Tk)</th><th class='border border-gray-300 p-1 text-right'>Amount (Tk)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1 font-semibold'>Revenues:</td><td></td><td></td></tr><tr><td class='border border-gray-300 p-1 pl-4'>Total Service Revenue (from part 'a')</td><td></td><td class='border border-gray-300 p-1 text-right'>85,000</td></tr><tr><td class='border border-gray-300 p-1 font-semibold'>Less: Expenses:</td><td></td><td></td></tr><tr><td class='border border-gray-300 p-1 pl-4'>Rent Expense</td><td class='border border-gray-300 p-1 text-right'>20,000</td><td></td></tr><tr><td class='border border-gray-300 p-1 pl-4'>Salary Expense</td><td class='border border-gray-300 p-1 text-right border-b border-gray-400'>10,000</td><td class='border border-gray-300 p-1 text-right'>(30,000)</td></tr><tr class='bg-amber-50 font-bold'><td class='border border-gray-300 p-1'>Net Profit</td><td></td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>55,000</td></tr></tbody></table></div></div>"
            }
        ]
    },"""

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

if OLD_BLOCK in content:
    new_content = content.replace(OLD_BLOCK, NEW_BLOCK)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: acc1_ch1_cq2 (Chittagong Board 2025) updated successfully.")
else:
    # Try a more flexible match if exact failed (e.g. whitespace differences)
    print("Exact match failed. Attempting flexible match.")
    # We know id: "b2" is at line 1764 and the block ends at 1785
    # Let's find by ID and then braces
    import re
    match = re.search(r'id:\s*"b2",', content)
    if match:
        start_pos = content.rfind('{', 0, match.start())
        # find closing brace
        brace_depth = 0
        end_pos = -1
        for i in range(start_pos, len(content)):
            if content[i] == '{': brace_depth += 1
            elif content[i] == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    end_pos = i + 1
                    break
        if end_pos > 0:
            # Check if there is a trailing comma
            if content[end_pos] == ',':
                end_pos += 1
            
            # Reconstruct
            new_content = content[:start_pos] + NEW_BLOCK + content[end_pos:]
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("SUCCESS: acc1_ch1_cq2 updated via flexible matching.")
        else:
            print("ERROR: Could not find end of block.")
    else:
        print("ERROR: Could not find id: 'b2' in data.js")
