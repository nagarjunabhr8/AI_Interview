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

        # Category is a free-text field across many question banks (some
        # use question-type labels like "scenario"/"coding_problem", older
        # banks use topic labels like "Collections"/"OOP") - normalize case
        # so labels that DO correspond to a specialized scorer are matched
        # regardless of how they were capitalized when authored.
        category = question.get("category", "general").strip().lower()
        expected_answer = question.get("expected_answer", "")
        question_guide = question.get("scoring_guide", self.scoring_guide["default"])

        # A trivial non-answer ("I don't know", "not sure", single word)
        # scores 1 regardless of category - everything else goes through
        # the category-specific evaluators below.
        if self._is_trivial_answer(answer):
            return 1, question_guide.get(1, self.scoring_guide["default"][1])

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

    # ------------------------------------------------------------------
    # Category-specific scorers
    #
    # All of these build on a shared base score derived from key-term
    # overlap with the expected answer plus general answer substance
    # (word count/structure), then apply category-specific bonuses for
    # depth (examples, trade-offs, edge cases, structure). The base score
    # never bottoms out at 0/1 purely because the candidate phrased a
    # substantial, on-topic answer differently than the reference text -
    # that was the main cause of unrealistically low scores across every
    # section regardless of actual answer quality.
    # ------------------------------------------------------------------

    def _score_fundamentals(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score fundamental/definition questions."""
        base = self._base_score(answer, expected)

        bonus = 0
        if self._has_examples(answer) or self._has_trade_offs(answer):
            bonus += 1
        if self._has_second_layer(answer):
            bonus += 1

        score = self._clamp(base + bonus)
        return score, guide.get(score, self.scoring_guide["default"][score])

    def _score_coding(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score coding/logic problems."""
        answer_lower = answer.lower()
        base = self._base_score(answer, expected)

        has_logic = self._has_logic_structure(answer)
        has_complexity_discussion = any(
            term in answer_lower for term in ["time complexity", "space complexity", "o(", "big-o", "big o", "complexity", "efficient", "efficiency"]
        )
        has_edge_cases = any(
            term in answer_lower for term in ["edge case", "empty", "null", "boundary", "negative number", "duplicate", "corner case"]
        )

        # A logically-described approach (even in plain English) is worth
        # at least a baseline "correct core idea" score.
        if has_logic:
            base = max(base, 3)

        bonus = 0
        if has_complexity_discussion:
            bonus += 1
        if has_edge_cases:
            bonus += 1
        if bonus >= 1 and self._has_trade_offs(answer):
            bonus += 1

        score = self._clamp(base + bonus)
        return score, guide.get(score, self.scoring_guide["coding"][score])

    def _score_design(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score design/architecture questions."""
        answer_lower = answer.lower()
        base = self._base_score(answer, expected)

        has_architecture = self._has_design_thinking(answer)
        has_considerations = any(term in answer_lower for term in ["consider", "handle", "manage", "trade-off", "constraint"])
        has_scalability = any(term in answer_lower for term in ["scale", "scalability", "performance", "load", "throughput", "latency"])
        has_implementation = self._has_code_example(answer)

        if has_architecture:
            base = max(base, 3)

        bonus = sum([has_considerations, has_scalability, has_implementation])
        if bonus >= 2 and self._has_trade_offs(answer):
            bonus += 1

        score = self._clamp(base + min(bonus, 2))
        return score, guide.get(score, self.scoring_guide["default"][score])

    def _score_behavioral(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score behavioral/soft skill questions."""
        answer_lower = answer.lower()

        # Look for STAR method components with a much broader vocabulary
        # than a handful of exact phrases.
        has_situation = any(word in answer_lower for word in [
            "situation", "context", "at the time", "was working", "working on",
            "during", "while i was", "back when", "on one project", "in a previous"
        ])
        has_task = any(word in answer_lower for word in [
            "task", "challenge", "problem", "issue", "needed to", "had to", "responsible for", "goal was"
        ])
        has_action = any(word in answer_lower for word in [
            "i did", "i decided", "i proposed", "i implemented", "i led", "i worked",
            "action", "decided", "approached", "organized", "coordinated", "reached out", "escalated"
        ])
        has_result = any(word in answer_lower for word in [
            "result", "outcome", "learned", "improved", "resolved", "led to", "as a result",
            "ended up", "successfully", "impact", "reduced", "increased"
        ])

        star_components = sum([has_situation, has_task, has_action, has_result])

        has_metrics = any(char.isdigit() for char in answer) or "%" in answer
        has_reflection = any(w in answer_lower for w in ["learned", "improved", "growth", "in hindsight", "next time"])

        # Substance floor: a lengthy, coherent narrative deserves at least
        # a "core idea present" score even if it doesn't hit every STAR
        # keyword bucket.
        word_count = len(answer.split())
        base = 3 if (star_components >= 2 or word_count >= 40) else max(1, 1 + star_components)

        bonus = 0
        if star_components >= 3:
            bonus += 1
        if has_metrics or has_reflection:
            bonus += 1

        score = self._clamp(base + bonus)
        return score, guide.get(score, self.scoring_guide["behavioral"][score])

    def _score_tool(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score tool/framework-specific questions."""
        answer_lower = answer.lower()
        base = self._base_score(answer, expected)

        has_how_it_works = "how" in answer_lower and ("work" in answer_lower or "use" in answer_lower)
        has_advantages = any(term in answer_lower for term in ["advantage", "benefit", "why", "useful", "helps", "because"])
        has_examples = self._has_examples(answer)

        bonus = sum([has_how_it_works, has_advantages, has_examples])
        score = self._clamp(base + min(bonus, 2))
        return score, guide.get(score, self.scoring_guide["default"][score])

    def _score_scenario(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Score scenario/judgment questions."""
        answer_lower = answer.lower()

        # Judgment answers rarely restate the reference answer's exact
        # wording, but the reference text still captures the sound
        # approach - use it as a base signal instead of ignoring it.
        base = self._base_score(answer, expected)

        has_prioritization = any(term in answer_lower for term in [
            "priorit", "first", "critical", "urgent", "immediately", "focus on"
        ])
        has_risk_assessment = any(term in answer_lower for term in [
            "risk", "important", "impact", "severity", "consequence"
        ])
        has_communication = any(term in answer_lower for term in [
            "commun", "notify", "stakeholder", "escalat", "inform", "discuss", "align", "team", "report", "flag"
        ])
        has_mitigation = any(term in answer_lower for term in [
            "mitigat", "fallback", "contingency", "plan b", "rollback", "workaround", "document", "sign-off", "sign off"
        ])
        has_reasoning = any(term in answer_lower for term in [
            "because", "since", "so that", "in order to", "therefore", "would"
        ])

        components = sum([has_prioritization, has_risk_assessment, has_communication, has_mitigation, has_reasoning])

        # A judgment-style answer with a clear course of action deserves
        # credit even without hitting every one of these buckets.
        if components >= 1:
            base = max(base, 3)

        bonus = 0
        if components >= 3:
            bonus += 1
        if components >= 4 and self._has_examples(answer):
            bonus += 1

        score = self._clamp(base + bonus)
        return score, guide.get(score, self.scoring_guide["default"][score])

    def _score_generic(self, answer: str, expected: str, guide: Dict) -> Tuple[int, str]:
        """Generic scoring fallback (also covers topic-labeled categories
        from older question banks like 'Collections', 'OOP', 'Basics')."""
        base = self._base_score(answer, expected)

        bonus = 0
        if self._has_trade_offs(answer):
            bonus += 1
        if self._has_examples(answer):
            bonus += 1

        score = self._clamp(base + min(bonus, 2))
        return score, guide.get(score, self.scoring_guide["default"][score])

    # ------------------------------------------------------------------
    # Shared scoring helpers
    # ------------------------------------------------------------------

    def _base_score(self, answer: str, expected: str) -> int:
        """
        Derive a 1-5 base score from key-term overlap with the expected
        answer, falling back to answer length/substance when there's
        nothing meaningful to compare against (or the candidate simply
        phrased a correct answer very differently).
        """
        word_count = len(answer.split())
        key_terms = self._extract_key_terms(expected)

        coverage = None
        if key_terms:
            matches = sum(1 for term in key_terms if term in answer.lower())
            coverage = matches / len(key_terms)

        if coverage is not None and coverage >= 0.45:
            return 4
        if coverage is not None and coverage >= 0.25:
            return 3
        if coverage is not None and coverage >= 0.1:
            return 3 if word_count >= 20 else 2

        # Low/no measurable overlap with the reference text - judge on
        # substance so a lengthy, coherent, on-topic answer isn't
        # penalized purely for using different vocabulary.
        if word_count >= 40:
            return 3
        if word_count >= 15:
            return 2
        if word_count >= 6:
            return 2
        return 1

    def _clamp(self, score: int) -> int:
        return max(1, min(5, score))

    def _is_trivial_answer(self, answer: str) -> bool:
        """Detect near-empty or explicit non-answers."""
        normalized = answer.strip().lower().strip(".!? ")
        trivial_phrases = {
            "i don't know", "i dont know", "not sure", "no idea", "n/a", "na",
            "idk", "skip", "pass", "none", "no comment", "not applicable",
        }
        if normalized in trivial_phrases:
            return True
        return len(answer.split()) < 3

    def _extract_key_terms(self, text: str) -> List[str]:
        """Extract important terms from text (words > 3 chars, not common)."""
        common_words = {
            "the", "and", "for", "with", "from", "that", "this", "have", "will", "your",
            "when", "what", "which", "would", "should", "could", "does", "into", "than",
            "then", "them", "they", "there", "their", "about", "each", "these", "those",
            "some", "such", "also", "over", "more", "most", "very", "just", "like",
        }
        words = re.findall(r'\b\w+\b', text.lower())
        return [w for w in words if len(w) > 3 and w not in common_words]

    def _has_examples(self, text: str) -> bool:
        """Check if answer includes concrete examples (specific enough
        phrases to avoid false positives like "in my opinion")."""
        example_indicators = [
            "for example", "such as", "for instance", "e.g.", "in my experience",
            "in my previous project", "in a previous role", "case study",
            "real-world scenario", "in practice", "specifically,",
        ]
        return any(indicator in text.lower() for indicator in example_indicators)

    def _has_trade_offs(self, text: str) -> bool:
        """Check if answer discusses trade-offs."""
        tradeoff_indicators = [
            "trade-off", "tradeoff", "vs", "versus", "however", "but", "on the other hand",
            "benefit", "disadvantage", "downside", "whereas", "compared to", "pros and cons",
        ]
        return any(indicator in text.lower() for indicator in tradeoff_indicators)

    def _has_second_layer(self, text: str) -> bool:
        """Check if answer goes beyond surface level."""
        depth_indicators = ["also", "additionally", "furthermore", "moreover", "such as", "specifically", "in addition", "beyond that"]
        return any(indicator in text.lower() for indicator in depth_indicators)

    def _has_logic_structure(self, text: str) -> bool:
        """Check if a coding answer describes an algorithmic approach -
        broad enough to recognize plain-English explanations, not just
        literal code syntax."""
        logic_indicators = [
            "if", "for", "while", "loop", "iterate", "iteration", "traverse", "traversal",
            "recursion", "recursive", "pointer", "index", "swap", "compare", "increment",
            "decrement", "array", "list", "hashmap", "hash map", "dictionary", "stack",
            "queue", "sort", "search", "function", "method", "algorithm", "return",
            "append", "push", "pop", "step", "check", "counter", "variable",
        ]
        return sum(1 for indicator in logic_indicators if indicator in text.lower()) >= 2

    def _has_code_example(self, text: str) -> bool:
        """Check if answer includes code or pseudo-code."""
        code_indicators = ["{", "}", "[", "]", "=>", "def ", "class ", "function", "()"]
        return sum(1 for indicator in code_indicators if indicator in text) >= 2

    def _has_design_thinking(self, text: str) -> bool:
        """Check for design/architecture thinking."""
        design_indicators = [
            "design", "pattern", "architecture", "structure", "component", "layer",
            "module", "interface", "decouple", "separation of concerns", "scalab",
        ]
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
