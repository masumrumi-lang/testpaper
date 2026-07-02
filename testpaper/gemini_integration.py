"""
Comprehensive Gemini AI Integration for TestPaper Project
Handles: Question Generation, Answer Evaluation, Content Summarization, 
Question Verification, and Data Processing
"""

import os
import json
import csv
import google.generativeai as genai
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from enum import Enum

# Configure Gemini API
def setup_gemini(api_key: str = None):
    """Initialize Gemini API"""
    if api_key is None:
        api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set. Set it via environment variable or pass it directly.")
    genai.configure(api_key=api_key)
    print("✓ Gemini API configured successfully")

def _log_token_usage(response, method_name: str):
    """Logs the token usage from a Gemini API response."""
    if hasattr(response, 'usage_metadata') and response.usage_metadata:
        usage = response.usage_metadata
        print(f"Token Usage for {method_name}:")
        print(f"  Prompt Tokens: {usage.prompt_token_count}")
        print(f"  Candidate Tokens: {usage.candidates_token_count}")
        print(f"  Total Tokens: {usage.total_token_count}")
    else:
        print(f"No usage metadata found for {method_name} response.")

class QuestionType(Enum):
    MCQ = "mcq"
    CQ = "cq"
    SHORTCQ = "shortcq"
    FULLCQ = "fullcq"


@dataclass
class Question:
    """Question data structure"""
    text: str
    options: List[str]
    correct_answer: str
    explanation: str
    subject: str
    chapter: str
    difficulty: str = "medium"


@dataclass
class StudentAnswer:
    """Student answer evaluation structure"""
    question: str
    student_answer: str
    correct_answer: str
    feedback: str = ""
    score: float = 0.0


# ==================== 1. QUESTION GENERATION ====================
class QuestionGenerator:
    """Generate new questions using Gemini"""
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_mcq(self, topic: str, difficulty: str = "medium", count: int = 1) -> List[Question]:
        """Generate multiple choice questions from a topic"""
        prompt = f"""Generate {count} multiple choice questions about "{topic}" at {difficulty} difficulty level.
        
        Format your response as a JSON array with this structure:
        [
            {{
                "question": "Question text here",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": "Option A",
                "explanation": "Why this is correct..."
            }}
        ]
        
        Requirements:
        - Questions should be clear and unambiguous
        - Options should be plausible distractors
        - Provide detailed explanations
        - For accounting topics, include calculations where relevant"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "QuestionGenerator.generate_mcq")
        questions = []
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            
            data = json.loads(json_str)
            for q in data:
                questions.append(Question(
                    text=q["question"],
                    options=q["options"],
                    correct_answer=q["correct_answer"],
                    explanation=q["explanation"],
                    subject=topic,
                    chapter=topic,
                    difficulty=difficulty
                ))
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Response: {response.text}")
        
        return questions
    
    def generate_conceptual_questions(self, topic: str, count: int = 1) -> List[Question]:
        """Generate conceptual/short answer questions"""
        prompt = f"""Generate {count} conceptual questions (short answer or definition-based) about "{topic}".
        
        Format as JSON:
        [
            {{
                "question": "Question text",
                "model_answer": "Model answer/definition",
                "key_points": ["Point 1", "Point 2", "Point 3"]
            }}
        ]"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "QuestionGenerator.generate_conceptual_questions")
        questions = []
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            
            data = json.loads(json_str)
            for q in data:
                questions.append(Question(
                    text=q["question"],
                    options=q.get("key_points", []),
                    correct_answer=q["model_answer"],
                    explanation="; ".join(q.get("key_points", [])),
                    subject=topic,
                    chapter=topic,
                    difficulty="medium"
                ))
        except json.JSONDecodeError:
            print("Error parsing conceptual questions JSON")
        
        return questions


