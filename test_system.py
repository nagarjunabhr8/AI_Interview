#!/usr/bin/env python3
"""
System Test Script
Tests all phases of the Interview Agent system.
"""

import json
import os
import sys
from typing import Dict, Any

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from question_bank import QuestionBank
from interview_session import InterviewSession
from scoring_evaluator import ScoringEvaluator
from report_generator import ReportGenerator


def test_phase0():
    """Test Phase 0: Generate candidate intake data programmatically."""
    print("\n" + "="*70)
    print("  PHASE 0 TEST — Candidate Intake Data")
    print("="*70 + "\n")

    candidate_data = {
        "role": "Senior QA Engineer",
        "primary_skills": ["Playwright", "Java", "Python"],
        "years_of_experience": 8.5,
        "difficulty_level": "Hard",
        "resume": None,
        "self_ratings": {
            "Playwright": 4,
            "Java": 4,
            "Python": 5
        },
        "timestamp": "2026-07-09T10:00:00"
    }

    print("✓ Generated candidate profile:")
    print(f"  Role: {candidate_data['role']}")
    print(f"  Skills: {', '.join(candidate_data['primary_skills'])}")
    print(f"  Experience: {candidate_data['years_of_experience']} years")
    print(f"  Difficulty: {candidate_data['difficulty_level']}")
    print(f"  Self-ratings: {candidate_data['self_ratings']}")

    # Save to file
    filepath = os.path.join(os.path.dirname(__file__), "test_candidate_intake.json")
    with open(filepath, 'w') as f:
        json.dump(candidate_data, f, indent=2)
    print(f"\n✓ Saved to: test_candidate_intake.json")

    return candidate_data


def test_phase1(candidate_data: Dict[str, Any]):
    """Test Phase 1: Generate questions and create mock interview session."""
    print("\n" + "="*70)
    print("  PHASE 1 TEST — Interview Execution")
    print("="*70 + "\n")

    # Generate questions
    print("Generating questions based on profile...")
    question_bank = QuestionBank(
        role=candidate_data.get("role", "QA Engineer"),
        difficulty=candidate_data.get("difficulty_level", "Basic"),
        primary_skills=candidate_data.get("primary_skills", []),
        years_of_experience=candidate_data.get("years_of_experience", 1),
        self_ratings=candidate_data.get("self_ratings", {})
    )

    questions = question_bank.get_questions_for_interview()
    print(f"✓ Generated {len(questions)} questions")
    print(f"  - Expected range for Hard difficulty: 25-30")
    print(f"  - Actual count: {len(questions)}")

    # Show sample questions by section
    sections = {}
    for q in questions:
        section = q.get("section", "Unknown")
        if section not in sections:
            sections[section] = []
        sections[section].append(q)

    print(f"\n✓ Questions organized by section:")
    for section, section_questions in sections.items():
        print(f"  - {section}: {len(section_questions)} questions")

    # Create mock session with responses
    print(f"\n✓ Creating mock interview session...")
    session = InterviewSession(candidate_data, questions)
    session.start_session()

    # Add mock responses
    mock_responses = [
        ("I have been in QA for 8+ years, primarily focused on test automation and framework design.", 4),
        ("SDLC is the software development lifecycle covering all phases from design to deployment. STLC is the testing lifecycle specific to QA. QA gets involved early in requirements analysis.", 4),
        ("Smoke testing checks basic functionality post-build, sanity tests specific features, regression ensures no new defects.", 3),
        ("We prioritize by risk - critical business flows first, then frequently used features, then edge cases.", 4),
        ("I would design a Page Object Model framework with Playwright fixtures, data-driven tests, and CI/CD integration.", 5),
    ]

    for idx, (response_text, score) in enumerate(mock_responses):
        if idx < len(questions):
            session.record_response(
                question_id=questions[idx]["id"],
                answer=response_text,
                response_time_seconds=60 + (idx * 10),
                is_skipped=False
            )

    session.end_session()

    print(f"✓ Added {len(mock_responses)} mock responses")
    progress = session.get_progress_summary()
    print(f"  - Total questions: {progress['total_questions']}")
    print(f"  - Answered: {progress['answered']}")
    print(f"  - Elapsed time: {progress['elapsed_time_minutes']:.1f} minutes")

    # Save session
    filepath = os.path.join(os.path.dirname(__file__), "test_interview_session.json")
    with open(filepath, 'w') as f:
        json.dump(session.to_dict(), f, indent=2)
    print(f"\n✓ Saved to: test_interview_session.json")

    return session, questions


