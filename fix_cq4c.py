with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_answer = "\"<div class='space-y-3'><p class='text-[11px] font-bold underline'>Balance Sheet Presentation (Extract):</p><table class='w-full text-xs border border-gray-300'><thead><tr class='bg-gray-100'><th class='border p-1'>Assets</th><th class='border p-1'>Amount (Tk)</th><th class='border p-1'>Total (Tk)</th></tr></thead><tbody><tr><td class='border p-1 font-semibold'>Fixed Assets:</td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Machinery (1,00,000 + 1,00,000)</td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Less: Accumulated Depreciation</td><td class='border p-1 text-right italic underline'>(38,245)</td><td class='border p-1'></td></tr><tr><td class='border p-1 font-bold'>Net Book Value (Dec 31, 2024)</td><td class='border p-1'></td><td class='border p-1 text-right font-bold'>1,61,755</td></tr></tbody></table><p class='text-[10px] italic text-gray-500'>*Accumulated Depreciation = Opening (14,500) + 2023 (8,550) + 2024 (15,195).</p></div>\""

new_answer = '''"<div class='space-y-4 font-mono'>
  <div class='text-center space-y-1'>
    <p class='font-semibold text-[11px]'>Saikat Bros</p>
    <p class='font-semibold text-[11px]'>Statement of Financial Position (Extract)</p>
    <p class='text-[10px]'>As on 31 December, ...</p>
  </div>
  
  <div class='overflow-x-auto'>
    <table class='w-full text-[10px] border-collapse border border-gray-300'>
      <thead>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1 text-center'>Particulars</th>
          <th class='border border-gray-300 p-1 text-center w-1/5'>Tk.</th>
          <th class='border border-gray-300 p-1 text-center w-1/5'>Tk.</th>
          <th class='border border-gray-300 p-1 text-center w-1/5'>Tk.</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold'>Fixed Assets: (2023)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Machine</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>1,00,000</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Less: Accumulated Depreciation (14,500 + 8,550)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right border-b border-gray-400'>(23,050)</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold text-center'>Total Fixed Assets</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>76,950</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold'>Fixed Assets: (2024)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Machine (1,00,000 + 1,00,000)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>2,00,000</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Less: Accumulated Depreciation (23,050 + 15,195)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right border-b border-gray-400'>(38,245)</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold text-center'>Total Fixed Assets</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>1,61,755</td>
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
    print("Successfully replaced CQ4(c) answer!")
else:
    print("Could not find the exact old string. Checking for partial match.")
    idx = content.find("Balance Sheet Presentation (Extract):")
    if idx != -1:
        start_idx = content.rfind('"<div', 0, idx)
        end_idx = content.find('</div>"', idx) + len('</div>"')
        print(f"Found partial match from {start_idx} to {end_idx}")
        print(f"Old content snippet: {content[start_idx:end_idx]}")
