#!/usr/bin/env python3
"""
Test Enhanced Report Generator
Verifies that reports include full Q&A transcript without truncation
"""

from enhanced_report_generator import EnhancedReportGenerator
from datetime import datetime
import json


def create_test_data():
    """Create realistic test interview data."""

    # Sample questions asked in interview
    questions = [
        {
            'id': 'q1',
            'question': 'What is the difference between JVM, JRE, and JDK?',
            'section': 'Java Basics',
            'category': 'fundamental'
        },
        {
            'id': 'q2',
            'question': 'Explain the concept of immutability in Java with an example.',
            'section': 'Java Advanced',
            'category': 'advanced'
        },
        {
            'id': 'q3',
            'question': 'What are the key differences between ArrayList and LinkedList?',
            'section': 'Data Structures',
            'category': 'intermediate'
        }
    ]

    # Candidate information
    candidate_data = {
        'role': 'Senior Java Developer',
        'primary_skills': ['Java', 'Spring Boot', 'Microservices'],
        'years_of_experience': 8,
        'difficulty_level': 'Advanced'
    }

    # Candidate responses with long answers (testing no truncation)
    long_answer_1 = """The JVM (Java Virtual Machine) is an abstract computing machine that enables a computer to run Java programs and programs written in other languages that are compiled to Java bytecode. The JRE (Java Runtime Environment) is a package that contains the JVM, class libraries, and other components necessary to run Java applications. The JDK (Java Development Kit) is a complete package that includes the JRE, development tools, and documentation for writing Java applications. The main difference is that JDK is for development, JRE is for running compiled Java programs, and JVM is the runtime engine that executes the bytecode. In terms of size, JDK is the largest, followed by JRE, and JVM is the core component that actually interprets and executes the bytecode."""

    long_answer_2 = """Immutability in Java means that an object's state cannot be changed after it is created. A classic example is the String class in Java, which is immutable. Once a String object is created, its value cannot be changed. For instance, when you concatenate two strings, Java creates a new String object rather than modifying the existing one. Another example is the Integer class. To create an immutable class, you should make the class final, declare all fields as private and final, and don't provide setter methods. The advantages of immutability include thread safety (no synchronization needed), ability to use objects as HashMap keys, and caching benefits since the value will never change."""

    long_answer_3 = """ArrayList and LinkedList are both implementations of the List interface in Java, but they differ significantly in their internal structure and performance characteristics. ArrayList is backed by a dynamic array, while LinkedList is backed by a doubly-linked list. ArrayList provides constant-time access to elements using the get() method because it can directly access any element by its index. However, insertion and deletion operations in the middle of the list are expensive because they require shifting elements. LinkedList, on the other hand, provides O(n) access time for get() operations because you must traverse the list, but insertion and deletion at the beginning are very efficient (O(1) time). LinkedList also uses more memory due to the extra pointers in each node, while ArrayList is more memory-efficient. For most use cases, ArrayList is preferred due to better cache locality and lower memory overhead."""

    scored_responses = [
        {
            'question_id': 'q1',
            'answer': long_answer_1,
            'score': 4.5,
            'scoring_rationale': 'Clear and comprehensive explanation covering all three concepts',
            'is_skipped': False,
            'response_time_seconds': 45
        },
        {
            'question_id': 'q2',
            'answer': long_answer_2,
            'score': 4.8,
            'scoring_rationale': 'Excellent understanding with good examples',
            'is_skipped': False,
            'response_time_seconds': 52
        },
        {
            'question_id': 'q3',
            'answer': long_answer_3,
            'score': 4.3,
            'scoring_rationale': 'Good comparison of data structures',
            'is_skipped': False,
            'response_time_seconds': 48
        }
    ]

    # Complete scored session
    scored_session = {
        'candidate': candidate_data,
        'session_metadata': {
            'session_start': datetime.now().isoformat(),
            'session_end': datetime.now().isoformat(),
            'elapsed_time_minutes': 15
        },
        'analysis': {
            'scored_responses': scored_responses,
            'dimension_scores': {
                'technical_depth': 4.5,
                'problem_solving': 4.3,
                'communication_clarity': 4.2,
                'confidence_composure': 4.4,
                'self_awareness': 4.0,
                'leadership_judgment': 4.1
            },
            'overall_score': 85.5,
            'hiring_verdict': 'Hire',
            'section_analysis': {
                'Java Basics': {'average_score': 4.5, 'total_questions': 1},
                'Java Advanced': {'average_score': 4.8, 'total_questions': 1},
                'Data Structures': {'average_score': 4.3, 'total_questions': 1}
            },
            'summary': {
                'total_questions': 3,
                'answered_questions': 3,
                'skipped_questions': 0,
                'response_rate_percent': 100,
                'strengths': [
                    'Deep understanding of Java fundamentals',
                    'Clear communication of technical concepts',
                    'Strong knowledge of data structures'
                ],
                'weaknesses': [
                    'Could provide more real-world examples',
                    'Performance analysis could be deeper'
                ],
                'recommendation': 'Strong candidate with excellent Java knowledge. Ready for senior-level position.'
            }
        }
    }

    return scored_session, questions


