import re
import glob

def bn_to_en_digits(bn_str):
    mapping = str.maketrans('০১২৩৪৫৬৭৮৯', '0123456789')
    return bn_str.translate(mapping)

def extract_numbers(text):
    en_text = bn_to_en_digits(text)
    return set(re.findall(r'\b\d{2,}\b', en_text))

# Parse Bengali questions
with open('raw_board.txt', 'r', encoding='utf-8') as f:
    raw_bn = f.read()

bn_blocks = re.split(r'\n(?=\d{2}\nQuestion \d{2})', raw_bn.strip())
bn_questions = []

for block in bn_blocks:
    lines = block.strip().split('\n')
    if len(lines) < 3: continue
    q_num = lines[0].strip()
    
    # Extract meta which is usually near the end before a,b,c
    # It looks like "Rajshahi · 2025"
    meta_match = re.search(r'([A-Za-z]+)\s*·\s*(\d{4})', block)
    meta = f"{meta_match.group(1)} {meta_match.group(2)}" if meta_match else ""
    
    nums = extract_numbers(block)
    
    bn_questions.append({
        'id': q_num,
        'meta': meta,
        'nums': nums,
        'block': block
    })

# Parse English questions from JS
en_questions = []
for file in sorted(glob.glob("fullCQ_board_part*.js")):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # split by { id:
    blocks = content.split('{')
    for b in blocks:
        if 'id:' not in b or 'stem:' not in b: continue
        id_match = re.search(r'id:\s*"(\d+)"', b)
        meta_match = re.search(r'meta:\s*"(.*?)"', b)
        stem_match = re.search(r'stem:\s*"(.*?)"', b)
        
        if not id_match or not meta_match or not stem_match: continue
        
        meta = meta_match.group(1).replace('', '').replace('  ', ' ').strip()
        stem = stem_match.group(1)
        nums = extract_numbers(stem)
        
        en_questions.append({
            'meta': meta,
            'nums': nums,
            'block': '{' + b.split('}')[0] + '}'
        })

# Match
matched = 0
unmatched = []

for bn in bn_questions:
    best_match = None
    best_score = 0
    
    bn_meta_board = bn['meta'].split(' ')[0] if bn['meta'] else ""
    bn_meta_year = bn['meta'].split(' ')[1] if bn['meta'] else ""
    
    for en in en_questions:
        en_meta_board = en['meta'].split(' ')[0] if en['meta'] else ""
        en_meta_year = en['meta'].split(' ')[-1] if en['meta'] else ""
        
        if bn_meta_year != en_meta_year: continue
        if bn_meta_board != en_meta_board: continue
        
        common_nums = bn['nums'].intersection(en['nums'])
        if len(common_nums) > best_score:
            best_score = len(common_nums)
            best_match = en
            
    if best_match and best_score > 3:
        matched += 1
    else:
        unmatched.append(bn['id'])

print(f"Matched: {matched}/{len(bn_questions)}")
print(f"Unmatched IDs: {unmatched}")
