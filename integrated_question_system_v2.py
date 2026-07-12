"""
Integrated Question System V2
IMPROVED: Uses DynamicQuestionFetcher for truly dynamic questions
2000+ real interview questions with actual randomization per session
"""

import random
from typing import List, Dict, Any
from official_question_bank import OfficialQuestionBank
from dynamic_question_fetcher import (
    JavaQuestionBank, SeleniumQuestionBank, TypeScriptQuestionBank
)
from coding_logic_questions import get_coding_logic_questions
from qa_process_questions import get_qa_process_questions
from playwright_js_ts_questions import get_playwright_js_ts_questions, is_playwright_selected
from universal_skills_questions import get_universal_skills_questions


class ImprovedIntegratedQuestionSystem:
    """
    Enterprise-grade question system with REAL DYNAMIC QUESTIONS
    - 2000+ questions per skill from official documentation
    - Multiple sources: Oracle, Selenium, Playwright, Stack Overflow, Tech Blogs
    - TRUE randomization per session (different questions every time)
    - Smart category-based selection
    - Session-based repetition prevention
    """

    def __init__(self):
        """Initialize improved integrated system."""
        self.official_bank = OfficialQuestionBank()
        self.session_history = {}  # Track questions asked per session

        # Initialize question banks from dynamic fetcher
        self.question_banks = {}

        # Java questions (comprehensive)
        self.question_banks['Java'] = {
            'common': JavaQuestionBank.get_common_questions(),
            'basic': JavaQuestionBank.get_basic_questions(),
            'intermediate': JavaQuestionBank.get_intermediate_questions(),
            'advanced': JavaQuestionBank.get_advanced_questions(),
            'tricks': JavaQuestionBank.get_trick_questions(),
            'version_comparison': JavaQuestionBank.get_version_comparison_questions(),
        }

        # Selenium questions (limited options)
        self.question_banks['Selenium'] = {
            'common': SeleniumQuestionBank.get_common_questions(),
            'basic': SeleniumQuestionBank.get_common_questions(),  # Use common as basic
            'intermediate': SeleniumQuestionBank.get_version_comparison(),
            'advanced': SeleniumQuestionBank.get_version_comparison(),
            'version_comparison': SeleniumQuestionBank.get_version_comparison(),
        }

        # TypeScript questions (limited options)
        self.question_banks['TypeScript'] = {
            'common': TypeScriptQuestionBank.get_recent_questions(),
            'basic': TypeScriptQuestionBank.get_recent_questions(),
            'intermediate': TypeScriptQuestionBank.get_recent_questions(),
            'advanced': TypeScriptQuestionBank.get_recent_questions(),
        }

        # Behavioral questions (general)
        self.general_questions = self._get_general_behavioral_questions()

    def get_interview_questions(
        self,
        role: str,
        skills: List[str],
        years_of_experience: float,
        difficulty: str,
        session_id: str = None,
        include_previous: bool = False,
        count: int = None
    ) -> List[Dict]:
        """
        Generate truly dynamic interview questions.

        Args:
            role: Target role (Senior Java Developer, QA Engineer, etc.)
            skills: List of primary skills (Java, Playwright, Python, etc.)
            years_of_experience: Years of experience (0-50)
            difficulty: Basic, Intermediate, Advanced, Hard
            session_id: Optional session ID for tracking
            include_previous: Whether to allow previously asked questions
            count: Number of questions to generate (25)

        Returns:
            List of unique interview questions - DIFFERENT every time
        """
        # Calculate dynamic question count based on difficulty and experience
        if count is None:
            count = self._calculate_question_count(difficulty, years_of_experience)

        all_questions = []

        print(f"\n{'='*70}")
        print(f"[INTERVIEW SETUP] Dynamic Question Count Calculation")
        print(f"{'='*70}")
        print(f"  Difficulty: {difficulty}")
        print(f"  Experience: {years_of_experience} years")
        print(f"  Calculated Question Count: {count}")
        print(f"{'='*70}\n")

        # Already-asked-question lookup for this session, applied to every
        # pool below so guaranteed-inclusion questions (coding/QA) still
        # respect include_previous like the rest of the pipeline.
        asked = set()
        if session_id and not include_previous:
            asked = self.session_history.get(session_id, {}).get('asked_questions', set())

        def _not_asked(q):
            return self._normalize_question(q.get('question', '')).lower() not in asked

        # Step 1: Reserve a fixed slice of coding/logic and QA-process
        # questions - every interview, regardless of difficulty, includes
        # a handful of each rather than only role-specific technical Qs.
        coding_target = random.randint(2, 5)
        qa_target = random.randint(5, 7)

        coding_pool = [q for q in get_coding_logic_questions(coding_target * 4, skills) if _not_asked(q)]
        qa_pool = [q for q in get_qa_process_questions(qa_target * 4) if _not_asked(q)]

        coding_selected = coding_pool[:coding_target]
        qa_selected = qa_pool[:qa_target]

        # Playwright is asked heavily whenever the candidate selects it
        # (with JS/TS or on its own) - at least 50 questions out of the
        # full interview come from this dedicated bank.
        playwright_selected = []
        if is_playwright_selected(skills):
            playwright_target = random.randint(50, 55)
            playwright_pool = [
                q for q in get_playwright_js_ts_questions(playwright_target * 2) if _not_asked(q)
            ]
            playwright_selected = playwright_pool[:playwright_target]

        # "Skills Set For All" - Jenkins/CI-CD, Agile/methodology, general
        # programming practices, framework explanation, and tricky
        # real-time scenarios - asked irrespective of the primary skill(s).
        universal_target = random.randint(15, 20)
        universal_pool = [
            q for q in get_universal_skills_questions(universal_target * 3) if _not_asked(q)
        ]
        universal_selected = universal_pool[:universal_target]

        print(f"[Question Type Coverage] Organizing questions by type")
        print(f"  - Coding/logic questions reserved: {len(coding_selected)}")
        print(f"  - QA process questions reserved: {len(qa_selected)}")
        print(f"  - Playwright questions reserved: {len(playwright_selected)}")
        print(f"  - Universal 'Skills Set For All' questions reserved: {len(universal_selected)}")

        # Step 2: Fill the rest of the interview from technical/behavioral
        # pools, sized to whatever remains of `count` after the reservation.
        # When Playwright is selected, its 50+ reservation plus the
        # universal bank already consumes most of the interview, leaving
        # only a smaller slice for the candidate's other named skill(s) -
        # matching "minimum 50 Playwright, remaining Skills Set For All".
        remaining = max(0, count - len(coding_selected) - len(qa_selected)
                         - len(playwright_selected) - len(universal_selected))
        # Behavioral pool is small and fixed (~10 total), so it's just a
        # bonus on top - the official/skill technical pools have to supply
        # nearly all of `remaining` on their own to reach the full count.
        behavioral_count = max(4, int(remaining * 0.25))
        technical_count = remaining

        print(f"  - Behavioral questions target: {behavioral_count}")
        print(f"  - Technical questions target: {technical_count}")

        # Step 3: Get skill-specific questions from dynamic fetchers
        print(f"\n[Question Generation] Getting questions for skills: {skills}")
        skill_questions = []
        for skill in skills:
            skill_qs = self._get_skill_questions(skill, difficulty)
            skill_questions.extend(skill_qs)
            print(f"  - {skill}: {len(skill_qs)} questions")

        # Step 4: Get behavioral/general questions
        behavioral = self._get_behavioral_questions(difficulty, behavioral_count)
        print(f"  - Behavioral/General: {len(behavioral)} questions")

        # Step 5: Get official bank questions for technical depth
        official = self._get_official_questions(skills, technical_count)
        print(f"  - Official Bank (Technical): {len(official)} questions")

        # Combine the filler pool (everything besides the reserved
        # coding/QA slices), dedupe, filter session history, and shuffle
        filler_pool = skill_questions + behavioral + official
        filler_pool = self._deduplicate(filler_pool)
        filler_pool = [q for q in filler_pool if _not_asked(q)]
        random.shuffle(filler_pool)
        print(f"[Question Pool] Filler pool after dedup/session-filter: {len(filler_pool)}")

        available_after_dedup = len(filler_pool)
        if available_after_dedup < remaining:
            filler_selected = filler_pool
            shortfall = remaining - available_after_dedup
            print(f"[Warning] Filler pool ({available_after_dedup}) smaller than target ({remaining})")
            print(f"[Top-up] Pulling {shortfall} more from the universal/coding banks (largest, skill-agnostic pools)")

            # Some skills (Selenium, Docker, Kubernetes, TypeScript, etc.)
            # have much thinner dedicated technical content than Java or
            # Python. Rather than accepting a much shorter interview,
            # backfill the shortfall from the universal skills and coding
            # logic banks - both large (70/28 questions) and not tied to
            # any one skill, so they can comfortably absorb the gap.
            already_ids = {
                q.get('id') for q in
                coding_selected + qa_selected + playwright_selected + universal_selected + filler_selected
            }
            topup_pool = [
                q for q in get_universal_skills_questions(200)
                if _not_asked(q) and q.get('id') not in already_ids
            ]
            topup_pool += [
                q for q in get_coding_logic_questions(200, skills)
                if _not_asked(q) and q.get('id') not in already_ids
            ]
            random.shuffle(topup_pool)
            filler_selected += topup_pool[:shortfall]
            print(f"[Top-up] Added {min(shortfall, len(topup_pool))} questions")
        else:
            filler_selected = filler_pool[:remaining]

        # Step 6: Combine reserved coding/QA/Playwright questions with the
        # filler pool and shuffle the whole set so they're interleaved,
        # not clustered.
        selected = coding_selected + qa_selected + playwright_selected + universal_selected + filler_selected
        random.shuffle(selected)
        print(f"[Result] Total selected before field-normalization: {len(selected)}")

        # Step 7: Track for this session
        if session_id:
            if session_id not in self.session_history:
                self.session_history[session_id] = {'asked_questions': set()}
            for q in selected:
                normalized = self._normalize_question(q.get('question', ''))
                self.session_history[session_id]['asked_questions'].add(normalized.lower())
            print(f"[Session History] Tracked {len(selected)} questions for session {session_id}")

        # Ensure all questions have required fields
        final_questions = []
        for idx, q in enumerate(selected, 1):
            # Make sure question has all required fields
            if not isinstance(q, dict):
                # Convert to dict if it's an object
                q = q.to_dict() if hasattr(q, 'to_dict') else {'question': str(q)}

            # Ensure required fields
            if 'id' not in q:
                q['id'] = f'q_{idx}'
            if 'section' not in q:
                q['section'] = 'General'
            if 'question' not in q:
                q['question'] = str(q.get('question_text', ''))
            if 'category' not in q:
                q['category'] = 'general'
            if 'difficulty' not in q:
                q['difficulty'] = difficulty

            final_questions.append(q)

        print(f"[Result] Selected {len(final_questions)} questions for interview")
        print(f"  - Will cover: Technical, Programming, Behavioral questions")
        print(f"  - Difficulty: {difficulty}")
        print(f"  - Mix: Basic to Advanced level questions")
        print(f"{'='*70}\n")
        return final_questions

    def _get_skill_questions(self, skill: str, difficulty: str) -> List[Dict]:
        """Get questions from skill-specific dynamic fetcher."""
        if skill not in self.question_banks:
            return []

        skill_bank = self.question_banks[skill]
        questions = []

        # Get all difficulty levels appropriate for the selected difficulty
        difficulty_levels = self._map_difficulty(difficulty)

        for level in difficulty_levels:
            if level in skill_bank:
                level_questions = skill_bank[level]
                # Convert DynamicQuestion objects to dict format
                for q in level_questions:
                    if hasattr(q, 'to_dict'):
                        questions.append(q.to_dict())
                    else:
                        questions.append(q)

        return questions

    def _get_general_behavioral_questions(self) -> List[Dict]:
        """Generate general behavioral questions."""
        return [
            {
                'id': 'behavioral_001',
                'question': 'Tell me about a time you had to debug a critical production issue. How did you approach it?',
                'section': 'Behavioral',
                'difficulty': 'Basic',
                'category': 'problem_solving'
            },
            {
                'id': 'behavioral_002',
                'question': 'How do you approach learning new technologies or frameworks?',
                'section': 'Behavioral',
                'difficulty': 'Basic',
                'category': 'learning'
            },
            {
                'id': 'behavioral_003',
                'question': 'Describe your approach to handling code reviews - both giving and receiving feedback.',
                'section': 'Behavioral',
                'difficulty': 'Intermediate',
                'category': 'collaboration'
            },
            {
                'id': 'behavioral_004',
                'question': 'How do you prioritize when you have multiple urgent tasks?',
                'section': 'Behavioral',
                'difficulty': 'Intermediate',
                'category': 'time_management'
            },
            {
                'id': 'behavioral_005',
                'question': 'Tell me about a time you disagreed with a technical decision. How did you handle it?',
                'section': 'Behavioral',
                'difficulty': 'Advanced',
                'category': 'leadership'
            },
            {
                'id': 'behavioral_006',
                'question': 'How do you mentor junior team members? Give a specific example.',
                'section': 'Behavioral',
                'difficulty': 'Advanced',
                'category': 'leadership'
            },
            {
                'id': 'behavioral_007',
                'question': 'What testing methodologies are you familiar with? How do you choose between them?',
                'section': 'Behavioral',
                'difficulty': 'Intermediate',
                'category': 'testing'
            },
            {
                'id': 'behavioral_008',
                'question': 'How do you approach creating a test strategy for a new feature?',
                'section': 'Behavioral',
                'difficulty': 'Advanced',
                'category': 'testing'
            },
            {
                'id': 'behavioral_009',
                'question': 'Describe your experience with test automation. What challenges have you faced?',
                'section': 'Behavioral',
                'difficulty': 'Intermediate',
                'category': 'automation'
            },
            {
                'id': 'behavioral_010',
                'question': 'You are assigned to test a critical feature with only 1 day before production release. How do you approach it?',
                'section': 'Behavioral',
                'difficulty': 'Advanced',
                'category': 'scenario'
            },
        ]

    def _get_behavioral_questions(self, difficulty: str, count: int) -> List[Dict]:
        """Get behavioral/general questions."""
        behavioral = []

        for q in self.general_questions[:count]:
            if hasattr(q, 'to_dict'):
                behavioral.append(q.to_dict())
            else:
                behavioral.append(q)

        return behavioral

    def _get_official_questions(self, skills: List[str], count: int) -> List[Dict]:
        """Get additional questions from official bank."""
        official = []

        for skill in skills:
            skill_questions = self.official_bank.get_questions_by_skill(skill, count // len(skills))
            official.extend(skill_questions)

        return official[:count]

    def _deduplicate(self, questions: List[Dict]) -> List[Dict]:
        """Remove duplicate questions."""
        seen = set()
        unique = []

        for q in questions:
            q_text = self._normalize_question(q.get('question', ''))
            if q_text not in seen:
                unique.append(q)
                seen.add(q_text)

        return unique

    def _normalize_question(self, text: str) -> str:
        """Normalize question text for comparison."""
        return text.strip().lower()

    def _map_difficulty(self, difficulty: str) -> List[str]:
        """Map difficulty to question bank levels."""
        mapping = {
            'Fresher': ['common', 'basic'],
            'Basic': ['common', 'basic', 'intermediate'],
            'Intermediate': ['basic', 'intermediate', 'advanced'],
            'Advanced': ['intermediate', 'advanced', 'tricks'],
            'Hard': ['advanced', 'tricks', 'version_comparison'],
            'Simple': ['common', 'basic', 'intermediate'],
        }
        return mapping.get(difficulty, ['common', 'basic', 'intermediate'])

    def _calculate_question_count(self, difficulty: str, years_of_experience: float) -> int:
        """
        Every interview targets a full 100-question set regardless of
        difficulty level or years of experience - difficulty instead
        controls which question tiers get pulled in (see _map_difficulty),
        not how many questions are asked overall.
        """
        return 100

    def clear_session_history(self, session_id: str = None):
        """Clear session history."""
        if session_id:
            if session_id in self.session_history:
                del self.session_history[session_id]
        else:
            self.session_history.clear()


# Singleton instance
_improved_system = None


def get_improved_question_system() -> ImprovedIntegratedQuestionSystem:
    """Get or create singleton instance."""
    global _improved_system
    if _improved_system is None:
        _improved_system = ImprovedIntegratedQuestionSystem()
    return _improved_system
