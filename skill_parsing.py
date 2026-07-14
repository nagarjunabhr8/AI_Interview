"""
Skill Input Parsing
Parses the candidate's free-text "Primary Skills" field into individual
skill names. The UI asks for comma-separated input, but candidates often
type natural-language phrasing instead (e.g. "Playwright JavaScript and
TypeScript" with no commas at all) - naive comma-splitting turns that
into one giant "skill" string that never matches anything downstream
(no Playwright reservation, no skill-specific technical questions, no
per-language phrasing), silently degrading the whole interview to
generic content only.
"""

import re
from typing import List

# Known skill keywords the rest of the app recognizes (SKILL_QUESTIONS_MAP
# keys, dynamic_question_fetcher banks, Playwright/language detection,
# etc.) plus other commonly-typed technologies. Longer/more specific
# names are matched before shorter overlapping ones (e.g. "Node.js"
# before a bare "Node", "C++"/"C#" before a bare "C").
KNOWN_SKILLS = [
    "JavaScript", "TypeScript", "Playwright", "Selenium", "Kubernetes",
    "Python", "Java", "Docker", "Cypress", "Jenkins",
    "React", "Angular", "Node.js", "MongoDB", "PostgreSQL", "MySQL",
    "AWS", "Azure", "GCP", "SQL", "HTML", "CSS", "Git", "JUnit", "TestNG",
    "Cucumber", "C++", "C#", "Go", "Ruby", "PHP", "Rust", "Kotlin", "Swift",
    "Rest Assured", "RestAssured", "Postman", "API Testing", "API",
]

_SORTED_SKILLS = sorted(KNOWN_SKILLS, key=len, reverse=True)
_SKILL_PATTERN = re.compile(
    r'(?<!\w)(' + '|'.join(re.escape(s) for s in _SORTED_SKILLS) + r')(?!\w)',
    re.IGNORECASE
)
_CANONICAL = {s.lower(): s for s in KNOWN_SKILLS}


def parse_skills(raw_text: str) -> List[str]:
    """
    Parse a free-text skills field into individual skill names.

    Handles the documented comma-separated format ("Playwright, Java")
    as well as natural-language phrasing without commas ("Playwright
    JavaScript and TypeScript") by recognizing known skill keywords
    embedded in the text. Segments that don't match any known keyword
    are kept as-typed so custom/unlisted skills (e.g. "REST APIs")
    still work.
    """
    if not raw_text or not raw_text.strip():
        return []

    segments = [s.strip() for s in raw_text.split(',') if s.strip()]
    skills: List[str] = []

    for segment in segments:
        matches = _SKILL_PATTERN.findall(segment)
        if matches:
            skills.extend(_CANONICAL[m.lower()] for m in matches)
        else:
            skills.append(segment)

    # De-duplicate while preserving first-seen order and casing.
    seen = set()
    unique_skills = []
    for s in skills:
        key = s.lower()
        if key not in seen:
            seen.add(key)
            unique_skills.append(s)
    return unique_skills
