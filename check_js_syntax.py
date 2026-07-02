# Since data.js is valid JS (a variable assignment), I can execute it with node if I wrap it or just use it.
# But I want to check for syntax errors.

import subprocess

def check_js_syntax(file_path):
    try:
        # We can use node -c (check syntax)
        result = subprocess.run(['node', '-c', file_path], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Syntax Error: {result.stderr}"
        return "Syntax OK"
    except Exception as e:
        return f"Error running node: {str(e)}"

if __name__ == "__main__":
    db_path = r"c:\Users\BMTF\.antigravity\testpaper\data.js"
    print(check_js_syntax(db_path))
