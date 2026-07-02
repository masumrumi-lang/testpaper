import math
import json
import re

def get_svg():
    r_inner = 45
    r_outer = 140
    r_text = 95
    r_arrow = 160
    
    # 7 sectors
    angles_mid = [90, 141.43, 192.86, 244.29, 295.71, 347.14, 38.57]
    angles_line = [115.71, 167.14, 218.57, 270.0, 321.43, 12.86, 64.29]
    
    svg = f"""<div class="flex justify-center w-full my-6 flex-col items-center">
<svg viewBox="-180 -180 360 380" width="100%" style="max-width: 400px; font-family: sans-serif;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowHead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#374151" />
    </marker>
  </defs>
"""
    
    # Arrows (clockwise)
    # Start slightly after line, end slightly before next line
    svg += '  <g stroke="#374151" stroke-width="3" fill="none" marker-end="url(#arrowHead)">\n'
    for line_ang in angles_line:
        # A 40 degree arc starting 5.7 degrees after the line
        start_ang = line_ang + 5.7
        end_ang = start_ang + 40
        x1 = r_arrow * math.cos(math.radians(start_ang))
        y1 = r_arrow * math.sin(math.radians(start_ang))
        x2 = r_arrow * math.cos(math.radians(end_ang))
        y2 = r_arrow * math.sin(math.radians(end_ang))
        svg += f'    <path d="M {x1:.1f} {y1:.1f} A {r_arrow} {r_arrow} 0 0 1 {x2:.1f} {y2:.1f}" />\n'
    svg += '  </g>\n\n'
    
    # Circles
    svg += f'  <circle cx="0" cy="0" r="{r_outer}" fill="none" stroke="#1f2937" stroke-width="3" />\n'
    svg += f'  <circle cx="0" cy="0" r="{r_inner}" fill="none" stroke="#1f2937" stroke-width="3" />\n\n'
    
    # Lines
    svg += '  <g stroke="#1f2937" stroke-width="3">\n'
    for a in angles_line:
        x1 = r_inner * math.cos(math.radians(a))
        y1 = r_inner * math.sin(math.radians(a))
        x2 = r_outer * math.cos(math.radians(a))
        y2 = r_outer * math.sin(math.radians(a))
        svg += f'    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" />\n'
    svg += '  </g>\n\n'
    
    # Center text
    svg += '  <text x="0" y="0" font-size="12" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="middle">Management</text>\n\n'
    
    # Texts
    labels = ["Planning", "Organizing", "?", "Directing", "Motivating", "Coordinating", "P"]
    nums = ["1", "2", "3", "4", "5", "6", "7"]
    
    for i in range(7):
        a = angles_mid[i]
        x = r_text * math.cos(math.radians(a))
        y = r_text * math.sin(math.radians(a))
        
        # Adjust Y slightly so number and text stack nicely
        font_size = "12" if len(labels[i]) > 8 else "14"
        svg += f'  <text x="{x:.1f}" y="{y-8:.1f}" font-size="14" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="middle">{nums[i]}</text>\n'
        svg += f'  <text x="{x:.1f}" y="{y+8:.1f}" font-size="{font_size}" font-weight="600" fill="#111827" text-anchor="middle" dominant-baseline="middle">{labels[i]}</text>\n'
    
    # Bottom title text inside SVG
    svg += '  <text x="0" y="190" font-size="16" font-weight="bold" fill="#111827" text-anchor="middle" dominant-baseline="middle">Management Cycle</text>\n'
    
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
        
        # Update CQ "06"
        for cq in cqs:
            if cq.get("id") == "06":
                cq["stem"] = svg_stem
                # Text should already be english. Let's just ensure it's not wrapped in Conceptual Diagram anymore.

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print("Successfully updated CQ 06 with English SVG.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
