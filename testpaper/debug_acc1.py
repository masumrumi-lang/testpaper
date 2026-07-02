import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

acc1_start = content.find('"acc1": {')
if acc1_start == -1:
    print('acc1 not found')
else:
    # Try to find the next subject or the end
    next_subject_matches = [m.start() for m in re.finditer(r'"\w+": \{', content[acc1_start+1:])]
    if next_subject_matches:
        acc1_end = acc1_start + 1 + next_subject_matches[0]
    else:
        acc1_end = len(content)
    
    acc1_content = content[acc1_start:acc1_end]
    
    # Check what chapters are in acc1
    chapters = re.findall(r'"(\d+)":\s*\{', acc1_content)
    print('Chapters in acc1:', set(chapters))
    print('acc1_content start:', acc1_content[:500])
    
    print('fullCQData count in acc1:', acc1_content.count('fullCQData:'))
    print('shortCQData count in acc1:', acc1_content.count('shortCQData:'))
    
    for ch in sorted(set(chapters)):
        ch_start = acc1_content.find(f'"{ch}":')
        # Find next chapter
        next_chs = [m.start() for m in re.finditer(r'"\d+":\s*\{', acc1_content[ch_start+1:])]
        ch_end = ch_start + 1 + next_chs[0] if next_chs else len(acc1_content)
        
        ch_content = acc1_content[ch_start:ch_end]
        has_full = 'fullCQData:' in ch_content
        has_short = 'shortCQData:' in ch_content
        has_mcq = 'mcqData:' in ch_content
        print(f"Chapter {ch}: MCQ={has_mcq}, Short={has_short}, Full={has_full}")
