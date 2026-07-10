#!/usr/bin/env python3
"""
PHASE 1 — INTERVIEW EXECUTION
Interview Agent: Conduct the actual interview with sequential, topic-by-topic questions.
"""

import json
import os
import sys
import time
from typing import Dict, Any, List
from question_bank import QuestionBank
from interview_session import InterviewSession, InterviewTimer


class InterviewExecutor:
    """Executes the interview phase."""

    def __init__(self, candidate_data: Dict[str, Any]):
        """Initialize interview executor with candidate profile."""
        self.candidate_data = candidate_data
        self.question_bank = QuestionBank(
            role=candidate_data.get("role", "QA Engineer"),
            difficulty=candidate_data.get("difficulty_level", "Basic"),
            primary_skills=candidate_data.get("primary_skills", []),
            years_of_experience=candidate_data.get("years_of_experience", 1),
            self_ratings=candidate_data.get("self_ratings", {})
        )

        self.questions = self.question_bank.get_questions_for_interview()
        self.session = InterviewSession(candidate_data, self.questions)
        self.timer = InterviewTimer(total_duration_minutes=45)
        self.current_section = None

    def clear_screen(self):
        """Clear console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_interview_header(self):
        """Print interview start header."""
        self.clear_screen()
        print("\n" + "="*70)
        print("  AI INTERVIEW PANELIST — INTERVIEW PHASE")
        print("="*70)
        print(f"\nCandidate: {self.candidate_data.get('role')}")
        print(f"Skills: {', '.join(self.candidate_data.get('primary_skills', []))}")
        print(f"Experience: {self.candidate_data.get('years_of_experience')} years")
        print(f"Difficulty: {self.candidate_data.get('difficulty_level')}")
        print(f"\nExpected Questions: {len(self.questions)}")
        print(f"Expected Duration: ~45 minutes")
        print("\n" + "="*70)
        print("\nReminder: Answer thoughtfully. I'll track timing and scoring silently.")
        print("You can say 'skip' if you need to skip a question.")
        print("\nLet's begin!\n")
        print("-"*70 + "\n")

    def print_section_transition(self, section: str, question_number: int):
        """Print transition message for new section."""
        if self.current_section != section:
            self.current_section = section
            elapsed = int(self.timer.get_elapsed_time_seconds() / 60)
            remaining = int(self.timer.get_remaining_time_minutes())

            print(f"\n{'='*70}")
            print(f"📍 Section: {section}")
            print(f"⏱️  Elapsed: {elapsed} min | Remaining: {remaining} min | Question {question_number}/{len(self.questions)}")
            print(f"{'='*70}\n")

    def print_question(self, question: Dict[str, Any], question_number: int):
        """Print a question with formatting."""
        section = question.get("section", "Unknown")
        self.print_section_transition(section, question_number)

        print(f"Q{question_number}: {question['question']}\n")

    def get_candidate_answer(self, timeout_seconds: int = 120) -> tuple[str, int]:
        """
        Get candidate's answer with timeout handling.

        Returns:
            (answer_text, response_time_seconds)
        """
        self.timer.start_question_timer()

        # Show timeout warning
        print(f"(You have up to 2 minutes to answer. Type your response below.)\n")

        answer_lines = []
        start_time = time.time()

        try:
            while True:
                elapsed = int(time.time() - start_time)
                remaining = timeout_seconds - elapsed

                if remaining <= 0:
                    print(f"\n⏱️  Time's up on this question.\n")
                    break

                # Show time warning at 30 seconds remaining
                if remaining == 30:
                    print(f"⚠️  30 seconds remaining...\n")

                line = input()

                # Check for skip command
                if line.lower().strip() in ["skip", "pass", "next"]:
                    return "[SKIPPED]", int(time.time() - start_time)

                if line:
                    answer_lines.append(line)
                elif len(answer_lines) > 0:
                    # Empty line after content = end of answer
                    break

        except KeyboardInterrupt:
            return "[INTERRUPTED]", int(time.time() - start_time)

        response_time = int(time.time() - start_time)
        answer = "\n".join(answer_lines).strip()

        if not answer:
            return "[NO RESPONSE]", response_time

        return answer, response_time

    def acknowledge_answer(self, is_skipped: bool = False):
        """Brief acknowledgment after answer (neutral, no evaluation)."""
        if is_skipped:
            print("\n✓ Moving to next question.\n")
        else:
            print("\n✓ Got it. Next question.\n")

    def run_interview(self) -> InterviewSession:
        """Run the full interview."""
        self.print_interview_header()
        self.session.start_session()
        self.timer.start()

        # Run through each question
        for question_number, question in enumerate(self.questions, 1):
            # Check if time is up
            if self.timer.is_time_up():
                print("\n" + "="*70)
                print("⏱️  Interview time is up. Let's wrap up.\n")
                break

            # Print question
            self.print_question(question, question_number)

            # Get candidate answer
            answer, response_time = self.get_candidate_answer()

            is_skipped = answer in ["[SKIPPED]", "[NO RESPONSE]", "[INTERRUPTED]"]

            # Record response
            self.session.record_response(
                question_id=question["id"],
                answer=answer,
                response_time_seconds=response_time,
                is_skipped=is_skipped
            )

            # Acknowledge (neutral tone)
            self.acknowledge_answer(is_skipped)

            # Print progress update every 4-5 questions
            if question_number % 5 == 0:
                progress = self.session.get_progress_summary()
                print(f"📊 Progress: {progress['answered']}/{progress['total_questions']} answered"
                      f" | {progress['elapsed_time_minutes']:.1f} min elapsed\n")

        # End session
        self.session.end_session()
        self.print_interview_closing()

        return self.session

    def print_interview_closing(self):
        """Print interview closing message."""
        print("\n" + "="*70)
        print("  INTERVIEW COMPLETE")
        print("="*70 + "\n")

        progress = self.session.get_progress_summary()
        print(f"Questions Asked: {len(self.session.responses)}")
        print(f"Questions Answered: {progress['answered']}")
        print(f"Questions Skipped: {progress['skipped']}")
        print(f"Total Time: {progress['elapsed_time_minutes']:.1f} minutes")

        print("\n✓ Your responses have been recorded.")
        print("✓ Silent scoring has been completed.")
        print("✓ A comprehensive report will be generated in Phase 2.")

        print("\nPhase 1 Complete! Proceeding to Phase 2 (Scoring & Analysis)...")
        print("="*70 + "\n")

    def save_session(self):
        """Save interview session for Phase 2."""
        filepath = self.session.save_session("interview_session.json")
        print(f"✓ Interview session saved: {filepath}\n")
        return filepath


def load_candidate_data(filename: str = "candidate_intake.json") -> Dict[str, Any]:
    """Load candidate data from Phase 0."""
    filepath = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(filepath):
        print(f"❌ Error: {filename} not found.")
        print("Please run PHASE 0 (phase0_intake.py) first.\n")
        sys.exit(1)

    with open(filepath, 'r') as f:
        return json.load(f)


def main():
    """Entry point for Phase 1."""
    # Load candidate data from Phase 0
    print("Loading candidate profile from Phase 0...\n")
    candidate_data = load_candidate_data()

    # Initialize and run interview
    executor = InterviewExecutor(candidate_data)

    # Run the interview
    session = executor.run_interview()

    # Save session for Phase 2
    executor.save_session()

    print("\n" + "="*70)
    print("Next Step: Run Phase 2 to generate your detailed interview report.")
    print("Command: python phase2_scoring.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
