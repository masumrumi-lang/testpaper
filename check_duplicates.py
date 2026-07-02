with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f'Count of "acc2": {content.count("acc2")}')
    print(f'Count of "acc2_ch4_cq1": {content.count("acc2_ch4_cq1")}')
    
    # Check if there is any other subject with "acc2"
    import re
    matches = re.findall(r'"acc2":', content)
    print(f'Matches for "acc2":: {len(matches)}')
