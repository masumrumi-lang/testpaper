"""
Flask Web Interface for Gemini Integration
A simple web app to use Gemini features without coding

Run with: python flask_app.py
Then visit: http://localhost:5000
"""

from flask import Flask, render_template_string, request, jsonify
import json
from pathlib import Path

try:
    from gemini_integration import (
        setup_gemini,
        QuestionGenerator,
        AnswerEvaluator,
        ContentSummarizer,
        QuestionVerifier,
        DataProcessor
    )
except ImportError:
    print("Error: gemini_integration module not found")
    exit(1)

app = Flask(__name__)

# Initialize Gemini
try:
    setup_gemini()
    generator = QuestionGenerator()
    evaluator = AnswerEvaluator()
    summarizer = ContentSummarizer()
    verifier = QuestionVerifier()
    processor = DataProcessor()
    gemini_ready = True
except Exception as e:
    print(f"Warning: Gemini initialization failed: {e}")
    gemini_ready = False

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini TestPaper Integration</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1000px; margin: 0 auto; }
        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        h1 { font-size: 2.5em; margin-bottom: 10px; }
        .status {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-bottom: 20px;
        }
        .status.ready { background: #4CAF50; color: white; }
        .status.error { background: #f44336; color: white; }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .tab-btn {
            padding: 12px 20px;
            background: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .tab-btn.active {
            background: #667eea;
            color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        
        .tab-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        
        .tab-content {
            display: none;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            animation: fadeIn 0.3s;
        }
        
        .tab-content.active { display: block; }
        
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-family: inherit;
            font-size: 1em;
            transition: border 0.3s;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        textarea { resize: vertical; min-height: 100px; }
        
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        
        button {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-primary {
            background: #667eea;
            color: white;
        }
        
        .btn-primary:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        
        .result-box {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
            border-left: 4px solid #667eea;
            max-height: 500px;
            overflow-y: auto;
        }
        
        .result-box.error {
            border-left-color: #f44336;
            background: #ffebee;
        }
        
        .result-box.success {
            border-left-color: #4CAF50;
            background: #e8f5e9;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        
        .question-card {
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 3px solid #667eea;
        }
        
        .question-text { font-weight: 600; margin-bottom: 10px; }
        .option { margin: 8px 0; padding: 8px; background: white; border-radius: 3px; }
        .correct { color: #4CAF50; font-weight: 600; }
        .wrong { color: #f44336; }
        
        footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            font-size: 0.9em;
            opacity: 0.8;
        }
        
        .info-box {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🤖 Gemini TestPaper Assistant</h1>
            <div class="status {% if gemini_ready %}ready{% else %}error{% endif %}">
                {% if gemini_ready %}✓ Gemini Ready{% else %}✗ Gemini Error{% endif %}
            </div>
        </header>
        
        <div class="tabs">
            <button class="tab-btn active" onclick="showTab('generate')">📝 Generate Questions</button>
            <button class="tab-btn" onclick="showTab('evaluate')">✓ Evaluate Answers</button>
            <button class="tab-btn" onclick="showTab('summarize')">📚 Summarize Content</button>
            <button class="tab-btn" onclick="showTab('verify')">🔍 Verify Questions</button>
            <button class="tab-btn" onclick="showTab('process')">⚙️ Process Data</button>
        </div>
        
        <!-- TAB 1: Generate Questions -->
        <div id="generate" class="tab-content active">
            <h2>Generate Multiple Choice Questions</h2>
            <div class="form-group">
                <label>Topic/Subject</label>
                <input type="text" id="gen_topic" placeholder="e.g., Double Entry Bookkeeping" value="Journal and Ledger">
            </div>
            <div class="form-group">
                <label>Difficulty Level</label>
                <select id="gen_difficulty">
                    <option value="easy">Easy</option>
                    <option value="medium" selected>Medium</option>
                    <option value="hard">Hard</option>
                </select>
            </div>
            <div class="form-group">
                <label>Number of Questions</label>
                <input type="number" id="gen_count" min="1" max="10" value="2">
            </div>
            <div class="button-group">
                <button class="btn-primary" onclick="generateQuestions()">Generate Questions</button>
            </div>
            <div id="gen_loading" class="loading"><div class="spinner"></div><p>Generating...</p></div>
            <div id="gen_result" class="result-box" style="display:none;"></div>
        </div>
        
        <!-- TAB 2: Evaluate Answers -->
        <div id="evaluate" class="tab-content">
            <h2>Evaluate Student Answer</h2>
            <div class="form-group">
                <label>Question</label>
                <textarea id="eval_question" placeholder="Enter the question..."></textarea>
            </div>
            <div class="form-group">
                <label>Options (separated by |)</label>
                <textarea id="eval_options" placeholder="Option 1 | Option 2 | Option 3 | Option 4"></textarea>
            </div>
            <div class="form-group">
                <label>Student's Answer</label>
                <input type="text" id="eval_student" placeholder="Enter student's answer...">
            </div>
            <div class="form-group">
                <label>Correct Answer</label>
                <input type="text" id="eval_correct" placeholder="Enter correct answer...">
            </div>
            <div class="button-group">
                <button class="btn-primary" onclick="evaluateAnswer()">Evaluate Answer</button>
            </div>
            <div id="eval_loading" class="loading"><div class="spinner"></div><p>Evaluating...</p></div>
            <div id="eval_result" class="result-box" style="display:none;"></div>
        </div>
        
        <!-- TAB 3: Summarize Content -->
        <div id="summarize" class="tab-content">
            <h2>Summarize Content</h2>
            <div class="info-box">
                Choose between summarizing existing content or generating study notes for a topic.
            </div>
            <div class="form-group">
                <label>Topic</label>
                <input type="text" id="sum_topic" placeholder="e.g., Trial Balance" value="Trial Balance">
            </div>
            <div class="form-group">
                <label>Type</label>
                <select id="sum_type" onchange="toggleSummarizeMode()">
                    <option value="notes">Generate Study Notes</option>
                    <option value="summary">Summarize Content</option>
                </select>
            </div>
            <div id="sum_content_group" class="form-group" style="display:none;">
                <label>Content to Summarize</label>
                <textarea id="sum_content" placeholder="Paste your content here..."></textarea>
            </div>
            <div class="form-group">
                <label>Detail Level</label>
                <select id="sum_detail">
                    <option value="brief">Brief (2-3 sentences)</option>
                    <option value="moderate" selected>Moderate (5-7 points)</option>
                    <option value="detailed">Detailed (comprehensive)</option>
                </select>
            </div>
            <div class="button-group">
                <button class="btn-primary" onclick="summarizeContent()">Generate</button>
            </div>
            <div id="sum_loading" class="loading"><div class="spinner"></div><p>Generating...</p></div>
            <div id="sum_result" class="result-box" style="display:none;"></div>
        </div>
        
        <!-- TAB 4: Verify Questions -->
        <div id="verify" class="tab-content">
            <h2>Verify Question Quality</h2>
            <div class="info-box">
                Check if your question is clear, has valid options, and proper difficulty level.
            </div>
            <div class="form-group">
                <label>Question</label>
                <textarea id="ver_question" placeholder="Enter the question..."></textarea>
            </div>
            <div class="form-group">
                <label>Options (separated by |)</label>
                <textarea id="ver_options" placeholder="Option A | Option B | Option C | Option D"></textarea>
            </div>
            <div class="form-group">
                <label>Correct Answer</label>
                <input type="text" id="ver_correct" placeholder="Which option is correct?">
            </div>
            <div class="button-group">
                <button class="btn-primary" onclick="verifyQuestion()">Verify Quality</button>
            </div>
            <div id="ver_loading" class="loading"><div class="spinner"></div><p>Verifying...</p></div>
            <div id="ver_result" class="result-box" style="display:none;"></div>
        </div>
        
        <!-- TAB 5: Process Data -->
        <div id="process" class="tab-content">
            <h2>Process CSV Data</h2>
            <div class="info-box">
                Enhance your question bank with better explanations and categorization.
            </div>
            <div class="form-group">
                <label>Operation</label>
                <select id="proc_operation">
                    <option value="categorize">Categorize Questions</option>
                    <option value="enhance">Enhance Explanations</option>
                </select>
            </div>
            <div class="button-group">
                <button class="btn-primary" onclick="processData()">Start Processing</button>
            </div>
            <div id="proc_loading" class="loading"><div class="spinner"></div><p>Processing...</p></div>
            <div id="proc_result" class="result-box" style="display:none;"></div>
        </div>
        
        <footer>
            <p>Powered by Google Gemini AI | TestPaper Project</p>
            <p>Built with ❤️ for educators and students</p>
        </footer>
    </div>
    
    <script>
        function showTab(tabName) {
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(tab => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
        
        function toggleSummarizeMode() {
            const type = document.getElementById('sum_type').value;
            const contentGroup = document.getElementById('sum_content_group');
            if (type === 'summary') {
                contentGroup.style.display = 'block';
            } else {
                contentGroup.style.display = 'none';
            }
        }
        
        async function generateQuestions() {
            const topic = document.getElementById('gen_topic').value;
            const difficulty = document.getElementById('gen_difficulty').value;
            const count = document.getElementById('gen_count').value;
            
            if (!topic) {
                alert('Please enter a topic');
                return;
            }
            
            showLoading('gen');
            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({topic, difficulty, count})
                });
                const data = await response.json();
                displayResult('gen', data);
            } catch (error) {
                displayError('gen', error.message);
            }
        }
        
        async function evaluateAnswer() {
            const question = document.getElementById('eval_question').value;
            const options = document.getElementById('eval_options').value.split('|').map(o => o.trim());
            const student = document.getElementById('eval_student').value;
            const correct = document.getElementById('eval_correct').value;
            
            if (!question || !student || !correct) {
                alert('Please fill all fields');
                return;
            }
            
            showLoading('eval');
            try {
                const response = await fetch('/api/evaluate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question, options, student, correct})
                });
                const data = await response.json();
                displayResult('eval', data);
            } catch (error) {
                displayError('eval', error.message);
            }
        }
        
        async function summarizeContent() {
            const topic = document.getElementById('sum_topic').value;
            const type = document.getElementById('sum_type').value;
            const detail = document.getElementById('sum_detail').value;
            const content = document.getElementById('sum_content').value;
            
            if (!topic) {
                alert('Please enter a topic');
                return;
            }
            
            showLoading('sum');
            try {
                const response = await fetch('/api/summarize', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({topic, type, detail, content})
                });
                const data = await response.json();
                displayResult('sum', data);
            } catch (error) {
                displayError('sum', error.message);
            }
        }
        
        async function verifyQuestion() {
            const question = document.getElementById('ver_question').value;
            const options = document.getElementById('ver_options').value.split('|').map(o => o.trim());
            const correct = document.getElementById('ver_correct').value;
            
            if (!question || !correct) {
                alert('Please fill all fields');
                return;
            }
            
            showLoading('ver');
            try {
                const response = await fetch('/api/verify', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question, options, correct})
                });
                const data = await response.json();
                displayResult('ver', data);
            } catch (error) {
                displayError('ver', error.message);
            }
        }
        
        async function processData() {
            const operation = document.getElementById('proc_operation').value;
            
            showLoading('proc');
            try {
                const response = await fetch('/api/process', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({operation})
                });
                const data = await response.json();
                displayResult('proc', data);
            } catch (error) {
                displayError('proc', error.message);
            }
        }
        
        function showLoading(prefix) {
            document.getElementById(prefix + '_loading').style.display = 'block';
            document.getElementById(prefix + '_result').style.display = 'none';
        }
        
        function displayResult(prefix, data) {
            document.getElementById(prefix + '_loading').style.display = 'none';
            const resultBox = document.getElementById(prefix + '_result');
            
            if (data.error) {
                resultBox.innerHTML = `<strong>Error:</strong> ${data.error}`;
                resultBox.classList.add('error');
                resultBox.classList.remove('success');
            } else {
                resultBox.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
                resultBox.classList.remove('error');
                resultBox.classList.add('success');
            }
            
            resultBox.style.display = 'block';
        }
        
        function displayError(prefix, error) {
            displayResult(prefix, {error: error});
        }
    </script>
