#!/usr/bin/env python3
"""
PHASE 3 — FINAL REPORT GENERATION
Interview Agent: Generate comprehensive, professional written interview reports.
"""

import json
import os
import sys
from typing import Dict, Any
from report_generator import ReportGenerator


def load_scored_session(filename: str = "scored_session.json") -> Dict[str, Any]:
    """Load scored session data from Phase 2."""
    filepath = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(filepath):
        print(f"❌ Error: {filename} not found.")
        print("Please run PHASE 2 (phase2_scoring.py) first.\n")
        sys.exit(1)

    with open(filepath, 'r') as f:
        return json.load(f)


def save_report(report_content: str, filename: str) -> str:
    """Save report to file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report_content)
    return filepath


def main():
    """Entry point for Phase 3."""
    print("\n" + "="*70)
    print("  PHASE 3 — FINAL REPORT GENERATION")
    print("="*70 + "\n")

    # Load scored session
    print("Loading scored session from Phase 2...\n")
    scored_session = load_scored_session()

    candidate_data = scored_session.get("candidate", {})
    print(f"Candidate: {candidate_data.get('role')}")
    print(f"Experience: {candidate_data.get('years_of_experience')} years")
    print(f"Difficulty: {candidate_data.get('difficulty_level')}\n")

    # Initialize report generator
    generator = ReportGenerator(scored_session)

    # Generate reports
    print("Generating comprehensive reports...\n")

    # Markdown report
    print("  • Generating Markdown report...")
    markdown_report = generator.generate_markdown_report()
    markdown_path = save_report(markdown_report, "interview_report.md")
    print(f"    ✓ Saved: interview_report.md")

    # HTML report
    print("  • Generating HTML report (with styling)...")
    html_report = generator.generate_html_report()
    html_path = save_report(html_report, "interview_report.html")
    print(f"    ✓ Saved: interview_report.html")

    # Print summary
    print("\n" + "="*70)
    print("  PHASE 3 COMPLETE — REPORTS GENERATED")
    print("="*70 + "\n")

    print("Reports created:")
    print(f"  1. interview_report.md   (Markdown format)")
    print(f"  2. interview_report.html (Professional HTML with styling)")
    print()
    print("To view the HTML report:")
    print(f"  • Open: interview_report.html in your web browser")
    print(f"  • Print to PDF: Use browser's Print function → 'Save as PDF'")
    print()
    print("To view the Markdown report:")
    print(f"  • Open: interview_report.md in any text editor or Markdown viewer")
    print()

    # Print report highlights
    print("="*70)
    print("  INTERVIEW HIGHLIGHTS")
    print("="*70 + "\n")

    analysis = scored_session.get("analysis", {})
    overall_score = analysis.get("overall_score", 0)
    verdict = analysis.get("hiring_verdict", "Unknown")

    print(f"Overall Score: {overall_score}/100")
    print(f"Verdict: {verdict}\n")

    summary = analysis.get("summary", {})
    print("Top Strengths:")
    for strength in summary.get("strengths", [])[:3]:
        print(f"  • {strength}")

    print("\nAreas for Improvement:")
    for weakness in summary.get("weaknesses", [])[:3]:
        print(f"  • {weakness}")

    print(f"\nRecommendation:")
    print(f"  {summary.get('recommendation', 'See full report')}")

    print("\n" + "="*70)
    print("All phases complete! Review your interview report above.")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
