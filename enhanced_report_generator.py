"""
Enhanced Report Generator
Generates comprehensive reports with complete interview Q&A transcript
Includes: Questions, Answers, Follow-ups, Voice Data, Communication Metrics
"""

import json
from typing import Dict, Any, List
from datetime import datetime


class EnhancedReportGenerator:
    """Generates comprehensive interview reports with full Q&A transcript."""

    def __init__(self, scored_session: Dict[str, Any], questions: List[Dict] = None,
                 conversation_flow: List[Dict] = None, voice_metrics: Dict = None):
        """
        Initialize enhanced report generator.

        Args:
            scored_session: Complete scoring data from Phase 2
            questions: List of questions asked in interview
            conversation_flow: Conversation history with follow-ups
            voice_metrics: Voice/communication metrics from voice interviews
        """
        self.scored_session = scored_session
        self.questions = questions or []
        self.conversation_flow = conversation_flow or []
        self.voice_metrics = voice_metrics or {}
        self.candidate = scored_session.get("candidate", {})
        self.analysis = scored_session.get("analysis", {})
        self.metadata = scored_session.get("session_metadata", {})

    def generate_markdown_report(self) -> str:
        """Generate comprehensive Markdown report with full Q&A."""
        sections = [
            self._section_header(),
            self._section_candidate_summary(),
            self._section_interview_overview(),
            self._section_overall_performance(),
            self._section_dimensions_table(),
            self._section_complete_qa_transcript(),
            self._section_voice_communication_analysis(),
            self._section_section_breakdown(),
            self._section_strengths(),
            self._section_improvement_areas(),
            self._section_recommendations(),
            self._section_footer()
        ]

        return "\n\n".join([s for s in sections if s])

    def generate_html_report(self) -> str:
        """Generate professional HTML report with styling."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interview Report - {self.candidate.get('role', 'Technical Interview')}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .header {{
            border-bottom: 3px solid #2c3e50;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}

        h1 {{
            color: #2c3e50;
            font-size: 28px;
            margin-bottom: 10px;
        }}

        h2 {{
            color: #34495e;
            font-size: 20px;
            margin-top: 30px;
            margin-bottom: 15px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}

        h3 {{
            color: #555;
            font-size: 16px;
            margin-top: 20px;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: #7f8c8d;
            font-size: 14px;
        }}

        .qa-section {{
            background: #f9f9f9;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
            page-break-inside: avoid;
        }}

        .question-number {{
            color: #3498db;
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 8px;
        }}

        .question-text {{
            color: #2c3e50;
            font-weight: 600;
            font-size: 15px;
            margin-bottom: 12px;
        }}

        .answer-label {{
            color: #7f8c8d;
            font-weight: 600;
            font-size: 13px;
            text-transform: uppercase;
            margin-top: 12px;
            margin-bottom: 8px;
        }}

        .answer-text {{
            color: #555;
            padding: 12px;
            background: white;
            border-left: 3px solid #95a5a6;
            margin: 8px 0;
        }}

        .followup-section {{
            background: #fff3cd;
            border-left: 3px solid #ffc107;
            padding: 12px;
            margin: 12px 0;
            border-radius: 3px;
            font-size: 14px;
        }}

        .followup-label {{
            color: #856404;
            font-weight: 600;
            margin-bottom: 5px;
        }}

        .followup-text {{
            color: #856404;
            font-style: italic;
        }}

        .score-badge {{
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-top: 10px;
        }}

        .score-badge.high {{
            background: #27ae60;
        }}

        .score-badge.medium {{
            background: #f39c12;
        }}

        .score-badge.low {{
            background: #e74c3c;
        }}

        .voice-metrics {{
            background: #ecf0f1;
            padding: 12px;
            margin: 8px 0;
            border-radius: 4px;
            font-size: 13px;
        }}

        .metrics-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 15px 0;
        }}

        .metric-item {{
            background: #ecf0f1;
            padding: 12px;
            border-radius: 4px;
        }}

        .metric-label {{
            font-weight: 600;
            color: #2c3e50;
            font-size: 12px;
        }}

        .metric-value {{
            font-size: 18px;
            font-weight: 700;
            color: #3498db;
            margin-top: 5px;
        }}

        .summary-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}

        .summary-table th,
        .summary-table td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}

        .summary-table th {{
            background: #ecf0f1;
            font-weight: 600;
            color: #2c3e50;
        }}

        .summary-table tr:hover {{
            background: #f9f9f9;
        }}

        .strength-item {{
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
        }}

        .weakness-item {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
        }}

        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #bdc3c7;
            text-align: center;
            color: #7f8c8d;
            font-size: 12px;
        }}

        .page-break {{
            page-break-after: always;
            margin: 40px 0;
        }}

        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .container {{
                box-shadow: none;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {self._html_section_header()}
        {self._html_section_candidate_summary()}
        {self._html_section_interview_overview()}
        {self._html_section_overall_performance()}
        {self._html_section_dimensions_table()}
        <div class="page-break"></div>
        {self._html_section_complete_qa_transcript()}
        <div class="page-break"></div>
        {self._html_section_voice_communication_analysis()}
        {self._html_section_section_breakdown()}
        {self._html_section_strengths()}
        {self._html_section_improvement_areas()}
        <div class="page-break"></div>
        {self._html_section_recommendations()}
        {self._html_section_footer()}
    </div>
</body>
</html>"""

    # ==================== MARKDOWN SECTIONS ====================

    def _section_header(self) -> str:
        """Generate report header."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        return f"""# Interview Assessment Report

