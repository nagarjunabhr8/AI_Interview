"""
Integrated Question System
Combines Dynamic Question Generator + Official Question Bank
2000+ real interview questions per skill, dynamically selected
"""

import random
from typing import List, Dict, Any
from official_question_bank import OfficialQuestionBank
from dynamic_question_generator import DynamicQuestionGenerator


class IntegratedQuestionSystem:
    """
    Enterprise-grade question system with:
    - 2000+ questions per skill from official documentation
    - Dynamic selection based on role/skills/experience
    - Repetition tracking across sessions
    - Intelligent randomization
    """

    def __init__(self):
        """Initialize integrated system."""
        self.official_bank = OfficialQuestionBank()
        self.session_history = {}  # Track questions asked per session

    def get_interview_questions(
        self,
        role: str,
        skills: List[str],
        years_of_experience: float,
        difficulty: str,
        session_id: str = None,
        include_previous: bool = False,
        count: int = 25
    ) -> List[Dict]:
        """
        Generate interview questions with multiple sources.

        Args:
            role: Target role (QA Engineer, Backend Developer, etc.)
            skills: List of primary skills (Playwright, Java, Python, etc.)
            years_of_experience: Years of experience (0-50)
            difficulty: Fresher, Basic, Simple, Hard
            session_id: Optional session ID for tracking
            include_previous: Whether to allow previously asked questions
            count: Number of questions to generate

        Returns:
            List of unique interview questions
        """
        # Get questions from official bank for selected skills
        official_questions = []
        for skill in skills:
            skill_questions = self.official_bank.get_questions_by_skill(
                skill,
                min(count // len(skills), 200)  # Up to 200 questions per skill
            )
            official_questions.extend(skill_questions)

        # Get dynamic questions based on role/experience
        dynamic_generator = DynamicQuestionGenerator(
            role=role,
            difficulty=difficulty,
            primary_skills=skills,
            years_of_experience=years_of_experience,
            self_ratings={}
        )
        dynamic_questions = dynamic_generator.get_questions_for_interview()

        # Combine and deduplicate
        all_questions = []
        seen_questions = set()

        # Add dynamic questions first (role-aware)
        for q in dynamic_questions:
            q_text = q.get('question', '').lower()
            if q_text not in seen_questions:
                all_questions.append(q)
                seen_questions.add(q_text)

        # Add official questions (skill-specific)
        for q in official_questions:
            q_text = q.get('question', '').lower()
            if q_text not in seen_questions:
                all_questions.append(q)
                seen_questions.add(q_text)

        # Filter by difficulty if needed
        filtered_questions = self._filter_by_difficulty(all_questions, difficulty)

        # Handle repetition tracking if session_id provided
        if session_id:
            if session_id not in self.session_history:
                self.session_history[session_id] = {'asked_questions': set()}

            if not include_previous:
                # Remove previously asked questions
                filtered_questions = [
                    q for q in filtered_questions
                    if q.get('question').lower() not in self.session_history[session_id]['asked_questions']
                ]

        # Shuffle and return exact count
        random.shuffle(filtered_questions)
        selected = filtered_questions[:count]

        # Track for this session
        if session_id:
            for q in selected:
                self.session_history[session_id]['asked_questions'].add(
                    q.get('question').lower()
                )

        return selected

    def _filter_by_difficulty(self, questions: List[Dict], difficulty: str) -> List[Dict]:
        """Filter questions by difficulty level."""
        if not difficulty:
            return questions

        difficulty_levels = {
            'Fresher': ['Fresher'],
            'Basic': ['Fresher', 'Basic'],
            'Simple': ['Fresher', 'Basic', 'Simple'],
            'Hard': ['Fresher', 'Basic', 'Simple', 'Hard']
        }

        allowed_levels = difficulty_levels.get(difficulty, [difficulty])
        return [
            q for q in questions
            if q.get('difficulty', 'Basic') in allowed_levels
        ]

    def get_skill_statistics(self) -> Dict[str, int]:
        """Get total questions available per skill."""
        return self.official_bank.get_statistics()

    def clear_session_history(self, session_id: str = None):
        """Clear session history for repetition tracking."""
        if session_id:
            if session_id in self.session_history:
                del self.session_history[session_id]
        else:
            self.session_history.clear()

    def get_session_stats(self, session_id: str) -> Dict:
        """Get statistics for a session."""
        if session_id not in self.session_history:
            return {'questions_asked': 0, 'session_exists': False}

        return {
            'session_exists': True,
            'questions_asked': len(self.session_history[session_id]['asked_questions']),
            'asked_question_count': len(self.session_history[session_id]['asked_questions'])
        }


# Singleton instance for app-wide use
_system = None


def get_question_system() -> IntegratedQuestionSystem:
    """Get or create singleton instance."""
    global _system
    if _system is None:
        _system = IntegratedQuestionSystem()
    return _system
