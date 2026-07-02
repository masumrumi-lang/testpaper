#!/usr/bin/env python3
"""
Practical Example: Using Gemini Integration for TestPaper Project
This script demonstrates all available features with real-world scenarios
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  python-dotenv not installed. Make sure GEMINI_API_KEY is set as environment variable.")

from gemini_integration import (
    setup_gemini,
    QuestionGenerator,
    AnswerEvaluator,
    ContentSummarizer,
    QuestionVerifier,
    DataProcessor,
    create_practice_test,
    export_questions_to_csv
)


def demo_question_generation():
    """Demo 1: Generate MCQ Questions"""
    print("\n" + "="*70)
    print("DEMO 1: QUESTION GENERATION")
    print("="*70)
    
    generator = QuestionGenerator()
    
    print("\n📝 Generating MCQ about 'Double Entry Bookkeeping'...")
    questions = generator.generate_mcq("Double Entry Bookkeeping", difficulty="medium", count=1)
    
    if questions:
        q = questions[0]
        print(f"\n✓ Generated Question:")
        print(f"  Q: {q.text}")
        print(f"\n  Options:")
        for i, opt in enumerate(q.options, 1):
            print(f"    {i}. {opt}")
        print(f"\n  Correct Answer: {q.correct_answer}")
        print(f"\n  Explanation: {q.explanation}")
    
    print("\n📝 Generating Conceptual Questions about 'Trial Balance'...")
    concept_q = generator.generate_conceptual_questions("Trial Balance", count=1)
    
    if concept_q:
        q = concept_q[0]
        print(f"\n✓ Generated Conceptual Question:")
        print(f"  Q: {q.text}")
        print(f"  Model Answer: {q.correct_answer}")
    
    return questions


def demo_answer_evaluation(questions):
    """Demo 2: Evaluate Student Answers"""
    print("\n" + "="*70)
    print("DEMO 2: ANSWER EVALUATION")
    print("="*70)
    
    evaluator = AnswerEvaluator()
    
    if questions:
        q = questions[0]
        
        print(f"\n❓ Question: {q.text[:100]}...")
        print(f"📋 Options: {', '.join(q.options)}")
        print(f"✓ Correct Answer: {q.correct_answer}")
        
        # Scenario 1: Correct answer
        print("\n📌 Scenario 1: Student answers CORRECTLY")
        correct_choice = q.correct_answer
        score, feedback = evaluator.evaluate_mcq_answer(q.text, q.options, correct_choice, q.correct_answer)
        print(f"   Score: {score*100:.0f}%")
        print(f"   Feedback: {feedback}")
        
        # Scenario 2: Incorrect answer
        print("\n📌 Scenario 2: Student answers INCORRECTLY")
        wrong_choice = [o for o in q.options if o != q.correct_answer][0] if len(q.options) > 1 else q.options[0]
        score, feedback = evaluator.evaluate_mcq_answer(q.text, q.options, wrong_choice, q.correct_answer)
        print(f"   Score: {score*100:.0f}%")
        print(f"   Feedback: {feedback[:300]}...")


def demo_content_summarization():
    """Demo 3: Content Summarization"""
    print("\n" + "="*70)
    print("DEMO 3: CONTENT SUMMARIZATION")
    print("="*70)
    
    summarizer = ContentSummarizer()
    
    # Sample chapter content
    chapter_content = """
    Accounting is the recording, classification, and summarization of economic transactions.
    The fundamental concepts include assets, liabilities, and equity. Every transaction must be 
    recorded following the principle of double entry bookkeeping, where each transaction affects 
    at least two accounts. The accounting equation states: Assets = Liabilities + Equity.
    """
    
    print("\n📖 Summarizing Chapter Content...")
    summary = summarizer.summarize_chapter(chapter_content, depth="moderate")
    print(f"\n✓ Summary:\n{summary}")
    
    print("\n📚 Generating Study Notes for 'Journal Entries'...")
    notes = summarizer.generate_study_notes("Journal Entries", include_examples=True)
    print(f"\n✓ Study Notes:\n{notes[:500]}...")


def demo_question_verification(questions):
    """Demo 4: Question Verification"""
    print("\n" + "="*70)
    print("DEMO 4: QUESTION VERIFICATION")
    print("="*70)
    
    verifier = QuestionVerifier()
    
    if questions:
        q = questions[0]
        
        print(f"\n🔍 Verifying Question Quality...")
        print(f"   Q: {q.text[:80]}...")
        
        quality_report = verifier.verify_question_quality(q.text, q.options, q.correct_answer)
        
        print(f"\n✓ Quality Report:")
        if "clarity_score" in quality_report:
            print(f"   Clarity Score: {quality_report.get('clarity_score', 'N/A')}/10")
            print(f"   Distractors Quality: {quality_report.get('distractors_quality', 'N/A')}/10")
            print(f"   Difficulty Level: {quality_report.get('difficulty', 'N/A')}")
            print(f"   Is Valid: {quality_report.get('is_valid', 'N/A')}")
            
            if quality_report.get('issues'):
                print(f"\n   Issues Found:")
                for issue in quality_report['issues']:
                    print(f"      • {issue}")
            
            if quality_report.get('suggestions'):
                print(f"\n   Suggestions:")
                for suggestion in quality_report['suggestions']:
                    print(f"      • {suggestion}")


def demo_data_processing():
    """Demo 5: Data Processing"""
    print("\n" + "="*70)
    print("DEMO 5: DATA PROCESSING")
    print("="*70)
    
    processor = DataProcessor()
    
    # Check if CSV file exists
    csv_path = Path(__file__).parent / "hsc_mcq_bank_WEB_READY.csv"
    
    if csv_path.exists():
        print(f"\n📊 CSV File Found: {csv_path.name}")
        print(f"   📌 Available Operations:")
        print(f"      1. Enhance CSV with better explanations")
        print(f"      2. Categorize questions by difficulty/topic")
        print(f"\n   To use: processor.enhance_csv_data('{csv_path}')")
        print(f"   Or: categories = processor.categorize_questions('{csv_path}')")
    else:
        print(f"\n⚠️  CSV file not found at {csv_path}")
        print(f"   Make sure hsc_mcq_bank_WEB_READY.csv is in the project root")


def demo_practice_test_generation():
    """Demo 6: Generate Practice Test"""
    print("\n" + "="*70)
    print("DEMO 6: PRACTICE TEST GENERATION")
    print("="*70)
    
    print("\n🎯 Generating a practice test with 10 questions...")
    questions = create_practice_test(num_questions=5, difficulty="medium", subject="Accounting")
    
    if questions:
        print(f"\n✓ Generated {len(questions)} questions")
        for i, q in enumerate(questions, 1):
            print(f"\n   {i}. {q.text[:60]}...")
            print(f"      Topic: {q.chapter}")
            print(f"      Difficulty: {q.difficulty}")
        
        # Export to CSV
        output_file = Path(__file__).parent / "practice_test_generated.csv"
        export_questions_to_csv(questions, str(output_file))
        print(f"\n✓ Exported to: {output_file.name}")


def demo_batch_evaluation():
    """Demo 7: Batch Student Evaluation"""
    print("\n" + "="*70)
    print("DEMO 7: BATCH EVALUATION SCENARIO")
    print("="*70)
    
    print("\n👥 Simulating 3 students taking a test...\n")
    
    evaluator = AnswerEvaluator()
    
    # Sample student answers
    students = [
        {
            "name": "Ahmed",
            "answer": "i & ii",
            "question": "Which of the following is correct?",
            "options": ["i & ii", "ii & iii", "i, ii & iii"],
            "correct": "ii & iii"
        },
        {
            "name": "Fatima",
            "answer": "ii & iii",
            "question": "Which of the following is correct?",
            "options": ["i & ii", "ii & iii", "i, ii & iii"],
            "correct": "ii & iii"
        },
        {
            "name": "Ali",
            "answer": "i, ii & iii",
            "question": "Which of the following is correct?",
            "options": ["i & ii", "ii & iii", "i, ii & iii"],
            "correct": "ii & iii"
        }
    ]
    
    for student in students:
        score, feedback = evaluator.evaluate_mcq_answer(
            student["question"],
            student["options"],
            student["answer"],
            student["correct"]
        )
        status = "✓ PASS" if score > 0 else "✗ FAIL"
        print(f"{status} - {student['name']}: {student['answer']} (Correct: {student['correct']})")


def main():
    """Run all demos"""
    print("\n" + "█"*70)
    print("  GEMINI AI TESTPAPER INTEGRATION - LIVE DEMO")
    print("█"*70)
    
    try:
        # Initialize Gemini
        print("\n🔌 Initializing Gemini API...")
        setup_gemini()
        print("✓ Gemini API ready!")
        
        # Run demos
        questions = demo_question_generation()
        
        if questions:
            demo_answer_evaluation(questions)
            demo_question_verification(questions)
        
        demo_content_summarization()
        demo_data_processing()
        demo_practice_test_generation()
        demo_batch_evaluation()
        
        print("\n" + "█"*70)
        print("✓ ALL DEMOS COMPLETED SUCCESSFULLY!")
        print("█"*70)
        print("\n📖 Next Steps:")
        print("   1. Read GEMINI_SETUP.md for detailed documentation")
        print("   2. Review gemini_integration.py for available classes")
        print("   3. Create your own scripts using the examples above")
        print("   4. Integrate with your web application")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print(f"\n📋 Troubleshooting:")
        print(f"   1. Make sure GEMINI_API_KEY is set (see GEMINI_SETUP.md)")
        print(f"   2. Run: pip install -r requirements.txt")
        print(f"   3. Check internet connection")
        print(f"   4. Verify API key at: https://aistudio.google.com")


if __name__ == "__main__":
    main()
