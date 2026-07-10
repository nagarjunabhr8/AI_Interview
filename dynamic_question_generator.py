"""
Dynamic Question Generator
Generates real-time interview questions based on skills, role, and experience.
Fetches contextual questions for each session with zero repetition.
"""

import random
from typing import List, Dict, Any, Set


class DynamicQuestionGenerator:
    """
    Generates interview questions dynamically based on:
    - Primary skills selected
    - Target role/designation
    - Years of experience
    - Difficulty level

    Each session generates unique questions with real interview content.
    """

    def __init__(self, role: str, difficulty: str, primary_skills: List[str],
                 years_of_experience: float, self_ratings: Dict[str, int]):
        """Initialize dynamic question generator."""
        self.role = role
        self.difficulty = difficulty
        self.primary_skills = primary_skills
        self.years_of_experience = years_of_experience
        self.self_ratings = self_ratings or {}
        self.generated_questions = []
        self._generate_dynamic_questions()

    def _generate_dynamic_questions(self):
        """Generate questions dynamically based on selected skills and role."""
        # Add role-specific foundational questions
        self._add_role_foundational_questions()

        # Add skill-specific questions for each primary skill
        for skill in self.primary_skills:
            self._add_skill_specific_questions(skill)

        # Add experience-level appropriate questions
        self.generated_questions.extend(self._experience_level_questions())

        # Add behavioral/situational questions
        self._add_behavioral_questions()

        # Add closing/scenario questions
        self._add_scenario_questions()

    def _add_role_foundational_questions(self):
        """Add questions specific to the selected role."""

        role_lower = self.role.lower()

        # QA/Testing Roles
        if any(keyword in role_lower for keyword in ["qa", "test", "automation", "sdet"]):
            self.generated_questions.extend([
                {
                    "id": f"role_qa_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Describe your understanding of the SDLC and where QA fits in the process.",
                    "difficulty_levels": ["Fresher", "Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Understanding of development lifecycle phases and QA's role in each.",
                },
                {
                    "id": f"role_qa_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "What testing methodologies are you familiar with? How do you choose between them?",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Knowledge of different testing approaches and when to apply them.",
                },
                {
                    "id": f"role_qa_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "How do you approach creating a test strategy for a new feature?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Strategic thinking about test planning and risk-based testing.",
                },
                {
                    "id": f"role_qa_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "What's your experience with test automation? What challenges have you faced?",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Real-world automation experience and problem-solving.",
                },
                {
                    "id": f"role_qa_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "How do you prioritize testing when time is limited?",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Risk-based prioritization and business-focused approach.",
                },
            ])

        # Backend Developer Roles
        elif any(keyword in role_lower for keyword in ["backend", "developer", "engineer"]):
            self.generated_questions.extend([
                {
                    "id": f"role_backend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Explain your approach to designing scalable backend systems.",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Knowledge of scalability patterns, load balancing, and system design.",
                },
                {
                    "id": f"role_backend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "How do you handle database optimization and query performance?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Indexing strategies, query optimization, and performance monitoring.",
                },
                {
                    "id": f"role_backend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Describe your experience with REST APIs. How do you design them?",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "RESTful principles, API design best practices, versioning strategies.",
                },
                {
                    "id": f"role_backend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "What's your approach to handling concurrent requests and threading?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Concurrency handling, thread safety, and deadlock prevention.",
                },
            ])

        # DevOps Roles
        elif any(keyword in role_lower for keyword in ["devops", "sre", "infrastructure"]):
            self.generated_questions.extend([
                {
                    "id": f"role_devops_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Explain your experience with containerization and orchestration.",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Docker, Kubernetes, container orchestration experience.",
                },
                {
                    "id": f"role_devops_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "How do you design and maintain CI/CD pipelines?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Pipeline design, automation, deployment strategies.",
                },
                {
                    "id": f"role_devops_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Describe your infrastructure as code experience.",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Terraform, CloudFormation, infrastructure automation.",
                },
            ])

        # Frontend Roles
        elif any(keyword in role_lower for keyword in ["frontend", "ui", "react", "angular", "vue"]):
            self.generated_questions.extend([
                {
                    "id": f"role_frontend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "Explain your approach to building responsive web applications.",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Responsive design, mobile-first approach, cross-browser compatibility.",
                },
                {
                    "id": f"role_frontend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "How do you optimize frontend performance?",
                    "difficulty_levels": ["Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Bundling, minification, lazy loading, caching strategies.",
                },
                {
                    "id": f"role_frontend_{len(self.generated_questions)}",
                    "section": "Role Fundamentals",
                    "question": "What's your experience with state management?",
                    "difficulty_levels": ["Basic", "Simple", "Hard"],
                    "category": "fundamentals",
                    "expected_answer": "Redux, Context API, Vuex, or similar state management patterns.",
                },
            ])

    def _add_skill_specific_questions(self, skill: str):
        """Add detailed questions for each specific skill."""

        skill_lower = skill.lower()
        skill_questions = self._get_skill_questions(skill_lower)

        # Randomize and add skill-specific questions
        random.shuffle(skill_questions)
        count = min(4, len(skill_questions))  # Add 4 questions per skill
        self.generated_questions.extend(skill_questions[:count])

    def _get_skill_questions(self, skill: str) -> List[Dict]:
        """Get comprehensive questions for a specific skill."""

        skill_db = {
            "playwright": self._playwright_skill_questions(),
            "selenium": self._selenium_skill_questions(),
            "java": self._java_skill_questions(),
            "python": self._python_skill_questions(),
            "javascript": self._javascript_skill_questions(),
            "typescript": self._typescript_skill_questions(),
            "restassured": self._restassured_skill_questions(),
            "cypress": self._cypress_skill_questions(),
            "docker": self._docker_skill_questions(),
            "kubernetes": self._kubernetes_skill_questions(),
            "aws": self._aws_skill_questions(),
            "azure": self._azure_skill_questions(),
            "gcp": self._gcp_skill_questions(),
            "react": self._react_skill_questions(),
            "angular": self._angular_skill_questions(),
            "vue": self._vue_skill_questions(),
            "nodejs": self._nodejs_skill_questions(),
            "go": self._go_skill_questions(),
            "rust": self._rust_skill_questions(),
            "c#": self._csharp_skill_questions(),
        }

        return skill_db.get(skill, [])

    def _playwright_skill_questions(self) -> List[Dict]:
        """Real Playwright interview questions."""
        return [
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "What is Playwright and how does it differ from Selenium? In what scenarios would you use Playwright?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Modern automation tool, multi-browser support, better auto-wait, architecture comparison."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "Explain the difference between fill(), type(), and press() methods in Playwright. When would you use each?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "fill() for direct value, type() for simulated keystrokes, press() for keyboard actions."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "How do you handle authentication in Playwright tests? Describe at least two approaches.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "UI login flow, API token injection, storage state persistence, cookies management."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "What are Browser Contexts and how do they help in test automation?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Isolated browser environments for parallel testing, session management, multi-user scenarios."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "Explain Playwright's auto-wait mechanism. How does it work and what are its limitations?",
                "difficulty_levels": ["Hard"],
                "category": "tool",
                "expected_answer": "Auto-waits for element visibility, actionability checks, timeout configuration, potential race conditions."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "How do you handle network interception and mocking in Playwright?",
                "difficulty_levels": ["Hard"],
                "category": "tool",
                "expected_answer": "route() method, request/response interception, mocking third-party APIs, handling dynamic data."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "Describe your approach to debugging Playwright tests. What tools and techniques do you use?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Playwright Inspector, trace viewer, debug mode, screenshots, videos, logs analysis."
            },
            {
                "id": f"skill_playwright_{random.randint(1000, 9999)}",
                "section": "Playwright Skills",
                "question": "How do you implement parallel test execution in Playwright? What are the considerations?",
                "difficulty_levels": ["Hard"],
                "category": "tool",
                "expected_answer": "Worker configuration, test sharding, resource management, state isolation, flakiness handling."
            },
        ]

    def _selenium_skill_questions(self) -> List[Dict]:
        """Real Selenium interview questions."""
        return [
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "Explain the architecture of Selenium WebDriver and how it communicates with browsers.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "WebDriver protocol, JSON-Wire protocol, browser drivers, client-server architecture."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "What's the difference between implicit and explicit waits? When should you use each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Implicit waits globally applied, explicit waits for specific conditions, best practices."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "Describe different locator strategies in Selenium and recommend when to use each.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "ID, Class, XPath, CSS selectors, Link text, advantages and disadvantages of each."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "How do you handle dropdown selections and multi-select elements?",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "tool",
                "expected_answer": "Select class, selecting by value/text/index, handling custom dropdowns."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "Explain how you would handle alerts, popups, and windows in Selenium.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Alert handling, window switching, managing multiple windows, popup strategies."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "How do you deal with flaky tests in Selenium? What strategies do you use?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Proper wait strategies, element stability, network considerations, retry logic."
            },
            {
                "id": f"skill_selenium_{random.randint(1000, 9999)}",
                "section": "Selenium Skills",
                "question": "Describe your approach to test data management in Selenium-based automation.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Data setup/teardown, isolation, persistence, environment management."
            },
        ]

    def _java_skill_questions(self) -> List[Dict]:
        """Real Java interview questions."""
        return [
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "Explain the difference between String, StringBuilder, and StringBuffer. When would you use each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "language",
                "expected_answer": "Immutability, mutability, thread safety, performance implications."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "What are generics in Java? Why are they important? Provide examples.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Type safety, type erasure, wildcards, bounded types, collections."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "Explain the Collection hierarchy in Java. What are key interfaces and implementations?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "language",
                "expected_answer": "List, Set, Map, ArrayList, HashMap, HashSet, their use cases."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "What is exception handling in Java? Explain checked vs unchecked exceptions.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "language",
                "expected_answer": "Try-catch-finally, checked exceptions, unchecked exceptions, custom exceptions."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "Explain the concept of streams in Java 8. How do they differ from collections?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Lazy evaluation, functional programming, map/filter/reduce operations."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "What is the difference between synchronized and volatile keywords?",
                "difficulty_levels": ["Hard"],
                "category": "language",
                "expected_answer": "Thread synchronization, memory visibility, atomicity, use cases."
            },
            {
                "id": f"skill_java_{random.randint(1000, 9999)}",
                "section": "Java Skills",
                "question": "Write a function to reverse a string and explain your approach.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "coding",
                "expected_answer": "Multiple approaches: using StringBuilder, recursion, loops."
            },
        ]

    def _python_skill_questions(self) -> List[Dict]:
        """Real Python interview questions."""
        return [
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "Explain list comprehensions and generator expressions. When would you use each?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "language",
                "expected_answer": "Syntax, performance, memory usage, use cases for both."
            },
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "What are decorators in Python? Provide examples of how you've used them.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Function wrapping, parametrized decorators, real-world applications."
            },
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "Explain the difference between *args and **kwargs.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "language",
                "expected_answer": "Positional arguments, keyword arguments, use cases."
            },
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "What is the Global Interpreter Lock (GIL)? How does it affect multithreading?",
                "difficulty_levels": ["Hard"],
                "category": "language",
                "expected_answer": "Thread safety, multiprocessing alternatives, CPU-bound vs I/O-bound."
            },
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "Explain closures and nested functions in Python.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Scope, captured variables, practical examples."
            },
            {
                "id": f"skill_python_{random.randint(1000, 9999)}",
                "section": "Python Skills",
                "question": "What are metaclasses? When would you use them?",
                "difficulty_levels": ["Hard"],
                "category": "language",
                "expected_answer": "Class creation, advanced patterns, real-world use cases."
            },
        ]

    def _experience_level_questions(self) -> List[Dict]:
        """Add questions appropriate to years of experience."""

        experience_questions = []

        if self.years_of_experience < 2:
            # Fresher level
            experience_questions.extend([
                {
                    "id": f"exp_fresher_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "What's the biggest challenge you've faced in your current/recent project?",
                    "difficulty_levels": ["Fresher"],
                    "category": "behavioral",
                    "expected_answer": "Real project experience, problem-solving approach, lessons learned."
                },
                {
                    "id": f"exp_fresher_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "How do you approach learning new technologies?",
                    "difficulty_levels": ["Fresher"],
                    "category": "behavioral",
                    "expected_answer": "Self-learning strategy, resources, continuous learning mindset."
                },
            ])

        elif self.years_of_experience < 5:
            # Mid-level
            experience_questions.extend([
                {
                    "id": f"exp_mid_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "Describe a time when you had to optimize performance. What approach did you take?",
                    "difficulty_levels": ["Simple"],
                    "category": "behavioral",
                    "expected_answer": "Analysis, optimization techniques, measurable results."
                },
                {
                    "id": f"exp_mid_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "How have you contributed to improving team processes or code quality?",
                    "difficulty_levels": ["Simple"],
                    "category": "behavioral",
                    "expected_answer": "Initiative, leadership, process improvements, metrics."
                },
            ])

        else:
            # Senior level
            experience_questions.extend([
                {
                    "id": f"exp_senior_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "Tell me about a system you architected. What design decisions did you make and why?",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Architecture thinking, scalability, trade-offs, decision rationale."
                },
                {
                    "id": f"exp_senior_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "How do you mentor junior team members? Give a specific example.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Mentoring approach, growth facilitation, team development."
                },
                {
                    "id": f"exp_senior_{random.randint(1000, 9999)}",
                    "section": "Experience Level",
                    "question": "Describe your approach to handling production incidents or critical issues.",
                    "difficulty_levels": ["Hard"],
                    "category": "behavioral",
                    "expected_answer": "Crisis management, root cause analysis, prevention strategies."
                },
            ])

        return experience_questions

    def _add_behavioral_questions(self):
        """Add behavioral and situational questions."""

        behavioral = [
            {
                "id": f"behavioral_{random.randint(1000, 9999)}",
                "section": "Behavioral Questions",
                "question": "Tell me about a time you had to work with a difficult team member. How did you handle it?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Conflict resolution, communication, empathy, positive outcome."
            },
            {
                "id": f"behavioral_{random.randint(1000, 9999)}",
                "section": "Behavioral Questions",
                "question": "Describe a situation where you had to learn something new quickly. How did you approach it?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Adaptability, learning strategy, resourcefulness, results."
            },
            {
                "id": f"behavioral_{random.randint(1000, 9999)}",
                "section": "Behavioral Questions",
                "question": "Tell me about your most complex project. What made it complex and how did you solve it?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Technical complexity, problem-solving, achievement, impact."
            },
            {
                "id": f"behavioral_{random.randint(1000, 9999)}",
                "section": "Behavioral Questions",
                "question": "How do you prioritize when you have multiple urgent tasks?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "behavioral",
                "expected_answer": "Prioritization methodology, impact analysis, time management."
            },
        ]

        self.generated_questions.extend(behavioral)

    def _add_scenario_questions(self):
        """Add scenario-based and problem-solving questions."""

        scenarios = [
            {
                "id": f"scenario_{random.randint(1000, 9999)}",
                "section": "Scenarios",
                "question": f"You are assigned to test a critical payment feature with only 1 day before production release. Walk me through your approach.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "scenario",
                "expected_answer": "Risk assessment, prioritization, testing strategy, scope management."
            },
            {
                "id": f"scenario_{random.randint(1000, 9999)}",
                "section": "Scenarios",
                "question": "Your test suite is taking too long to run (2+ hours). How would you optimize it?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "scenario",
                "expected_answer": "Parallelization, selective testing, optimization techniques, metrics."
            },
            {
                "id": f"scenario_{random.randint(1000, 9999)}",
                "section": "Scenarios",
                "question": "A critical production issue is discovered. How would you approach investigating and fixing it?",
                "difficulty_levels": ["Hard"],
                "category": "scenario",
                "expected_answer": "Investigation methodology, communication, fixes, prevention."
            },
        ]

        self.generated_questions.extend(scenarios)

    # Placeholder methods for other skills
    def _javascript_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_js_{random.randint(1000, 9999)}",
                "section": "JavaScript Skills",
                "question": "Explain hoisting in JavaScript and provide examples.",
                "difficulty_levels": ["Basic", "Simple"],
                "category": "language",
                "expected_answer": "Variable hoisting, function hoisting, temporal dead zone."
            },
            {
                "id": f"skill_js_{random.randint(1000, 9999)}",
                "section": "JavaScript Skills",
                "question": "What is the event loop and how does it handle asynchronous operations?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Call stack, event queue, promises, async/await."
            },
        ]

    def _typescript_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_ts_{random.randint(1000, 9999)}",
                "section": "TypeScript Skills",
                "question": "Explain generics in TypeScript and how they improve type safety.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Generic functions, interfaces, constraints, real-world use cases."
            },
        ]

    def _restassured_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_ra_{random.randint(1000, 9999)}",
                "section": "RestAssured Skills",
                "question": "How do you structure and organize REST API tests using RestAssured?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Base URIs, request/response specifications, assertions, patterns."
            },
        ]

    def _cypress_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_cy_{random.randint(1000, 9999)}",
                "section": "Cypress Skills",
                "question": "How does Cypress differ from Selenium? When would you choose Cypress?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Architecture, debugging capabilities, limitations, use cases."
            },
        ]

    def _docker_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_docker_{random.randint(1000, 9999)}",
                "section": "Docker Skills",
                "question": "Explain Docker containers, images, and Dockerfile. How would you containerize an application?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Container concepts, image building, Dockerfile best practices."
            },
        ]

    def _kubernetes_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_k8s_{random.randint(1000, 9999)}",
                "section": "Kubernetes Skills",
                "question": "Explain key Kubernetes concepts: pods, services, deployments, and namespaces.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Container orchestration, resource management, service discovery."
            },
        ]

    def _aws_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_aws_{random.randint(1000, 9999)}",
                "section": "AWS Skills",
                "question": "Describe your experience with AWS services. Which ones have you used and for what purposes?",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "EC2, S3, Lambda, RDS, IAM, networking concepts."
            },
        ]

    def _azure_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_azure_{random.randint(1000, 9999)}",
                "section": "Azure Skills",
                "question": "Explain your experience with Azure cloud services.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Azure VMs, App Services, SQL Database, DevOps, cost management."
            },
        ]

    def _gcp_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_gcp_{random.randint(1000, 9999)}",
                "section": "GCP Skills",
                "question": "What GCP services have you worked with? Describe your experience.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "tool",
                "expected_answer": "Compute Engine, Cloud Functions, BigQuery, Firestore, networking."
            },
        ]

    def _react_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_react_{random.randint(1000, 9999)}",
                "section": "React Skills",
                "question": "Explain React hooks and how they differ from class components.",
                "difficulty_levels": ["Basic", "Simple", "Hard"],
                "category": "language",
                "expected_answer": "useState, useEffect, custom hooks, lifecycle management."
            },
        ]

    def _angular_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_angular_{random.randint(1000, 9999)}",
                "section": "Angular Skills",
                "question": "Explain Angular's dependency injection and how it's used in components.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "DI containers, services, providers, component interaction."
            },
        ]

    def _vue_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_vue_{random.randint(1000, 9999)}",
                "section": "Vue Skills",
                "question": "Explain Vue's composition API and how it differs from the Options API.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Composition functions, state management, component structure."
            },
        ]

    def _nodejs_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_nodejs_{random.randint(1000, 9999)}",
                "section": "Node.js Skills",
                "question": "Explain the event-driven architecture of Node.js and how it handles I/O operations.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Event loop, non-blocking I/O, callbacks, promises, async/await."
            },
        ]

    def _go_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_go_{random.randint(1000, 9999)}",
                "section": "Go Skills",
                "question": "Explain goroutines and channels in Go. How do they enable concurrent programming?",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Lightweight concurrency, channel communication, synchronization."
            },
        ]

    def _rust_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_rust_{random.randint(1000, 9999)}",
                "section": "Rust Skills",
                "question": "Explain Rust's ownership system and how it ensures memory safety.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Ownership rules, borrowing, lifetimes, mutability."
            },
        ]

    def _csharp_skill_questions(self) -> List[Dict]:
        return [
            {
                "id": f"skill_csharp_{random.randint(1000, 9999)}",
                "section": "C# Skills",
                "question": "Explain LINQ and how it enables query-like syntax in C#.",
                "difficulty_levels": ["Simple", "Hard"],
                "category": "language",
                "expected_answer": "Query syntax, method syntax, IEnumerable, performance considerations."
            },
        ]

    def get_questions_for_interview(self) -> List[Dict]:
        """Get randomized questions for the interview."""

        total_needed = self._calculate_question_count()

        # Filter by difficulty
        available = [q for q in self.generated_questions
                    if self.difficulty in q.get("difficulty_levels", [])]

        # Randomize selection
        if len(available) > total_needed:
            selected = random.sample(available, total_needed)
        else:
            selected = available

        # Organize by section
        return self._organize_by_section(selected)

    def _calculate_question_count(self) -> int:
        """Calculate total questions needed."""
        if self.difficulty in ["Fresher", "Basic"]:
            return 15 + int(self.years_of_experience)
        elif self.difficulty == "Simple":
            return 20 + int(self.years_of_experience * 0.5)
        else:  # Hard
            return 25 + int(self.years_of_experience * 0.5)

    def _organize_by_section(self, questions: List[Dict]) -> List[Dict]:
        """Organize questions by section for logical flow."""
        section_order = [
            "Role Fundamentals",
            "Experience Level",
            f"{self.primary_skills[0]} Skills" if self.primary_skills else "Skills",
            "Behavioral Questions",
            "Scenarios"
        ]

        result = []
        for section in section_order:
            section_qs = [q for q in questions if q.get("section") == section]
            result.extend(section_qs)

        # Add any remaining questions not in the section order
        added_ids = {q.get("id") for q in result}
        remaining = [q for q in questions if q.get("id") not in added_ids]
        result.extend(remaining)

        return result[:self._calculate_question_count()]
