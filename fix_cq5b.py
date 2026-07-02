with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_answer = "\"<p class='text-xs'>Standard ledgers closing to Income Summary (80k and 128k).</p>\""

new_answer = '''"<div class='space-y-4 font-mono'>
  <div class='text-center space-y-1'>
    <p class='font-semibold text-[11px]'>Ahnaf Traders</p>
    <p class='text-[10px]'>Ledger Book (Moving Balance Method)</p>
  </div>
  
  <div class='overflow-x-auto'>
    <table class='w-full text-[10px] border-collapse border border-gray-300'>
      <caption class='text-[11px] font-bold py-1 border-t border-l border-r border-gray-300 bg-sky-50'>Depreciation Account</caption>
      <thead>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1' rowspan='2'>Date</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Particulars</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Ref</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Debit (Tk)</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Credit (Tk)</th>
          <th class='border border-gray-300 p-1' colspan='2'>Balance</th>
        </tr>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1'>Debit (Tk)</th>
          <th class='border border-gray-300 p-1'>Credit (Tk)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class='border border-gray-300 p-1'>2023<br>Dec. 31</td>
          <td class='border border-gray-300 p-1'>Accumulated Depreciation A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
          <td class='border border-gray-300 p-1 text-center'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 text-center'>&quot; 31</td>
          <td class='border border-gray-300 p-1'>Income Summary A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
          <td class='border border-gray-300 p-1 text-center'>&minus;</td>
          <td class='border border-gray-300 p-1 text-center'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1'>2024<br>Dec. 31</td>
          <td class='border border-gray-300 p-1'>Accumulated Depreciation A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>1,28,000</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>1,28,000</td>
          <td class='border border-gray-300 p-1 text-center'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 text-center'>&quot; 31</td>
          <td class='border border-gray-300 p-1'>Income Summary A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>1,28,000</td>
          <td class='border border-gray-300 p-1 text-center'>&minus;</td>
          <td class='border border-gray-300 p-1 text-center'></td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <div class='overflow-x-auto'>
    <table class='w-full text-[10px] border-collapse border border-gray-300'>
      <caption class='text-[11px] font-bold py-1 border-t border-l border-r border-gray-300 bg-sky-50'>Accumulated Depreciation Account</caption>
      <thead>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1' rowspan='2'>Date</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Particulars</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Ref</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Debit (Tk)</th>
          <th class='border border-gray-300 p-1' rowspan='2'>Credit (Tk)</th>
          <th class='border border-gray-300 p-1' colspan='2'>Balance</th>
        </tr>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1'>Debit (Tk)</th>
          <th class='border border-gray-300 p-1'>Credit (Tk)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class='border border-gray-300 p-1'>2023<br>Dec. 31</td>
          <td class='border border-gray-300 p-1'>Depreciation A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1'>2024<br>Jan. 1</td>
          <td class='border border-gray-300 p-1'>Balance b/d</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>80,000</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1'>Dec. 31</td>
          <td class='border border-gray-300 p-1'>Depreciation A/C</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>1,28,000</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>2,08,000</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"'''

new_answer_stripped = new_answer.replace("\n", "").replace("  ", "")

if old_answer in content:
    content = content.replace(old_answer, new_answer_stripped)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced CQ5(b) answer!")
else:
    print("Could not find the exact old string. Checking for partial match.")
    idx = content.find("Standard ledgers closing to Income Summary")
    if idx != -1:
        start_idx = content.rfind('"<p', 0, idx)
        end_idx = content.find('</p>"', idx) + len('</p>"')
        print(f"Found partial match from {start_idx} to {end_idx}")
        print(f"Old content snippet: {content[start_idx:end_idx]}")
