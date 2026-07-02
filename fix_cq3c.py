with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find CQ3 part c answer - it's the one with "Ledger Extracts for Khan Ltd. (2023-2025)"
old = "<div class='space-y-4'><p class='text-[11px] font-bold'>Ledger Extracts for Khan Ltd. (2023-2025):</p>"

idx = content.find(old)
print(f'Found CQ3(c) start at: {idx}')

if idx > 0:
    # Find the full answer string boundaries
    # Go back to find answer: "
    ans_start = content.rfind('answer: "', max(0, idx-100), idx)
    print(f'answer: " starts at: {ans_start}')
    
    # Find the closing quote of this answer string
    # Starting from idx, find the pattern: </div>"
    # But we need the LAST </div>" that closes the answer
    search_start = idx
    pos = search_start
    last_close = -1
    while True:
        next_close = content.find('</div>"', pos)
        if next_close == -1 or next_close > idx + 5000:
            break
        last_close = next_close
        pos = next_close + 1
    
    if last_close > 0:
        ans_end = last_close + len('</div>"')
        print(f'Answer ends at: {ans_end}')
        
        old_answer = content[ans_start:ans_end]
        print(f'Old answer length: {len(old_answer)}')
        print(f'Old answer preview: {old_answer[:200]}...')
        print(f'Old answer tail: ...{old_answer[-100:]}')
        
        # Build the new answer
        new_answer = '''answer: "<div class='space-y-4'><p class='text-[11px] font-bold'>Khan Ltd. Ledger (2023-2025):</p><div class='overflow-x-auto'><table class='w-full text-[10px] border border-gray-300'><caption class='text-[11px] font-bold py-1 bg-sky-50 border border-gray-300'>Depreciation Account</caption><thead><tr class='bg-gray-100'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Ref</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1' colspan='2'>Balance</th></tr></thead><tbody><tr><td class='border p-1'>2023<br>Dec. 31</td><td class='border p-1'>Accumulated Depreciation A/C</td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1'>Dr</td></tr><tr><td class='border p-1'>&quot; 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'>&ndash;</td><td class='border p-1'></td></tr><tr><td class='border p-1'>2024<br>Dec. 31</td><td class='border p-1'>Accumulated Depreciation A/C</td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1'>Dr</td></tr><tr><td class='border p-1'>&quot; 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'>&ndash;</td><td class='border p-1'></td></tr><tr><td class='border p-1'>2025<br>Dec. 31</td><td class='border p-1'>Accumulated Depreciation A/C</td><td class='border p-1'></td><td class='border p-1 text-right'>5,18,400</td><td class='border p-1'></td><td class='border p-1 text-right'>5,18,400</td><td class='border p-1'>Dr</td></tr><tr><td class='border p-1'>&quot; 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>5,18,400</td><td class='border p-1 text-right'>&ndash;</td><td class='border p-1'></td></tr></tbody></table></div><div class='overflow-x-auto'><table class='w-full text-[10px] border border-gray-300'><caption class='text-[11px] font-bold py-1 bg-sky-50 border border-gray-300'>Accumulated Depreciation Account</caption><thead><tr class='bg-gray-100'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Ref</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1' colspan='2'>Balance</th></tr></thead><tbody><tr><td class='border p-1'>2023<br>Dec. 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1'>Cr</td></tr><tr><td class='border p-1'>2024<br>Jan. 1</td><td class='border p-1'>Balance b/d</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1'>Cr</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'>10,08,000</td><td class='border p-1'>Cr</td></tr><tr><td class='border p-1'>2025<br>Jan. 1</td><td class='border p-1'>Balance b/d</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>10,08,000</td><td class='border p-1'>Cr</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>5,18,400</td><td class='border p-1 text-right font-bold'>15,26,400</td><td class='border p-1 font-bold'>Cr</td></tr></tbody></table></div><p class='text-[9px] text-gray-500'>*2025 Dep = (36,00,000 &minus; 3,60,000 &minus; 6,48,000) &times; 20% = 5,18,400.</p></div>"'''
        
        content = content[:ans_start] + new_answer + content[ans_end:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print('CQ3(c) replaced successfully!')
    else:
        print('ERROR: Could not find answer end')
else:
    print('ERROR: Could not find CQ3(c)')