**Generated:** {timestamp}
**Interview Type:** {self._get_interview_type()}
"""

    def _section_candidate_summary(self) -> str:
        """Generate candidate information."""
        role = self.candidate.get('role', 'Unknown')
        skills = ', '.join(self.candidate.get('primary_skills', []))
        experience = self.candidate.get('years_of_experience', 'Not specified')
        difficulty = self.candidate.get('difficulty_level', 'Not specified')

        return f"""## Candidate Information

| Field | Value |
|-------|-------|
| **Position** | {role} |
| **Skills** | {skills} |
| **Experience** | {experience} years |
| **Difficulty Level** | {difficulty} |
"""

    def _section_interview_overview(self) -> str:
        """Generate interview overview."""
        responses = self.analysis.get("scored_responses", [])
        total_questions = len(self.questions) if self.questions else len(responses)
        answered = len([r for r in responses if not r.get('is_skipped')])
        skipped = len([r for r in responses if r.get('is_skipped')])

        metadata = self.metadata or {}
        session_start = metadata.get('session_start', 'Not recorded')
        elapsed_time = metadata.get('elapsed_time_minutes', 'Not recorded')

        return f"""## Interview Overview

| Metric | Value |
|--------|-------|
| **Total Questions** | {total_questions} |
| **Questions Answered** | {answered} |
| **Questions Skipped** | {skipped} |
| **Response Rate** | {int((answered / total_questions * 100)) if total_questions > 0 else 0}% |
| **Interview Duration** | {elapsed_time} minutes |
| **Interview Start** | {session_start} |
"""

    def _section_overall_performance(self) -> str:
        """Generate overall performance section."""
        overall_score = self.analysis.get("overall_score", 0)
        verdict = self.analysis.get("hiring_verdict", "Pending")

        return f"""## Overall Performance

### Score: **{overall_score:.1f}/100**
### Verdict: **{verdict}**
"""

    def _section_dimensions_table(self) -> str:
        """Generate dimension scores."""
        dims = self.analysis.get("dimension_scores", {})

        section = "## Evaluation Dimensions\n\n"
        section += "| Dimension | Score | Assessment |\n"
        section += "|-----------|-------|------------|\n"

        for dim_name, score in dims.items():
            if isinstance(score, dict):
                score_val = score.get('score', 0)
            else:
                score_val = score

            assessment = self._score_to_assessment(score_val)
            dim_display = dim_name.replace('_', ' ').title()
            section += f"| {dim_display} | {score_val}/5 | {assessment} |\n"

        return section

    def _section_complete_qa_transcript(self) -> str:
        """Generate complete Q&A transcript with all questions and answers."""
        responses = self.analysis.get("scored_responses", [])

        transcript = "## Complete Question & Answer Transcript\n\n"

        for idx, response in enumerate(responses, 1):
            question_id = response.get("question_id")
            answer = response.get("answer", "[No response]")
            score = response.get("score", 0)
            is_skipped = response.get("is_skipped", False)

            # Get question from questions list
            question_text = self._get_question_text(question_id, idx)

            # Status indicator
            status = "SKIPPED" if is_skipped else "ANSWERED"
            score_text = f"**Score: {score}/5**" if not is_skipped else "**STATUS: SKIPPED**"

            # Format answer with proper quoting
            answer_display = f"> {answer}" if answer and answer != "[No response]" else "> [No response provided]"

            transcript += f"""### Question {idx}: {status}

**Question:**
{question_text}

**Candidate's Answer:**
{answer_display}

{score_text}

---

