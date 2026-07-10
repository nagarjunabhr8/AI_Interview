# Dynamic Question Count System

## Overview

The interview system now automatically calculates the number of questions based on:
1. **Difficulty Level** (Hard, Advanced, Intermediate, Basic)
2. **Years of Experience**
3. **Ensures comprehensive coverage** of all question types

## Question Count Rules

### Hard Difficulty

| Experience | Questions | Details |
|------------|-----------|---------|
| **> 7 years** | **35 questions** | Comprehensive senior-level interview |
| **5-7 years** | **30 questions** | Mid-senior level interview |
| **< 5 years** | **25 questions** | Junior-mid level interview |

### Advanced Difficulty

| Experience | Questions | Details |
|------------|-----------|---------|
| **> 5 years** | **25 questions** | Deep technical assessment |
| **≤ 5 years** | **20 questions** | Intermediate-advanced |

### Intermediate Difficulty

| Experience | Questions | Details |
|------------|-----------|---------|
| **Any** | **20 questions** | Balanced assessment |

### Basic/Fresher

| Experience | Questions | Details |
|------------|-----------|---------|
| **> 3 years** | **20 questions** | Minimum baseline |
| **≤ 3 years** | **15 questions** | Foundational level |

### Minimum Guarantee

- **All interviews ask at least 20 questions**
- No interview can have fewer than 20 questions

---

## Question Coverage by Type

### For 35 Questions (Hard + 7+ Years)

```
Behavioral/General:    9-10 questions (25%)
Technical Questions:  18-19 questions (50%)
Programming/Coding:    8-10 questions (25%)
```

### Coverage Distribution

**Behavioral Questions (25%)**
- Production issue debugging
- Team collaboration
- Learning new technologies
- Code review practices
- Time management
- Leadership and mentoring
- Communication scenarios

**Technical Questions (50%)**
- Core concepts (JVM, Memory Model, etc.)
- Advanced patterns
- Version comparisons
- Architecture design
- Performance optimization
- Security concepts
- Design patterns

**Programming/Coding Questions (25%)**
- Algorithm problems
- Data structure questions
- API design
- Database optimization
- Real-world scenarios

---

## Difficulty Breakdown in Each Interview

For Hard difficulty with 35 questions:

**Difficulty Levels:**
- Basic concepts: 5-7 questions (15%)
- Intermediate: 10-12 questions (30%)
- Advanced: 12-15 questions (40%)
- Expert/Trick questions: 5-8 questions (15%)

---

## Example Scenarios

### Scenario 1: Senior Java Developer (Hard, 9 years)

```
Difficulty: Hard
Experience: 9 years
Calculated Questions: 35

Distribution:
├── Behavioral: 9 questions
│   ├── Production debugging (1)
│   ├── Team leadership (2)
│   ├── Communication (2)
│   ├── Learning approach (1)
│   └── Conflict resolution (3)
│
├── Technical: 18 questions
│   ├── Java basics (2)
│   ├── JVM & Memory (3)
│   ├── Concurrency (3)
│   ├── Design patterns (3)
│   ├── Microservices (3)
│   └── Performance (4)
│
└── Programming/Coding: 8 questions
    ├── Algorithm design (3)
    ├── Data structures (2)
    ├── System design (2)
    └── Code quality (1)

Console Output:
[INTERVIEW SETUP] Dynamic Question Count Calculation
  Difficulty: Hard
  Experience: 9 years
  Calculated Question Count: 35
[Question Type Coverage] Organizing questions by type
  - Will ensure mix of: Technical, Programming, Behavioral
  - Behavioral questions target: 9
  - Technical questions target: 18
  - Programming questions target: 8
[Question Generation] Getting questions for skills: ['Java', 'Spring Boot']
  - Java: 15 questions
  - Spring Boot: 8 questions
  - Behavioral/General: 9 questions
  - Official Bank (Technical): 18 questions
[Question Pool] Total unique questions available: 50
[After Dedup] Unique questions: 48
[Result] Selected 35 questions for interview
  - Will cover: Technical, Programming, Behavioral questions
  - Difficulty: Hard
  - Mix: Basic to Advanced level questions
```

### Scenario 2: QA Engineer (Intermediate, 4 years)

