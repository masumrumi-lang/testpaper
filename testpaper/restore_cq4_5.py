with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The CQ3(c) answer now ends with: </div>"\n
# After that it goes directly to CQ5 part (b): label: "b", text: "Prepare Dep A/C..."
# We need to insert: CQ3 closing + CQ4 + CQ5 opening + CQ5(a)

# Find the insertion point
marker = '''</div>"\n            },\n            {\n                label: "b",\n                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",\n                answer: "<p class='text-xs'>Standard ledgers closing to Income Summary (80k and 128k).</p>"'''

idx = content.find(marker)
print(f'Found insertion point at: {idx}')

if idx > 0:
    # We need to insert AFTER the </div>" but BEFORE the CQ5 part(b)
    insert_point = idx + len('</div>"')
    
    missing_content = '''
            }
        ]
    },
    {
        id: 4,
        stem: "<p>On Jan 1, 2023, Saikat Bros Machine balance: 1,00,000 and Accum. Dep: 14,500. On Apr 1, 2024, bought another for 70,000 and spent 30,000 for installation. 10% Reducing Balance method is used.</p>",
        meta: "Notre Dame College \u00b7 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Calculate depreciation for 2023 and 2024.",
                answer: "<div class='text-xs font-mono'><p><strong>2023:</strong> (1,00,000 - 14,500) &times; 10% = 8,550.</p><p><strong>2024:</strong><br>M1: (85,500 - 8,550) &times; 10% = 7,695.<br>M2: 1,00,000 &times; 10% &times; 9/12 = 7,500.<br>Total = 15,195.</p></div>"
            },
            {
                label: "b",
                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",
                answer: "<p class='text-xs'>Accum Dep Bal Dec 31, 2024 = 14,500 + 8,550 + 15,195 = 38,245. Ledgers follow standard dual-entry format closing to income summary.</p>"
            },
            {
                label: "c",
                text: "Show presentation in the Balance Sheet.",
                answer: "<div class='space-y-3'><p class='text-[11px] font-bold underline'>Balance Sheet Presentation (Extract):</p><table class='w-full text-xs border border-gray-300'><thead><tr class='bg-gray-100'><th class='border p-1'>Assets</th><th class='border p-1'>Amount (Tk)</th><th class='border p-1'>Total (Tk)</th></tr></thead><tbody><tr><td class='border p-1 font-semibold'>Fixed Assets:</td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Machinery (1,00,000 + 1,00,000)</td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Less: Accumulated Depreciation</td><td class='border p-1 text-right italic underline'>(38,245)</td><td class='border p-1'></td></tr><tr><td class='border p-1 font-bold'>Net Book Value (Dec 31, 2024)</td><td class='border p-1'></td><td class='border p-1 text-right font-bold'>1,61,755</td></tr></tbody></table><p class='text-[10px] italic text-gray-500'>*Accumulated Depreciation = Opening (14,500) + 2023 (8,550) + 2024 (15,195).</p></div>"
            }
        ]
    },
    {
        id: 5,
        stem: "<p>Ahnaf Traders bought a machine for 4,00,000 on July 1, 2023. Life 5 yrs, salvage 40,000. Reducing Balance method is used.</p>",
        meta: "Dhaka Commerce College \u00b7 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine 2023 and 2024 depreciation.",
                answer: "<div class='text-xs font-mono'><p>Rate = (100/5)&times;2 = 40%.</p><p>2023 Dep (6 mo): 4,00,000 &times; 40% &times; 6/12 = 80,000.</p><p>2024 Dep: (4,00,000 - 80,000) &times; 40% = 1,28,000.</p></div>"
            },'''
    
    content = content[:insert_point] + missing_content + content[insert_point:]
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Verify
    saikat = content.find('Saikat')
    ahnaf = content.find('Ahnaf')
    print(f'Saikat (CQ4) restored at: {saikat}')
    print(f'Ahnaf (CQ5) restored at: {ahnaf}')
    
    # Check CQ IDs
    import re
    area = content[insert_point-2000:insert_point+10000]
    ids = re.findall(r'id:\s*(\d+),', area)
    print(f'CQ IDs in area: {ids}')
    
    print('Restoration complete!')
else:
    print('ERROR: Could not find insertion point')
