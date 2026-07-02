with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
bus2_idx = content.find('"bus2":')
if bus2_idx != -1:
    subj_start = content.find('{', bus2_idx)
    bracket = 0
    subj_end = -1
    for i in range(subj_start, len(content)):
        if content[i] == '{': bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                subj_end = i+1
                break
    bus2_block = content[subj_start:subj_end]
    
    import re
    ch_match = re.search(r'"1":\s*\{', bus2_block)
    if ch_match:
        ch_start = ch_match.start()
        ch_bracket = 0
        ch_end = -1
        for i in range(ch_start, len(bus2_block)):
            if bus2_block[i] == '{': ch_bracket += 1
            elif bus2_block[i] == '}':
                ch_bracket -= 1
                if ch_bracket == 0:
                    ch_end = i+1
                    break
        ch_block = bus2_block[ch_start:ch_end]
        print('Start of bus2 ch1:', ch_block[:500])
