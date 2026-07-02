import subprocess, json

# Try to validate the JS by extracting the object and parsing with a simple check
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Write a small JS validation script
js_code = '''
try {
    ''' + content + '''
    if (testDatabase && testDatabase["acc1"] && testDatabase["acc1"]["8"]) {
        const ch8 = testDatabase["acc1"]["8"];
        console.log("OK: Chapter 8 loaded");
        console.log("Subject:", ch8.subjectName);
        console.log("Chapter:", ch8.chapterName);
        console.log("MCQ count:", ch8.mcqData ? ch8.mcqData.length : 0);
        console.log("CQ count:", ch8.fullCQData ? ch8.fullCQData.length : 0);
    } else {
        console.log("ERROR: Chapter 8 not found in testDatabase");
    }
} catch(e) {
    console.log("PARSE ERROR:", e.message);
    // Try to find the line number
    const lines = e.stack;
    console.log("Stack:", lines);
}
'''

with open('_validate.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Validation script written. Please run with: node _validate.js")
print("Or if node not available, try opening browser console.")
