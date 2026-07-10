"""
Report Generator
Generates comprehensive, professional written interview reports.
"""

import json
import os
from typing import Dict, Any, List
from datetime import datetime


class ReportGenerator:
    """Generates professional interview reports."""

    def __init__(self, scored_session: Dict[str, Any]):
        """
        Initialize report generator with scored session data.

        Args:
            scored_session: Complete scoring data from Phase 2
        """
        self.scored_session = scored_session
        self.candidate = scored_session.get("candidate", {})
        self.analysis = scored_session.get("analysis", {})
        self.metadata = scored_session.get("session_metadata", {})

    def generate_markdown_report(self) -> str:
        """Generate comprehensive Markdown report."""
        sections = [
            self._section_header(),
            self._section_candidate_summary(),
            self._section_overall_performance(),
            self._section_dimensions_table(),
            self._section_qa_transcript(),
            self._section_section_breakdown(),
            self._section_strengths(),
            self._section_improvement_areas(),
            self._section_communication_feedback(),
            self._section_recommendations(),
            self._section_footer()
        ]

        return "\n\n".join(sections)

    def generate_html_report(self) -> str:
        """Generate comprehensive HTML report (professional styling)."""
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
            max-width: 900px;
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

        .subtitle {{
            color: #7f8c8d;
            font-size: 14px;
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
            color: #34495e;
            font-size: 16px;
            margin-top: 15px;
            margin-bottom: 10px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 14px;
        }}

        th {{
            background: #34495e;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}

        tr:nth-child(even) {{
            background: #f9f9f9;
        }}

        tr:hover {{
            background: #f0f0f0;
        }}

        .score-cell {{
            font-weight: 600;
            text-align: center;
        }}

        .score-excellent {{
            color: #27ae60;
        }}

        .score-strong {{
            color: #2980b9;
        }}

        .score-adequate {{
            color: #f39c12;
        }}

        .score-weak {{
            color: #e74c3c;
        }}

        .score-poor {{
            color: #c0392b;
        }}

        .summary-box {{
            background: #ecf0f1;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }}

        .verdict-box {{
            background: #d5f4e6;
            border-left: 4px solid #27ae60;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }}

        .verdict-strong {{
            background: #d5f4e6;
            border-left-color: #27ae60;
        }}

        .verdict-hire {{
            background: #d6eaf8;
            border-left-color: #2980b9;
        }}

        .verdict-reservations {{
            background: #fdebd0;
            border-left-color: #f39c12;
        }}

        .verdict-nohire {{
            background: #fadbd8;
            border-left-color: #e74c3c;
        }}

        .score-breakdown {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 15px 0;
        }}

        .score-item {{
            background: #ecf0f1;
            padding: 12px;
            border-radius: 4px;
        }}

        .score-label {{
            font-weight: 600;
            color: #2c3e50;
        }}

        .score-value {{
            font-size: 24px;
            font-weight: 700;
            color: #3498db;
            margin-top: 5px;
        }}

        .qa-block {{
            background: #f9f9f9;
            border-left: 3px solid #95a5a6;
            padding: 15px;
            margin: 15px 0;
            border-radius: 3px;
        }}

        .qa-question {{
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 8px;
        }}

        .qa-answer {{
            color: #555;
            font-style: italic;
            margin: 8px 0;
            padding-left: 10px;
            border-left: 2px solid #bdc3c7;
        }}

        .qa-expected {{
            color: #27ae60;
            margin: 8px 0;
            padding-left: 10px;
            border-left: 2px solid #27ae60;
        }}

        .qa-score {{
            margin-top: 8px;
            font-size: 14px;
        }}

        .strength-item, .weakness-item {{
            background: #f9f9f9;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #27ae60;
        }}

        .weakness-item {{
            border-left-color: #e74c3c;
        }}

        .evidence {{
            color: #7f8c8d;
            font-size: 13px;
            margin-top: 5px;
            font-style: italic;
        }}

        .resource-list {{
            list-style: none;
            padding-left: 0;
        }}

        .resource-list li {{
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
        }}

        .resource-list li:before {{
            content: "→";
            position: absolute;
            left: 0;
            color: #3498db;
            font-weight: bold;
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
            a {{
                color: #2980b9;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {self._html_section_header()}
        {self._html_section_candidate_summary()}
        {self._html_section_overall_performance()}
        {self._html_section_dimensions_table()}
        <div class="page-break"></div>
        {self._html_section_qa_transcript()}
        <div class="page-break"></div>
        {self._html_section_section_breakdown()}
        {self._html_section_strengths()}
        {self._html_section_improvement_areas()}
        <div class="page-break"></div>
        {self._html_section_communication_feedback()}
        {self._html_section_recommendations()}
        {self._html_section_footer()}
    </div>
</body>
</html>"""

    # Markdown sections
    def _section_header(self) -> str:
        """Generate report header."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        return f"""# Interview Assessment Report

**Candidate:** {self.candidate.get('role', 'Technical Role')}
**Date:** {timestamp}
**Difficulty Level:** {self.candidate.get('difficulty_level', 'Unknown')}
**Experience:** {self.candidate.get('years_of_experience', 'N/A')} years

---"""

    def _section_candidate_summary(self) -> str:
        """Generate candidate summary."""
        summary = self.analysis.get("summary", {})
        skills = ", ".join(self.candidate.get("primary_skills", []))

        return f"""## Candidate Summary

| Aspect | Details |
|--------|---------|
| **Role Targeted** | {self.candidate.get('role', 'N/A')} |
| **Years of Experience** | {self.candidate.get('years_of_experience', 'N/A')} |
| **Primary Skills** | {skills} |
| **Interview Difficulty** | {self.candidate.get('difficulty_level', 'N/A')} |
| **Questions Asked** | {summary.get('total_questions', 0)} |
| **Questions Answered** | {summary.get('answered_questions', 0)} |
| **Questions Skipped** | {summary.get('skipped_questions', 0)} |
| **Response Rate** | {summary.get('response_rate_percent', 0)}% |
| **Interview Duration** | {self.metadata.get('elapsed_time_minutes', 'N/A')} minutes |"""

    def _section_overall_performance(self) -> str:
        """Generate overall performance section."""
        overall_score = self.analysis.get("overall_score", 0)
        verdict = self.analysis.get("hiring_verdict", "Unknown")

        return f"""## Overall Performance

**Overall Score:** {overall_score}/100

**Hiring Verdict:** **{verdict}**

{self._verdict_explanation(verdict)}"""

    def _verdict_explanation(self, verdict: str) -> str:
        """Generate explanation for verdict."""
        explanations = {
            "Strong Hire": "Exceptional candidate demonstrating strong technical expertise, clear communication, and confident problem-solving. Ready for immediate offer consideration.",
            "Hire": "Solid candidate with good technical competencies and communication skills. Suitable for the role with positive trajectory.",
            "Hire with Reservations / Needs one more round": "Candidate shows potential but has development areas in key skills. Recommend another interview round for assessment or structured feedback plan.",
            "No Hire (this round)": "Candidate did not meet minimum requirements for this level at this time. Consider re-interview for lower level or with additional preparation."
        }
        return explanations.get(verdict, "")

    def _section_dimensions_table(self) -> str:
        """Generate dimensions breakdown table."""
        dims = self.analysis.get("dimension_scores", {})

        rows = []
        for dimension, score in dims.items():
            if score is not None:
                dim_name = dimension.replace("_", " ").title()
                level = self._performance_level(score)
                rows.append(f"| {dim_name} | {score}/5 | {level} |")

        table = """## Performance Dimensions

| Dimension | Score | Level |
|-----------|-------|-------|
""" + "\n".join(rows)

        return table

    def _section_qa_transcript(self) -> str:
        """Generate Q&A transcript."""
        responses = self.analysis.get("scored_responses", [])

        transcript = "## Question-by-Question Transcript\n\n"

        for idx, response in enumerate(responses, 1):
            question = response.get("question_text", "Unknown")
            answer = response.get("answer", "[No response]")
            score = response.get("score", 0)
            rationale = response.get("scoring_rationale", "")
            is_skipped = response.get("is_skipped", False)

            # Truncate long answers
            if len(answer) > 300:
                answer = answer[:300] + "..."

            score_text = f"Score: **{score}/5**" if not is_skipped else "**SKIPPED**"
            rationale_text = f"*{rationale}*" if rationale else ""

            transcript += f"""### Q{idx}: {question}

**Candidate's Answer:**
> {answer}

{score_text}
{rationale_text}

---

"""

        return transcript

    def _section_section_breakdown(self) -> str:
        """Generate section-wise performance breakdown."""
        section_analysis = self.analysis.get("section_analysis", {})

        breakdown = "## Section-wise Performance Breakdown\n\n"
        breakdown += "| Section | Avg Score | Level | Questions |\n"
        breakdown += "|---------|-----------|-------|----------|\n"

        for section, data in sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0), reverse=True):
            avg = data.get("average_score", 0)
            level = data.get("performance_level", "Unknown")
            count = data.get("total_questions", 0)
            breakdown += f"| {section} | {avg}/5 | {level} | {count} |\n"

        return breakdown

    def _section_strengths(self) -> str:
        """Generate strengths section."""
        summary = self.analysis.get("summary", {})
        strengths = summary.get("strengths", [])

        section = "## Key Strengths\n\n"
        for i, strength in enumerate(strengths[:5], 1):
            section += f"{i}. {strength}\n"

        return section

    def _section_improvement_areas(self) -> str:
        """Generate improvement areas."""
        summary = self.analysis.get("summary", {})
        weaknesses = summary.get("weaknesses", [])

        section = "## Areas for Improvement\n\n"
        for i, weakness in enumerate(weaknesses[:5], 1):
            topic = weakness.split(":")[0]
            section += f"**{i}. {topic}**  \n"
            section += f"Current Level: {weakness}  \n"
            section += self._improvement_guidance(topic) + "\n\n"

        return section

    def _improvement_guidance(self, topic: str) -> str:
        """Generate specific improvement guidance."""
        guidance_map = {
            "playwright": "Review Playwright's auto-wait mechanism, actionability checks, browser context isolation, and advanced features like network interception and visual testing.",
            "selenium": "Study Selenium's architecture, WebDriver protocol, explicit vs implicit waits, and advanced locator strategies.",
            "coding": "Practice algorithmic problems focusing on time/space complexity analysis, edge case handling, and multiple solution approaches.",
            "communication clarity": "Work on structuring answers using clear paragraphs, avoiding jargon, and using concrete examples to explain concepts.",
            "technical depth": "Deep dive into fundamentals: SDLC/STLC lifecycle, testing types, frameworks, and methodologies. Read industry resources and case studies.",
            "confidence": "Practice mock interviews, prepare for common questions, and develop a growth mindset around uncertainty.",
            "self-awareness": "Assess your actual skill level honestly. Practice and validate self-ratings before interviews.",
        }

        for key, value in guidance_map.items():
            if key.lower() in topic.lower():
                return value

        return "Review this topic in detail and practice with real-world examples."

    def _section_communication_feedback(self) -> str:
        """Generate communication and presentation feedback."""
        dims = self.analysis.get("dimension_scores", {})
        comm_score = dims.get("communication_clarity", 3)

        feedback = """## Communication & Presentation Feedback

### Clarity & Structure
"""

        if comm_score >= 4:
            feedback += "✓ **Strong** - Answers were well-structured with clear logical flow.\n"
        elif comm_score >= 3:
            feedback += "⚠ **Adequate** - Answers had basic structure but could be more organized.\n"
        else:
            feedback += "✗ **Needs Improvement** - Answers were unclear or rambling.\n"

        feedback += """
### Conciseness
"""

        if comm_score >= 4:
            feedback += "✓ Appropriate length for most questions without unnecessary verbosity.\n"
        elif comm_score >= 3:
            feedback += "⚠ Some answers could be more concise or some could provide more detail.\n"
        else:
            feedback += "✗ Consider trimming verbose answers or adding necessary detail.\n"

        feedback += """
### Technical Vocabulary
"""
        if comm_score >= 4:
            feedback += "✓ Appropriate use of technical terms with clear explanations.\n"
        elif comm_score >= 3:
            feedback += "⚠ Generally good but could clarify some technical terms.\n"
        else:
            feedback += "✗ Review technical terminology and practice explaining complex concepts simply.\n"

        return feedback

    def _section_recommendations(self) -> str:
        """Generate recommendations."""
        summary = self.analysis.get("summary", {})
        overall_score = self.analysis.get("overall_score", 0)
        section_analysis = self.analysis.get("section_analysis", {})

        # Find weakest sections
        weakest_sections = sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0))[:3]

        recommendations = """## Recommended Next Steps

### Study Plan (Prioritized by Weakness)

"""
        for i, (section, data) in enumerate(weakest_sections, 1):
            score = data.get("average_score", 0)
            recommendations += f"**{i}. {section}** (Current: {score}/5)\n"

        recommendations += f"""
### Suggested Re-attempt Difficulty
"""

        if overall_score >= 85:
            recommendations += "Consider attempting a **Higher Difficulty** level (if available) to further challenge yourself."
        elif overall_score >= 70:
            recommendations += "Current difficulty level is appropriate. For continued growth, consider **Hard/Advanced** level after 2-4 weeks of preparation."
        elif overall_score >= 55:
            recommendations += "Recommend focusing on improving core areas for 2-4 weeks, then **re-attempt at current difficulty level**."
        else:
            recommendations += "Recommend **re-attempting at a lower difficulty level** (Fresher or Basic) with focused study on fundamentals."

        recommendations += f"""

### Resource Recommendations

- **Technical Fundamentals:** Review SDLC/STLC, testing types, and QA methodologies documentation
- **Tool-Specific:** Official documentation and tutorials for declared tools
- **Coding Skills:** Practice on LeetCode, HackerRank (start with Easy, progress to Medium)
- **Communication:** Practice explaining technical concepts to non-technical audience
- **Mock Interviews:** Conduct 2-3 mock interviews before re-attempt

### Timeline Recommendation

- **Days 1-3:** Study weakest areas
- **Days 4-7:** Practice coding problems and tool-specific scenarios
- **Days 8-10:** Conduct mock interviews and get feedback
- **Day 11+:** Re-attempt interview when confident
"""

        return recommendations

    def _section_footer(self) -> str:
        """Generate footer."""
        return f"""---

## Report Metadata

- **Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
- **Assessment Version:** 1.0
- **Interviewer:** AI Interview Panelist

This report is confidential and intended for the candidate's personal development.
Best of luck with your continued growth!"""

    # HTML sections
    def _html_section_header(self) -> str:
        """Generate HTML header."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        return f"""<div class="header">
            <h1>Interview Assessment Report</h1>
            <p class="subtitle">
                {self.candidate.get('role', 'Technical Role')}
                • {self.candidate.get('difficulty_level', 'Unknown')} Difficulty
                • {timestamp}
            </p>
        </div>"""

    def _html_section_candidate_summary(self) -> str:
        """Generate HTML candidate summary."""
        summary = self.analysis.get("summary", {})
        skills = ", ".join(self.candidate.get("primary_skills", []))

        return f"""<h2>Candidate Summary</h2>
        <table>
            <tr>
                <th>Aspect</th>
                <th>Details</th>
            </tr>
            <tr>
                <td><strong>Role Targeted</strong></td>
                <td>{self.candidate.get('role', 'N/A')}</td>
            </tr>
            <tr>
                <td><strong>Years of Experience</strong></td>
                <td>{self.candidate.get('years_of_experience', 'N/A')}</td>
            </tr>
            <tr>
                <td><strong>Primary Skills</strong></td>
                <td>{skills}</td>
            </tr>
            <tr>
                <td><strong>Interview Difficulty</strong></td>
                <td>{self.candidate.get('difficulty_level', 'N/A')}</td>
            </tr>
            <tr>
                <td><strong>Questions Asked</strong></td>
                <td>{summary.get('total_questions', 0)}</td>
            </tr>
            <tr>
                <td><strong>Questions Answered</strong></td>
                <td>{summary.get('answered_questions', 0)}</td>
            </tr>
            <tr>
                <td><strong>Questions Skipped</strong></td>
                <td>{summary.get('skipped_questions', 0)}</td>
            </tr>
            <tr>
                <td><strong>Response Rate</strong></td>
                <td>{summary.get('response_rate_percent', 0)}%</td>
            </tr>
            <tr>
                <td><strong>Interview Duration</strong></td>
                <td>{self.metadata.get('elapsed_time_minutes', 'N/A')} minutes</td>
            </tr>
        </table>"""

    def _html_section_overall_performance(self) -> str:
        """Generate HTML overall performance."""
        overall_score = self.analysis.get("overall_score", 0)
        verdict = self.analysis.get("hiring_verdict", "Unknown")
        verdict_class = self._get_verdict_class(verdict)

        return f"""<h2>Overall Performance</h2>
        <div class="verdict-box {verdict_class}">
            <div style="font-size: 36px; font-weight: 700; color: #2c3e50;">
                {overall_score}/100
            </div>
            <div style="font-size: 18px; font-weight: 600; margin-top: 10px;">
                {verdict}
            </div>
            <p style="margin-top: 10px; color: #555;">
                {self._verdict_explanation(verdict)}
            </p>
        </div>"""

    def _html_section_dimensions_table(self) -> str:
        """Generate HTML dimensions table."""
        dims = self.analysis.get("dimension_scores", {})

        rows = ""
        for dimension, score in dims.items():
            if score is not None:
                dim_name = dimension.replace("_", " ").title()
                level = self._performance_level(score)
                score_class = self._get_score_class(score)
                rows += f"""<tr>
                    <td>{dim_name}</td>
                    <td class="score-cell {score_class}">{score}/5</td>
                    <td>{level}</td>
                </tr>"""

        return f"""<h2>Performance Dimensions</h2>
        <table>
            <tr>
                <th>Dimension</th>
                <th>Score</th>
                <th>Level</th>
            </tr>
            {rows}
        </table>"""

    def _html_section_qa_transcript(self) -> str:
        """Generate HTML Q&A transcript."""
        responses = self.analysis.get("scored_responses", [])

        qa_blocks = ""
        for idx, response in enumerate(responses, 1):
            question = response.get("question_text", "Unknown")
            answer = response.get("answer", "[No response]")
            score = response.get("score", 0)
            rationale = response.get("scoring_rationale", "")
            is_skipped = response.get("is_skipped", False)

            if len(answer) > 300:
                answer = answer[:300] + "..."

            score_html = f"<span class='score-cell {self._get_score_class(score)}'>Score: {score}/5</span>" if not is_skipped else "<span style='color: #e74c3c; font-weight: 600;'>SKIPPED</span>"

            qa_blocks += f"""<div class="qa-block">
                <div class="qa-question">Q{idx}: {question}</div>
                <div class="qa-answer"><strong>Your Answer:</strong> {answer}</div>
                <div style="margin-top: 8px;">{score_html}</div>
                <div style="color: #7f8c8d; font-size: 13px; margin-top: 5px;"><em>{rationale}</em></div>
            </div>"""

        return f"""<h2>Question-by-Question Transcript</h2>
        {qa_blocks}"""

    def _html_section_section_breakdown(self) -> str:
        """Generate HTML section breakdown."""
        section_analysis = self.analysis.get("section_analysis", {})

        rows = ""
        for section, data in sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0), reverse=True):
            avg = data.get("average_score", 0)
            level = data.get("performance_level", "Unknown")
            count = data.get("total_questions", 0)
            score_class = self._get_score_class(avg)
            rows += f"""<tr>
                <td>{section}</td>
                <td class="score-cell {score_class}">{avg}/5</td>
                <td>{level}</td>
                <td class="score-cell">{count}</td>
            </tr>"""

        return f"""<h2>Section-wise Performance Breakdown</h2>
        <table>
            <tr>
                <th>Section</th>
                <th>Avg Score</th>
                <th>Level</th>
                <th>Questions</th>
            </tr>
            {rows}
        </table>"""

    def _html_section_strengths(self) -> str:
        """Generate HTML strengths."""
        summary = self.analysis.get("summary", {})
        strengths = summary.get("strengths", [])

        strength_items = ""
        for strength in strengths[:5]:
            strength_items += f"""<div class="strength-item">
                <strong>{strength}</strong>
            </div>"""

        return f"""<h2>Key Strengths</h2>
        {strength_items}"""

    def _html_section_improvement_areas(self) -> str:
        """Generate HTML improvement areas."""
        summary = self.analysis.get("summary", {})
        weaknesses = summary.get("weaknesses", [])

        weakness_items = ""
        for weakness in weaknesses[:5]:
            topic = weakness.split(":")[0]
            guidance = self._improvement_guidance(topic)
            weakness_items += f"""<div class="weakness-item">
                <strong>{weakness}</strong>
                <div class="evidence">{guidance}</div>
            </div>"""

        return f"""<h2>Areas for Improvement</h2>
        {weakness_items}"""

    def _html_section_communication_feedback(self) -> str:
        """Generate HTML communication feedback."""
        dims = self.analysis.get("dimension_scores", {})
        comm_score = dims.get("communication_clarity", 3)

        clarity_feedback = "✓ <strong>Strong</strong> - Answers were well-structured with clear logical flow." if comm_score >= 4 else ("⚠ <strong>Adequate</strong> - Answers had basic structure but could be more organized." if comm_score >= 3 else "✗ <strong>Needs Improvement</strong> - Answers were unclear or rambling.")

        return f"""<h2>Communication & Presentation Feedback</h2>
        <h3>Clarity & Structure</h3>
        <p>{clarity_feedback}</p>
        <h3>Conciseness</h3>
        <p>Ensure answers are appropriately detailed without unnecessary verbosity or excessive brevity.</p>
        <h3>Technical Vocabulary</h3>
        <p>Continue refining technical communication - balance precision with clarity for varied audiences.</p>"""

    def _html_section_recommendations(self) -> str:
        """Generate HTML recommendations."""
        summary = self.analysis.get("summary", {})
        overall_score = self.analysis.get("overall_score", 0)
        section_analysis = self.analysis.get("section_analysis", {})

        weakest_sections = sorted(section_analysis.items(), key=lambda x: x[1].get("average_score", 0))[:3]

        weakest_html = ""
        for i, (section, data) in enumerate(weakest_sections, 1):
            score = data.get("average_score", 0)
            weakest_html += f"<div style='margin: 10px 0;'><strong>{i}. {section}</strong> (Current: {score}/5)</div>"

        difficulty_rec = "Consider attempting a **Higher Difficulty** level to further challenge yourself." if overall_score >= 85 else ("Current difficulty level is appropriate. For growth, consider **Hard/Advanced** level after 2-4 weeks of preparation." if overall_score >= 70 else ("Recommend focusing on improving core areas for 2-4 weeks, then **re-attempt at current difficulty level**." if overall_score >= 55 else "Recommend **re-attempting at a lower difficulty level** with focused study on fundamentals."))

        return f"""<h2>Recommended Next Steps</h2>
        <h3>Study Plan (Prioritized by Weakness)</h3>
        {weakest_html}
        <h3>Suggested Re-attempt Difficulty</h3>
        <p>{difficulty_rec}</p>
        <h3>Resource Recommendations</h3>
        <ul class="resource-list">
            <li>Technical Fundamentals: SDLC/STLC, testing types, methodologies</li>
            <li>Tool-Specific: Official documentation for declared tools</li>
            <li>Coding Skills: LeetCode, HackerRank (Easy → Medium)</li>
            <li>Communication: Practice explaining technical concepts</li>
            <li>Mock Interviews: 2-3 before re-attempt</li>
        </ul>"""

    def _html_section_footer(self) -> str:
        """Generate HTML footer."""
        return f"""<div class="footer">
            <p><strong>Generated:</strong> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
            <p><strong>Assessment Version:</strong> 1.0</p>
            <p>This report is confidential and intended for personal development. Best of luck with your continued growth!</p>
        </div>"""

    # Helper methods
    def _performance_level(self, score: float) -> str:
        """Convert score to performance level."""
        if score >= 4.5:
            return "Excellent"
        elif score >= 3.5:
            return "Strong"
        elif score >= 2.5:
            return "Adequate"
        elif score >= 1.5:
            return "Weak"
        else:
            return "Poor"

    def _get_score_class(self, score: float) -> str:
        """Get CSS class for score."""
        if score >= 4.5:
            return "score-excellent"
        elif score >= 3.5:
            return "score-strong"
        elif score >= 2.5:
            return "score-adequate"
        elif score >= 1.5:
            return "score-weak"
        else:
            return "score-poor"

    def _get_verdict_class(self, verdict: str) -> str:
        """Get CSS class for verdict."""
        if "Strong Hire" in verdict:
            return "verdict-strong"
        elif "Hire" in verdict and "Reservations" not in verdict:
            return "verdict-hire"
        elif "Reservations" in verdict:
            return "verdict-reservations"
        else:
            return "verdict-nohire"