"""

        return transcript

    def _section_voice_communication_analysis(self) -> str:
        """Generate voice communication analysis if available."""
        if not self.voice_metrics:
            return ""

        section = "## Communication & Voice Analysis\n\n"

        # Check if voice data exists
        has_voice = self.voice_metrics.get('voice_responses', 0) > 0

        if has_voice:
            section += "### Voice Interaction Metrics\n\n"
            section += "| Metric | Value |\n"
            section += "|--------|-------|\n"
            section += f"| Voice Responses | {self.voice_metrics.get('voice_responses', 0)} |\n"
            section += f"| Text Fallback | {self.voice_metrics.get('text_responses', 0)} |\n"
            section += f"| Clarity Score | {self.voice_metrics.get('clarity', 0)}/5 |\n"
            section += f"| Speaking Pace | {self.voice_metrics.get('pace', 'Normal')} |\n"
            section += f"| Confidence Level | {self.voice_metrics.get('confidence', 'Not assessed')} |\n"
            section += f"| Hesitation Markers | {self.voice_metrics.get('hesitation_markers', 0)} |\n"

        return section

    def _section_section_breakdown(self) -> str:
        """Generate section-wise performance breakdown."""
        section_analysis = self.analysis.get("section_analysis", {})

        if not section_analysis:
            return ""

        breakdown = "## Section-wise Performance Breakdown\n\n"
        breakdown += "| Section | Avg Score | Performance | Questions |\n"
        breakdown += "|---------|-----------|-------------|----------|\n"

        for section, data in sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0), reverse=True):
            avg = data.get("average_score", 0)
            level = self._score_to_assessment(avg)
            count = data.get("total_questions", 0)
            breakdown += f"| {section} | {avg:.1f}/5 | {level} | {count} |\n"

        return breakdown

    def _section_strengths(self) -> str:
        """Generate strengths section."""
        summary = self.analysis.get("summary", {})
        strengths = summary.get("strengths", [])

        section = "## Key Strengths\n\n"
        if strengths:
            for i, strength in enumerate(strengths[:5], 1):
                section += f"**{i}. {strength}**\n"
        else:
            section += "No strengths recorded.\n"

        return section

    def _section_improvement_areas(self) -> str:
        """Generate improvement areas."""
        summary = self.analysis.get("summary", {})
        weaknesses = summary.get("weaknesses", [])

        section = "## Areas for Improvement\n\n"
        if weaknesses:
            for i, weakness in enumerate(weaknesses[:5], 1):
                section += f"**{i}. {weakness}**\n"
                section += f"- {self._improvement_guidance(weakness)}\n\n"
        else:
            section += "No areas for improvement identified.\n"

        return section

    def _section_recommendations(self) -> str:
        """Generate recommendations."""
        summary = self.analysis.get("summary", {})
        recommendation = summary.get("recommendation", "")

        section = "## Recommendations\n\n"
        if recommendation:
            section += f"{recommendation}\n"
        else:
            section += "Based on the interview performance, continue skill development in identified areas.\n"

        return section

    def _section_footer(self) -> str:
        """Generate report footer."""
        return """---

**Report generated by AI Interview Panelist**

*This report is confidential and intended for authorized use only.*"""

    # ==================== HTML SECTIONS ====================

    def _html_section_header(self) -> str:
        """Generate HTML header."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        return f"""<div class="header">
    <h1>Interview Assessment Report</h1>
    <p class="subtitle">Generated: {timestamp} | Type: {self._get_interview_type()}</p>
</div>"""

    def _html_section_candidate_summary(self) -> str:
        """Generate HTML candidate summary."""
        role = self.candidate.get('role', 'Unknown')
        skills = ', '.join(self.candidate.get('primary_skills', []))
        experience = self.candidate.get('years_of_experience', 'Not specified')
        difficulty = self.candidate.get('difficulty_level', 'Not specified')

        return f"""<div>
    <h2>Candidate Information</h2>
    <table class="summary-table">
        <tr>
            <th>Position</th>
            <td>{role}</td>
        </tr>
        <tr>
            <th>Skills</th>
            <td>{skills}</td>
        </tr>
        <tr>
            <th>Experience</th>
            <td>{experience} years</td>
        </tr>
        <tr>
            <th>Difficulty Level</th>
            <td>{difficulty}</td>
        </tr>
    </table>
