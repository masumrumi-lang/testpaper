import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    db_content = f.read()

# 1. Isolate the "bus2" block
bus2_match = re.search(r'("bus2":\s*\{)', db_content)
start_pos = bus2_match.start()

bracket_count = 0
end_pos = -1
for i in range(start_pos, len(db_content)):
    if db_content[i] == '{':
        bracket_count += 1
    elif db_content[i] == '}':
        bracket_count -= 1
        if bracket_count == 0:
            end_pos = i + 1
            break

bus2_content = db_content[start_pos:end_pos]

# 2. Isolate the "1" block inside "bus2"
ch_match = re.search(r'("1":\s*\{)', bus2_content)
ch_start = ch_match.start()

bracket_count = 0
ch_end = -1
for i in range(ch_start, len(bus2_content)):
    if bus2_content[i] == '{':
        bracket_count += 1
    elif bus2_content[i] == '}':
        bracket_count -= 1
        if bracket_count == 0:
            ch_end = i + 1
            break

ch_content = bus2_content[ch_start:ch_end]

# 3. Find fullCQData array using bracket matching
array_start = ch_content.find('"fullCQData":')
if array_start != -1:
    array_start = ch_content.find('[', array_start)
    array_bracket_count = 0
    array_end = -1
    for i in range(array_start, len(ch_content)):
        if ch_content[i] == '[':
            array_bracket_count += 1
        elif ch_content[i] == ']':
            array_bracket_count -= 1
            if array_bracket_count == 0:
                array_end = i + 1
                break
    
    cq_json_str = ch_content[array_start:array_end]
    cqs = json.loads(cq_json_str)
    
    svg_stem = """<div class="flex justify-center w-full my-6">
<svg viewBox="-180 -180 360 360" width="100%" style="max-width: 400px; font-family: sans-serif;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowHead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#374151" />
    </marker>
  </defs>
  
  <g stroke="#374151" stroke-width="3" fill="none" marker-end="url(#arrowHead)">
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(51.4)" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(102.8)" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(154.2)" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(205.7)" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(257.1)" />
    <path d="M -54.7 -150.2 A 160 160 0 0 1 54.7 -150.2" transform="rotate(308.5)" />
  </g>

  <circle cx="0" cy="0" r="140" fill="none" stroke="#1f2937" stroke-width="3" />
  <circle cx="0" cy="0" r="30" fill="none" stroke="#1f2937" stroke-width="3" />
  
  <g stroke="#1f2937" stroke-width="3">
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(51.4)" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(102.8)" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(154.2)" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(205.7)" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(257.1)" />
    <line x1="-13" y1="-27" x2="-60.6" y2="-126.1" transform="rotate(308.5)" />
  </g>

  <text x="0" y="-85" font-size="24" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="middle">B</text>
  <text x="66" y="-53" font-size="14" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">Planning</text>
  <text x="83" y="19" font-size="24" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="middle">A</text>
  <text x="37" y="76" font-size="14" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">Staffing</text>
  <text x="-37" y="76" font-size="14" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">Directing</text>
  <text x="-83" y="19" font-size="13" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">Motivating</text>
  <text x="-66" y="-53" font-size="12" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">Coordinating</text>
</svg>
</div>"""
    
    # Update CQ "02"
    for cq in cqs:
        if cq.get("id") == "02":
            cq["stem"] = svg_stem
            
            # Replace 'ক' with 'A' and 'খ' with 'B' in text
            for q in cq.get("questions", []):
                if q.get("text"):
                    q["text"] = q["text"].replace("'ক'", "'A'").replace("'খ'", "'B'")
                if q.get("answer"):
                    q["answer"] = q["answer"].replace("'ক'", "'A'").replace("'খ'", "'B'")

    new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
    
    # Reconstruct
    new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
    new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
    final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("Successfully updated CQ 02 with English SVG and text replacement.")
else:
    print("fullCQData not found")