# ==================== 2. ANSWER EVALUATION ====================
class AnswerEvaluator:
    """Evaluate student answers using Gemini"""
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def evaluate_mcq_answer(self, question: str, options: List[str], 
                          student_choice: str, correct_answer: str) -> Tuple[float, str]:
        """Evaluate MCQ answer"""
        if student_choice.lower() == correct_answer.lower():
            return 1.0, "Correct! Well done."
        else:
            prompt = f"""
            Question: {question}
            Options: {', '.join(options)}
            Student's Answer: {student_choice}
            Correct Answer: {correct_answer}
            
            Provide constructive feedback explaining why the correct answer is right
            and what the student might have misunderstood."""
            
            response = self.model.generate_content(prompt)
            _log_token_usage(response, "AnswerEvaluator.evaluate_mcq_answer (incorrect)")
            return 0.0, response.text
    
    def evaluate_short_answer(self, question: str, student_answer: str, 
                             model_answer: str, key_points: List[str]) -> Tuple[float, str]:
        """Evaluate short/conceptual answer with AI-based scoring"""
        prompt = f"""Evaluate this student's answer:
        
        Question: {question}
        
        Model Answer: {model_answer}
        
        Key Points Should Include:
        {json.dumps(key_points)}
        
        Student's Answer: {student_answer}
        
        Provide:
        1. A score out of 10
        2. Feedback on what they got right
        3. What could be improved
        4. Which key points they missed (if any)
        
        Format as JSON:
        {{
            "score": 0-10,
            "feedback": "Your feedback",
            "strengths": ["point1", "point2"],
            "improvements": ["point1", "point2"],
            "missed_points": ["point1", "point2"]
        }}"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "AnswerEvaluator.evaluate_short_answer")
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            
            data = json.loads(json_str)
            score = data.get("score", 0) / 10.0
            feedback = f"""
Score: {data.get("score", 0)}/10

Feedback: {data.get("feedback", "")}

Strengths:
{chr(10).join('- ' + s for s in data.get("strengths", []))}

Areas for Improvement:
{chr(10).join('- ' + i for i in data.get("improvements", []))}

Missed Key Points:
{chr(10).join('- ' + p for p in data.get("missed_points", []))}
            """
            return score, feedback.strip()
        except json.JSONDecodeError:
            return 0.0, response.text


# ==================== 3. CONTENT SUMMARIZATION ====================
class ContentSummarizer:
    """Summarize content using Gemini"""
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def summarize_chapter(self, chapter_content: str, depth: str = "moderate") -> str:
        """Summarize a chapter"""
        length_map = {
            "brief": "2-3 sentences",
            "moderate": "5-7 key points",
            "detailed": "comprehensive breakdown with examples"
        }
        
        prompt = f"""Summarize the following chapter content in {length_map.get(depth, length_map['moderate'])}:
        
        {chapter_content}
        
        Focus on:
        1. Main concepts
        2. Key definitions
        3. Important relationships between concepts
        4. Practical applications (especially for accounting/business topics)"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "ContentSummarizer.summarize_chapter")
        return response.text
    
    def generate_study_notes(self, topic: str, include_examples: bool = True) -> str:
        """Generate comprehensive study notes"""
        example_req = "Include 2-3 practical examples" if include_examples else "Focus on theory"
        
        prompt = f"""Create comprehensive study notes for: {topic}
        
        Structure:
        1. Definition & Scope
        2. Key Concepts (numbered list)
        3. Important Terms (with definitions)
        4. {example_req}
        5. Common Misconceptions
        6. Practice Tips
        
        Make it suitable for HSC/College level accounting/business students."""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "ContentSummarizer.generate_study_notes")
        return response.text
    
    def create_formula_sheet(self, topic: str) -> str:
        """Generate a formula sheet for a topic"""
        prompt = f"""Create a formula sheet for: {topic}
        
        Format each formula as:
        Formula Name: Formula Expression
        Where: Explanation of variables
        Example: One numerical example
        
        Include all relevant formulas and their variations."""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "ContentSummarizer.create_formula_sheet")
        return response.text


