"""
Interview Session Manager
Manages interview state, response tracking, and silent scoring.
"""

import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import time


class InterviewResponse:
    """Represents a single question response."""

    def __init__(self, question_id: str, question_text: str, section: str):
        self.question_id = question_id
        self.question_text = question_text
        self.section = section
        self.answer = None
        self.is_skipped = False
        self.score = None
        self.scoring_rationale = None
        self.timestamp = None
        self.response_time_seconds = 0

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "question_id": self.question_id,
            "question_text": self.question_text,
            "section": self.section,
            "answer": self.answer,
            "is_skipped": self.is_skipped,
            "score": self.score,
            "scoring_rationale": self.scoring_rationale,
            "response_time_seconds": self.response_time_seconds,
            "timestamp": self.timestamp
        }


class InterviewSession:
    """Manages the overall interview session state and scoring."""

    def __init__(self, candidate_data: Dict[str, Any], questions: List[Dict[str, Any]]):
        """
        Initialize interview session.

        Args:
            candidate_data: Candidate profile from Phase 0
            questions: Question list from question bank
        """
        self.candidate_data = candidate_data
        self.questions = questions
        self.responses: List[InterviewResponse] = []
        self.current_question_index = 0
        self.session_start_time = None
        self.session_end_time = None

        # Scoring tracking
        self.section_scores: Dict[str, List[int]] = {}
        self.dimension_scores = {
            "technical_depth": 0,
            "problem_solving": 0,
            "communication_clarity": 0,
            "confidence_composure": 0,
            "self_awareness": 0,
            "leadership_judgment": 0
        }

    def start_session(self):
        """Mark session start time."""
        self.session_start_time = datetime.now()

    def end_session(self):
        """Mark session end time."""
        self.session_end_time = datetime.now()

    def get_elapsed_time_minutes(self) -> float:
        """Get elapsed time in minutes."""
        if not self.session_start_time:
            return 0
        end = self.session_end_time or datetime.now()
        delta = end - self.session_start_time
        return delta.total_seconds() / 60

    def record_response(self, question_id: str, answer: str, score: int = None,
                       rationale: str = None, response_time_seconds: int = None,
                       is_skipped: bool = False):
        """
        Record a response and optional score.

        Args:
            question_id: ID of the question
            answer: Candidate's answer text
            score: Optional score (0-5) - can be added later
            rationale: Optional scoring rationale
            response_time_seconds: Time taken to answer
            is_skipped: Whether the candidate skipped/didn't answer
        """
        # Find the response object or create new
        response = None
        if self.current_question_index < len(self.responses):
            response = self.responses[self.current_question_index]
        else:
            # Find question details
            question_text = "Unknown"
            section = "Unknown"
            for q in self.questions:
                if q["id"] == question_id:
                    question_text = q["question"]
                    section = q["section"]
                    break

            response = InterviewResponse(question_id, question_text, section)
            self.responses.append(response)

        # Record response details
        response.answer = answer if not is_skipped else "[SKIPPED]"
        response.is_skipped = is_skipped
        response.score = score if not is_skipped else 0
        response.scoring_rationale = rationale
        response.response_time_seconds = response_time_seconds or 0
        response.timestamp = datetime.now().isoformat()

        # Track section scores
        if response.section not in self.section_scores:
            self.section_scores[response.section] = []
        if not is_skipped and score is not None:
            self.section_scores[response.section].append(score)

        self.current_question_index += 1

    def score_response(self, response_index: int, score: int, rationale: str):
        """
        Score a response after the interview (Phase 2).

        Args:
            response_index: Index of response to score
            score: Score 0-5
            rationale: Scoring explanation
        """
        if 0 <= response_index < len(self.responses):
            self.responses[response_index].score = score
            self.responses[response_index].scoring_rationale = rationale

            # Update section tracking
            section = self.responses[response_index].section
            if section not in self.section_scores:
                self.section_scores[section] = []
            self.section_scores[section].append(score)

    def update_dimension_score(self, dimension: str, score: float):
        """Update a dimension score (1-5 scale)."""
        if dimension in self.dimension_scores:
            self.dimension_scores[dimension] = score

    def get_section_average(self, section: str) -> float:
        """Get average score for a section."""
        scores = self.section_scores.get(section, [])
        if not scores:
            return 0
        return sum(scores) / len(scores)

    def get_all_section_averages(self) -> Dict[str, float]:
        """Get average scores for all sections."""
        return {section: self.get_section_average(section)
                for section in self.section_scores.keys()}

    def calculate_overall_score(self) -> float:
        """
        Calculate overall score out of 100.
        Weighting: technical 50%, coding 20%, communication 15%, leadership 15%
        """
        # Calculate technical average (all non-coding, non-leadership questions)
        technical_scores = []
        coding_scores = []
        communication_scores = []
        leadership_scores = []

        for response in self.responses:
            if response.score is None or response.is_skipped:
                continue

            section = response.section.lower()

            if "leadership" in section:
                leadership_scores.append(response.score)
            elif "coding" in section or "programming" in section:
                coding_scores.append(response.score)
            else:
                # Treat as technical
                technical_scores.append(response.score)

        # Calculate averages (scale 0-5 to 0-100)
        tech_avg = (sum(technical_scores) / len(technical_scores) if technical_scores else 3) * 20
        coding_avg = (sum(coding_scores) / len(coding_scores) if coding_scores else 3) * 20
        comm_avg = self.dimension_scores["communication_clarity"] * 20
        leadership_avg = (sum(leadership_scores) / len(leadership_scores) if leadership_scores else 3) * 20

        # Apply weights
        overall = (tech_avg * 0.50 +
                  coding_avg * 0.20 +
                  comm_avg * 0.15 +
                  leadership_avg * 0.15)

        return overall

    def get_hiring_verdict(self, overall_score: float) -> str:
        """Map overall score to hiring verdict."""
        if overall_score >= 85:
            return "Strong Hire"
        elif overall_score >= 70:
            return "Hire"
        elif overall_score >= 55:
            return "Hire with Reservations / Needs one more round"
        else:
            return "No Hire (this round)"

    def get_progress_summary(self) -> Dict[str, Any]:
        """Get current interview progress summary."""
        total_questions = len(self.questions)
        answered = sum(1 for r in self.responses if not r.is_skipped)
        skipped = sum(1 for r in self.responses if r.is_skipped)
        remaining = total_questions - len(self.responses)

        return {
            "total_questions": total_questions,
            "answered": answered,
            "skipped": skipped,
            "remaining": remaining,
            "progress_percent": int((len(self.responses) / total_questions) * 100) if total_questions > 0 else 0,
            "elapsed_time_minutes": round(self.get_elapsed_time_minutes(), 1)
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary for JSON serialization."""
        return {
            "candidate": self.candidate_data,
            "session_start": self.session_start_time.isoformat() if self.session_start_time else None,
            "session_end": self.session_end_time.isoformat() if self.session_end_time else None,
            "elapsed_time_minutes": self.get_elapsed_time_minutes(),
            "responses": [r.to_dict() for r in self.responses],
            "section_scores": {section: {"scores": scores, "average": self.get_section_average(section)}
                              for section, scores in self.section_scores.items()},
            "dimension_scores": self.dimension_scores,
            "overall_score": self.calculate_overall_score(),
            "hiring_verdict": self.get_hiring_verdict(self.calculate_overall_score()),
            "progress": self.get_progress_summary()
        }

    def save_session(self, filename: str = "interview_session.json"):
        """Save session data to JSON file."""
        import os
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        return filepath

    def load_from_file(self, filename: str = "candidate_intake.json") -> Dict[str, Any]:
        """Load candidate data from Phase 0 JSON."""
        import os
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return {}


class InterviewTimer:
    """Manages interview timing and question pace."""

    def __init__(self, total_duration_minutes: int = 45):
        self.total_duration_minutes = total_duration_minutes
        self.start_time = None
        self.question_start_time = None
        self.answer_timeout_seconds = 120  # 2 minutes per question

    def start(self):
        """Start interview timer."""
        self.start_time = time.time()

    def start_question_timer(self):
        """Start timer for current question."""
        self.question_start_time = time.time()

    def get_elapsed_time_seconds(self) -> float:
        """Get total elapsed time."""
        if not self.start_time:
            return 0
        return time.time() - self.start_time

    def get_question_elapsed_time_seconds(self) -> float:
        """Get time spent on current question."""
        if not self.question_start_time:
            return 0
        return time.time() - self.question_start_time

    def is_question_timeout(self) -> bool:
        """Check if question answer time has exceeded limit."""
        return self.get_question_elapsed_time_seconds() > self.answer_timeout_seconds

    def get_remaining_time_minutes(self) -> float:
        """Get remaining interview time."""
        elapsed = self.get_elapsed_time_seconds() / 60
        remaining = self.total_duration_minutes - elapsed
        return max(0, remaining)

    def is_time_up(self) -> bool:
        """Check if interview time is up."""
        return self.get_remaining_time_minutes() <= 0
