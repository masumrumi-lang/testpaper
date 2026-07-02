import json
import re

def get_svg():
    svg = f"""<p class="mb-4 text-gray-700 dark:text-gray-300">Observe the following diagram and answer the relevant questions:</p>
<div class="flex justify-center w-full my-6 flex-col items-center">
<svg viewBox="0 0 300 270" width="100%" style="max-width: 300px; font-family: sans-serif;" xmlns="http://www.w3.org/2000/svg">
  <!-- Triangle -->
  <polygon points="150,30 30,210 270,210" fill="none" stroke="#1f2937" stroke-width="3" stroke-linejoin="round" />
  
  <!-- Horizontal Lines -->
  <line x1="110" y1="90" x2="190" y2="90" stroke="#1f2937" stroke-width="3" />
  <line x1="70" y1="150" x2="230" y2="150" stroke="#1f2937" stroke-width="3" />
  
  <!-- Circles -->
  <circle cx="150" cy="65" r="16" fill="none" stroke="#1f2937" stroke-width="2" />
  <circle cx="150" cy="120" r="16" fill="none" stroke="#1f2937" stroke-width="2" />
  <circle cx="150" cy="180" r="16" fill="none" stroke="#1f2937" stroke-width="2" />
  
  <!-- Text -->
  <text x="150" y="65" font-size="18" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="central">A</text>
  <text x="150" y="120" font-size="18" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="central">B</text>
  <text x="150" y="180" font-size="18" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="central">C</text>
  
  <!-- Title -->
  <text x="150" y="250" font-size="16" font-weight="bold" fill="#111827" text-anchor="middle">Figure: Hierarchy of Management Levels</text>
</svg>
</div>"""
    return svg

def process():
    svg_stem = get_svg()
    
    with open('data.js', 'r', encoding='utf-8') as f:
        db_content = f.read()

    # 1. Isolate the "bus2" block
    bus2_match = re.search(r'("bus2":\s*\{)', db_content)
    if not bus2_match: return
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
    if not ch_match: return
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

    # 3. Find fullCQData array
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
        
        # Update CQ "17"
        for cq in cqs:
            if cq.get("id") == "17":
                cq["stem"] = svg_stem
                # No text replacement needed for this CQ

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print("Successfully updated CQ 17 with English SVG.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
