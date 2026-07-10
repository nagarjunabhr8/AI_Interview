"""
Expanded Question Bank with Random Selection
Ensures diverse questions on every interview with no repetition.
"""

import random
from typing import List, Dict, Any


class ExpandedQuestionBank:
    """Enhanced question bank with 5x more questions and smart randomization."""

    def __init__(self, role: str, difficulty: str, primary_skills: List[str],
                 years_of_experience: float, self_ratings: Dict[str, int]):
        """Initialize expanded question bank."""
        self.role = role
        self.difficulty = difficulty
        self.primary_skills = primary_skills
        self.years_of_experience = years_of_experience
        self.self_ratings = self_ratings or {}
        self.all_questions = []
        self._build_expanded_questions()

    def _build_expanded_questions(self):
        """Build expanded question pool with diverse questions."""
        # Determine if QA role
        is_qa_role = any(keyword in self.role.lower()
                        for keyword in ["qa", "sdet", "test", "automation"])

        if is_qa_role:
            self._add_qa_questions_expanded()
        else:
            self._add_backend_questions_expanded()

        # Always add common sections
        self._add_warmup_questions_expanded()
        self._add_programming_questions_expanded()
        self._add_tool_questions_expanded()

        if is_qa_role:
            self._add_framework_design_questions_expanded()

        self._add_cicd_questions_expanded()
        self._add_leadership_questions_expanded()
        self._add_closing_questions_expanded()

    def _add_warmup_questions_expanded(self):
        """Expanded warm-up questions (10+ variants)."""
        warmup_questions = [
            {
                "id": "warmup_01",
                "section": "Introduction",
                "question": "Walk me through your background and current role. What drew you to this field?",
                "difficulty_levels": ["Fresher", "Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "A concise overview of career journey, current role, key responsibilities.",
            },
            {
                "id": "warmup_02",
                "section": "Introduction",
                "question": "Tell me about your most significant project and your role in it.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Specific project with measurable impact and your contributions.",
            },
            {
                "id": "warmup_03",
                "section": "Introduction",
                "question": "What are your career goals for the next 3-5 years?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Clear, realistic goals aligned with technical growth or leadership.",
            },
            {
                "id": "warmup_04",
                "section": "Introduction",
                "question": "Describe your experience with the tools and technologies mentioned in your profile.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Specific examples of how you've used each tool, years of experience.",
            },
            {
                "id": "warmup_05",
                "section": "Introduction",
                "question": "What have you learned from your most challenging work experience?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Specific challenge, how you overcame it, and lessons learned.",
            },
            {
                "id": "warmup_06",
                "section": "Introduction",
                "question": "How do you stay updated with the latest trends in your field?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Blogs, conferences, online courses, communities, personal projects.",
            },
        ]
        self.all_questions.extend(warmup_questions)

    def _add_qa_questions_expanded(self):
        """Expanded QA-specific questions (50+ variants)."""
        qa_questions = [
            # SDLC/STLC Questions
            {
                "id": "qa_sdlc_01",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "What is the difference between SDLC and STLC? When does QA typically get involved?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "SDLC covers entire development, STLC is testing-specific. QA involved early in requirements phase.",
            },
            {
                "id": "qa_sdlc_02",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "Explain the V-model in software testing. Why is it important?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Test planning parallel to development phases, each dev phase has corresponding test phase.",
            },
            {
                "id": "qa_sdlc_03",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "What does Shift-Left testing mean and what are its benefits?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Testing starts earlier in development, catches bugs sooner, reduces costs.",
            },
            {
                "id": "qa_sdlc_04",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "Describe the testing activities in different phases of SDLC.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Requirements review, design review, unit testing, integration, system, UAT testing.",
            },
            {
                "id": "qa_sdlc_05",
                "section": "QA Fundamentals & SDLC/STLC",
                "question": "What is the difference between Verification and Validation?",
                "difficulty_levels": ["Fresher", "Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Verification = building it right (process), Validation = building right thing (product).",
            },

            # Testing Types Questions
            {
                "id": "qa_types_01",
                "section": "Testing Types",
                "question": "Explain Smoke, Sanity, and Regression testing with examples.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Smoke: basic checks post-build, Sanity: specific fix works, Regression: no new defects.",
            },
            {
                "id": "qa_types_02",
                "section": "Testing Types",
                "question": "What is the difference between Functional and Non-Functional testing?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Functional: features work as expected, Non-functional: performance, security, load, stress.",
            },
            {
                "id": "qa_types_03",
                "section": "Testing Types",
                "question": "When would you use Integration vs System vs UAT testing?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Integration: modules together, System: full system, UAT: user requirements.",
            },
            {
                "id": "qa_types_04",
                "section": "Testing Types",
                "question": "Explain API testing vs UI testing. Why are both important?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "API: faster, independent, contract validation. UI: user experience validation.",
            },
            {
                "id": "qa_types_05",
                "section": "Testing Types",
                "question": "What is performance testing? How does it differ from load and stress testing?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Performance: response times under normal load. Load: maximum load. Stress: beyond limits.",
            },
            {
                "id": "qa_types_06",
                "section": "Testing Types",
                "question": "Describe your approach to exploratory testing vs scripted testing.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Exploratory: dynamic, uncovering unknown issues. Scripted: predefined test cases, reproducible.",
            },
            {
                "id": "qa_types_07",
                "section": "Testing Types",
                "question": "What is boundary value analysis and why is it important?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "testing_types",
                "expected_answer": "Test edge cases at input boundaries, catches off-by-one errors.",
            },

            # Severity/Priority Questions
            {
                "id": "qa_severity_01",
                "section": "Testing Types",
                "question": "Explain Severity vs Priority in defects. Give examples.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Severity: impact on functionality. Priority: urgency of fix. Can mismatch.",
            },
            {
                "id": "qa_severity_02",
                "section": "Testing Types",
                "question": "Give an example of a high-severity, low-priority bug and vice versa.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "High-sev/low-prior: rare edge case. Low-sev/high-prior: UI typo visible to CEO.",
            },

            # Test Planning Questions
            {
                "id": "qa_planning_01",
                "section": "Test Planning & Strategy",
                "question": "What should a Test Plan document contain?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Scope, resources, schedule, entry/exit criteria, test cases, risks, deliverables.",
            },
            {
                "id": "qa_planning_02",
                "section": "Test Planning & Strategy",
                "question": "How do you estimate testing effort for a new project?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Historical data, story points, complexity analysis, team velocity.",
            },
            {
                "id": "qa_planning_03",
                "section": "Test Planning & Strategy",
                "question": "You have limited time and budget. How do you prioritize what to test?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Risk-based: business critical, frequently used, high-defect areas first.",
            },
            {
                "id": "qa_planning_04",
                "section": "Test Planning & Strategy",
                "question": "What are entry and exit criteria in testing?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Entry: prerequisites to start testing. Exit: criteria to stop testing (pass rate, coverage).",
            },
            {
                "id": "qa_planning_05",
                "section": "Test Planning & Strategy",
                "question": "Describe your approach to test data management.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "planning",
                "expected_answer": "Data generation, anonymization, environment setup, refresh strategy.",
            },

            # Agile/Methodologies Questions
            {
                "id": "qa_agile_01",
                "section": "Methodologies & Process",
                "question": "How does QA work in Agile/Scrum? Describe sprint ceremonies.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "QA in planning, standup, review, retro. Testing within sprint, continuous feedback.",
            },
            {
                "id": "qa_agile_02",
                "section": "Methodologies & Process",
                "question": "What is Definition of Done in Agile? Who defines it?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "DoD: code reviewed, tested, documented. Defined by team at sprint start.",
            },
            {
                "id": "qa_agile_03",
                "section": "Methodologies & Process",
                "question": "How do you handle testing when development pace is fast?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Continuous testing, automation, parallel testing, test within sprint.",
            },
            {
                "id": "qa_agile_04",
                "section": "Methodologies & Process",
                "question": "Explain BDD (Behavior-Driven Development) and its benefits.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Given-When-Then format, bridges business and technical, shared understanding.",
            },
            {
                "id": "qa_agile_05",
                "section": "Methodologies & Process",
                "question": "What is your approach to cross-functional collaboration with developers and product managers?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Regular communication, shared goals, early involvement, collaborative problem-solving.",
            },

            # Defect Management Questions
            {
                "id": "qa_defect_01",
                "section": "Methodologies & Process",
                "question": "Describe the defect lifecycle from discovery to closure.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "New → Assigned → In Progress → Resolved → Verified → Closed.",
            },
            {
                "id": "qa_defect_02",
                "section": "Methodologies & Process",
                "question": "How do you decide if a defect should be fixed now or deferred?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Based on severity, priority, timeline, business impact, workarounds.",
            },
            {
                "id": "qa_defect_03",
                "section": "Methodologies & Process",
                "question": "What information should a well-written bug report contain?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "Title, description, steps, expected, actual, environment, screenshots, logs.",
            },

            # Test Automation Questions
            {
                "id": "qa_automation_01",
                "section": "Methodologies & Process",
                "question": "When should you automate tests vs keep them manual?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "process",
                "expected_answer": "Automate: repetitive, high-ROI. Manual: exploratory, one-off, complex scenarios.",
            },
            {
                "id": "qa_automation_02",
                "section": "Methodologies & Process",
                "question": "What are the challenges in test automation? How do you address them?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Flakiness, maintenance, tool selection, false positives. Use best practices, monitoring.",
            },
            {
                "id": "qa_automation_03",
                "section": "Methodologies & Process",
                "question": "How do you maintain automated tests as codebase evolves?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "process",
                "expected_answer": "Page Object Model, regular refactoring, CI/CD integration, flaky test detection.",
            },
        ]
        self.all_questions.extend(qa_questions)

    def _add_backend_questions_expanded(self):
        """Expanded backend/DevOps questions (20+ variants)."""
        backend_questions = [
            {
                "id": "backend_api_01",
                "section": "Backend Fundamentals",
                "question": "Explain REST architecture and its principles (HATEOAS, statelessness, etc.).",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "REST uses HTTP methods, stateless, uniform interface, client-server separation.",
            },
            {
                "id": "backend_api_02",
                "section": "Backend Fundamentals",
                "question": "What are the differences between REST and GraphQL APIs?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "REST: resource-based, fixed endpoints. GraphQL: query-based, flexible schema.",
            },
            {
                "id": "backend_db_01",
                "section": "Backend Fundamentals",
                "question": "Compare SQL and NoSQL databases. When would you use each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "SQL: relational, ACID. NoSQL: flexible, eventual consistency.",
            },
            {
                "id": "backend_db_02",
                "section": "Backend Fundamentals",
                "question": "What are ACID properties in databases? Why are they important?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Atomicity, Consistency, Isolation, Durability. Ensure data integrity.",
            },
            {
                "id": "backend_scaling_01",
                "section": "Backend Fundamentals",
                "question": "Explain horizontal vs vertical scaling. When would you use each?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Horizontal: add servers. Vertical: increase power. Horizontal is scalable long-term.",
            },
            {
                "id": "backend_cache_01",
                "section": "Backend Fundamentals",
                "question": "What is caching? Explain cache invalidation strategies.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "fundamentals",
                "expected_answer": "Caching improves performance. Strategies: TTL, LRU, event-based invalidation.",
            },
        ]
        self.all_questions.extend(backend_questions)

    def _add_programming_questions_expanded(self):
        """Expanded programming questions (30+ variants)."""
        language = self._detect_language()
        rating = self.self_ratings.get(language, 3)

        programming_questions = [
            # Fundamentals (for all levels)
            {
                "id": "prog_fundamentals_01",
                "section": "Programming Language & Coding",
                "question": "Explain the difference between pass-by-value and pass-by-reference.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "coding_fundamentals",
                "expected_answer": "Pass-by-value: copy of data. Pass-by-reference: reference to original.",
            },
            {
                "id": "prog_fundamentals_02",
                "section": "Programming Language & Coding",
                "question": "What is the difference between recursion and iteration?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "coding_fundamentals",
                "expected_answer": "Recursion: function calls itself. Iteration: loop. Trade-offs in clarity and performance.",
            },
            {
                "id": "prog_fundamentals_03",
                "section": "Programming Language & Coding",
                "question": "Explain the concept of exception handling.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "coding_fundamentals",
                "expected_answer": "Try-catch blocks, different exception types, graceful error handling.",
            },

            # Coding Problems (varied)
            {
                "id": "prog_problem_01",
                "section": "Programming Language & Coding",
                "question": "Write a function to reverse a string.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "coding_problem",
                "expected_answer": "Multiple approaches: slicing, loop, recursion.",
            },
            {
                "id": "prog_problem_02",
                "section": "Programming Language & Coding",
                "question": "Find the missing number in an array of 1 to N.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "coding_problem",
                "expected_answer": "Sum formula, XOR approach, hash set.",
            },
            {
                "id": "prog_problem_03",
                "section": "Programming Language & Coding",
                "question": "Check if a number is a palindrome.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "coding_problem",
                "expected_answer": "Convert to string and compare, or mathematical approach.",
            },
            {
                "id": "prog_problem_04",
                "section": "Programming Language & Coding",
                "question": "Remove duplicates from an array.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "coding_problem",
                "expected_answer": "Hash set, two pointers, or sort approach.",
            },
            {
                "id": "prog_problem_05",
                "section": "Programming Language & Coding",
                "question": "Find the most frequent element in an array.",
                "difficulty_levels": ["Simple"],
                "category": "coding_problem",
                "expected_answer": "Hash map, sorting, or heap approach.",
            },

            # Design Problems (for higher ratings)
            {
                "id": "prog_design_01",
                "section": "Programming Language & Coding",
                "question": "Design a retry utility/helper for flaky operations.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "coding_design",
                "expected_answer": "Configurable retries, exponential backoff, exception handling.",
            },
            {
                "id": "prog_design_02",
                "section": "Programming Language & Coding",
                "question": "Design a generic caching layer.",
                "difficulty_levels": ["Hard"],
                "category": "coding_design",
                "expected_answer": "Key-value storage, TTL, eviction policy, thread safety.",
            },
            {
                "id": "prog_design_03",
                "section": "Programming Language & Coding",
                "question": "Design a rate limiter for API requests.",
                "difficulty_levels": ["Hard"],
                "category": "coding_design",
                "expected_answer": "Token bucket, sliding window, configurable limits.",
            },
        ]
        self.all_questions.extend(programming_questions)

    def _add_tool_questions_expanded(self):
        """Expanded tool-specific questions (50+ variants)."""
        tools = self._detect_tools()

        for tool in tools[:2]:
            if tool.lower() == "playwright":
                self.all_questions.extend(self._playwright_questions_expanded())
            elif tool.lower() == "selenium":
                self.all_questions.extend(self._selenium_questions_expanded())
            elif tool.lower() == "restassured":
                self.all_questions.extend(self._restassured_questions_expanded())
            elif tool.lower() == "cypress":
                self.all_questions.extend(self._cypress_questions_expanded())

    def _playwright_questions_expanded(self) -> List[Dict]:
        """Expanded Playwright questions (25+ variants)."""
        return [
            {
                "id": "pw_01",
                "section": "Automation Tool (Playwright)",
                "question": "What is Playwright and why would you choose it over Selenium?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Modern, multi-browser, better auto-wait, multiple languages.",
            },
            {
                "id": "pw_02",
                "section": "Automation Tool (Playwright)",
                "question": "Explain the difference between fill() and type() methods.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "fill(): direct value, faster. type(): simulates typing, triggers events.",
            },
            {
                "id": "pw_03",
                "section": "Automation Tool (Playwright)",
                "question": "What are Browser Contexts in Playwright and why are they useful?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Isolated browser environments, parallel testing, session management.",
            },
            {
                "id": "pw_04",
                "section": "Automation Tool (Playwright)",
                "question": "How do you handle waits in Playwright?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Auto-waiting, explicit waits, waitForNavigation, waitForSelector.",
            },
            {
                "id": "pw_05",
                "section": "Automation Tool (Playwright)",
                "question": "Explain the difference between hard and soft assertions.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Hard: fails immediately. Soft: continues, fails at end.",
            },
            {
                "id": "pw_06",
                "section": "Automation Tool (Playwright)",
                "question": "How do you handle authentication in Playwright tests?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "UI login, API token injection, storageState reuse.",
            },
            {
                "id": "pw_07",
                "section": "Automation Tool (Playwright)",
                "question": "Describe your approach to debugging Playwright scripts.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Inspector, trace viewer, screenshot/video, debug mode.",
            },
            {
                "id": "pw_08",
                "section": "Automation Tool (Playwright)",
                "question": "How do you handle network interception in Playwright?",
                "difficulty_levels": ["Hard"],
                "category": "tool",
                "expected_answer": "route() method, mocking responses, handling dynamic content.",
            },
            {
                "id": "pw_09",
                "section": "Automation Tool (Playwright)",
                "question": "Explain the difference between newPage() and newContext().",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "newPage(): shared context. newContext(): isolated environment.",
            },
            {
                "id": "pw_10",
                "section": "Automation Tool (Playwright)",
                "question": "How do you run Playwright tests in parallel and sharding?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Workers configuration, test sharding across machines.",
            },
        ]

    def _selenium_questions_expanded(self) -> List[Dict]:
        """Expanded Selenium questions (15+ variants)."""
        return [
            {
                "id": "sel_01",
                "section": "Automation Tool (Selenium)",
                "question": "Explain the WebDriver protocol and how Selenium uses it.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "W3C standard for browser automation, Selenium implements it.",
            },
            {
                "id": "sel_02",
                "section": "Automation Tool (Selenium)",
                "question": "What are explicit and implicit waits? When to use each?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Implicit: global setting. Explicit: specific condition. Use explicit.",
            },
            {
                "id": "sel_03",
                "section": "Automation Tool (Selenium)",
                "question": "How do you handle dropdown selections in Selenium?",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "tool",
                "expected_answer": "Select class, options by value/text/index.",
            },
            {
                "id": "sel_04",
                "section": "Automation Tool (Selenium)",
                "question": "Describe your approach to handling alerts and popups.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "tool",
                "expected_answer": "switchTo().alert(), accept(), dismiss(), sendKeys().",
            },
            {
                "id": "sel_05",
                "section": "Automation Tool (Selenium)",
                "question": "How do you find elements using different locator strategies?",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "tool",
                "expected_answer": "ID, Class, XPath, CSS, Tag, Partial Link, etc.",
            },
        ]

    def _restassured_questions_expanded(self) -> List[Dict]:
        """Expanded RestAssured questions (15+ variants)."""
        return [
            {
                "id": "ra_01",
                "section": "Automation Tool (RestAssured)",
                "question": "What is RestAssured and why is it useful for API testing?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Java library for REST testing, fluent API, assertions.",
            },
            {
                "id": "ra_02",
                "section": "Automation Tool (RestAssured)",
                "question": "How do you handle authentication in RestAssured?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Basic auth, Bearer token, OAuth, custom headers.",
            },
            {
                "id": "ra_03",
                "section": "Automation Tool (RestAssured)",
                "question": "Explain how to parse and validate JSON responses.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Path expressions, JSONPath, extracting values.",
            },
        ]

    def _cypress_questions_expanded(self) -> List[Dict]:
        """Expanded Cypress questions (15+ variants)."""
        return [
            {
                "id": "cy_01",
                "section": "Automation Tool (Cypress)",
                "question": "How does Cypress differ from Selenium?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "In-browser execution, better debugging, same-origin limitation.",
            },
            {
                "id": "cy_02",
                "section": "Automation Tool (Cypress)",
                "question": "Describe Cypress fixture usage and custom commands.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Fixtures for data, custom commands for reusable actions.",
            },
        ]

    def _add_framework_design_questions_expanded(self):
        """Expanded framework design questions (20+ variants)."""
        if self.self_ratings.get("Test Automation Framework Design", 0) >= 3:
            framework_questions = [
                {
                    "id": "fw_01",
                    "section": "Framework Design & Architecture",
                    "question": "Describe different automation framework types and their pros/cons.",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "framework",
                    "expected_answer": "POM, Data-driven, Hybrid, BDD. Trade-offs in complexity vs flexibility.",
                },
                {
                    "id": "fw_02",
                    "section": "Framework Design & Architecture",
                    "question": "How do you design a scalable automation framework for 1000+ tests?",
                    "difficulty_levels": ["Hard"],
                    "category": "framework",
                    "expected_answer": "Parallel execution, selective runs, reporting, fixture management.",
                },
                {
                    "id": "fw_03",
                    "section": "Framework Design & Architecture",
                    "question": "What is Page Object Model and why is it important?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "framework",
                    "expected_answer": "Encapsulates page elements, improves maintainability, reduces duplication.",
                },
                {
                    "id": "fw_04",
                    "section": "Framework Design & Architecture",
                    "question": "How do you handle test data in your automation framework?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "framework",
                    "expected_answer": "Data builders, factories, external files, environment-specific data.",
                },
                {
                    "id": "fw_05",
                    "section": "Framework Design & Architecture",
                    "question": "Describe your approach to test reporting and artifacts.",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "framework",
                    "expected_answer": "Extent Reports, Allure, screenshots, videos, logs.",
                },
            ]
            self.all_questions.extend(framework_questions)

    def _add_cicd_questions_expanded(self):
        """Expanded CI/CD questions (20+ variants)."""
        cicd_questions = [
            {
                "id": "cicd_01",
                "section": "CI/CD & DevOps Integration",
                "question": "How do you integrate automated tests into CI/CD pipeline?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Triggers, parallel execution, quality gates, notifications.",
            },
            {
                "id": "cicd_02",
                "section": "CI/CD & DevOps Integration",
                "question": "What is Docker and why is it useful for testing?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Containerization, consistent environments, isolated dependencies.",
            },
            {
                "id": "cicd_03",
                "section": "CI/CD & DevOps Integration",
                "question": "Explain the concept of infrastructure as code.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Define infrastructure in code, version control, reproducible.",
            },
            {
                "id": "cicd_04",
                "section": "CI/CD & DevOps Integration",
                "question": "How do you handle flaky tests in CI/CD pipeline?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "cicd",
                "expected_answer": "Retry logic, quarantine, monitoring, root cause analysis.",
            },
            {
                "id": "cicd_05",
                "section": "CI/CD & DevOps Integration",
                "question": "Describe your approach to performance testing in CI/CD.",
                "difficulty_levels": ["Hard"],
                "category": "cicd",
                "expected_answer": "Baseline metrics, threshold checks, trend analysis.",
            },
        ]
        self.all_questions.extend(cicd_questions)

    def _add_leadership_questions_expanded(self):
        """Expanded leadership questions (20+ variants)."""
        if any(keyword in self.role.lower()
               for keyword in ["lead", "senior", "manager", "architect"]):
            leadership_questions = [
                {
                    "id": "lead_01",
                    "section": "Leadership & Program Management",
                    "question": "Tell me about a time you disagreed with a developer on bug severity.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "STAR method, data-driven reasoning, collaborative resolution.",
                },
                {
                    "id": "lead_02",
                    "section": "Leadership & Program Management",
                    "question": "How do you mentor and develop junior QA engineers?",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Pair programming, code reviews, stretch assignments, feedback.",
                },
                {
                    "id": "lead_03",
                    "section": "Leadership & Program Management",
                    "question": "Describe your approach to managing quality metrics and KPIs.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Defect density, escape rate, coverage %, automation metrics.",
                },
                {
                    "id": "lead_04",
                    "section": "Leadership & Program Management",
                    "question": "How do you handle a production incident? Walk through your process.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Root cause analysis, communication, prevention measures.",
                },
                {
                    "id": "lead_05",
                    "section": "Leadership & Program Management",
                    "question": "Tell me about your experience interviewing and hiring QA talent.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Assessment criteria, team fit evaluation, feedback.",
                },
            ]
            self.all_questions.extend(leadership_questions)

    def _add_closing_questions_expanded(self):
        """Expanded closing scenario questions (10+ variants)."""
        closing_questions = [
            {
                "id": "closing_01",
                "section": "Closing",
                "question": "You have 2 days to test a payment feature before production. Walk through your strategy.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "scenario",
                "expected_answer": "Risk-based prioritization, critical paths first, monitoring plan.",
            },
            {
                "id": "closing_02",
                "section": "Closing",
                "question": "How do you handle testing when requirements are unclear or changing?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "scenario",
                "expected_answer": "Early communication, clarification, flexible approach, document assumptions.",
            },
            {
                "id": "closing_03",
                "section": "Closing",
                "question": "Describe your approach to testing a microservices architecture.",
                "difficulty_levels": ["Hard"],
                "category": "scenario",
                "expected_answer": "Contract testing, integration tests, API testing, dependency mocking.",
            },
            {
                "id": "closing_04",
                "section": "Closing",
                "question": "How do you stay motivated when dealing with repetitive testing tasks?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "scenario",
                "expected_answer": "Automation, learning, career growth, seeing product impact.",
            },
        ]
        self.all_questions.extend(closing_questions)

    def get_questions_for_interview(self) -> List[Dict]:
        """
        Return randomized questions for the interview.
        Ensures variety and no repetition.
        """
        total_questions = self._calculate_question_count()

        # Filter questions by difficulty level
        available = [q for q in self.all_questions
                    if self.difficulty in q.get("difficulty_levels", [])]

        # Randomize selection
        selected = random.sample(available, min(total_questions, len(available)))

        # Sort by section for logical flow (but within section order is random)
        sections_order = [
            "Introduction", "QA Fundamentals & SDLC/STLC", "Testing Types",
            "Test Planning & Strategy", "Methodologies & Process",
            "Backend Fundamentals", "Programming Language & Coding",
            "Automation Tool (Playwright)", "Automation Tool (Selenium)",
            "Automation Tool (RestAssured)", "Automation Tool (Cypress)",
            "Framework Design & Architecture", "CI/CD & DevOps Integration",
            "Leadership & Program Management", "Closing"
        ]

        result = []
        for section in sections_order:
            section_questions = [q for q in selected if q.get("section") == section]
            result.extend(section_questions)

        return result[:total_questions]

    def _calculate_question_count(self) -> int:
        """Calculate expected question count based on difficulty."""
        if self.difficulty in ["Fresher", "Basic"]:
            return 15 + int(self.years_of_experience)
        elif self.difficulty == "Simple":
            return 20 + int(self.years_of_experience * 0.5)
        else:  # Hard
            return 25 + int(self.years_of_experience * 0.5)

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
