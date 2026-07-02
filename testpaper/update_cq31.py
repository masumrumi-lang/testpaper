import math
import json
import re

def get_svg():
    r_outer = 140
    r_text = 85
    r_arrow = 160
    
    # 7 sectors, lines starting from top (-90 degrees)
    angles_line = [-90, -38.57, 12.86, 64.29, 115.71, 167.14, 218.57]
    angles_mid = [-64.29, -12.85, 38.58, 90.0, 141.43, 192.86, -115.71]
    
    svg = f"""<div class="flex justify-center w-full my-6 flex-col items-center">
<svg viewBox="-180 -180 360 360" width="100%" style="max-width: 350px; font-family: sans-serif;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowHead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#374151" />
    </marker>
  </defs>

  <!-- Arrows (clockwise) -->
  <g stroke="#374151" stroke-width="3" fill="none" marker-end="url(#arrowHead)">\n"""
  
    for line_ang in angles_line:
        start_ang = line_ang + 5.7
        end_ang = start_ang + 40
        x1 = r_arrow * math.cos(math.radians(start_ang))
        y1 = r_arrow * math.sin(math.radians(start_ang))
        x2 = r_arrow * math.cos(math.radians(end_ang))
        y2 = r_arrow * math.sin(math.radians(end_ang))
        svg += f'    <path d="M {x1:.1f} {y1:.1f} A {r_arrow} {r_arrow} 0 0 1 {x2:.1f} {y2:.1f}" />\n'
    svg += '  </g>\n\n'

    svg += f"""  <!-- Outer Circle -->
  <circle cx="0" cy="0" r="{r_outer}" fill="none" stroke="#1f2937" stroke-width="3" />
  
  <!-- Lines from center -->
  <g stroke="#1f2937" stroke-width="3">\n"""

    for a in angles_line:
        x2 = r_outer * math.cos(math.radians(a))
        y2 = r_outer * math.sin(math.radians(a))
        svg += f'    <line x1="0" y1="0" x2="{x2:.1f}" y2="{y2:.1f}" />\n'
    svg += '  </g>\n\n'
    
    # Texts
    labels = ["A", "Organizing", "Staffing", "Directing", "Motivating", "Coordinating", "B"]
    
    for i in range(7):
        a = angles_mid[i]
        x = r_text * math.cos(math.radians(a))
        y = r_text * math.sin(math.radians(a))
        
        # Adjust font size for longer words
        font_size = "12" if len(labels[i]) > 10 else "14"
        if labels[i] in ["A", "B"]:
            font_size = "28"
            font_weight = "bold"
        else:
            font_weight = "600"
            
        svg += f'  <text x="{x:.1f}" y="{y:.1f}" font-size="{font_size}" font-weight="{font_weight}" fill="#111827" text-anchor="middle" dominant-baseline="middle">{labels[i]}</text>\n'
    
    svg += "</svg>\n</div>"
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
        
        # Update CQ "31"
        for cq in cqs:
            if cq.get("id") == "31":
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
        
        print("Successfully updated CQ 31 with English SVG and text replacement.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
