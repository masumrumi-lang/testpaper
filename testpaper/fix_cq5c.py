with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_answer = "\"<div class='space-y-3'><p class='text-xs font-bold'>Balance Sheet (Extract) as of Dec 31, 2024:</p><table class='w-full text-xs border border-gray-400'><thead><tr class='bg-gray-100'><th class='border p-1'>Assets</th><th class='border p-1'>Taka</th><th class='border p-1'>Taka</th></tr></thead><tbody><tr><td class='border p-1'>Fixed Assets:</td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-3'>Machinery</td><td class='border p-1 text-right'>4,00,000</td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-3'>(-) Accumulated Depreciation</td><td class='border p-1 text-right underline'>(2,08,000)</td><td class='border p-1'></td></tr><tr><td class='border p-1 font-bold'>Net Asset Value</td><td class='border p-1'></td><td class='border p-1 text-right font-bold'>1,92,000</td></tr></tbody></table><div class='p-2 bg-emerald-50 text-[10px] border-l-4 border-emerald-400'><p><strong>Working:</strong> Accum. Dep = 80,000 (2023) + 1,28,000 (2024) = 2,08,000.</p></div></div>\""

new_answer = '''"<div class='space-y-4 font-mono'>
  <div class='text-center space-y-1'>
    <p class='font-semibold text-[11px]'>Ahnaf Traders</p>
    <p class='font-semibold text-[11px]'>Statement of Financial Position (Extract)</p>
    <p class='text-[10px]'>As on 31 December, .......</p>
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
          <td class='border border-gray-300 p-1 font-bold text-center'>Assets</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold'>Fixed Assets: (2023 Year)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Machinery</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>4,00,000</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Less: Accumulated Depreciation &minus; Machinery</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right border-b border-gray-400'>(80,000)</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold text-center'>Total Fixed Assets</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>3,20,000</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold mt-2'>Fixed Assets: (2024 Year)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Machinery</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right'>4,00,000</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 pl-4'>Less: Accumulated Depreciation &minus; Machinery (80,000 + 1,28,000)</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right border-b border-gray-400'>(2,08,000)</td>
          <td class='border border-gray-300 p-1'></td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 font-semibold text-center'>Total Fixed Assets</td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1 text-right font-bold' style='text-decoration: underline double;'>1,92,000</td>
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
    print("Successfully replaced CQ5(c) answer!")
else:
    print("Could not find the exact old string. Still...")