# ==================== 4. QUESTION VERIFICATION ====================
class QuestionVerifier:
    """Verify and validate questions using Gemini"""
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def verify_question_quality(self, question: str, options: List[str], 
                               correct_answer: str) -> Dict[str, Any]:
        """Verify question quality and provide suggestions"""
        prompt = f"""Analyze this MCQ for quality:
        
        Question: {question}
        Options: {json.dumps(options)}
        Correct Answer: {correct_answer}
        
        Check for:
        1. Clarity - Is the question unambiguous?
        2. Distractors - Are wrong options plausible?
        3. Difficulty - Is it appropriate?
        4. Correctness - Is the answer definitely correct?
        5. Relevance - Does it test important concepts?
        
        Format as JSON:
        {{
            "is_valid": true/false,
            "clarity_score": 1-10,
            "distractors_quality": 1-10,
            "difficulty": "easy/medium/hard",
            "issues": ["issue1", "issue2"],
            "suggestions": ["suggestion1", "suggestion2"],
            "overall_feedback": "summary"
        }}"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "QuestionVerifier.verify_question_quality")
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {"error": response.text}
    
    def check_answer_ambiguity(self, question: str, options: List[str], 
                              correct_answer: str) -> Dict[str, Any]:
        """Check if multiple answers could be correct"""
        prompt = f"""Could multiple answers be correct for this question?
        
        Question: {question}
        Options: {json.dumps(options)}
        Stated Correct Answer: {correct_answer}
        
        Analyze if any other options could also be justified as correct.
        
        Format as JSON:
        {{
            "has_ambiguity": true/false,
            "analysis": "detailed analysis",
            "problematic_options": ["option1"],
            "recommendation": "keep/revise/reject"
        }}"""
        
        response = self.model.generate_content(prompt)
        _log_token_usage(response, "QuestionVerifier.check_answer_ambiguity")
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {"error": response.text}


# ==================== 5. DATA PROCESSING ====================
class DataProcessor:
    """Process and enhance data using Gemini"""
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def enhance_csv_data(self, csv_file: str, output_file: str = None):
        """Enhance CSV with better explanations"""
        if output_file is None:
            output_file = csv_file.replace(".csv", "_enhanced.csv")
        
        rows = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        enhanced_rows = []
        for i, row in enumerate(rows):
            print(f"Processing row {i+1}/{len(rows)}...")
            
            if not row.get("Explanation") or len(row.get("Explanation", "")) < 20:
                prompt = f"""Provide a detailed explanation for this question:
                
Question: {row.get('Question', '')}
Correct Answer: {row.get('Answer', '')}
Subject: {row.get('Subject', '')}

Explanation should be 2-3 sentences, clear and educational."""
                
                response = self.model.generate_content(prompt)
                _log_token_usage(response, f"DataProcessor.enhance_csv_data (row {i+1})")
                row["Explanation"] = response.text
            
            enhanced_rows.append(row)
        
        # Write enhanced data
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(enhanced_rows)
        
        print(f"✓ Enhanced data saved to {output_file}")
        return output_file
    
    def categorize_questions(self, csv_file: str) -> Dict[str, List[Dict]]:
        """Categorize questions by difficulty and topic"""
        prompt = """Analyze these questions and categorize them by:
1. Difficulty level (Easy, Medium, Hard)
2. Topic/Concept
3. Question Type (Calculation, Conceptual, Application, Analysis)

Questions to analyze:
{questions_text}

