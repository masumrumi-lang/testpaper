import subprocess
result = subprocess.run(
    ['node', '-e', 'try { require("./data.js"); console.log("PASS: data.js loads without errors"); } catch(e) { console.log("FAIL:", e.message); }'],
    capture_output=True, text=True, cwd='.'
)
print(result.stdout.strip())
if result.stderr.strip():
    print("STDERR:", result.stderr.strip()[:500])
