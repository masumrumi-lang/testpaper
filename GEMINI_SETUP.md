# Gemini Integration Setup Guide

## Quick Start

### 1. Get Your API Key
- Visit: https://aistudio.google.com
- Click "Get API key"
- Create a new API key (free tier available)
- Copy the key

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Set Up Environment
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_key_here
```

Or set environment variable:
```powershell
$env:GEMINI_API_KEY = "your_key_here"
```

### 4. Test the Setup
```python
from gemini_integration import setup_gemini
setup_gemini()
```

---

## Available Features

### 1. Question Generation
```python
from gemini_integration import QuestionGenerator

generator = QuestionGenerator()

# Generate MCQs
questions = generator.generate_mcq(
    topic="Double Entry Bookkeeping",
    difficulty="medium",
    count=5
)

# Generate conceptual questions
questions = generator.generate_conceptual_questions(
    topic="Balance Sheet",
    count=3
)
```

### 2. Answer Evaluation
```python
from gemini_integration import AnswerEvaluator

evaluator = AnswerEvaluator()

# Evaluate MCQ
score, feedback = evaluator.evaluate_mcq_answer(
    question="What is the full form of GAAP?",
    options=["Generally Accepted Accounting Principles", "..."],
    student_choice="Generally Accepted Accounting Principles",
    correct_answer="Generally Accepted Accounting Principles"
)
print(f"Score: {score}")
print(f"Feedback: {feedback}")

# Evaluate short answer
score, feedback = evaluator.evaluate_short_answer(
    question="Define depreciation",
    student_answer="Loss of value of asset over time",
    model_answer="Depreciation is the reduction in value of an asset...",
    key_points=["Systematic process", "Time period", "Useful life", "Salvage value"]
)
```

### 3. Content Summarization
```python
from gemini_integration import ContentSummarizer

summarizer = ContentSummarizer()

# Summarize chapter
summary = summarizer.summarize_chapter(
    chapter_content="Full chapter text here...",
    depth="moderate"  # brief, moderate, detailed
)

# Generate study notes
notes = summarizer.generate_study_notes(
    topic="Journal and Ledger",
    include_examples=True
)

# Create formula sheet
formulas = summarizer.create_formula_sheet(topic="Profit & Loss Statement")
```

### 4. Question Verification
```python
from gemini_integration import QuestionVerifier

verifier = QuestionVerifier()

# Verify question quality
quality_report = verifier.verify_question_quality(
    question="What is accounting?",
    options=["Recording", "Classification", "Summarization", "All of above"],
    correct_answer="All of above"
)

# Check for ambiguous answers
ambiguity_check = verifier.check_answer_ambiguity(
    question="...",
    options=["...", "..."],
    correct_answer="..."
)
```

### 5. Data Processing
```python
from gemini_integration import DataProcessor

processor = DataProcessor()

# Enhance CSV with better explanations
processor.enhance_csv_data(
    csv_file="hsc_mcq_bank_WEB_READY.csv",
    output_file="hsc_mcq_bank_ENHANCED.csv"
)

# Categorize questions
categories = processor.categorize_questions("hsc_mcq_bank_WEB_READY.csv")
```

### 6. Create Practice Tests
```python
from gemini_integration import create_practice_test, export_questions_to_csv

# Create a practice test
questions = create_practice_test(
    num_questions=10,
    difficulty="medium",
    subject="Accounting"
)

# Export to CSV
export_questions_to_csv(questions, "practice_test.csv")
```

---

## Complete Example Script

```python
import os
from dotenv import load_dotenv
from gemini_integration import (
    setup_gemini,
    QuestionGenerator,
    AnswerEvaluator,
    ContentSummarizer,
    QuestionVerifier,
    DataProcessor,
    export_questions_to_csv
)

# Load environment variables
load_dotenv()

# Initialize
setup_gemini()

# 1. Generate questions
print("Generating questions...")
generator = QuestionGenerator()
questions = generator.generate_mcq("Accounting Principles", difficulty="medium", count=3)

# 2. Evaluate a student answer
print("Evaluating answer...")
evaluator = AnswerEvaluator()
if questions:
    q = questions[0]
    score, feedback = evaluator.evaluate_mcq_answer(
        question=q.text,
        options=q.options,
        student_choice=q.options[1],  # Student picked wrong option
        correct_answer=q.correct_answer
    )
    print(f"Score: {score}")
    print(f"Feedback: {feedback}")

# 3. Generate study notes
print("Generating study notes...")
summarizer = ContentSummarizer()
notes = summarizer.generate_study_notes("Trial Balance", include_examples=True)
print(notes)

# 4. Verify question quality
print("Verifying question quality...")
verifier = QuestionVerifier()
if questions:
    q = questions[0]
    quality = verifier.verify_question_quality(q.text, q.options, q.correct_answer)
    print(quality)

# 5. Export questions
print("Exporting questions...")
export_questions_to_csv(questions, "generated_questions.csv")

print("✓ All tasks completed!")
```

---

## Costs & Limits

- **Free Tier**: 15 requests per minute, up to 1 million tokens/month
- **Pricing**: Pay-as-you-go after free tier (very cheap for testing)
- **Rate Limits**: Adjust batch sizes if you hit rate limits

---

## Troubleshooting

### "GEMINI_API_KEY not set"
- Check that `.env` file exists in project root
- Or set `$env:GEMINI_API_KEY` in PowerShell
- Verify the key is valid at https://aistudio.google.com

### "JSON decode error"
- Some responses might not be valid JSON
- The module tries to extract JSON from markdown code blocks
- If issues persist, check the raw response text in error messages

### "Rate limit exceeded"
- Reduce the number of questions per request
- Add delays between requests using `time.sleep(2)`

### Import errors
- Make sure you ran `pip install -r requirements.txt`
- Use full paths or add to PYTHONPATH if needed

---

## Next Steps

1. **Integrate with web interface**: Add a Flask/FastAPI endpoint to use Gemini for real-time question generation
2. **Batch processing**: Process your entire CSV to enhance all questions
3. **Custom categories**: Train Gemini to understand your curriculum structure
4. **Student dashboard**: Show personalized recommendations based on weak areas
5. **Auto-grading**: Implement auto-grading system for open-ended questions

---

## Resources

- [Gemini API Docs](https://ai.google.dev/)
- [Python SDK GitHub](https://github.com/google/generative-ai-python)
- [API Pricing](https://ai.google.dev/pricing)