</div>"""

    def _html_section_interview_overview(self) -> str:
        """Generate HTML interview overview."""
        responses = self.analysis.get("scored_responses", [])
        total_questions = len(self.questions) if self.questions else len(responses)
        answered = len([r for r in responses if not r.get('is_skipped')])
        skipped = len([r for r in responses if r.get('is_skipped')])
        response_rate = int((answered / total_questions * 100)) if total_questions > 0 else 0

        metadata = self.metadata or {}
        elapsed_time = metadata.get('elapsed_time_minutes', 'Not recorded')

        return f"""<div>
    <h2>Interview Overview</h2>
    <table class="summary-table">
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Total Questions</td>
            <td>{total_questions}</td>
        </tr>
        <tr>
            <td>Questions Answered</td>
            <td>{answered}</td>
        </tr>
        <tr>
            <td>Questions Skipped</td>
            <td>{skipped}</td>
        </tr>
        <tr>
            <td>Response Rate</td>
            <td>{response_rate}%</td>
        </tr>
        <tr>
            <td>Duration</td>
            <td>{elapsed_time} minutes</td>
        </tr>
    </table>
</div>"""

    def _html_section_overall_performance(self) -> str:
        """Generate HTML overall performance."""
        overall_score = self.analysis.get("overall_score", 0)
        verdict = self.analysis.get("hiring_verdict", "Pending")

        return f"""<div>
    <h2>Overall Performance</h2>
    <div class="metrics-grid">
        <div class="metric-item">
            <div class="metric-label">Overall Score</div>
            <div class="metric-value">{overall_score:.1f}/100</div>
        </div>
        <div class="metric-item">
            <div class="metric-label">Hiring Verdict</div>
            <div class="metric-value">{verdict}</div>
        </div>
    </div>
</div>"""

    def _html_section_dimensions_table(self) -> str:
        """Generate HTML dimensions table."""
        dims = self.analysis.get("dimension_scores", {})

        html = "<div><h2>Evaluation Dimensions</h2><table class=\"summary-table\"><tr><th>Dimension</th><th>Score</th><th>Assessment</th></tr>"

        for dim_name, score in dims.items():
            if isinstance(score, dict):
                score_val = score.get('score', 0)
            else:
                score_val = score

            assessment = self._score_to_assessment(score_val)
            dim_display = dim_name.replace('_', ' ').title()
            html += f"<tr><td>{dim_display}</td><td>{score_val}/5</td><td>{assessment}</td></tr>"

        html += "</table></div>"
        return html

    def _html_section_complete_qa_transcript(self) -> str:
        """Generate HTML Q&A transcript."""
        responses = self.analysis.get("scored_responses", [])

        html = "<div><h2>Complete Question & Answer Transcript</h2>"

        for idx, response in enumerate(responses, 1):
            question_id = response.get("question_id")
            answer = response.get("answer", "[No response]")
            score = response.get("score", 0)
            is_skipped = response.get("is_skipped", False)

            question_text = self._get_question_text(question_id, idx)
            status = "SKIPPED" if is_skipped else "ANSWERED"

            score_html = f'<span class="score-badge {self._score_to_css_class(score)}">{score}/5</span>' if not is_skipped else '<span class="score-badge">SKIPPED</span>'

            html += f"""<div class="qa-section">
    <div class="question-number">Question {idx} • {status}</div>
    <div class="question-text">{question_text}</div>
    <div class="answer-label">Candidate's Answer</div>
    <div class="answer-text">{answer if answer else '[No response provided]'}</div>
    {score_html}
</div>"""

        html += "</div>"
        return html

    def _html_section_voice_communication_analysis(self) -> str:
        """Generate HTML voice analysis."""
        if not self.voice_metrics:
            return ""

        html = "<div><h2>Communication & Voice Analysis</h2>"

        if self.voice_metrics.get('voice_responses', 0) > 0:
            html += """<h3>Voice Interaction Metrics</h3>
