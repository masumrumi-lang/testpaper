import json

def indent_json_string(json_str, num_spaces):
    lines = json_str.splitlines()
    indented_lines = []
    indented_lines.append(lines[0])
    for line in lines[1:]:
        indented_lines.append(" " * num_spaces + line)
    return "\n".join(indented_lines)

cqs = [{"id": "01", "stem": "stem text", "questions": [{"label": "a", "text": "q1", "answer": "a1"}]}]
j_str = json.dumps(cqs, indent=4, ensure_ascii=False)
formatted = indent_json_string(j_str, 16)
print("Formatted JSON:")
print(formatted)
