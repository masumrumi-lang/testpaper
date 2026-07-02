import sys

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old = "<div class='text-xs font-mono'><p>RB Rate = (100/10)&times;2 = 20%.</p><p>2023 Dep (6 mo) = 36,00,000 &times; 20% &times; 6/12 = 3,60,000.<br>2024 Dep = (36L - 3.6L) &times; 20% = 6,48,000.</p></div>"

new = "<div class='space-y-2 text-xs font-mono'><p>RB Rate = (100/10)&times;2 = <strong>20%</strong>.</p><p>2023 Dep (6 mo) = 36,00,000 &times; 20% &times; 6/12 = <strong>3,60,000</strong>.</p><p>2024 Dep = (36,00,000 - 3,60,000) &times; 20% = <strong>6,48,000</strong>.</p><div class='overflow-x-auto'><p class='font-semibold underline text-center'>Khan Ltd. &mdash; Journal Entries</p><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Account Title &amp; Explanation</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2023<br>July 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em>(Machine purchased including duty, carriage &amp; installation)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>36,00,000</td><td class='border p-1 text-right'><br>36,00,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C (Machine)<br><em>(Depreciation charged on machine)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'><br>3,60,000</td></tr><tr><td class='border p-1'>\" &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'><br>3,60,000</td></tr><tr><td class='border p-1'>2024<br>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C (Machine)<br><em>(Depreciation charged on machine)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'><br>6,48,000</td></tr><tr><td class='border p-1'>\" &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'><br>6,48,000</td></tr></tbody></table></div></div>"

count = content.count(old)
print(f'Found {count} occurrence(s)')
if count == 1:
    content = content.replace(old, new)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print('CQ3(b) replaced successfully!')
else:
    print('ERROR: unexpected count')