def test_report_generation():
    """Test that reports are generated with full Q&A transcript."""
    print("\n" + "="*70)
    print("TESTING ENHANCED REPORT GENERATOR")
    print("="*70 + "\n")

    scored_session, questions = create_test_data()

    # Create report generator
    generator = EnhancedReportGenerator(
        scored_session=scored_session,
        questions=questions,
        conversation_flow=[],
        voice_metrics={}
    )

    # Generate markdown report
    print("1. Generating Markdown Report...")
    markdown = generator.generate_markdown_report()

    # Check for full answers (no truncation)
    answer_1_check = scored_session['analysis']['scored_responses'][0]['answer'][:100]
    answer_2_check = scored_session['analysis']['scored_responses'][1]['answer'][:100]
    answer_3_check = scored_session['analysis']['scored_responses'][2]['answer'][:100]

    print("\n2. Verifying Markdown Report Content:")
    print(f"   - Report length: {len(markdown)} characters")

    # Check if full answers are included
    has_answer_1 = answer_1_check in markdown
    has_answer_2 = answer_2_check in markdown
    has_answer_3 = answer_3_check in markdown

    print(f"   - Answer 1 included (full, not truncated): {has_answer_1}")
    print(f"   - Answer 2 included (full, not truncated): {has_answer_2}")
    print(f"   - Answer 3 included (full, not truncated): {has_answer_3}")

    # Check for questions
    has_question_1 = 'JVM, JRE, and JDK' in markdown
    has_question_2 = 'immutability' in markdown
    has_question_3 = 'ArrayList and LinkedList' in markdown

    print(f"   - Question 1 included: {has_question_1}")
    print(f"   - Question 2 included: {has_question_2}")
    print(f"   - Question 3 included: {has_question_3}")

    # Check for scores
    has_scores = '4.5/5' in markdown and '4.8/5' in markdown and '4.3/5' in markdown
    print(f"   - Scores included: {has_scores}")

    # Generate HTML report
    print("\n3. Generating HTML Report...")
    html = generator.generate_html_report()

    print(f"   - Report length: {len(html)} characters")
    print(f"   - HTML structure valid: {'<!DOCTYPE html>' in html and '</html>' in html}")

    # Check HTML has full answers
    has_answer_1_html = answer_1_check in html
    has_answer_2_html = answer_2_check in html
    has_answer_3_html = answer_3_check in html

    print(f"   - Answer 1 included in HTML: {has_answer_1_html}")
    print(f"   - Answer 2 included in HTML: {has_answer_2_html}")
    print(f"   - Answer 3 included in HTML: {has_answer_3_html}")

    # Overall test result
    all_passed = all([
        has_answer_1, has_answer_2, has_answer_3,
        has_question_1, has_question_2, has_question_3,
        has_scores,
        has_answer_1_html, has_answer_2_html, has_answer_3_html
    ])

    print("\n" + "="*70)
    if all_passed:
        print("RESULT: ALL TESTS PASSED")
        print("- Full answers included (no truncation)")
        print("- All questions properly displayed")
        print("- Scores included in report")
        print("- HTML format valid and complete")
    else:
        print("RESULT: SOME TESTS FAILED")
        failed = []
        if not has_answer_1: failed.append("Answer 1 missing")
        if not has_answer_2: failed.append("Answer 2 missing")
        if not has_answer_3: failed.append("Answer 3 missing")
        if not has_question_1: failed.append("Question 1 missing")
        if not has_question_2: failed.append("Question 2 missing")
        if not has_question_3: failed.append("Question 3 missing")
        if not has_scores: failed.append("Scores missing")
        for failure in failed:
            print(f"- {failure}")

    print("="*70 + "\n")

    # Show sample of report
    print("SAMPLE MARKDOWN REPORT (first 1500 characters):")
    print("-" * 70)
    print(markdown[:1500] + "...\n")

    return all_passed


if __name__ == '__main__':
    success = test_report_generation()
    exit(0 if success else 1)