Return as JSON with structure:
{{
    "categories": {{
        "by_difficulty": {{}},
        "by_topic": {{}},
        "by_type": {{}}
    }}
}}"""
        
        # Read CSV and extract questions
        questions = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                questions.append(row.get('Question', ''))
        
        questions_text = "\n".join(questions[:50])  # Limit to first 50 for API
        
        full_prompt = prompt.format(questions_text=questions_text)
        response = self.model.generate_content(full_prompt)
        _log_token_usage(response, "DataProcessor.categorize_questions")
        
        try:
            json_str = response.text.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1].replace("json", "").strip()
            return json.loads(json_str)
        except json.JSONDecodeError:
            print(f"Error parsing categorization: {response.text}")
            return {}


# ==================== UTILITY FUNCTIONS ====================
def create_practice_test(num_questions: int = 10, difficulty: str = "mixed", 
                        subject: str = "Accounting") -> List[Question]:
    """Create a practice test with random questions"""
    generator = QuestionGenerator()
    topics = [
        "Journal and Ledger",
        "Trial Balance",
        "Profit and Loss",
        "Balance Sheet",
        "Banking Transactions"
    ]
    
    questions = []
    per_topic = num_questions // len(topics)
    
    for topic in topics:
        questions.extend(generator.generate_mcq(topic, difficulty, per_topic))
    
    return questions[:num_questions]


def export_questions_to_csv(questions: List[Question], filename: str):
    """Export generated questions to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Subject', 'Chapter', 'Question', 'Options', 'Correct_Answer', 
                     'Explanation', 'Difficulty']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for q in questions:
            writer.writerow({
                'Subject': q.subject,
                'Chapter': q.chapter,
                'Question': q.text,
                'Options': ' | '.join(q.options),
                'Correct_Answer': q.correct_answer,
                'Explanation': q.explanation,
                'Difficulty': q.difficulty
            })
    
    print(f"✓ Questions exported to {filename}")


# ==================== MAIN EXECUTION EXAMPLE ====================
if __name__ == "__main__":
    # Set your API key
    # os.environ["GEMINI_API_KEY"] = "your_api_key_here"
    
    # Initialize Gemini
    setup_gemini()
    
    print("\n" + "="*60)
    print("GEMINI TESTPAPER INTEGRATION - DEMO")
    print("="*60)
    
    # 1. Question Generation
    print("\n1. GENERATING MCQ QUESTIONS...")
    generator = QuestionGenerator()
    questions = generator.generate_mcq("Double Entry Bookkeeping", difficulty="medium", count=2)
    for q in questions:
        print(f"\n📝 Q: {q.text}")
        print(f"   Options: {q.options}")
        print(f"   Answer: {q.correct_answer}")
        print(f"   💡 {q.explanation[:100]}...")
    
    # 2. Answer Evaluation
    print("\n\n2. EVALUATING STUDENT ANSWERS...")
    evaluator = AnswerEvaluator()
    if questions:
        q = questions[0]
        score, feedback = evaluator.evaluate_mcq_answer(q.text, q.options, 
                                                        q.options[0], q.correct_answer)
        print(f"Score: {score}")
        print(f"Feedback: {feedback[:200]}...")
    
    # 3. Content Summarization
    print("\n\n3. SUMMARIZING CONTENT...")
    summarizer = ContentSummarizer()
    summary = summarizer.summarize_chapter(
        "Accounting is the recording, classification, and summarization of economic transactions...",
        depth="moderate"
    )
    print(f"Summary: {summary[:300]}...")
    
    # 4. Question Verification
    print("\n\n4. VERIFYING QUESTION QUALITY...")
    verifier = QuestionVerifier()
    if questions:
        q = questions[0]
        quality = verifier.verify_question_quality(q.text, q.options, q.correct_answer)
        print(f"Quality Check: {json.dumps(quality, indent=2)[:300]}...")
    
    # 5. Data Processing
    print("\n\n5. DATA PROCESSING...")
    processor = DataProcessor()
    print("   → Ready to process CSV files")
    print("   → Can enhance explanations")
    print("   → Can categorize questions")
    
    print("\n" + "="*60)
    print("✓ All Gemini integrations ready!")
    print("="*60)