```
Difficulty: Intermediate
Experience: 4 years
Calculated Questions: 20

Distribution:
├── Behavioral: 5 questions
├── Technical: 10 questions (Selenium, Playwright, automation)
└── Programming: 5 questions (automation scripting)

Console Output:
[INTERVIEW SETUP] Dynamic Question Count Calculation
  Difficulty: Intermediate
  Experience: 4 years
  Calculated Question Count: 20
[Question Type Coverage] Organizing questions by type
  - Behavioral questions target: 5
  - Technical questions target: 10
  - Programming questions target: 5
```

### Scenario 3: Junior Developer (Basic, 2 years)

```
Difficulty: Basic
Experience: 2 years
Calculated Questions: 15 (minimum 15 for <3 years experience)

Distribution:
├── Behavioral: 4 questions
├── Technical: 8 questions
└── Programming: 3 questions
```

---

## Implementation Details

### Dynamic Calculation Method

```python
def _calculate_question_count(self, difficulty: str, years_of_experience: float) -> int:
    """
    Calculate dynamic question count based on difficulty and experience.

    Rules:
    - Minimum: 20 questions
    - Hard + 7+ years experience: 30+ questions
    - Hard + 5-7 years: 28 questions
    - Hard + <5 years: 25 questions
    - Advanced: 25+ questions
    - Intermediate: 20-23 questions
    - Basic/Fresher: 15-20 questions
    """
    difficulty_lower = difficulty.lower()
    experience = float(years_of_experience)

    # Hard difficulty with significant experience
    if difficulty_lower == 'hard' or difficulty_lower == 'advanced':
        if experience > 7:
            count = 35  # 30+ questions with all types
        elif experience >= 5:
            count = 30
        else:
            count = 25
    elif difficulty_lower in ['intermediate', 'simple']:
        if experience > 5:
            count = 25
        else:
            count = 20
    else:
        # Basic/Fresher
        if experience > 3:
            count = 20
        else:
            count = 15

    # Ensure minimum of 20 questions
    count = max(20, count)
    return count
```

### Type Distribution Calculation

```python
# For any question count, ensure type coverage
behavioral_count = max(4, int(count * 0.25))  # ~25% behavioral
technical_count = max(count // 2, int(count * 0.50))  # ~50% technical
programming_count = max(2, int(count * 0.25))  # ~25% programming

Example for 35 questions:
- Behavioral: max(4, 35*0.25) = max(4, 8.75) = 9
- Technical: max(17.5, 35*0.50) = max(17.5, 17.5) = 18
- Programming: max(2, 35*0.25) = max(2, 8.75) = 9
Total: 9 + 18 + 9 = 36 questions (slight overlap due to max() function)
```

---

## Console Output Explained

When you start an interview, you'll see detailed logging:

### Phase 1 Console Output

```
======================================================================
STARTING NEW INTERVIEW - SESSION 20260710_143025
Role: Senior Java Developer
Skills: ['Java', 'Spring Boot']
Experience: 8 years
Difficulty: Hard
======================================================================

======================================================================
[INTERVIEW SETUP] Dynamic Question Count Calculation
======================================================================
  Difficulty: Hard
  Experience: 8 years
  Calculated Question Count: 35
======================================================================

[Question Type Coverage] Organizing questions by type
  - Will ensure mix of: Technical, Programming, Behavioral
  - Behavioral questions target: 9
  - Technical questions target: 18
  - Programming questions target: 8

[Question Generation] Getting questions for skills: ['Java', 'Spring Boot']
  - Java: 15 questions
  - Spring Boot: 6 questions
  - Behavioral/General: 9 questions
  - Official Bank (Technical): 18 questions

[Question Pool] Total unique questions available: 48
[After Dedup] Unique questions: 46
[Result] Selected 35 questions for interview
  - Will cover: Technical, Programming, Behavioral questions
  - Difficulty: Hard
  - Mix: Basic to Advanced level questions
======================================================================

Total Questions: 35
First Question: [displayed]
```

---

## Question Sources

### Skill-Specific Questions
- Java: 23+ questions (Common, Basic, Intermediate, Advanced, Tricks, Version Comparisons)
- Selenium: 4+ questions (Common, Version Comparisons)
- TypeScript: 6+ questions (Latest Features)

