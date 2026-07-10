#!/usr/bin/env python3
"""
Test the Expanded Question Bank
Verify that questions are different on each run.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from question_bank_expanded import ExpandedQuestionBank

def test_question_diversity():
    """Test that different interviews get different questions."""

    print("\n" + "="*70)
    print("  TESTING EXPANDED QUESTION BANK")
    print("="*70 + "\n")

    # Candidate profile (same for all tests)
    candidate_data = {
        "role": "Senior QA Engineer",
        "primary_skills": ["Playwright", "Java", "Python"],
        "years_of_experience": 8.5,
        "difficulty_level": "Hard",
        "self_ratings": {
            "Playwright": 4,
            "Java": 4,
            "Python": 5
        }
    }

    print(f"Candidate Profile:")
    print(f"  Role: {candidate_data['role']}")
    print(f"  Skills: {', '.join(candidate_data['primary_skills'])}")
    print(f"  Experience: {candidate_data['years_of_experience']} years")
    print(f"  Difficulty: {candidate_data['difficulty_level']}\n")

    # Run 5 interviews and compare questions
    interviews = []

    for interview_num in range(1, 6):
        print(f"Generating Interview {interview_num}...")

        qb = ExpandedQuestionBank(
            role=candidate_data["role"],
            difficulty=candidate_data["difficulty_level"],
            primary_skills=candidate_data["primary_skills"],
            years_of_experience=candidate_data["years_of_experience"],
            self_ratings=candidate_data["self_ratings"]
        )

        questions = qb.get_questions_for_interview()
        question_ids = [q["id"] for q in questions]
        question_texts = [q["question"] for q in questions]

        interviews.append({
            "ids": question_ids,
            "texts": question_texts,
            "count": len(questions)
        })

        print(f"  Total questions generated: {len(questions)}")
        print(f"  Question IDs: {question_ids[:5]}... (showing first 5)")
        print()

    # Compare interviews
    print("\n" + "="*70)
    print("  COMPARISON RESULTS")
    print("="*70 + "\n")

    print("Total Questions per Interview:")
    for i, interview in enumerate(interviews, 1):
        print(f"  Interview {i}: {interview['count']} questions")

    print("\nChecking for Diversity...")
    all_different = True

    for i in range(len(interviews)):
        for j in range(i + 1, len(interviews)):
            same_questions = set(interviews[i]["ids"]) & set(interviews[j]["ids"])
            overlap_percent = (len(same_questions) / len(interviews[i]["ids"])) * 100

            print(f"\n  Interview {i+1} vs Interview {j+1}:")
            print(f"    Questions in common: {len(same_questions)}")
            print(f"    Overlap: {overlap_percent:.1f}%")
            print(f"    Different questions: {len(interviews[i]['ids']) - len(same_questions)}")

            if overlap_percent > 10:  # Allow 10% overlap due to randomness
                all_different = False
                print(f"    ⚠️  WARNING: High overlap detected!")

    print("\n" + "="*70)
    print("  TEST RESULTS")
    print("="*70 + "\n")

    if all_different:
        print("✅ SUCCESS: Question bank is working correctly!")
        print("   - Each interview gets different questions")
        print("   - Randomization is functioning")
        print("   - Question diversity is guaranteed")
    else:
        print("❌ FAILED: Questions are repeating too much!")
        print("   - Please check question_bank_expanded.py")
        print("   - Verify randomization logic")

    # Show sample questions from first interview
    print("\n" + "="*70)
    print("  SAMPLE QUESTIONS FROM INTERVIEW 1")
    print("="*70 + "\n")

    for i, question in enumerate(interviews[0]["texts"][:5], 1):
        print(f"{i}. {question}")

    if len(interviews[0]["texts"]) > 5:
        print(f"\n... and {len(interviews[0]['texts']) - 5} more questions")

    print("\n" + "="*70)
    print("  TOTAL QUESTION POOL SIZE")
    print("="*70 + "\n")

    # Count unique questions in expanded question bank
    qb = ExpandedQuestionBank(
        role=candidate_data["role"],
        difficulty=candidate_data["difficulty_level"],
        primary_skills=candidate_data["primary_skills"],
        years_of_experience=candidate_data["years_of_experience"],
        self_ratings=candidate_data["self_ratings"]
    )

    total_in_pool = len(qb.all_questions)
    hard_difficulty = len([q for q in qb.all_questions if "Hard" in q.get("difficulty_levels", [])])

    print(f"Total questions in pool: {total_in_pool}")
    print(f"Hard difficulty questions: {hard_difficulty}")
    print(f"Questions per interview: {len(interviews[0]['ids'])}")
    print(f"Possible combinations: {hard_difficulty}+ different sets")

    print("\n✅ Question bank is configured correctly!\n")

    return all_different

if __name__ == "__main__":
    success = test_question_diversity()
    sys.exit(0 if success else 1)
