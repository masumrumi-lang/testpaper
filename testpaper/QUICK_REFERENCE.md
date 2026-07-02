# Gemini Integration - Quick Reference

## Installation (First Time Only)
```powershell
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
# Copy .env.example to .env and add your key from https://aistudio.google.com
```

---

## Common Tasks

### Task 1: Generate 10 Multiple Choice Questions
```python
from gemini_integration import QuestionGenerator, export_questions_to_csv

generator = QuestionGenerator()
questions = generator.generate_mcq(
    topic="Journal and Ledger",
    difficulty="medium",
    count=10
)

# Save to CSV
export_questions_to_csv(questions, "my_questions.csv")
```

### Task 2: Evaluate a Student's Answer
```python
from gemini_integration import AnswerEvaluator

evaluator = AnswerEvaluator()

score, feedback = evaluator.evaluate_mcq_answer(
    question="What is debit?",
    options=["Left side", "Right side", "Both"],
    student_choice="Left side",
    correct_answer="Left side"
)

print(f"Score: {score * 100}%")
print(f"Feedback: {feedback}")
```

### Task 3: Grade a Short Answer Question
```python
score, feedback = evaluator.evaluate_short_answer(
    question="Define depreciation",
    student_answer="Loss of value over time due to wear and tear",
    model_answer="Depreciation is the systematic allocation of asset cost...",
    key_points=["Systematic", "Time period", "Asset value", "Useful life"]
)

print(f"Score: {score * 10}/10")
print(f"Detailed Feedback:\n{feedback}")
```

### Task 4: Create Study Notes for a Topic
```python
from gemini_integration import ContentSummarizer

summarizer = ContentSummarizer()

notes = summarizer.generate_study_notes(
    topic="Balance Sheet",
    include_examples=True
)

print(notes)

# Save to file
with open("balance_sheet_notes.txt", "w") as f:
    f.write(notes)
```

### Task 5: Verify Question Quality
```python
from gemini_integration import QuestionVerifier

verifier = QuestionVerifier()

report = verifier.verify_question_quality(
    question="What is the accounting equation?",
    options=["A=L+E", "A+L=E", "A=L-E", "None"],
    correct_answer="A=L+E"
)

if report.get("is_valid"):
    print("✓ Question is valid")
else:
    print("✗ Issues found:")
    for issue in report.get("issues", []):
        print(f"  - {issue}")
```

### Task 6: Enhance Your CSV File
```python
from gemini_integration import DataProcessor

processor = DataProcessor()

# Improve explanations for all questions
processor.enhance_csv_data(
    csv_file="hsc_mcq_bank_WEB_READY.csv",
    output_file="hsc_mcq_bank_ENHANCED.csv"
)
```

### Task 7: Generate a Full Practice Test
```python
from gemini_integration import create_practice_test, export_questions_to_csv

# Create 15 random questions at mixed difficulty
questions = create_practice_test(
    num_questions=15,
    difficulty="mixed",
    subject="Accounting"
)

# Export as CSV
export_questions_to_csv(questions, "practice_test.csv")

# Or create JSON file
import json

json_data = []
for q in questions:
    json_data.append({
        "question": q.text,
        "options": q.options,
        "correct_answer": q.correct_answer,
        "explanation": q.explanation,
        "difficulty": q.difficulty
    })

with open("practice_test.json", "w") as f:
    json.dump(json_data, f, indent=2)
```

### Task 8: Summarize a Chapter
```python
summarizer = ContentSummarizer()

# Read chapter from file
with open("chapter_content.txt", "r") as f:
    content = f.read()

# Get different summary lengths
brief = summarizer.summarize_chapter(content, depth="brief")
detailed = summarizer.summarize_chapter(content, depth="detailed")

print("Brief Summary:")
print(brief)
print("\nDetailed Summary:")
print(detailed)
```

### Task 9: Check for Ambiguous Questions
```python
verifier = QuestionVerifier()

ambiguity_report = verifier.check_answer_ambiguity(
    question="Which is accounting?",
    options=["Recording", "Classifying", "Summarizing", "All"],
    correct_answer="All"
)

if ambiguity_report.get("has_ambiguity"):
    print("⚠️  Question might have multiple correct answers")
    print(ambiguity_report["analysis"])
else:
    print("✓ Question is unambiguous")
```

