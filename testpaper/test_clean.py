import re

# Let's write a robust clean function
def clean_previous_injection(ch_text):
    short_idx = ch_text.find('"shortCQData"')
    if short_idx == -1:
        return ch_text
    
    # Find the last ']' before "shortCQData"
    last_mcq_bracket = ch_text.rfind(']', 0, short_idx)
    if last_mcq_bracket == -1:
        return ch_text
    
    # The clean text is just the text up to that bracket plus the closing brace
    # Let's get the indentation/newlines of the original end
    clean_text = ch_text[:last_mcq_bracket + 1] + "\n        }"
    return clean_text

# Let's test on a mock string
mock_ch = """{
    "subjectName": "Test Subject",
    "mcqData": [
        {"id": 1, "text": "Q1"}
    ],
    "shortCQData": [],
    "fullCQData": [
        {"id": "01", "stem": "S1"}
    ]
}"""

print("Cleaned mock:")
print(clean_previous_injection(mock_ch))
