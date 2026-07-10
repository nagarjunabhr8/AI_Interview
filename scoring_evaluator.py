"""
Scoring Evaluator
Evaluates interview responses against scoring rubrics and question-specific guides.
"""

from typing import Dict, Any, Tuple, List
import re


class ScoringEvaluator:
    """Evaluates responses and provides scores with rationale."""

    def __init__(self):
        """Initialize scoring evaluator."""
        self.scoring_guide = self._build_scoring_guide()

    def _build_scoring_guide(self) -> Dict[str, Any]:
        """Build generic and question-specific scoring guides."""
        return {
            "default": {
                0: "No answer / skipped / timeout",
                1: "Attempted, fundamentally incorrect or severely incomplete",
                2: "Partially correct, major conceptual gaps",
                3: "Correct core concept, missing depth or edge cases",
                4: "Correct, well-explained, minor gaps or lacks nuance",
                5: "Correct, precise, includes real-world trade-offs and context"
            },
            "behavioral": {
                0: "No response / evasive",
                1: "Rambling, lacks structure or clarity",
                2: "Some structure but outcome unclear or conflict mishandled",
                3: "STAR method evident, collaborative resolution",
                4: "Clear STAR with metrics/data supporting decision",
                5: "Compelling narrative with team dynamics and strategic value"
            },
            "coding": {
                0: "No attempt",
                1: "Attempted but logic is fundamentally flawed",
                2: "Partially correct logic, fails on edge cases",
                3: "Correct solution but suboptimal time/space complexity",
                4: "Correct with good complexity, minor improvements possible",
                5: "Optimal solution with discussion of trade-offs"
            }
        }

    def score_response(self, response: Dict[str, Any], question: Dict[str, Any]) -> Tuple[int, str]:
        """
        Score a response based on question and answer content.

        Args:
            response: Response dict with answer, skip status, etc.
            question: Question dict with expected answer and scoring guide

        Returns:
            (score: 0-5, rationale: explanation)
        """
        answer = response.get("answer", "").strip()
        is_skipped = response.get("is_skipped", False)

        # Handle skipped/no response
        if is_skipped or not answer or answer in ["[SKIPPED]", "[NO RESPONSE]", "[INTERRUPTED]"]:
            return 0, "No answer provided (skipped, timeout, or no response)"

        # Get question category and expected answer
        category = question.get("category", "general")
        expected_answer = question.get("expected_answer", "")
        question_guide = question.get("scoring_guide", self.scoring_guide["default"])

        # Evaluate based on category
        if category == "fundamentals":
            return self._score_fundamentals(answer, expected_answer, question_guide)
        elif category == "coding_problem":
            return self._score_coding(answer, expected_answer, question_guide)
        elif category == "coding_design":
            return self._score_design(answer, expected_answer, question_guide)
        elif category == "behavioral":
            return self._score_behavioral(answer, expected_answer, question_guide)
        elif category == "tool":
            return self._score_tool(answer, expected_answer, question_guide)
        elif category == "scenario":
            return self._score_scenario(answer, expected_answer, question_guide)
        else:
            return self._score_generic(answer, expected_answer, question_guide)

    def _score_fundamentals(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score fundamental/definition questions."""
        answer_lower = answer.lower()
        expected_lower = expected.lower()

        # Extract key terms from expected answer
        key_terms = self._extract_key_terms(expected)

        # Check coverage
        matching_terms = sum(1 for term in key_terms if term.lower() in answer_lower)
        coverage = matching_terms / len(key_terms) if key_terms else 0

        # Determine score
        if coverage >= 0.8:
            # Check for depth/nuance
            if self._has_examples(answer) or self._has_trade_offs(answer):
                return 5, guide[5]
            elif self._has_second_layer(answer):
                return 4, guide[4]
            else:
                return 3, guide[3]
        elif coverage >= 0.5:
            if self._has_examples(answer):
                return 3, guide[3]
            else:
                return 2, guide[2]
        elif coverage >= 0.25:
            return 2, guide[2]
        else:
            return 1, guide[1]

    def _score_coding(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score coding/logic problems."""
        answer_lower = answer.lower()

        # Check for key indicators
        has_logic = self._has_logic_structure(answer)
        has_complexity_discussion = "time" in answer_lower or "space" in answer_lower or "o(" in answer_lower
        has_edge_cases = "edge" in answer_lower or "empty" in answer_lower or "null" in answer_lower

        if not has_logic:
            return 1, guide[1]

        # Score based on completeness
        if has_complexity_discussion and has_edge_cases:
            if self._has_trade_offs(answer):
                return 5, guide[5]
            else:
                return 4, guide[4]
        elif has_complexity_discussion or has_edge_cases:
            return 3, guide[3]
        elif has_logic:
            return 2, guide[2]
        else:
            return 1, guide[1]

    def _score_design(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score design/architecture questions."""
        answer_lower = answer.lower()

        # Check for design considerations
        has_architecture = "architecture" in answer_lower or "design" in answer_lower or "pattern" in answer_lower
        has_considerations = "consider" in answer_lower or "handle" in answer_lower or "manage" in answer_lower
        has_scalability = "scale" in answer_lower or "performance" in answer_lower or "load" in answer_lower
        has_implementation = self._has_code_example(answer)

        if not has_architecture and not has_design_thinking(answer):
            return 1, guide[1]

        design_points = sum([has_architecture, has_considerations, has_scalability, has_implementation])

        if design_points >= 3 and has_implementation:
            if self._has_trade_offs(answer):
                return 5, guide[5]
            else:
                return 4, guide[4]
        elif design_points >= 2:
            return 3, guide[3]
        elif design_points >= 1:
            return 2, guide[2]
        else:
            return 1, guide[1]

    def _score_behavioral(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score behavioral/soft skill questions."""
        answer_lower = answer.lower()

        # Look for STAR method
        has_situation = any(word in answer_lower for word in ["started at", "was working", "working on", "situation", "was"])
        has_task = any(word in answer_lower for word in ["needed to", "task", "challenge", "problem", "issue"])
        has_action = any(word in answer_lower for word in ["i did", "i said", "i proposed", "action", "decided", "worked"])
        has_result = any(word in answer_lower for word in ["result", "outcome", "learned", "improved", "resolved"])

        star_components = sum([has_situation, has_task, has_action, has_result])

        # Check for specific details and metrics
        has_metrics = any(char.isdigit() for char in answer) or "%" in answer
        has_reflection = "learned" in answer_lower or "improved" in answer_lower or "growth" in answer_lower

        if star_components < 2:
            return 1, guide[1]
        elif star_components == 2:
            return 2, guide[2]
        elif star_components == 3:
            if has_metrics or has_reflection:
                return 4, guide[4]
            else:
                return 3, guide[3]
        else:  # star_components == 4
            if has_metrics and has_reflection:
                return 5, guide[5]
            elif has_metrics or has_reflection:
                return 4, guide[4]
            else:
                return 3, guide[3]

    def _score_tool(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score tool-specific questions."""
        answer_lower = answer.lower()
        expected_lower = expected.lower()

        # Extract key concepts from expected answer
        key_concepts = self._extract_key_terms(expected)
        matching = sum(1 for term in key_concepts if term.lower() in answer_lower)
        coverage = matching / len(key_concepts) if key_concepts else 0

        # Check for depth
        has_architecture = "architecture" in answer_lower or "how" in answer_lower and "work" in answer_lower
        has_advantages = "advantage" in answer_lower or "benefit" in answer_lower or "why" in answer_lower
        has_examples = self._has_examples(answer)

        if coverage >= 0.75:
            if has_architecture and (has_advantages or has_examples):
                return 5, guide[5]
            elif has_architecture or has_advantages:
                return 4, guide[4]
            else:
                return 3, guide[3]
        elif coverage >= 0.5:
            if has_examples:
                return 3, guide[3]
            else:
                return 2, guide[2]
        else:
            return 1, guide[1]

    def _score_scenario(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score scenario/judgment questions."""
        answer_lower = answer.lower()

        # Check for strategic thinking
        has_prioritization = "priorit" in answer_lower or "first" in answer_lower or "critical" in answer_lower
        has_risk_assessment = "risk" in answer_lower or "important" in answer_lower
        has_communication = "commun" in answer_lower or "notify" in answer_lower or "stakeholder" in answer_lower
        has_metrics = "measure" in answer_lower or "metric" in answer_lower or "track" in answer_lower
        has_fallback = "fallback" in answer_lower or "contingency" in answer_lower or "plan b" in answer_lower

        components = sum([has_prioritization, has_risk_assessment, has_communication, has_metrics, has_fallback])

        if components < 2:
            return 1, guide[1]
        elif components == 2:
            return 2, guide[2]
        elif components == 3:
            return 3, guide[3]
        elif components == 4:
            if self._has_examples(answer):
                return 5, guide[5]
            else:
                return 4, guide[4]
        else:  # components == 5
            return 5, guide[5]

    def _score_generic(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Generic scoring fallback."""
        # Extract and match key terms
        key_terms = self._extract_key_terms(expected)
        matching = sum(1 for term in key_terms if term.lower() in answer.lower())
        coverage = matching / len(key_terms) if key_terms else 0

        if coverage >= 0.8:
            return 5 if self._has_trade_offs(answer) else 4, guide[4 if not self._has_trade_offs(answer) else 5]
        elif coverage >= 0.6:
            return 4 if self._has_examples(answer) else 3, guide[3 if not self._has_examples(answer) else 4]
        elif coverage >= 0.4:
            return 2, guide[2]
        elif coverage > 0:
            return 1, guide[1]
        else:
            return 0, guide[0]

    # Helper methods

    def _extract_key_terms(self, text: str) -> List[str]:
        """Extract important terms from text (words > 3 chars, not common)."""
        common_words = {"the", "and", "for", "with", "from", "that", "this", "have", "will", "your"}
        words = re.findall(r'\b\w+\b', text.lower())
        return [w for w in words if len(w) > 3 and w not in common_words]

    def _has_examples(self, text: str) -> bool:
        """Check if answer includes examples."""
        example_indicators = ["example", "such as", "like", "for instance", "e.g.", "in", "project", "case"]
        return any(indicator in text.lower() for indicator in example_indicators)

    def _has_trade_offs(self, text: str) -> bool:
        """Check if answer discusses trade-offs."""
        tradeoff_indicators = ["trade-off", "tradeoff", "vs", "versus", "however", "but", "on the other hand", "benefit", "disadvantage"]
        return any(indicator in text.lower() for indicator in tradeoff_indicators)

    def _has_second_layer(self, text: str) -> bool:
        """Check if answer goes beyond surface level."""
        depth_indicators = ["also", "additionally", "furthermore", "moreover", "such as", "specifically"]
        return any(indicator in text.lower() for indicator in depth_indicators)

    def _has_logic_structure(self, text: str) -> bool:
        """Check if coding answer has logical structure."""
        logic_indicators = ["if", "for", "while", "loop", "function", "method", "=>", "=", "return", "append"]
        return sum(1 for indicator in logic_indicators if indicator in text.lower()) >= 2

    def _has_code_example(self, text: str) -> bool:
        """Check if answer includes code or pseudo-code."""
        code_indicators = ["{", "}", "[", "]", "=>", "def ", "class ", "function", "()"]
        return sum(1 for indicator in code_indicators if indicator in text) >= 2

    def _has_design_thinking(self, text: str) -> bool:
        """Check for design/architecture thinking."""
        design_indicators = ["design", "pattern", "architecture", "structure", "component", "layer"]
        return any(indicator in text.lower() for indicator in design_indicators)

    def evaluate_communication(self, responses: List[Dict[str, Any]]) -> float:
        """
        Evaluate overall communication clarity (1-5 scale).
        Looks at answer structure, clarity, and conciseness across all responses.
        """
        if not responses:
            return 3

        clarity_scores = []

        for response in responses:
            if response.get("is_skipped"):
                continue

            answer = response.get("answer", "").strip()
            if not answer:
                clarity_scores.append(1)
                continue

            # Check structure (paragraphs vs rambling)
            lines = [l.strip() for l in answer.split("\n") if l.strip()]
            has_structure = len(lines) >= 2 and len(lines) <= 10

            # Check conciseness
            avg_line_length = sum(len(line) for line in lines) / len(lines) if lines else 0
            is_concise = avg_line_length < 150  # Reasonable sentence length

            # Check clarity (no excessive jargon, clear explanations)
            jargon_count = sum(1 for term in ["aforementioned", "hereinafter", "notwithstanding"]
                             if term in answer.lower())
            is_clear = jargon_count == 0

            # Score
            score = 3  # baseline
            if has_structure:
                score += 0.5
            if is_concise:
                score += 0.5
            if is_clear:
                score += 0.5

            clarity_scores.append(min(5, score))

        return sum(clarity_scores) / len(clarity_scores) if clarity_scores else 3

    def evaluate_confidence(self, responses: List[Dict[str, Any]]) -> float:
        """
        Evaluate confidence and composure (1-5 scale).
        Looks for hesitation, certainty, and calm handling of difficult questions.
        """
        if not responses:
            return 3

        confidence_scores = []

        for response in responses:
            if response.get("is_skipped"):
                confidence_scores.append(2)  # Skipping suggests lower confidence
                continue

            answer = response.get("answer", "").strip()
            response_time = response.get("response_time_seconds", 0)

            if not answer:
                confidence_scores.append(1)
                continue

            # Check for hesitation language
            hesitation_words = ["i think", "maybe", "probably", "i guess", "not sure", "um", "uh"]
            hesitation_count = sum(1 for word in hesitation_words if word in answer.lower())

            # Check for certainty language
            certainty_words = ["definitely", "clearly", "obviously", "certainly", "absolutely"]
            certainty_count = sum(1 for word in certainty_words if word in answer.lower())

            # Check response time (too quick = maybe not thinking, too slow = hesitation)
            time_score = 3
            if 30 <= response_time <= 90:
                time_score = 4
            elif response_time > 120:
                time_score = 2

            # Calculate score
            score = 3 + (certainty_count * 0.3) - (hesitation_count * 0.3)
            score = (score + time_score) / 2
            confidence_scores.append(min(5, max(1, score)))

        return sum(confidence_scores) / len(confidence_scores) if confidence_scores else 3

    def evaluate_self_awareness(self, candidate_data: Dict[str, Any], responses: List[Dict[str, Any]]) -> float:
        """
        Evaluate self-awareness (1-5 scale).
        Compares self-ratings vs actual performance. Honesty and accurate self-assessment.
        """
        self_ratings = candidate_data.get("self_ratings", {})
        if not self_ratings:
            return 3  # Neutral if no self-ratings provided

        # Calculate average actual performance
        actual_scores = [r.get("score", 3) for r in responses if not r.get("is_skipped") and r.get("score") is not None]
        actual_avg = sum(actual_scores) / len(actual_scores) if actual_scores else 3

        # Scale self-ratings to 0-5
        self_rating_avg = sum(self_ratings.values()) / len(self_ratings) if self_ratings else 3

        # Calculate difference (ideal is close to 0)
        difference = abs(actual_avg - self_rating_avg)

        if difference <= 0.5:
            return 5  # Excellent self-awareness
        elif difference <= 1.0:
            return 4  # Good self-awareness
        elif difference <= 1.5:
            return 3  # Moderate self-awareness
        elif difference <= 2.0:
            return 2  # Poor self-awareness
        else:
            return 1  # Very poor self-awareness


def has_design_thinking(text: str) -> bool:
    """Standalone function for design thinking check."""
    design_indicators = ["design", "pattern", "architecture", "structure", "component", "layer"]
    return any(indicator in text.lower() for indicator in design_indicators)
