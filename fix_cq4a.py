with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_answer = "\"<div class='text-xs font-mono'><p><strong>2023:</strong> (1,00,000 - 14,500) &times; 10% = 8,550.</p><p><strong>2024:</strong><br>M1: (85,500 - 8,550) &times; 10% = 7,695.<br>M2: 1,00,000 &times; 10% &times; 9/12 = 7,500.<br>Total = 15,195.</p></div>\""

new_answer = '''"<div class='space-y-2 text-xs font-mono'>
  <p class='font-semibold underline text-center'>Calculation of Depreciation for 2023 &amp; 2024</p>
  <div class='overflow-x-auto'>
    <table class='w-full text-[10px] border-collapse border border-gray-300 text-center'>
      <thead>
        <tr class='bg-gray-100'>
          <th class='border border-gray-300 p-1'>Year</th>
          <th class='border border-gray-300 p-1'>Opening Value (Tk)</th>
          <th class='border border-gray-300 p-1'>Dep. Rate</th>
          <th class='border border-gray-300 p-1'>Annual Dep. (Tk)</th>
          <th class='border border-gray-300 p-1'>Accum. Dep. (Tk)</th>
          <th class='border border-gray-300 p-1'>Closing Value (Tk)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class='border border-gray-300 p-1'>2023</td>
          <td class='border border-gray-300 p-1'>85,500</td>
          <td class='border border-gray-300 p-1'>10%</td>
          <td class='border border-gray-300 p-1'>8,550</td>
          <td class='border border-gray-300 p-1'>23,050</td>
          <td class='border border-gray-300 p-1'>76,950</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1 align-top' rowspan='3'>2024</td>
          <td class='border border-gray-300 p-1'>76,950</td>
          <td class='border border-gray-300 p-1 align-middle' rowspan='3'>10%</td>
          <td class='border border-gray-300 p-1'>7,695</td>
          <td class='border border-gray-300 p-1 align-middle' rowspan='3'>38,245</td>
          <td class='border border-gray-300 p-1'>69,255</td>
        </tr>
        <tr>
          <td class='border border-gray-300 p-1'>1,00,000 (9 mo)</td>
          <td class='border border-gray-300 p-1 border-b border-gray-400'>7,500</td>
          <td class='border border-gray-300 p-1 border-b border-gray-400'>92,500</td>
        </tr>
        <tr class='font-bold'>
          <td class='border border-gray-300 p-1'></td>
          <td class='border border-gray-300 p-1' style='text-decoration: underline double;'>15,195</td>
          <td class='border border-gray-300 p-1' style='text-decoration: underline double;'>1,61,755</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class='text-[9px] text-gray-500 text-left'>*Note: In 2023, Machine Opening Value = (1,00,000 &minus; 14,500) = 85,500 Tk; Accumulated Depreciation = (14,500 + 8,550) = 23,050 Tk.</p>
</div>"'''

# strip newlines inside new_answer to not break JSON string format
new_answer_stripped = new_answer.replace("\n", "").replace("  ", "")

if old_answer in content:
    content = content.replace(old_answer, new_answer_stripped)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced CQ4(a) answer!")
else:
    print("Could not find the exact old string. Let me know the content.")