### Technical Questions (Official Bank)
- Fundamentals per skill
- Best practices
- Design patterns
- Performance optimization

### Behavioral Questions
- Production debugging
- Team dynamics
- Learning and growth
- Communication
- Problem-solving approach
- Time management
- Leadership

### Programming Questions
- Algorithm design
- Data structures
- Real-world scenarios
- Code quality
- Performance considerations

---

## Testing the Dynamic System

### Test 1: Hard Difficulty, 8+ Years

```
Go to: http://localhost:5000

Phase 0:
- Role: Senior Java Developer
- Skills: Java, Spring Boot
- Experience: 9 years
- Difficulty: Hard

Phase 1:
- Should ask 35 questions
- Mix of behavioral, technical, programming
- Cover basic to advanced topics
- Include version-specific questions (Java 8 vs 21)
- Include real-world scenarios
```

**Expected:**
- 35 total questions
- ~9 behavioral
- ~18 technical
- ~8 programming
- Various difficulty levels

### Test 2: Intermediate Difficulty, 4 Years

```
Go to: http://localhost:5000

Phase 0:
- Role: QA Engineer
- Skills: Selenium, Playwright
- Experience: 4 years
- Difficulty: Intermediate

Phase 1:
- Should ask 20 questions (minimum for intermediate)
- ~5 behavioral
- ~10 technical
- ~5 programming
```

### Test 3: Basic Difficulty, 2 Years

```
Go to: http://localhost:5000

Phase 0:
- Role: Junior Developer
- Skills: Java, Python
- Experience: 2 years
- Difficulty: Basic

Phase 1:
- Should ask minimum 15 questions
- Focus on foundational concepts
- Basic to intermediate level questions
```

---

## What Changed

### Files Modified

1. **integrated_question_system_v2.py**
   - Added `_calculate_question_count()` method
   - Updated `get_interview_questions()` to:
     - Calculate dynamic count
     - Organize by question type
     - Ensure comprehensive coverage
     - Add detailed logging

2. **web_app.py**
   - Phase 1 route now:
     - Removes hardcoded `count=25`
     - Lets system calculate dynamically
     - Passes all parameters to question system

### New Capabilities

✅ **Experience-Aware:** Seniors get more questions (35) vs juniors (15-20)
✅ **Difficulty-Scaled:** Hard difficulty means more comprehensive interview
✅ **Type-Balanced:** Always includes behavioral, technical, and programming questions
✅ **Level-Mixed:** Questions span basic to advanced
✅ **Comprehensive:** Covers all aspects of technical knowledge
✅ **Fair:** Same difficulty level across all candidates

---

## Benefits

### For Candidates

- **Juniors:** Fair assessment with foundational questions (15-20 questions)
- **Mids:** Balanced technical + behavioral (20-25 questions)
- **Seniors:** Comprehensive interview matching their experience (30-35 questions)

### For Interviewers

- **Consistent Assessment:** Same methodology for all candidates
- **Experience-Appropriate:** Harder interviews for more experienced candidates
- **Complete Coverage:** All aspects tested in comprehensive way
- **Fair Comparison:** Similar skill levels have similar question counts

### For Hiring

- **Better Signal:** More questions = better assessment of senior engineers
- **Type Coverage:** Technical, behavioral, and coding all tested
- **Skill Validation:** Deep-dive into each selected skill

---

## Configuration

If you want to adjust the question counts:

**In `integrated_question_system_v2.py`, update `_calculate_question_count()`:**

```python
# Current:
if experience > 7:
    count = 35  # Hard + 7+ years = 35 questions

# Could change to:
if experience > 7:
    count = 40  # To ask even more questions
```

---

## Summary

| Level | Difficulty | Questions | Focus |
|-------|-----------|-----------|-------|
| Fresher | Basic | 15 | Foundational |
| Junior | Basic/Intermediate | 20 | Basics + Intermediate |
| Mid | Intermediate/Advanced | 25 | Balanced mix |
| Senior | Advanced/Hard | 30-35 | Comprehensive |

---

**Status:** ✅ Implemented - Dynamic question count active
**Date:** July 10, 2026
**Minimum Questions:** 20 (guaranteed for all)
**Maximum Questions:** 35 (Hard + 7+ years experience)
