with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check what's around the CQ3(c) replacement now
idx = content.find('Khan Ltd. Ledger (2023-2025)')
print(f'New CQ3(c) at: {idx}')

if idx > 0:
    # Find the end of this new answer
    end_area = content[idx:idx+5000]
    close_idx = end_area.find('</div>"')
    print(f'New answer closes at offset: {close_idx}')
    
    # Check what comes AFTER the closing
    after = content[idx+close_idx:idx+close_idx+500]
    print(f'\nAfter new answer:')
    print(repr(after[:300]))
    
    # Check: does CQ4 (id: 4, Saikat Bros) still exist?
    saikat = content.find('Saikat')
    print(f'\n"Saikat" (CQ4) at: {saikat}')
    
    # Check: does CQ5 (id: 5, Ahnaf Traders) still exist?
    ahnaf = content.find('Ahnaf')
    print(f'"Ahnaf" (CQ5) at: {ahnaf}')
    
    # Check: does CQ6 (id: 6, Nadia) exist?
    nadia = content.find('Nadia Co')
    print(f'"Nadia Co" (CQ6) at: {nadia}')
    
    # Check how many CQs remain in chapter 8
    import re
    cq_ids = re.findall(r'id:\s*(\d+),', content[idx-2000:idx+50000])
    print(f'\nCQ IDs found near ch8: {cq_ids[:30]}')