### Task 10: Create Formula Sheet
```python
summarizer = ContentSummarizer()

formulas = summarizer.create_formula_sheet(
    topic="Profit & Loss Statement"
)

print(formulas)

# Save to file
with open("formula_sheet.txt", "w") as f:
    f.write(formulas)
```

---

## API Response Formats

### Generated Question
```python
{
    "text": "Question text here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct_answer": "Option A",
    "explanation": "Explanation text",
    "subject": "Accounting",
    "chapter": "Chapter Name",
    "difficulty": "medium"
}
```

### Evaluation Response
```python
{
    "score": 0.85,  # 0 to 1
    "feedback": "Your detailed feedback here"
}
```

### Quality Report
```python
{
    "is_valid": True,
    "clarity_score": 9,  # 1-10
    "distractors_quality": 8,  # 1-10
    "difficulty": "medium",
    "issues": ["Issue 1", "Issue 2"],
    "suggestions": ["Suggestion 1"],
    "overall_feedback": "Overall assessment"
}
```

---

## Running Full Demo
```powershell
# From project root directory
python example_usage.py
```

This will run all demonstrations including:
- ✓ Question generation
- ✓ Answer evaluation
- ✓ Content summarization
- ✓ Question verification
- ✓ Data processing
- ✓ Practice test generation

---

## Batch Processing Examples

### Process 100 Questions
```python
from gemini_integration import QuestionVerifier
import time

verifier = QuestionVerifier()
questions = [...]  # Your questions list

for i, q in enumerate(questions):
    print(f"Verifying {i+1}/100...")
    report = verifier.verify_question_quality(q.text, q.options, q.correct_answer)
    
    # Add delay to avoid rate limits
    if i % 10 == 0:
        time.sleep(2)
```

### Grade Multiple Student Answers
```python
from gemini_integration import AnswerEvaluator

evaluator = AnswerEvaluator()
student_answers = [
    {"question": "...", "answer": "...", "correct": "..."},
    # ... more answers
]

results = []
for ans in student_answers:
    score, feedback = evaluator.evaluate_mcq_answer(
        ans["question"],
        ["opt1", "opt2", "opt3", "opt4"],
        ans["answer"],
        ans["correct"]
    )
    results.append({
        "score": score,
        "feedback": feedback
    })
```

---

## Error Handling

```python
import json
from gemini_integration import setup_gemini, QuestionGenerator

try:
    setup_gemini()
    generator = QuestionGenerator()
    questions = generator.generate_mcq("Topic", "medium", 5)
    
    if not questions:
        print("⚠️  No questions generated")
    else:
        print(f"✓ Generated {len(questions)} questions")
        
except ValueError as e:
    print(f"❌ Configuration Error: {e}")
except json.JSONDecodeError as e:
    print(f"❌ Response Parsing Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
```

---

## Performance Tips

1. **Batch Similar Requests**: Generate 5 questions at once instead of 1 at a time
2. **Cache Results**: Save generated questions locally
3. **Limit Retries**: Set a reasonable timeout for API calls
4. **Use Difficulty Levels**: Vary difficulty to test different aspects
5. **Reuse Evaluator**: Create one evaluator instance for multiple evaluations

```python
# ✓ Good - One evaluator for multiple uses
evaluator = AnswerEvaluator()
for student_answer in student_answers:
    score, feedback = evaluator.evaluate_mcq_answer(...)

# ✗ Avoid - Creating new evaluator each time
for student_answer in student_answers:
    evaluator = AnswerEvaluator()  # Inefficient
    score, feedback = evaluator.evaluate_mcq_answer(...)
```

---

## Getting Help

1. Check [GEMINI_SETUP.md](GEMINI_SETUP.md) for detailed setup
2. Review [example_usage.py](example_usage.py) for working examples
3. Read [gemini_integration.py](gemini_integration.py) for full API
4. Visit [https://ai.google.dev/](https://ai.google.dev/) for Gemini docs