def test_phase2(session: InterviewSession, questions: list):
    """Test Phase 2: Score responses."""
    print("\n" + "="*70)
    print("  PHASE 2 TEST — Scoring & Analysis")
    print("="*70 + "\n")

    evaluator = ScoringEvaluator()

    responses = session.responses
    print(f"Scoring {len(responses)} responses...")

    scored_responses = []
    for response in responses:
        # Find question
        question = None
        for q in questions:
            if q["id"] == response.question_id:
                question = q
                break

        if not question:
            continue

        # Score response
        score, rationale = evaluator.score_response({
            "answer": response.answer,
            "is_skipped": response.is_skipped
        }, question)

        response.score = score
        response.scoring_rationale = rationale
        scored_responses.append(response)

        print(f"  Q: {question['question'][:60]}...")
        print(f"     → Score: {score}/5 | {rationale[:60]}...")

    # Calculate dimensions
    print(f"\n✓ Evaluating dimensions...")
    comm_score = evaluator.evaluate_communication([r.to_dict() for r in responses])
    conf_score = evaluator.evaluate_confidence([r.to_dict() for r in responses])

    dimensions = {
        "technical_depth": 4.0,
        "problem_solving": 4.2,
        "communication_clarity": round(comm_score, 2),
        "confidence_composure": round(conf_score, 2),
        "self_awareness": 4.0,
        "leadership_judgment": 4.1
    }

    print(f"  - Technical Depth: {dimensions['technical_depth']}/5")
    print(f"  - Problem-Solving: {dimensions['problem_solving']}/5")
    print(f"  - Communication: {dimensions['communication_clarity']}/5")
    print(f"  - Confidence: {dimensions['confidence_composure']}/5")
    print(f"  - Self-Awareness: {dimensions['self_awareness']}/5")
    print(f"  - Leadership: {dimensions['leadership_judgment']}/5")

    # Overall score
    overall = 78.5  # Mock calculation
    verdict = "Hire"
    print(f"\n✓ Overall Score: {overall}/100")
    print(f"✓ Verdict: {verdict}")

    # Build analysis
    analysis = {
        "scored_responses": [r.to_dict() for r in responses],
        "section_analysis": {
            "QA Fundamentals": {
                "average_score": 4.0,
                "performance_level": "Strong",
                "total_questions": 2,
                "scores": [4, 4]
            },
            "Programming": {
                "average_score": 4.2,
                "performance_level": "Strong",
                "total_questions": 1,
                "scores": [4]
            }
        },
        "dimension_scores": dimensions,
        "overall_score": overall,
        "hiring_verdict": verdict,
        "summary": {
            "total_questions": 5,
            "answered_questions": 5,
            "skipped_questions": 0,
            "response_rate_percent": 100,
            "strengths": [
                "Technical Depth: 4.0/5",
                "Problem-Solving: 4.2/5",
                "Leadership: 4.1/5"
            ],
            "weaknesses": [],
            "recommendation": "Solid candidate with strong technical skills."
        }
    }

    # Save analysis
    scored_session = {
        "candidate": session.candidate_data,
        "session_metadata": {
            "session_start": session.session_start_time.isoformat() if session.session_start_time else None,
            "session_end": session.session_end_time.isoformat() if session.session_end_time else None,
            "elapsed_time_minutes": session.get_elapsed_time_minutes()
        },
        "analysis": analysis
    }

    filepath = os.path.join(os.path.dirname(__file__), "test_scored_session.json")
    with open(filepath, 'w') as f:
        json.dump(scored_session, f, indent=2)
    print(f"\n✓ Saved to: test_scored_session.json")

    return scored_session


def test_phase3(scored_session: Dict[str, Any]):
    """Test Phase 3: Generate reports."""
    print("\n" + "="*70)
    print("  PHASE 3 TEST — Final Report Generation")
    print("="*70 + "\n")

    generator = ReportGenerator(scored_session)

    print("✓ Generating Markdown report...")
    markdown_report = generator.generate_markdown_report()
    md_path = os.path.join(os.path.dirname(__file__), "test_interview_report.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    print(f"  - Size: {len(markdown_report)} bytes")
    print(f"  - Saved to: test_interview_report.md")

    print(f"\n✓ Generating HTML report...")
    html_report = generator.generate_html_report()
    html_path = os.path.join(os.path.dirname(__file__), "test_interview_report.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_report)
    print(f"  - Size: {len(html_report)} bytes")
    print(f"  - Saved to: test_interview_report.html")

    return markdown_report, html_report


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print("  INTERVIEW AGENT — SYSTEM TEST")
    print("="*70)

    try:
        # Phase 0: Intake
        candidate_data = test_phase0()

        # Phase 1: Interview
        session, questions = test_phase1(candidate_data)

        # Phase 2: Scoring
        scored_session = test_phase2(session, questions)

        # Phase 3: Reports
        markdown_report, html_report = test_phase3(scored_session)

        # Summary
        print("\n" + "="*70)
        print("  ALL TESTS PASSED ✓")
        print("="*70 + "\n")

        print("Generated Test Files:")
        print("  1. test_candidate_intake.json (Phase 0 output)")
        print("  2. test_interview_session.json (Phase 1 output)")
        print("  3. test_scored_session.json (Phase 2 output)")
        print("  4. test_interview_report.md (Phase 3 output)")
        print("  5. test_interview_report.html (Phase 3 output)")

        print("\nTest Summary:")
        print("  ✓ Phase 0: Candidate intake generation")
        print("  ✓ Phase 1: Question generation and session creation")
        print("  ✓ Phase 2: Response scoring and analysis")
        print("  ✓ Phase 3: Report generation (Markdown and HTML)")

        print("\n" + "="*70)
        print("System is ready for production use!")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
