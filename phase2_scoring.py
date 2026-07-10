#!/usr/bin/env python3
"""
PHASE 2 — SCORING & ANALYSIS
Interview Agent: Evaluate all responses, score dimensions, and calculate overall performance.
"""

import json
import os
import sys
from typing import Dict, Any, List
from interview_session import InterviewSession, InterviewResponse
from scoring_evaluator import ScoringEvaluator


class ScoringAnalyzer:
    """Analyzes interview responses and produces comprehensive scoring."""

    def __init__(self, session_data: Dict[str, Any], questions: List[Dict[str, Any]]):
        """
        Initialize scoring analyzer.

        Args:
            session_data: Interview session data from Phase 1
            questions: Question bank from Phase 1
        """
        self.session_data = session_data
        self.questions = questions
        self.evaluator = ScoringEvaluator()
        self.scored_session = None

    def analyze_all_responses(self) -> Dict[str, Any]:
        """
        Score all responses and produce comprehensive analysis.

        Returns:
            Updated session data with scores and analysis
        """
        responses = self.session_data.get("responses", [])
        candidate = self.session_data.get("candidate", {})

        print("\n" + "="*70)
        print("  PHASE 2 — SCORING & ANALYSIS")
        print("="*70 + "\n")

        print("Evaluating responses...\n")

        # Score each response
        section_scores = {}
        scored_responses = []

        for idx, response_data in enumerate(responses, 1):
            # Find the original question
            question = self._find_question(response_data.get("question_id"))
            if not question:
                continue

            # Score this response
            score, rationale = self.evaluator.score_response(response_data, question)

            # Update response with score
            response_data["score"] = score
            response_data["scoring_rationale"] = rationale

            scored_responses.append(response_data)

            # Track by section
            section = response_data.get("section", "Unknown")
            if section not in section_scores:
                section_scores[section] = []
            if not response_data.get("is_skipped"):
                section_scores[section].append(score)

            # Print progress
            if idx % 5 == 0:
                print(f"  ✓ Scored {idx}/{len(responses)} responses...")

        print(f"  ✓ Completed scoring all {len(responses)} responses.\n")

        # Calculate section averages
        section_analysis = self._analyze_sections(section_scores)

        # Calculate dimension scores
        dimension_scores = self._evaluate_dimensions(scored_responses, candidate)

        # Calculate overall score
        overall_score = self._calculate_overall_score(section_scores, dimension_scores)
        verdict = self._get_hiring_verdict(overall_score)

        # Build analysis report
        analysis = {
            "scored_responses": scored_responses,
            "section_analysis": section_analysis,
            "dimension_scores": dimension_scores,
            "overall_score": overall_score,
            "hiring_verdict": verdict,
            "summary": self._generate_summary(section_analysis, dimension_scores, overall_score)
        }

        return analysis

    def _find_question(self, question_id: str) -> Dict[str, Any]:
        """Find a question by ID."""
        for question in self.questions:
            if question.get("id") == question_id:
                return question
        return None

    def _analyze_sections(self, section_scores: Dict[str, List[int]]) -> Dict[str, Any]:
        """Analyze performance by section."""
        section_analysis = {}

        for section, scores in section_scores.items():
            if not scores:
                avg = 0
                count = 0
            else:
                avg = sum(scores) / len(scores)
                count = len(scores)

            section_analysis[section] = {
                "average_score": round(avg, 2),
                "total_questions": count,
                "scores": scores,
                "performance_level": self._performance_level(avg)
            }

        return section_analysis

    def _evaluate_dimensions(self, responses: List[Dict[str, Any]], candidate: Dict[str, Any]) -> Dict[str, float]:
        """Evaluate performance across dimensions."""
        dimensions = {}

        # Technical Depth (average of all technical question scores)
        technical_scores = [
            r.get("score", 3) for r in responses
            if not r.get("is_skipped") and "fundamentals" in r.get("section", "").lower()
        ]
        dimensions["technical_depth"] = round(
            sum(technical_scores) / len(technical_scores) if technical_scores else 3, 2
        )

        # Problem-Solving / Coding Ability
        coding_scores = [
            r.get("score", 3) for r in responses
            if not r.get("is_skipped") and "coding" in r.get("section", "").lower()
        ]
        dimensions["problem_solving"] = round(
            sum(coding_scores) / len(coding_scores) if coding_scores else 3, 2
        )

        # Communication Clarity (evaluated across all answers)
        dimensions["communication_clarity"] = round(
            self.evaluator.evaluate_communication(responses), 2
        )

        # Confidence & Composure
        dimensions["confidence_composure"] = round(
            self.evaluator.evaluate_confidence(responses), 2
        )

        # Self-Awareness (self-ratings vs actual performance)
        dimensions["self_awareness"] = round(
            self.evaluator.evaluate_self_awareness(candidate, responses), 2
        )

        # Leadership & Stakeholder Judgment (if applicable)
        leadership_scores = [
            r.get("score", 3) for r in responses
            if not r.get("is_skipped") and "leadership" in r.get("section", "").lower()
        ]
        if leadership_scores:
            dimensions["leadership_judgment"] = round(
                sum(leadership_scores) / len(leadership_scores), 2
            )
        else:
            dimensions["leadership_judgment"] = None

        return dimensions

    def _calculate_overall_score(self, section_scores: Dict[str, List[int]],
                                dimensions: Dict[str, float]) -> float:
        """Calculate weighted overall score (0-100)."""
        # Collect all scored responses
        all_scores = []
        for scores in section_scores.values():
            all_scores.extend(scores)

        if not all_scores:
            return 0

        # Base technical average (scale 0-5 to 0-100)
        technical_avg = sum(all_scores) / len(all_scores)
        technical_score = technical_avg * 20  # 0-100

        # Communication score
        communication_score = (dimensions.get("communication_clarity", 3) * 20)

        # Problem-solving score
        problem_solving_score = (dimensions.get("problem_solving", 3) * 20)

        # Leadership score (if applicable)
        leadership_score = (dimensions.get("leadership_judgment", 3) * 20) if dimensions.get("leadership_judgment") else 0

        # Apply weights
        if dimensions.get("leadership_judgment"):
            # For senior/lead roles
            overall = (
                technical_score * 0.40 +
                problem_solving_score * 0.20 +
                communication_score * 0.15 +
                leadership_score * 0.25
            )
        else:
            # For individual contributor roles
            overall = (
                technical_score * 0.50 +
                problem_solving_score * 0.20 +
                communication_score * 0.30
            )

        return round(min(100, max(0, overall)), 1)

    def _get_hiring_verdict(self, overall_score: float) -> str:
        """Map overall score to hiring verdict."""
        if overall_score >= 85:
            return "Strong Hire"
        elif overall_score >= 70:
            return "Hire"
        elif overall_score >= 55:
            return "Hire with Reservations / Needs one more round"
        else:
            return "No Hire (this round)"

    def _performance_level(self, average_score: float) -> str:
        """Convert numeric score to performance level."""
        if average_score >= 4.5:
            return "Excellent"
        elif average_score >= 3.5:
            return "Strong"
        elif average_score >= 2.5:
            return "Adequate"
        elif average_score >= 1.5:
            return "Weak"
        else:
            return "Poor"

    def _generate_summary(self, section_analysis: Dict, dimensions: Dict, overall_score: float) -> Dict[str, Any]:
        """Generate summary statistics."""
        all_section_scores = []
        for section_data in section_analysis.values():
            all_section_scores.extend(section_data.get("scores", []))

        total_responses = sum(s.get("total_questions", 0) for s in section_analysis.values())
        answered = len(all_section_scores)
        skipped = total_responses - answered

        # Find strengths and weaknesses
        strengths = self._identify_strengths(section_analysis, dimensions)
        weaknesses = self._identify_weaknesses(section_analysis, dimensions)

        return {
            "total_questions": total_responses,
            "answered_questions": answered,
            "skipped_questions": skipped,
            "response_rate_percent": round((answered / total_responses * 100) if total_responses > 0 else 0, 1),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendation": self._recommendation(overall_score)
        }

    def _identify_strengths(self, section_analysis: Dict, dimensions: Dict) -> List[str]:
        """Identify top 3-5 performance strengths."""
        strengths = []

        # Check dimensions
        for dimension, score in dimensions.items():
            if score and score >= 4:
                strengths.append((dimension.replace("_", " ").title(), score))

        # Check sections
        for section, data in section_analysis.items():
            avg = data.get("average_score", 0)
            if avg >= 4 and len(strengths) < 5:
                strengths.append((section, avg))

        # Sort by score and return top 3-5
        strengths.sort(key=lambda x: x[1], reverse=True)
        return [f"{name}: {score}/5" for name, score in strengths[:5]]

    def _identify_weaknesses(self, section_analysis: Dict, dimensions: Dict) -> List[str]:
        """Identify top 3-5 performance weaknesses."""
        weaknesses = []

        # Check dimensions
        for dimension, score in dimensions.items():
            if score and score <= 2.5:
                weaknesses.append((dimension.replace("_", " ").title(), score))

        # Check sections
        for section, data in section_analysis.items():
            avg = data.get("average_score", 0)
            if avg <= 2.5 and len(weaknesses) < 5:
                weaknesses.append((section, avg))

        # Sort by score and return bottom 3-5
        weaknesses.sort(key=lambda x: x[1])
        return [f"{name}: {score}/5" for name, score in weaknesses[:5]]

    def _recommendation(self, overall_score: float) -> str:
        """Generate recommendation based on score."""
        verdict = self._get_hiring_verdict(overall_score)

        if overall_score >= 85:
            return "Candidate demonstrates strong technical expertise and communication. Recommend immediate offer discussion."
        elif overall_score >= 70:
            return "Candidate shows solid competencies across most areas. Recommend proceeding to next interview round or offer consideration."
        elif overall_score >= 55:
            return "Candidate has potential but needs development in key areas. Recommend another round to assess improvement or more structured feedback."
        else:
            return "Candidate did not meet minimum requirements for this level. Recommend re-interview for lower level or structured training."

    def print_analysis(self, analysis: Dict[str, Any]):
        """Print scoring analysis to console."""
        print("\n" + "="*70)
        print("  SCORING ANALYSIS COMPLETE")
        print("="*70 + "\n")

        summary = analysis.get("summary", {})
        print(f"Questions: {summary.get('answered_questions')}/{summary.get('total_questions')} answered")
        print(f"Response Rate: {summary.get('response_rate_percent')}%\n")

        # Section breakdown
        print("Section Performance:")
        print("-" * 70)
        section_analysis = analysis.get("section_analysis", {})
        for section, data in sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0), reverse=True):
            avg = data.get("average_score", 0)
            total = data.get("total_questions", 0)
            level = data.get("performance_level", "Unknown")
            print(f"  {section}: {avg}/5 ({level}) - {total} questions")

        # Dimension breakdown
        print("\nDimension Scores:")
        print("-" * 70)
        dimensions = analysis.get("dimension_scores", {})
        for dimension, score in dimensions.items():
            if score is not None:
                dim_name = dimension.replace("_", " ").title()
                level = self._performance_level(score)
                print(f"  {dim_name}: {score}/5 ({level})")

        # Overall score
        print("\nOverall Performance:")
        print("-" * 70)
        overall = analysis.get("overall_score", 0)
        verdict = analysis.get("hiring_verdict", "Unknown")
        print(f"  Overall Score: {overall}/100")
        print(f"  Hiring Verdict: {verdict}\n")

        # Strengths and weaknesses
        print("Top Strengths:")
        print("-" * 70)
        for i, strength in enumerate(summary.get("strengths", [])[:3], 1):
            print(f"  {i}. {strength}")

        print("\nAreas for Improvement:")
        print("-" * 70)
        for i, weakness in enumerate(summary.get("weaknesses", [])[:3], 1):
            print(f"  {i}. {weakness}")

        print("\nRecommendation:")
        print("-" * 70)
        print(f"  {summary.get('recommendation', 'See full report')}\n")

    def save_analysis(self, analysis: Dict[str, Any], filename: str = "scored_session.json") -> str:
        """Save complete analysis to file."""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'w') as f:
            json.dump({
                "candidate": self.session_data.get("candidate", {}),
                "session_metadata": {
                    "session_start": self.session_data.get("session_start"),
                    "session_end": self.session_data.get("session_end"),
                    "elapsed_time_minutes": self.session_data.get("elapsed_time_minutes")
                },
                "analysis": analysis
            }, f, indent=2)
        return filepath


