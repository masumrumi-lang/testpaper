with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_answer = "\"<div class='text-xs font-mono'><p>Rate = (100/5)&times;2 = 40%.</p><p>2023 Dep (6 mo): 4,00,000 &times; 40% &times; 6/12 = 80,000.</p><p>2024 Dep: (4,00,000 - 80,000) &times; 40% = 1,28,000.</p></div>\""

new_answer = '''"<div class='space-y-4 text-xs font-mono'>
  <p class='font-semibold underline text-center'>Calculation of Depreciation for 2023 &amp; 2024</p>
  <div class='overflow-x-auto'>
    <table class='w-full text-[10px] border-collapse border border-gray-300 text-center'>
      <thead>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1'>Year</th>
          <th class='border border-gray-300 p-1'>Opening Value (Tk)</th>
          <th class='border border-gray-300 p-1'>Time</th>
          <th class='border border-gray-300 p-1'>Dep. Rate</th>
          <th class='border border-gray-300 p-1'>Annual Dep. (Tk)</th>
          <th class='border border-gray-300 p-1'>Accum. Dep. (Tk)</th>
          <th class='border border-gray-300 p-1'>Closing Value (Tk)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class='border border-gray-300 p-1'>2023</td>
          <td class='border border-gray-300 p-1'>4,00,000</td>
          <td class='border border-gray-300 p-1'>6 months</td>
          <td class='border border-gray-300 p-1'>40%</td>
          <td class='border border-gray-300 p-1'>80,000</td>
          <td class='border border-gray-300 p-1'>80,000</td>
          <td class='border border-gray-300 p-1'>3,20,000</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1'>2024</td>
          <td class='border border-gray-300 p-1'>3,20,000</td>
          <td class='border border-gray-300 p-1'>1 year</td>
          <td class='border border-gray-300 p-1'>40%</td>
          <td class='border border-gray-300 p-1'>1,28,000</td>
          <td class='border border-gray-300 p-1'>2,08,000</td>
          <td class='border border-gray-300 p-1'>1,92,000</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class='flex justify-center items-center mt-2'>
    <span class='mr-2 text-[9px]'>*Here, Dep. Rate under Reducing Balance Method =</span>
    <div class='inline-flex flex-col items-center mx-1'>
      <span class='border-b border-gray-800 leading-tight px-1'>100%</span>
      <span class='leading-tight px-1'>Estimated Life</span>
    </div>
    <span class='mx-1'>&times; 2 =</span>
    <div class='inline-flex flex-col items-center mx-1'>
      <span class='border-b border-gray-800 leading-tight px-1'>100%</span>
      <span class='leading-tight px-1'>5</span>
    </div>
    <span class='ml-1'>&times; 2 = 40%</span>
  </div>
</div>"'''

new_answer_stripped = new_answer.replace("\n", "").replace("  ", "")

if old_answer in content:
    content = content.replace(old_answer, new_answer_stripped)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced CQ5(a) answer!")
else:
    print("Could not find the exact old string. Checking for partial match.")
    idx = content.find("Rate = (100/5)&times;2 = 40%.")
    if idx != -1:
        start_idx = content.rfind('"<div', 0, idx)
        end_idx = content.find('</div>"', idx) + len('</div>"')
        print(f"Found partial match from {start_idx} to {end_idx}")
        print(f"Old content snippet: {content[start_idx:end_idx]}")
