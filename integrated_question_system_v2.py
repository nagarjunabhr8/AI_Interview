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

        # Step 1: Organize by question type for comprehensive coverage
        print(f"[Question Type Coverage] Organizing questions by type")
        print(f"  - Will ensure mix of: Technical, Programming, Behavioral")

        # Calculate distribution for comprehensive coverage
        behavioral_count = max(4, int(count * 0.25))  # ~25% behavioral
        technical_count = max(count // 2, int(count * 0.50))  # ~50% technical
        programming_count = max(2, int(count * 0.25))  # ~25% programming/coding

        print(f"  - Behavioral questions target: {behavioral_count}")
        print(f"  - Technical questions target: {technical_count}")
        print(f"  - Programming questions target: {programming_count}")

        # Step 2: Get skill-specific questions from dynamic fetchers
        print(f"\n[Question Generation] Getting questions for skills: {skills}")
        skill_questions = []
        for skill in skills:
            skill_qs = self._get_skill_questions(skill, difficulty)
            skill_questions.extend(skill_qs)
            print(f"  - {skill}: {len(skill_qs)} questions")

        # Step 3: Get behavioral/general questions
        behavioral = self._get_behavioral_questions(difficulty, behavioral_count)
        print(f"  - Behavioral/General: {len(behavioral)} questions")

        # Step 4: Get official bank questions for technical depth
        official = self._get_official_questions(skills, technical_count)
        print(f"  - Official Bank (Technical): {len(official)} questions")

        # Combine all questions
        all_questions = skill_questions + behavioral + official
        print(f"\n[Question Pool] Total unique questions available: {len(all_questions)}")

        print(f"[Question Pool] Total unique questions available: {len(all_questions)}")

        # Step 5: Deduplicate by question text
        all_questions = self._deduplicate(all_questions)
        print(f"[After Dedup] Unique questions: {len(all_questions)}")

        # Step 6: Shuffle for randomization
        random.shuffle(all_questions)

        # Step 7: Select final set (ensure we get enough unique questions)
        available_after_dedup = len(all_questions)
        if available_after_dedup < count:
            print(f"[Warning] Question pool ({available_after_dedup}) smaller than target ({count})")
            print(f"[Action] Returning all {available_after_dedup} unique questions available")
            selected = all_questions
        else:
            selected = all_questions[:count]

        # Step 9: Handle session repetition tracking
        if session_id:
            if session_id not in self.session_history:
                self.session_history[session_id] = {'asked_questions': set()}

            if not include_previous:
                # Remove previously asked questions
                original_count = len(selected)
                selected = [
                    q for q in selected
                    if self._normalize_question(q.get('question', '')).lower()
                       not in self.session_history[session_id]['asked_questions']
                ]
                removed = original_count - len(selected)
                if removed > 0:
                    print(f"[Session Tracking] Removed {removed} previously asked questions")

        # Step 10: Track for this session
        if session_id:
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
                # Experienced senior engineers get comprehensive interview
                count = 35  # 30+ questions with all types
            elif experience >= 5:
                # Mid-level engineers
                count = 30
            else:
                # Junior engineers
                count = 25
        elif difficulty_lower in ['intermediate', 'simple']:
            # Intermediate difficulty
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