def load_session_data(filename: str = "interview_session.json") -> Dict[str, Any]:
    """Load interview session from Phase 1."""
    filepath = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(filepath):
        print(f"❌ Error: {filename} not found.")
        print("Please run PHASE 1 (phase1_interview.py) first.\n")
        sys.exit(1)

    with open(filepath, 'r') as f:
        return json.load(f)


def load_questions(candidate_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Reconstruct question bank for scoring reference."""
    from question_bank import QuestionBank

    question_bank = QuestionBank(
        role=candidate_data.get("role", "QA Engineer"),
        difficulty=candidate_data.get("difficulty_level", "Basic"),
        primary_skills=candidate_data.get("primary_skills", []),
        years_of_experience=candidate_data.get("years_of_experience", 1),
        self_ratings=candidate_data.get("self_ratings", {})
    )

    return question_bank.questions


def main():
    """Entry point for Phase 2."""
    # Load session data from Phase 1
    print("Loading interview session from Phase 1...\n")
    session_data = load_session_data()

    candidate_data = session_data.get("candidate", {})
    print(f"Candidate: {candidate_data.get('role')}")
    print(f"Experience: {candidate_data.get('years_of_experience')} years")
    print(f"Difficulty: {candidate_data.get('difficulty_level')}\n")

    # Load questions
    questions = load_questions(candidate_data)

    # Initialize analyzer
    analyzer = ScoringAnalyzer(session_data, questions)

    # Run comprehensive analysis
    analysis = analyzer.analyze_all_responses()

    # Print results
    analyzer.print_analysis(analysis)

    # Save analysis
    filepath = analyzer.save_analysis(analysis)
    print(f"✓ Detailed analysis saved to: scored_session.json\n")

    print("="*70)
    print("Phase 2 Complete!")
    print("="*70)
    print("\nNext Step: Run Phase 3 to generate your final interview report.")
    print("Command: python phase3_report.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
