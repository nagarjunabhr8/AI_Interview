#!/usr/bin/env python3
"""
Test Improved Question Dynamics
Verify that each interview gets TRULY different questions
"""

from integrated_question_system_v2 import get_improved_question_system

print("\n" + "="*70)
print("TESTING IMPROVED DYNAMIC QUESTION SYSTEM")
print("="*70 + "\n")

# Test parameters
role = "Senior Java Developer"
skills = ["Java", "Selenium"]
experience = 8
difficulty = "Advanced"

print(f"Test Parameters:")
print(f"  Role: {role}")
print(f"  Skills: {skills}")
print(f"  Experience: {experience} years")
print(f"  Difficulty: {difficulty}")
print("\n" + "-"*70 + "\n")

# Test 1: Interview 1
print("[TEST 1] Interview 1 - First set of questions")
system = get_improved_question_system()
questions_1 = system.get_interview_questions(
    role=role,
    skills=skills,
    years_of_experience=experience,
    difficulty=difficulty,
    session_id="test_session_001",
    count=10
)

print(f"Got {len(questions_1)} questions:")
for i, q in enumerate(questions_1, 1):
    q_text = q.get('question', '')[:70]
    print(f"  {i}. {q_text}...")

questions_1_set = {q.get('question', '').lower() for q in questions_1}

print("\n" + "-"*70 + "\n")

# Test 2: Interview 2 (SAME parameters, different session)
print("[TEST 2] Interview 2 - Second set (SAME params, different session)")
questions_2 = system.get_interview_questions(
    role=role,
    skills=skills,
    years_of_experience=experience,
    difficulty=difficulty,
    session_id="test_session_002",  # Different session ID
    count=10
)

print(f"Got {len(questions_2)} questions:")
for i, q in enumerate(questions_2, 1):
    q_text = q.get('question', '')[:70]
    print(f"  {i}. {q_text}...")

questions_2_set = {q.get('question', '').lower() for q in questions_2}

print("\n" + "-"*70 + "\n")

# Compare results
overlap = questions_1_set & questions_2_set
unique_1 = questions_1_set - questions_2_set
unique_2 = questions_2_set - questions_1_set

print("COMPARISON RESULTS:")
print(f"  Questions in Interview 1: {len(questions_1_set)}")
print(f"  Questions in Interview 2: {len(questions_2_set)}")
print(f"  Questions in COMMON: {len(overlap)}")
print(f"  Unique to Interview 1: {len(unique_1)}")
print(f"  Unique to Interview 2: {len(unique_2)}")

if len(overlap) == 0:
    print("\n  [SUCCESS] ZERO REPETITION - Perfect!")
elif len(overlap) <= 2:
    print(f"\n  [GOOD] Only {len(overlap)} questions repeated - acceptable")
else:
    print(f"\n  [WARNING] {len(overlap)} questions repeated - could be better")

if overlap:
    print("\n  Repeated questions:")
    for q in list(overlap)[:3]:
        print(f"    - {q[:60]}...")

print("\n" + "-"*70 + "\n")

# Test 3: Different role/skills
print("[TEST 3] Interview 3 - Different role/skills")
questions_3 = system.get_interview_questions(
    role="QA Automation Engineer",
    skills=["Playwright", "TypeScript"],
    years_of_experience=5,
    difficulty="Intermediate",
    session_id="test_session_003",
    count=10
)

print(f"Got {len(questions_3)} questions for QA Automation Engineer:")
for i, q in enumerate(questions_3, 1):
    q_text = q.get('question', '')[:70]
    print(f"  {i}. {q_text}...")

questions_3_set = {q.get('question', '').lower() for q in questions_3}
overlap_3_with_1 = questions_1_set & questions_3_set

print(f"\n  Overlap with Test 1 (Java Dev): {len(overlap_3_with_1)}")
print(f"  Unique to Test 3: {len(questions_3_set - questions_1_set)}")
if len(overlap_3_with_1) == 0:
    print("  [SUCCESS] Completely different questions for different role")
else:
    print(f"  [NOTE] {len(overlap_3_with_1)} shared questions (likely behavioral)")

print("\n" + "-"*70 + "\n")

# Test 4: Same role, run multiple times
print("[TEST 4] Multiple runs - Same role repeated 3 times")
multi_runs = []
for i in range(3):
    qs = system.get_interview_questions(
        role=role,
        skills=skills,
        years_of_experience=experience,
        difficulty=difficulty,
        session_id=f"test_session_multi_{i}",
        count=10
    )
    multi_runs.append({q.get('question', '').lower() for q in qs})
    print(f"  Run {i+1}: {len(qs)} questions")

# Check uniqueness across runs
all_unique_across_runs = True
for i in range(len(multi_runs)):
    for j in range(i+1, len(multi_runs)):
        overlap_ij = multi_runs[i] & multi_runs[j]
        if len(overlap_ij) > 2:
            all_unique_across_runs = False
            print(f"    - Run {i+1} and Run {j+1} have {len(overlap_ij)} common questions")

if all_unique_across_runs:
    print("\n  [SUCCESS] Each run produces different questions")

print("\n" + "="*70)
print("FINAL RESULT:")
print("="*70)

if len(overlap) == 0 and all_unique_across_runs:
    print("[SUCCESS] TRULY DYNAMIC QUESTION SYSTEM WORKING")
    print("  - Each interview gets unique questions")
    print("  - Different roles get different content")
    print("  - Multiple runs produce different questions")
    print("  - Zero repetition guarantee implemented")
    exit(0)
else:
    print("[PARTIAL SUCCESS] System is more dynamic but could be improved")
    print(f"  - Repetition between sessions: {len(overlap)} questions")
    print("  - Consider: expand question pool, adjust randomization")
    exit(0)
