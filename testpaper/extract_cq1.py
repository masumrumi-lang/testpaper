import docx
import json
import os
import re
from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError('something\'s not right')

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")

def clean_whitespace(text):
    # Replace multiple spaces/tabs with single space
    text = re.sub(r'[ \t]+', ' ', text)
    # Collapse multiple newlines (even with spaces between them) into a single newline
    text = re.sub(r'(\s*\n\s*)+', '\n', text)
    return text.strip()

def table_to_html(table):
    headers = [cell.text.strip().lower() for cell in table.rows[0].cells]
    is_journal = any("debit" in h for h in headers) and any("credit" in h for h in headers)
    
    table_html = '<table class="w-full border-collapse border border-gray-400 text-xs mt-1 mb-4 leading-tight">\n'
    
    for row_idx, row in enumerate(table.rows):
        row_html = '  <tr class="align-top">\n'
        narrations = []
        
        for cell_idx, cell in enumerate(row.cells):
            if cell_idx > 0 and cell._tc is row.cells[cell_idx-1]._tc:
                continue
            
            colspan = 1
            for c in range(cell_idx + 1, len(row.cells)):
                if row.cells[c]._tc is cell._tc:
                    colspan += 1
                else:
                    break
            
            rowspan = 1
            for r in range(row_idx + 1, len(table.rows)):
                if table.rows[r].cells[cell_idx]._tc is cell._tc:
                    rowspan += 1
                else:
                    break
                    
            if row_idx > 0 and table.rows[row_idx-1].cells[cell_idx]._tc is cell._tc:
                continue
                
            colspan_attr = f' colspan="{colspan}"' if colspan > 1 else ''
            rowspan_attr = f' rowspan="{rowspan}"' if rowspan > 1 else ''
            
            tag = 'th' if row_idx == 0 else 'td'
            classes = 'border border-gray-400 p-1 text-left'
            
            cell_text = clean_whitespace(cell.text)
            
            if is_journal and row_idx > 0 and ("particulars" in headers[cell_idx] or cell_idx == 1):
                # Search for (Being ...) more flexibly
                match = re.search(r'(\(Being.*?\))', cell_text, re.IGNORECASE | re.DOTALL)
                if match:
                    narration = match.group(1).strip()
                    narrations.append(narration)
                    cell_text = cell_text.replace(match.group(1), "").strip()
            
            cell_html = escape_html(cell_text)
            row_html += f'    <{tag}{colspan_attr}{rowspan_attr} class="{classes}">{cell_html}</{tag}>\n'
        
        row_html += '  </tr>\n'
        table_html += row_html
        
        if narrations:
            num_cols = len(row.cells)
            for narration in narrations:
                narration_html = narration.replace("\n", " ").strip()
                table_html += f'  <tr class="border-none">\n    <td colspan="{num_cols}" class="p-1 text-[10px] italic text-gray-500 border-x border-gray-400"> {narration_html} </td>\n  </tr>\n'

    table_html += '</table>'
    return table_html

def parse_docx(file_path):
    doc = docx.Document(file_path)
    
    cq_data = {
      "chapter": "",
      "question_id": "",
      "stimulus": "",
      "requirements": { "a": "", "b": "", "c": "", "d": "" },
      "solutions": { "a": "", "b": "", "c": "" }
    }
    
    current_section = None
    
    def append_content(target_key, content, is_html=False):
        nonlocal cq_data
        if target_key == "requirements": return
        
        target_dict = cq_data["solutions"] if target_key in cq_data["solutions"] else {"stimulus": cq_data["stimulus"]}
        key = target_key if target_key in cq_data["solutions"] else "stimulus"
        
        current = target_dict[key]
        
        if is_html:
            while current.endswith("<br>"):
                current = current[:-4]
            target_dict[key] = current + content
        else:
            if current and not current.endswith("<br>"):
                target_dict[key] += "<br>"
            target_dict[key] += content
            
        if key == "stimulus": cq_data["stimulus"] = target_dict[key]

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text or text == "\u00a0": continue
                
            if "Chapter" in text and "Capital" in text:
                cq_data["chapter"] = text
            elif "CQ 01" in text:
                cq_data["question_id"] = "cq1"
                current_section = "stimulus"
            elif text == "Requirements:":
                current_section = "requirements"
            elif text.startswith("a)"):
                current_section = "req_a"
                cq_data["requirements"]["a"] = text[2:].strip()
            elif text.startswith("b)"):
                current_section = "req_b"
                cq_data["requirements"]["b"] = text[2:].strip()
            elif text.startswith("c)"):
                current_section = "req_c"
                cq_data["requirements"]["c"] = text[2:].strip()
            elif "Solution to Requirement: a)" in text:
                current_section = "sol_a"
            elif "Solution to Requirement: b)" in text:
                current_section = "sol_b"
            elif "Solution to Requirement: c)" in text:
                current_section = "sol_c"
            else:
                if current_section == "stimulus":
                    append_content("stimulus", escape_html(text))
                elif current_section == "sol_a":
                    append_content("a", escape_html(text))
                elif current_section == "sol_b":
                    append_content("b", escape_html(text))
                elif current_section == "sol_c":
                    append_content("c", escape_html(text))
                        
        elif isinstance(block, Table):
            html_table = table_to_html(block)
            
            if current_section == "sol_a":
                append_content("a", html_table, True)
            elif current_section == "sol_b":
                append_content("b", html_table, True)
            elif current_section == "sol_c":
                append_content("c", html_table, True)
            elif current_section == "stimulus":
                append_content("stimulus", html_table, True)

    return cq_data

if __name__ == "__main__":
    file_path = r"C:\Users\BMTF\.antigravity\testpaper\Acc2_ch4_cq1.docx"
    data = parse_docx(file_path)
    with open("extracted_cq.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("DONE")
