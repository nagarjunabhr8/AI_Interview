"""
Programming/Coding Logic Question Bank
Short algorithmic and logic-building problems asked verbally during the
interview (candidate describes or writes out the approach/code in the
answer box). Language-agnostic by default; phrased using the candidate's
primary language when one can be detected from their skills.
"""

import random
from typing import Dict, List, Optional


# Each question is language-agnostic; {lang} is substituted with the
# candidate's detected primary language (falls back to a neutral phrase).
CODING_LOGIC_QUESTIONS: List[Dict] = [
    {
        "id": "code_logic_001",
        "template": "Write a {lang} program/function to reverse a given number (e.g. 12345 -> 54321).",
        "expected_answer": "Repeatedly extract the last digit with modulo 10, build the reversed number, divide by 10, loop until zero. Handle negative numbers and overflow.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_002",
        "template": "Write a {lang} program to reverse a given string without using a built-in reverse function.",
        "expected_answer": "Use two pointers from start and end swapping characters, or build a new string iterating from the last index. O(n) time, O(1) or O(n) space.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_003",
        "template": "Given an array of strings, write a {lang} program to count how many times each string is duplicated.",
        "expected_answer": "Use a hash map/dictionary to count occurrences of each string, then filter entries with count > 1. O(n) time.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_004",
        "template": "Write a {lang} program to count duplicate characters in a given string.",
        "expected_answer": "Use a hash map keyed by character to tally frequency, then report characters with frequency > 1. Consider case sensitivity.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_005",
        "template": "Write a {lang} program to find the largest and smallest numbers in a given array of elements.",
        "expected_answer": "Single pass tracking running min and max, O(n) time, O(1) space. Avoid sorting for optimal complexity.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_006",
        "template": "How would you swap two integers, both with and without using a third/temporary variable, in {lang}?",
        "expected_answer": "With temp variable: store one in temp, assign, swap. Without: arithmetic (a=a+b; b=a-b; a=a-b) or XOR swap, or tuple/multiple assignment where the language supports it.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_007",
        "template": "How would you swap two strings, with and without using a third variable, in {lang}?",
        "expected_answer": "With temp variable: standard three-step swap. Without: language-specific tuple/multiple assignment (a, b = b, a) since strings can't use arithmetic swap tricks.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_008",
        "template": (
            "Given an array of strings 'patterns' and a string 'word', write a {lang} function that returns the "
            "number of strings in patterns that exist as a substring in word. Example: patterns = [\"a\",\"abc\",\"bc\",\"d\"], "
            "word = \"abc\" -> Output: 3, because \"a\", \"abc\", and \"bc\" all appear as substrings of \"abc\", but \"d\" does not."
        ),
        "expected_answer": "Iterate patterns, for each check if pattern in word (substring containment), increment counter. O(n*m) with built-in substring search, can discuss KMP for optimization.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_009",
        "template": "How many total substrings of a given string match a target substring? Explain your approach in {lang}.",
        "expected_answer": "Slide a window of the target's length across the string, compare each window, count matches. O((n-m+1)*m), or use KMP/rolling hash for O(n).",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_010",
        "template": "Write a {lang} program to find the second occurrence (index) of a given character in a string. Example: find the second occurrence of 's' in 'abcabc s appears...' style strings.",
        "expected_answer": "Iterate the string keeping a count of matches for the target character; return the index when the count reaches 2. Handle the case where it occurs fewer than twice.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_011",
        "template": "Write a {lang} program to print all Fibonacci numbers below 100.",
        "expected_answer": "Start with 0 and 1, repeatedly sum the last two values and print while the value stays below 100.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_012",
        "template": (
            "Write a {lang} program to check if two lists of strings contain exactly the same elements in the "
            "same order. Bonus: modify it to ignore order."
        ),
        "expected_answer": "Order-sensitive: compare lengths then element-by-element (or direct list equality). Order-insensitive: compare sorted copies, or compare as multisets/Counters to also account for duplicate counts.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_013",
        "template": (
            "Given two lists of integers, write a {lang} program to print the elements common to both. "
            "Example: List1 = [1,2,3,4], List2 = [3,4,5,6] -> Output: [3,4]."
        ),
        "expected_answer": "Convert one list to a set for O(1) lookups, iterate the other list keeping elements present in the set. Discuss handling duplicates if needed.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_014",
        "template": (
            "Write a {lang} program to remove duplicate elements from a list while preserving order. "
            "Example: [10,20,10,30,20] -> Output: [10,20,30]."
        ),
        "expected_answer": "Track seen elements in a set while building a result list, appending only unseen elements to preserve original order.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_015",
        "template": (
            "Given an array of strings, write a {lang} program to sort them by length. "
            "Example: [\"apple\",\"hi\",\"banana\"] -> Output: [\"hi\",\"apple\",\"banana\"]."
        ),
        "expected_answer": "Use a sort with a custom key/comparator based on string length (e.g., sorted(list, key=len)), stable sort preserves relative order for equal lengths.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_016",
        "template": (
            "Write a {lang} program to check which numbers in a list are palindromes. "
            "Example: [121, 123, 454] -> Output: [121, 454]."
        ),
        "expected_answer": "Convert each number to a string (or reverse digits mathematically) and compare with its reverse; collect the ones that match.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_017",
        "template": (
            "Write a {lang} program to print an array in reverse order without using a built-in reverse "
            "utility (e.g. no Collections.reverse()/reversed()). Example: Input: [1,2,3,4] -> Output: [4,3,2,1]."
        ),
        "expected_answer": "Iterate from the last index to the first manually, or swap elements in place from both ends toward the middle.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_018",
        "template": "Write a {lang} program to print a pyramid, right triangle, or diamond number/star pattern (candidate's choice).",
        "expected_answer": "Use nested loops: outer loop for rows, inner loops for leading spaces and characters per row, mirroring the row count for a diamond's bottom half.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_019",
        "template": "Write a {lang} program to check whether a given number is an Armstrong number.",
        "expected_answer": "An Armstrong number equals the sum of its own digits each raised to the power of the digit count (e.g. 153 = 1^3+5^3+3^3). Extract digits, raise to power of digit count, sum, compare to original.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_020",
        "template": "Write a {lang} program to check if a given string is an anagram of another string.",
        "expected_answer": "Compare sorted versions of both strings, or compare character-frequency maps/Counters; equal frequencies means anagram.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_021",
        "template": "Write a {lang} program to find the missing number in an array containing 1 to N with one number missing.",
        "expected_answer": "Use the formula sum(1..N) - sum(array), or XOR all numbers 1..N with all array elements; the result is the missing number. O(n) time, O(1) space.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_022",
        "template": "Write a {lang} program to check if a string of brackets/parentheses is balanced.",
        "expected_answer": "Use a stack: push opening brackets, pop and match on closing brackets; string is balanced if the stack is empty at the end and every pop matched.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_023",
        "template": "Write a {lang} program to check if a given number is prime.",
        "expected_answer": "Check divisibility from 2 up to sqrt(n); if none divide evenly, the number is prime. Handle n<2 as not prime.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_024",
        "template": "Write a {lang} program to compute the factorial of a number, both iteratively and recursively.",
        "expected_answer": "Iterative: loop multiplying 1..n. Recursive: n * factorial(n-1) with base case factorial(0)=1. Discuss stack depth trade-off of recursion.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_025",
        "template": "Write a {lang} program to merge two already-sorted arrays/lists into a single sorted array.",
        "expected_answer": "Two-pointer merge similar to the merge step of merge sort: compare heads of both lists, append the smaller, advance that pointer, then append any remainder. O(n+m) time.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_026",
        "template": "Explain and implement binary search on a sorted array in {lang}.",
        "expected_answer": "Maintain low/high pointers, compare target to the middle element, narrow the search range by half each iteration. O(log n) time, requires sorted input.",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_027",
        "template": "Write a {lang} program to count vowels and consonants in a given string.",
        "expected_answer": "Iterate characters, classify letters as vowels (a,e,i,o,u case-insensitive) or consonants, tally counts, ignoring non-alphabetic characters.",
        "difficulty": "Basic",
        "category": "coding_problem",
    },
    {
        "id": "code_logic_028",
        "template": "Write a {lang} program to find the greatest common divisor (GCD) and least common multiple (LCM) of two numbers.",
        "expected_answer": "Use the Euclidean algorithm for GCD (gcd(a,b) = gcd(b, a mod b)), then LCM = (a*b) / gcd(a,b).",
        "difficulty": "Intermediate",
        "category": "coding_problem",
    },
]


LANGUAGE_ALIASES = {
    "java": "Java",
    "python": "Python",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c++": "C++",
    "cpp": "C++",
    "c#": "C#",
    "csharp": "C#",
    "selenium": "Java (Selenium)",
}


def _detect_language(skills: Optional[List[str]]) -> str:
    """Map a candidate's skills to a phrasing-friendly language name."""
    if not skills:
        return "your preferred language"

    for skill in skills:
        key = skill.strip().lower()
        if key in LANGUAGE_ALIASES:
            return LANGUAGE_ALIASES[key]

    return "your preferred language"


def get_coding_logic_questions(count: int, skills: Optional[List[str]] = None) -> List[Dict]:
    """
    Select `count` random coding/logic questions, phrased for the
    candidate's primary language when one can be detected.
    """
    lang = _detect_language(skills)
    pool = random.sample(
        CODING_LOGIC_QUESTIONS, min(count, len(CODING_LOGIC_QUESTIONS))
    )

    questions = []
    for q in pool:
        questions.append({
            "id": q["id"],
            "question": q["template"].format(lang=lang),
            "expected_answer": q["expected_answer"],
            "section": "Programming/Coding",
            "difficulty": q["difficulty"],
            "category": q["category"],
        })
    return questions