</body>
</html>
"""

# API Routes
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, gemini_ready=gemini_ready)

@app.route('/api/generate', methods=['POST'])
def api_generate():
    try:
        data = request.json
        questions = generator.generate_mcq(
            data.get('topic', ''),
            data.get('difficulty', 'medium'),
            int(data.get('count', 1))
        )
        
        return jsonify({
            'questions': [
                {
                    'text': q.text,
                    'options': q.options,
                    'correct_answer': q.correct_answer,
                    'explanation': q.explanation,
                    'difficulty': q.difficulty
                } for q in questions
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/evaluate', methods=['POST'])
def api_evaluate():
    try:
        data = request.json
        score, feedback = evaluator.evaluate_mcq_answer(
            data.get('question', ''),
            data.get('options', []),
            data.get('student', ''),
            data.get('correct', '')
        )
        
        return jsonify({
            'score': score,
            'feedback': feedback,
            'passed': score > 0
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    try:
        data = request.json
        
        if data.get('type') == 'notes':
            result = summarizer.generate_study_notes(
                data.get('topic', ''),
                data.get('include_examples', True)
            )
        else:
            result = summarizer.summarize_chapter(
                data.get('content', ''),
                data.get('detail', 'moderate')
            )
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/verify', methods=['POST'])
def api_verify():
    try:
        data = request.json
        report = verifier.verify_question_quality(
            data.get('question', ''),
            data.get('options', []),
            data.get('correct', '')
        )
        
        return jsonify(report)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/process', methods=['POST'])
def api_process():
    try:
        data = request.json
        operation = data.get('operation', 'categorize')
        
        csv_path = Path(__file__).parent / "hsc_mcq_bank_WEB_READY.csv"
        
        if not csv_path.exists():
            return jsonify({'error': 'CSV file not found'})
        
        if operation == 'categorize':
            result = processor.categorize_questions(str(csv_path))
            return jsonify({'result': result})
        else:
            processor.enhance_csv_data(str(csv_path))
            return jsonify({'result': 'CSV enhanced successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Gemini TestPaper Web Interface")
    print("="*60)
    print(f"\n✓ Gemini Status: {'Ready' if gemini_ready else 'Error'}")
    print(f"📍 Visit: http://localhost:5000")
    print(f"\n👤 Press Ctrl+C to stop\n")
    
    app.run(debug=True, host='localhost', port=5000)
