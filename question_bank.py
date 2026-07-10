"""
Question Bank for Interview Agent
Generates role-specific, difficulty-scaled questions based on candidate profile.
"""

from typing import List, Dict, Any, Optional


class QuestionBank:
    """Manages question generation and retrieval."""

    def __init__(self, role: str, difficulty: str, primary_skills: List[str],
                 years_of_experience: float, self_ratings: Dict[str, int]):
        """
        Initialize question bank based on candidate profile.

        Args:
            role: Target role (e.g., 'QA Engineer', 'Backend Developer')
            difficulty: Fresher, Basic, Simple, or Hard
            primary_skills: List of primary skills
            years_of_experience: Numeric years
            self_ratings: Dict of skill -> rating (1-5)
        """
        self.role = role
        self.difficulty = difficulty
        self.primary_skills = primary_skills
        self.years_of_experience = years_of_experience
        self.self_ratings = self_ratings or {}

        self.questions: List[Dict[str, Any]] = []
        self._generate_questions()

    def _generate_questions(self):
        """Generate question pool based on role and difficulty."""
        # Determine if QA role
        is_qa_role = any(keyword in self.role.lower()
                        for keyword in ["qa", "sdet", "test", "automation"])

        if is_qa_role:
            self._add_qa_questions()
        else:
            self._add_backend_questions()

        # Always add common sections
        self._add_warmup_questions()
        self._add_programming_questions()
        self._add_tool_questions()

        if is_qa_role:
            self._add_framework_design_questions()

        self._add_cicd_questions()
        self._add_leadership_questions()
        self._add_closing_questions()

    def _add_warmup_questions(self):
        """Section 1: Warm-up / Introduction."""
        self.questions.append({
            "id": "warmup_01",
            "section": "Introduction",
            "question": "Walk me through your background and current role. What drew you to this field?",
            "difficulty_levels": ["Fresher", "Basic", "Simple", "Hard"],
            "category": "behavioral",
            "expected_answer": "A concise 2-3 min overview of career journey, current role, key responsibilities, and motivation.",
            "scoring_guide": {
                0: "No response / evasive",
                1: "Rambling, lacks structure or clarity",
                2: "Basic overview but missing key details or motivation",
                3: "Clear, well-structured, mentions role and motivation",
                4: "Well-articulated with specific achievements and growth trajectory",
                5: "Compelling narrative showing progression, strategic thinking, and clear motivation"
            }
        })

    def _add_qa_questions(self):
        """QA-specific fundamental questions."""

        # A. QA Fundamentals & SDLC/STLC
        self.questions.extend([
            {
                "id": "qa_fundamentals_01",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "What is the difference between SDLC and STLC? When does QA typically get involved?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "SDLC = full software development cycle; STLC = test-specific cycle. QA should be involved from requirements phase (shift-left).",
                "scoring_guide": {
                    0: "No answer",
                    1: "Confused or incorrect definitions",
                    2: "Partial understanding, missing shift-left concept",
                    3: "Correct definitions, mentions involvement in early phases",
                    4: "Clear, includes entry/exit criteria implications",
                    5: "Detailed, includes risk-based testing tie-in and real-world examples"
                }
            },
            {
                "id": "qa_fundamentals_02",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "Explain the difference between Verification and Validation.",
                "difficulty_levels": ["Fresher", "Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Verification = are we building it right? (process-focused). Validation = are we building the right thing? (product-focused).",
                "scoring_guide": {
                    0: "No answer",
                    1: "Confused or reversed definitions",
                    2: "One definition correct, other unclear",
                    3: "Both correct with simple examples",
                    4: "Clear distinction with practical examples",
                    5: "Detailed with V-model positioning and phase mapping"
                }
            },
            {
                "id": "qa_fundamentals_03",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "What's the difference between Severity and Priority in a defect? Give an example.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Severity = impact on functionality (critical/high/medium/low). Priority = when to fix (1/2/3/4). A low-priority critical bug & high-priority minor bug can coexist.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Confused, no clear distinction",
                    2: "Definitions reversed or vague",
                    3: "Correct definitions, basic example",
                    4: "Clear definitions with good example",
                    5: "Detailed with matrix examples (high severity/low priority, etc.)"
                }
            },
        ])

        # B. Test Planning & Strategy
        self.questions.extend([
            {
                "id": "qa_planning_01",
                "section": "Test Planning & Strategy",
                "question": "What's the difference between a Test Plan and a Test Strategy?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Test Strategy = high-level approach (document scope, types, approach). Test Plan = detailed execution plan for specific release (timeline, resources, tools).",
                "scoring_guide": {
                    0: "No answer",
                    1: "No clear distinction",
                    2: "Partial understanding, some confusion",
                    3: "Clear distinction with scope/resources/timeline examples",
                    4: "Well-articulated with document contents",
                    5: "Detailed, includes entry/exit criteria, risk considerations"
                }
            },
            {
                "id": "qa_planning_02",
                "section": "Test Planning & Strategy",
                "question": "You're given a tight deadline and can't test everything. How do you decide what to test first?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Risk-based testing: prioritize by business criticality, frequency of use, and defect history. Focus on core flows first.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Ad-hoc or uninformed approach",
                    2: "Some prioritization logic but incomplete",
                    3: "Risk-based approach, mentions business criticality",
                    4: "Clear strategy with risk matrix or prioritization framework",
                    5: "Strategic with real-world examples and stakeholder communication"
                }
            },
        ])

        # C. Types of Testing
        self.questions.extend([
            {
                "id": "qa_testing_types_01",
                "section": "Testing Types",
                "question": "Explain the difference between Smoke, Sanity, and Regression testing.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Smoke = basic flow checks post-build (quick). Sanity = verify specific fix/feature works. Regression = ensure no new defects in unchanged code.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Confused, no clear distinction",
                    2: "Partial understanding, scope overlaps",
                    3: "Correct distinctions with examples",
                    4: "Clear with timing and scope details",
                    5: "Detailed with automation strategy per test type"
                }
            },
            {
                "id": "qa_testing_types_02",
                "section": "Testing Types",
                "question": "What is the difference between Functional and Non-Functional testing? Name 3 non-functional types.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Functional = does feature work as expected. Non-functional = performance, security, accessibility, usability, load/stress testing.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Unclear distinction, few examples",
                    2: "Basic understanding, 1-2 non-functional types",
                    3: "Clear distinction, 3+ non-functional types correct",
                    4: "Detailed with examples and tools",
                    5: "Strategic view including how to prioritize non-functional testing"
                }
            },
            {
                "id": "qa_testing_types_03",
                "section": "Testing Types",
                "question": "When would you use API testing over UI testing? What are the benefits?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "API testing is faster, less flaky, independent of UI changes. Use for contract validation, edge cases. UI testing validates actual user experience.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or incorrect benefits",
                    2: "Some benefits mentioned, incomplete reasoning",
                    3: "Good understanding of when/why to use each",
                    4: "Strategic layer thinking, tool awareness",
                    5: "Balanced view with test pyramid strategy and tool recommendations"
                }
            },
        ])

        # D. Methodologies & Process
        self.questions.extend([
            {
                "id": "qa_agile_01",
                "section": "Methodologies & Process",
                "question": "Describe QA's role in an Agile/Scrum sprint. What is 'Definition of Done'?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "QA participates in sprint planning, daily standup, review. Definition of Done = criteria a story must meet (code review, test coverage, docs, etc.) before close.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or limited understanding",
                    2: "Mentions sprint ceremonies but unclear DoD",
                    3: "Clear role and DoD criteria examples",
                    4: "Detailed with collaboration points and test coverage expectations",
                    5: "Strategic including shift-left, test automation, and metrics"
                }
            },
            {
                "id": "qa_agile_02",
                "section": "Methodologies & Process",
                "question": "What is BDD and how does it differ from traditional test automation?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "BDD (Behavior-Driven Development) uses Gherkin (Given-When-Then) to bridge business & technical. Tests read like requirements. Differs from script-based automation.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Unclear or incorrect",
                    2: "Basic understanding of Gherkin format",
                    3: "Clear understanding, mentions business collaboration",
                    4: "Includes cucumber/tool knowledge and benefits",
                    5: "Strategic view on when/how to adopt, team dynamics"
                }
            },
        ])

    def _add_backend_questions(self):
        """Backend/DevOps-specific fundamental questions."""
        self.questions.extend([
            {
                "id": "backend_fundamentals_01",
                "section": "Backend Fundamentals",
                "question": "Explain the difference between REST and GraphQL APIs. When would you use each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "REST = resource-based, fixed endpoints. GraphQL = query-based, flexible data fetching. REST for simple CRUD, GraphQL for complex/flexible queries.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague, incorrect comparison",
                    2: "Basic understanding, incomplete trade-offs",
                    3: "Clear distinction with use-case examples",
                    4: "Detailed with performance and client implications",
                    5: "Strategic with caching, versioning, and real-world considerations"
                }
            },
            {
                "id": "backend_fundamentals_02",
                "section": "Backend Fundamentals",
                "question": "What is the difference between SQL and NoSQL databases? When would you choose each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "SQL = relational, ACID, structured schema. NoSQL = document/key-value, eventual consistency. SQL for consistent data, NoSQL for scale/flexibility.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or reversed",
                    2: "Basic understanding, incomplete trade-offs",
                    3: "Clear distinction with examples",
                    4: "Detailed with scaling and consistency discussion",
                    5: "Strategic with real-world scenarios and data modeling trade-offs"
                }
            },
        ])

    def _add_programming_questions(self):
        """Programming language fundamentals and coding challenges."""

        # Detect primary programming language
        language = self._detect_language()
        rating = self.self_ratings.get(language, 3)

        # Based on rating, determine question depth
        if rating <= 2:
            # Fundamentals only
            self.questions.extend([
                {
                    "id": f"coding_fundamentals_01",
                    "section": "Programming Language & Coding",
                    "question": f"What is a variable and how do you declare one in {language}?",
                    "difficulty_levels": ["Fresher"],
                    "category": "coding_fundamentals",
                    "expected_answer": f"A variable stores data. Syntax varies by language (e.g., int x = 5 in Java, x = 5 in Python).",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Incorrect or very vague",
                        2: "Basic understanding, syntax unclear",
                        3: "Clear explanation with correct syntax",
                        4: "Includes scoping or type information",
                        5: "Comprehensive with memory/reference considerations"
                    }
                }
            ])
        elif rating == 3:
            # Practical usage + scenario
            self.questions.extend([
                {
                    "id": "coding_practical_01",
                    "section": "Programming Language & Coding",
                    "question": f"Write a function to reverse a string in {language}. Explain your approach.",
                    "difficulty_levels": ["Basic", "Simple"],
                    "category": "coding_problem",
                    "expected_answer": "Iterate from end to start or use built-in reverse. Example: for i in range(len(s)-1, -1, -1): reversed += s[i]",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Attempted but incorrect logic",
                        2: "Partially correct, missing edge cases",
                        3: "Correct solution with explanation",
                        4: "Correct with optimal time/space complexity",
                        5: "Multiple approaches, trade-off discussion"
                    }
                }
            ])
        else:  # rating 4-5
            # Deep internals + design questions
            self.questions.extend([
                {
                    "id": "coding_advanced_01",
                    "section": "Programming Language & Coding",
                    "question": f"Design a generic retry utility/helper in {language} for flaky operations. What would you consider (error types, backoff strategy)?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "coding_design",
                    "expected_answer": "Implement retry with exponential backoff, configurable max attempts, handle specific exceptions, logging.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Basic retry logic, missing considerations",
                        2: "Retry with some strategy, incomplete",
                        3: "Good design with backoff and error handling",
                        4: "Includes configurable params, logging, thread safety",
                        5: "Production-ready with circuit breaker pattern, metrics"
                    }
                },
                {
                    "id": "coding_advanced_02",
                    "section": "Programming Language & Coding",
                    "question": f"Find duplicate values in a list without using extra space (optimize for space complexity). Discuss trade-offs.",
                    "difficulty_levels": ["Hard"],
                    "category": "coding_problem",
                    "expected_answer": "Use HashMap for O(n) time, or sorting for O(1) space. Discuss trade-offs between time and space.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Naive approach, no optimization",
                        2: "One approach, missing trade-offs",
                        3: "Multiple approaches with complexity analysis",
                        4: "Detailed with language-specific optimizations",
                        5: "Includes edge cases, performance testing considerations"
                    }
                }
            ])

    def _add_tool_questions(self):
        """Tool-specific (Playwright, Selenium, RestAssured, etc.) questions."""
        tools = self._detect_tools()

        for tool in tools[:2]:  # Focus on top 2 tools
            if tool.lower() == "playwright":
                self.questions.extend(self._playwright_questions())
            elif tool.lower() == "selenium":
                self.questions.extend(self._selenium_questions())
            elif tool.lower() == "restassured":
                self.questions.extend(self._restassured_questions())
            elif tool.lower() == "cypress":
                self.questions.extend(self._cypress_questions())

    def _playwright_questions(self) -> List[Dict]:
        """Playwright-specific questions."""
        return [
            {
                "id": "playwright_01",
                "section": "Automation Tool (Playwright)",
                "question": "What is Playwright and why would you choose it over Selenium?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Playwright is modern, supports multiple browsers (Chromium, Firefox, WebKit), better auto-wait, multi-tab/context handling.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or incorrect",
                    2: "Basic understanding, some advantages",
                    3: "Clear advantages with architecture understanding",
                    4: "Includes auto-wait, cross-browser, API testing",
                    5: "Strategic comparison with performance, community, CI/CD integration"
                }
            },
            {
                "id": "playwright_02",
                "section": "Automation Tool (Playwright)",
                "question": "Explain the difference between fill() and type() in Playwright. When would you use each?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "fill() = direct value set (faster). type() = simulates typing (triggers input events). Use type() for validation fields, fill() for forms.",
                "scoring_guide": {
                    0: "No answer",
                    1: "No clear distinction",
                    2: "One method understood, use case unclear",
                    3: "Clear distinction with correct use cases",
                    4: "Includes event triggering understanding",
                    5: "Discusses performance impact and flakiness scenarios"
                }
            },
            {
                "id": "playwright_03",
                "section": "Automation Tool (Playwright)",
                "question": "What are Browser Contexts in Playwright and why are they useful?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Isolated browser environments (separate cookies/storage). Useful for parallelization, testing multi-user scenarios, session isolation.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or incorrect",
                    2: "Basic understanding, limited use cases",
                    3: "Clear understanding with parallelization example",
                    4: "Includes authentication, isolation benefits",
                    5: "Strategic with performance and test architecture implications"
                }
            },
        ]

    def _selenium_questions(self) -> List[Dict]:
        """Selenium-specific questions."""
        return [
            {
                "id": "selenium_01",
                "section": "Automation Tool (Selenium)",
                "question": "What is Selenium WebDriver and how does it interact with browsers?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Selenium WebDriver is a tool for automating browsers. It uses the WebDriver protocol to communicate with browser drivers.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague",
                    2: "Basic understanding",
                    3: "Clear with protocol knowledge",
                    4: "Includes driver architecture and browser compatibility",
                    5: "Detailed with performance considerations and limitations vs Playwright"
                }
            },
            {
                "id": "selenium_02",
                "section": "Automation Tool (Selenium)",
                "question": "What are explicit and implicit waits in Selenium? When would you use each?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Implicit = applies globally to all elements. Explicit = wait for specific condition. Use explicit for reliability, avoid mixing.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Confused",
                    2: "Basic understanding, incomplete guidance",
                    3: "Clear with examples",
                    4: "Includes WebDriverWait and conditions",
                    5: "Strategic with anti-patterns and best practices"
                }
            },
        ]

    def _restassured_questions(self) -> List[Dict]:
        """RestAssured-specific questions (API testing)."""
        return [
            {
                "id": "restassured_01",
                "section": "Automation Tool (RestAssured)",
                "question": "What is RestAssured and what are its main advantages for API testing?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "RestAssured is a Java library for REST API testing. Fluent syntax, built-in assertions, response validation, JSON/XML parsing.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague",
                    2: "Basic understanding, few advantages",
                    3: "Clear with fluent syntax example",
                    4: "Includes assertions, serialization, authentication",
                    5: "Strategic with test data builders, performance, mocking"
                }
            },
        ]

    def _cypress_questions(self) -> List[Dict]:
        """Cypress-specific questions."""
        return [
            {
                "id": "cypress_01",
                "section": "Automation Tool (Cypress)",
                "question": "How does Cypress differ from Selenium? What are its strengths and limitations?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Cypress runs in-browser, better debugging, time-travel debugging. Limited to same-origin, single browser tab.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague",
                    2: "Some differences noted",
                    3: "Clear strengths and limitations",
                    4: "Includes architectural differences",
                    5: "Strategic with when to use Cypress vs other tools"
                }
            },
        ]

    def _add_framework_design_questions(self):
        """Framework design & architecture (QA focus)."""
        if self.self_ratings.get("Test Automation Framework Design", 0) >= 3:
            self.questions.extend([
                {
                    "id": "framework_01",
                    "section": "Framework Design & Architecture",
                    "question": "Describe different automation framework types (POM, Data-driven, Hybrid, BDD). What are the pros/cons of each?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "framework",
                    "expected_answer": "POM = organized, maintainable. Data-driven = parametrized tests. Hybrid = POM + data. BDD = business language. Trade-offs in complexity vs flexibility.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Vague or confused",
                        2: "One framework understood",
                        3: "Clear descriptions of 2-3 frameworks",
                        4: "Detailed pros/cons and when to use",
                        5: "Strategic with real-world examples and team dynamics"
                    }
                },
                {
                    "id": "framework_02",
                    "section": "Framework Design & Architecture",
                    "question": "How do you ensure your automation framework scales for a large test suite (1000+ tests)?",
                    "difficulty_levels": ["Hard"],
                    "category": "framework",
                    "expected_answer": "Parallel execution, selective test execution, reporting (Extent/Allure), CI/CD integration, page object organization, fixture management.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Ad-hoc approach",
                        2: "Mentions parallelization only",
                        3: "Multiple strategies (parallel, selective, reporting)",
                        4: "Includes CI/CD and fixture management",
                        5: "Strategic with metrics, flakiness reduction, team scalability"
                    }
                },
            ])

    def _add_cicd_questions(self):
        """CI/CD and DevOps integration."""
        self.questions.extend([
            {
                "id": "cicd_01",
                "section": "CI/CD & DevOps Integration",
                "question": "How do you integrate automated tests into a CI/CD pipeline (Jenkins, GitLab CI, GitHub Actions)?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Trigger on push/PR, run tests in parallel, collect artifacts (reports, screenshots), gate deployment on pass/fail, notify stakeholders.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague",
                    2: "Basic understanding of pipeline stages",
                    3: "Clear with trigger and reporting",
                    4: "Includes parallelization and quality gates",
                    5: "Strategic with flakiness handling, selective runs, metrics"
                }
            },
            {
                "id": "cicd_02",
                "section": "CI/CD & DevOps Integration",
                "question": "What is Docker and why is it useful for test automation?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Docker = containerization. Useful for consistent test environments, isolated dependencies, parallel test execution, portability.",
                "scoring_guide": {
                    0: "No answer",
                    1: "Vague or incorrect",
                    2: "Basic understanding, limited benefits",
                    3: "Clear benefits for test environments",
                    4: "Includes image composition and orchestration",
                    5: "Strategic with Kubernetes, resource optimization"
                }
            },
        ])

    def _add_leadership_questions(self):
        """Leadership & program management (for Senior/Lead roles)."""
        if any(keyword in self.role.lower()
               for keyword in ["lead", "senior", "manager", "architect"]):
            self.questions.extend([
                {
                    "id": "leadership_01",
                    "section": "Leadership & Program Management",
                    "question": "Tell me about a time you disagreed with a developer/PM on defect severity. How did you handle it?",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Use STAR method: Situation, Task, Action, Result. Show data-driven reasoning, stakeholder management, diplomatic resolution.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Vague or defensive",
                        2: "Some structure, conflict handled poorly",
                        3: "STAR method used, collaborative resolution",
                        4: "Clear with data/metrics supporting decision",
                        5: "Compelling with team dynamics, long-term relationship value"
                    }
                },
                {
                    "id": "leadership_02",
                    "section": "Leadership & Program Management",
                    "question": "How do you mentor junior engineers? Describe your approach to upskilling your team.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Pair programming, code reviews, stretch assignments, clear feedback, learning resources, regular 1-on-1s.",
                    "scoring_guide": {
                        0: "No answer",
                        1: "Ad-hoc or unclear",
                        2: "One or two approaches mentioned",
                        3: "Multiple structured approaches",
                        4: "Includes mentoring philosophy and examples",
                        5: "Strategic with team growth metrics and retention focus"
                    }
                },
            ])

    def _add_closing_questions(self):
        """Closing scenario/judgment question."""
        self.questions.append({
            "id": "closing_01",
            "section": "Closing",
            "question": "Imagine you have 2 days to test a new payment feature before production release. The feature is complex, but you can't automate everything in time. Walk me through your testing strategy.",
            "difficulty_levels": ["Simple", "Hard"],
            "category": "scenario",
            "expected_answer": "Risk-based approach: critical paths first, manual exploratory testing, automated smoke tests, performance checks, production monitoring plan.",
            "scoring_guide": {
                0: "No answer",
                1: "Ad-hoc or panic-driven",
                2: "Some strategy but incomplete",
                3: "Risk-based prioritization, covers main areas",
                4: "Detailed with resource allocation and communication",
                5: "Strategic with business context, fallback plans, metrics"
            }
        })

    def get_questions_for_interview(self) -> List[Dict]:
        """
        Return ordered questions for the interview.
        Scaled to difficulty and years of experience.
        """
        total_questions = self._calculate_question_count()

        # Filter questions by difficulty level
        available = [q for q in self.questions
                    if self.difficulty in q.get("difficulty_levels", [])]

        # Organize by section for sequential delivery
        sections = {}
        for q in available:
            section = q["section"]
            if section not in sections:
                sections[section] = []
            sections[section].append(q)

        # Build ordered question list
        ordered_questions = []
        section_order = [
            "Introduction", "QA Fundamentals & SDLC/STLC", "Testing Types",
            "Test Planning & Strategy", "Methodologies & Process",
            "Backend Fundamentals", "Programming Language & Coding",
            "Automation Tool (Playwright)", "Automation Tool (Selenium)",
            "Automation Tool (RestAssured)", "Automation Tool (Cypress)",
            "Framework Design & Architecture", "CI/CD & DevOps Integration",
            "Leadership & Program Management", "Closing"
        ]

        for section in section_order:
            if section in sections:
                ordered_questions.extend(sections[section])

        # Return scaled question count
        return ordered_questions[:total_questions]

    def _calculate_question_count(self) -> int:
        """Calculate expected question count based on difficulty and experience."""
        if self.difficulty in ["Fresher", "Basic"]:
            return 15 + int(self.years_of_experience)  # 15-20 range
        elif self.difficulty == "Simple":
            return 20 + int(self.years_of_experience * 0.5)  # 20-25 range
        else:  # Hard
            return 25 + int(self.years_of_experience * 0.5)  # 25-30 range

    def _detect_language(self) -> str:
        """Detect primary programming language from skills."""
        languages = [s for s in self.primary_skills
                    if s.lower() in ["java", "python", "javascript", "typescript", "c#", "go", "rust"]]
        return languages[0] if languages else "Python"

    def _detect_tools(self) -> List[str]:
        """Detect automation tools from skills."""
        tools = [s for s in self.primary_skills
                if s.lower() in ["playwright", "selenium", "cypress", "restassured", "appium"]]
        return tools if tools else ["Selenium"]
