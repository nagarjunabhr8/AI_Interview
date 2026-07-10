#!/usr/bin/env python3
"""
Test Question Dynamics
Verify that each interview gets different questions
"""

from integrated_question_system import IntegratedQuestionSystem
import json

print("\n" + "="*70)
print("TESTING QUESTION DYNAMICS")
print("="*70 + "\n")

# Test parameters
role = "Senior Java Developer"
skills = ["Java", "Spring Boot"]
experience = 8
difficulty = "Hard"

print(f"Test Parameters:")
print(f"  Role: {role}")
print(f"  Skills: {skills}")
print(f"  Experience: {experience} years")
print(f"  Difficulty: {difficulty}")
print("\n" + "-"*70 + "\n")

# Test 1: Get questions from Interview 1
print("Interview 1 - Getting 5 questions...")
system = IntegratedQuestionSystem()
questions_1 = system.get_interview_questions(
    role=role,
    skills=skills,
    years_of_experience=experience,
    difficulty=difficulty,
    session_id="session_001",
    count=5
)

print(f"Got {len(questions_1)} questions:")
for i, q in enumerate(questions_1, 1):
    print(f"  {i}. {q['question'][:80]}...")

questions_1_set = {q['question'].lower() for q in questions_1}

print("\n" + "-"*70 + "\n")

# Test 2: Get questions from Interview 2 (NEW SESSION)
print("Interview 2 - Getting 5 NEW questions (different session)...")
questions_2 = system.get_interview_questions(
    role=role,
    skills=skills,
    years_of_experience=experience,
    difficulty=difficulty,
    session_id="session_002",  # Different session
    count=5
)

print(f"Got {len(questions_2)} questions:")
for i, q in enumerate(questions_2, 1):
    print(f"  {i}. {q['question'][:80]}...")

questions_2_set = {q['question'].lower() for q in questions_2}

print("\n" + "-"*70 + "\n")

# Test 3: Compare results
overlap = questions_1_set & questions_2_set
unique_1 = questions_1_set - questions_2_set
unique_2 = questions_2_set - questions_1_set

print("COMPARISON RESULTS:")
print(f"  Questions in Interview 1: {len(questions_1_set)}")
print(f"  Questions in Interview 2: {len(questions_2_set)}")
print(f"  Questions in common: {len(overlap)}")
print(f"  Unique to Interview 1: {len(unique_1)}")
print(f"  Unique to Interview 2: {len(unique_2)}")

if overlap:
    print(f"\n  [WARNING] REPEATED QUESTIONS:")
    for q in list(overlap)[:3]:
        print(f"     - {q[:60]}...")
else:
    print(f"\n  [SUCCESS] NO REPEATED QUESTIONS - Perfect!")

print("\n" + "-"*70 + "\n")

# Test 4: Try different role/skills
print("Interview 3 - Testing with DIFFERENT role and skills...")
questions_3 = system.get_interview_questions(
    role="QA Engineer",
    skills=["Playwright", "Selenium"],
    years_of_experience=5,
    difficulty="Basic",
    session_id="session_003",
    count=5
)

print(f"Got {len(questions_3)} questions for QA Engineer:")
for i, q in enumerate(questions_3, 1):
    print(f"  {i}. {q['question'][:80]}...")

questions_3_set = {q['question'].lower() for q in questions_3}
overlap_3 = questions_1_set & questions_3_set

print(f"\n  Overlap with Interview 1 (Java Dev): {len(overlap_3)}")
if overlap_3:
    print("  [NOTE] Some shared questions (expected for common topics)")
else:
    print("  [SUCCESS] Different role produces different questions")

print("\n" + "="*70)
print("CONCLUSION:")
print("="*70)

if len(overlap) == 0:
    print("[SUCCESS] DYNAMIC QUESTIONS WORKING")
    print("   - Different sessions get different questions")
    print("   - No repetition across interviews")
    print("   - System is functioning correctly")
else:
    print("[ISSUE] QUESTIONS ARE REPEATING")
    print("   - Questions are repeating across sessions")
    print("   - This may indicate caching or insufficient question pool")

print("\n")