<table class="summary-table">
    <tr>
        <th>Metric</th>
        <th>Value</th>
    </tr>"""
            html += f"<tr><td>Voice Responses</td><td>{self.voice_metrics.get('voice_responses', 0)}</td></tr>"
            html += f"<tr><td>Text Fallback</td><td>{self.voice_metrics.get('text_responses', 0)}</td></tr>"
            html += f"<tr><td>Clarity</td><td>{self.voice_metrics.get('clarity', 0)}/5</td></tr>"
            html += f"<tr><td>Pace</td><td>{self.voice_metrics.get('pace', 'Normal')}</td></tr>"
            html += f"<tr><td>Confidence</td><td>{self.voice_metrics.get('confidence', 'Not assessed')}</td></tr>"
            html += f"<tr><td>Hesitation Markers</td><td>{self.voice_metrics.get('hesitation_markers', 0)}</td></tr>"
            html += "</table>"

        html += "</div>"
        return html

    def _html_section_section_breakdown(self) -> str:
        """Generate HTML section breakdown."""
        section_analysis = self.analysis.get("section_analysis", {})

        if not section_analysis:
            return ""

        html = "<div><h2>Section-wise Performance</h2><table class=\"summary-table\"><tr><th>Section</th><th>Avg Score</th><th>Performance</th><th>Questions</th></tr>"

        for section, data in sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0), reverse=True):
            avg = data.get("average_score", 0)
            level = self._score_to_assessment(avg)
            count = data.get("total_questions", 0)
            html += f"<tr><td>{section}</td><td>{avg:.1f}/5</td><td>{level}</td><td>{count}</td></tr>"

        html += "</table></div>"
        return html

    def _html_section_strengths(self) -> str:
        """Generate HTML strengths."""
        summary = self.analysis.get("summary", {})
        strengths = summary.get("strengths", [])

        html = "<div><h2>Key Strengths</h2>"
        if strengths:
            for i, strength in enumerate(strengths[:5], 1):
                html += f'<div class="strength-item"><strong>{i}. {strength}</strong></div>'
        else:
            html += "<p>No strengths recorded.</p>"
        html += "</div>"
        return html

    def _html_section_improvement_areas(self) -> str:
        """Generate HTML improvement areas."""
        summary = self.analysis.get("summary", {})
        weaknesses = summary.get("weaknesses", [])

        html = "<div><h2>Areas for Improvement</h2>"
        if weaknesses:
            for i, weakness in enumerate(weaknesses[:5], 1):
                html += f'<div class="weakness-item"><strong>{i}. {weakness}</strong><br/><small>{self._improvement_guidance(weakness)}</small></div>'
        else:
            html += "<p>No areas for improvement identified.</p>"
        html += "</div>"
        return html

    def _html_section_recommendations(self) -> str:
        """Generate HTML recommendations."""
        summary = self.analysis.get("summary", {})
        recommendation = summary.get("recommendation", "")

        html = "<div><h2>Recommendations</h2>"
        if recommendation:
            html += f"<p>{recommendation}</p>"
        else:
            html += "<p>Based on the interview performance, continue skill development in identified areas.</p>"
        html += "</div>"
        return html

    def _html_section_footer(self) -> str:
        """Generate HTML footer."""
        return """<div class="footer">
    <p><strong>Report generated by AI Interview Panelist</strong></p>
    <p><em>This report is confidential and intended for authorized use only.</em></p>
</div>"""

    # ==================== HELPER METHODS ====================

    def _get_question_text(self, question_id: str, idx: int) -> str:
        """Get question text from questions list or response data."""
        if not question_id:
            return f'Question {idx}'

        if self.questions:
            # Try exact match on id
            for q in self.questions:
                if q.get('id') == question_id:
                    return q.get('question', f'Question {idx}')

            # Try string match as fallback
            question_id_str = str(question_id)
            for q in self.questions:
                if str(q.get('id', '')) == question_id_str:
                    return q.get('question', f'Question {idx}')

        return f'Question {idx}'

    def _get_interview_type(self) -> str:
        """Determine interview type."""
        if self.voice_metrics and self.voice_metrics.get('voice_responses', 0) > 0:
            return "Interactive Voice Interview"
        return "Standard Interview"

    def _score_to_assessment(self, score: float) -> str:
        """Convert score to assessment level."""
        if score >= 4.5:
            return "Excellent"
        elif score >= 4:
            return "Very Good"
        elif score >= 3:
            return "Good"
        elif score >= 2:
            return "Fair"
        else:
            return "Needs Improvement"

    def _score_to_css_class(self, score: float) -> str:
        """Convert score to CSS class."""
        if score >= 4:
            return "high"
        elif score >= 3:
            return "medium"
        else:
            return "low"

    def _improvement_guidance(self, topic: str) -> str:
        """Generate improvement guidance."""
        guidance_map = {
            "playwright": "Review Playwright documentation, practice auto-wait mechanics, and study actionability checks.",
            "selenium": "Study Selenium WebDriver architecture and explicit/implicit wait patterns.",
            "coding": "Practice algorithmic problems focusing on complexity analysis and edge cases.",
            "communication": "Work on clear explanation structure and using concrete examples.",
            "technical depth": "Deep dive into fundamentals from official documentation and industry resources.",
            "confidence": "Practice mock interviews and prepare thoroughly for common questions.",
            "self-awareness": "Honestly assess your skill level and validate self-ratings.",
        }

        for key, value in guidance_map.items():
            if key.lower() in topic.lower():
                return value

        return "Review this topic in detail and practice with real-world examples."
