"""
Dynamic Question Fetcher
Collects latest interview questions from multiple sources
Real-time, up-to-date, version-aware questions
"""

from typing import List, Dict, Any
import json
from datetime import datetime


class QuestionSource:
    """Represents a source of interview questions."""

    def __init__(self, name: str, url: str, category: str, source_type: str):
        self.name = name
        self.url = url
        self.category = category
        self.source_type = source_type  # tutorial, video, blog, stackoverflow, etc.
        self.last_updated = datetime.now().isoformat()


class DynamicQuestion:
    """Enhanced question with metadata."""

    def __init__(self, question_id: str, question_text: str, difficulty: str,
                 category: str, source: str, question_type: str,
                 expected_concepts: List[str] = None,
                 follow_up_questions: List[str] = None,
                 version_specific: Dict = None,
                 is_recent: bool = False):
        self.id = question_id
        self.question_text = question_text
        self.difficulty = difficulty  # Common, Basic, Intermediate, Advanced, Mixed/Trick
        self.category = category
        self.source = source
        self.question_type = question_type  # direct, follow-up, comparison, scenario, etc.
        self.expected_concepts = expected_concepts or []
        self.follow_up_questions = follow_up_questions or []
        self.version_specific = version_specific or {}
        self.is_recent = is_recent
        self.created_date = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'id': self.id,
            'question': self.question_text,
            'difficulty': self.difficulty,
            'category': self.category,
            'source': self.source,
            'type': self.question_type,
            'expected_concepts': self.expected_concepts,
            'follow_up_questions': self.follow_up_questions,
            'version_specific': self.version_specific,
            'is_recent': self.is_recent
        }


class JavaQuestionBank:
    """Latest Java interview questions - real-time relevant."""

    @staticmethod
    def get_common_questions() -> List[DynamicQuestion]:
        """Very common Java questions asked in every interview."""
        return [
            DynamicQuestion(
                'java_common_001',
                'What is the difference between JDK, JRE, and JVM?',
                'Common',
                'Java Basics',
                'Oracle Docs',
                'direct',
                expected_concepts=['JDK', 'JRE', 'JVM', 'compilation', 'execution'],
                follow_up_questions=[
                    'Can you run Java without JDK?',
                    'What happens during compilation vs runtime?',
                    'Why do we need different versions?'
                ],
                version_specific={
                    'Java 8': 'JDK 8 introduced functional programming',
                    'Java 11': 'Removed JRE from package, modular system',
                    'Java 17': 'LTS with sealed classes and pattern matching',
                    'Java 21': 'Virtual threads and structured concurrency'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_common_002',
                'Explain the concept of Object-Oriented Programming in Java with real examples.',
                'Common',
                'OOP Concepts',
                'Real Interview Feedback',
                'direct',
                expected_concepts=['Encapsulation', 'Inheritance', 'Polymorphism', 'Abstraction'],
                follow_up_questions=[
                    'How does encapsulation protect your code?',
                    'What\'s the difference between inheritance and composition?',
                    'When should you use abstract classes vs interfaces?',
                    'Can you give a real-world example from your projects?'
                ],
                is_recent=True
            ),

            DynamicQuestion(
                'java_common_003',
                'What is a Java Collection? Name some common collections and their use cases.',
                'Common',
                'Collections',
                'Tech Interview Handbook',
                'direct',
                expected_concepts=['Collection Framework', 'List', 'Set', 'Map', 'Performance'],
                follow_up_questions=[
                    'What\'s the time complexity of ArrayList vs LinkedList operations?',
                    'When would you choose HashMap over TreeMap?',
                    'How does HashSet ensure uniqueness?'
                ],
                version_specific={
                    'Java 8': 'Added Stream API and functional interfaces',
                    'Java 9': 'Collections factory methods (List.of, Set.of, Map.of)',
                    'Java 16': 'Sealed classes for restricted hierarchies'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_common_004',
                'Explain Exception Handling in Java. What is the difference between checked and unchecked exceptions?',
                'Common',
                'Exception Handling',
                'Real Interview Questions',
                'direct',
                expected_concepts=['try-catch-finally', 'Checked Exceptions', 'Unchecked Exceptions', 'Custom Exceptions'],
                follow_up_questions=[
                    'How would you handle multiple exceptions?',
                    'What is try-with-resources?',
                    'When should you create custom exceptions?',
                    'How do you decide whether to throw or handle an exception?'
                ],
                version_specific={
                    'Java 7': 'Multi-catch and try-with-resources',
                    'Java 14': 'Records can throw checked exceptions'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_common_005',
                'What is multithreading? How do you create threads in Java?',
                'Common',
                'Concurrency',
                'Real Interview Scenarios',
                'direct',
                expected_concepts=['Thread', 'Runnable', 'Synchronization', 'Thread States', 'Deadlock'],
                follow_up_questions=[
                    'What\'s the difference between extending Thread and implementing Runnable?',
                    'How do you prevent race conditions?',
                    'What is a deadlock and how do you avoid it?',
                    'What are virtual threads in Java 21?'
                ],
                version_specific={
                    'Java 5': 'Introduced ExecutorService and Thread pools',
                    'Java 7': 'ForkJoinPool for divide-and-conquer',
                    'Java 21': 'Virtual threads revolutionize concurrency'
                },
                is_recent=True
            ),
        ]

    @staticmethod
    def get_basic_questions() -> List[DynamicQuestion]:
        """Basic Java concepts - foundational knowledge."""
        return [
            DynamicQuestion(
                'java_basic_001',
                'What are the access modifiers in Java? Explain each one.',
                'Basic',
                'Java Basics',
                'Oracle Java Documentation',
                'direct',
                expected_concepts=['public', 'private', 'protected', 'default', 'visibility'],
                follow_up_questions=[
                    'How do access modifiers affect inheritance?',
                    'Why use protected instead of public?',
                    'What is package-private visibility?'
                ]
            ),

            DynamicQuestion(
                'java_basic_002',
                'What is the String class in Java? Why are strings immutable?',
                'Basic',
                'String Handling',
                'Java Memory Model',
                'direct',
                expected_concepts=['Immutability', 'String Pool', 'String.intern()', 'Security'],
                follow_up_questions=[
                    'How is the String pool implemented?',
                    'What\'s the performance impact of string immutability?',
                    'When would you use StringBuilder vs String concatenation?'
                ],
                version_specific={
                    'Java 9': 'Changed internal String representation (byte array instead of char)',
                    'Java 11': 'New String methods (isBlank, lines, repeat)'
                }
            ),

            DynamicQuestion(
                'java_basic_003',
                'Explain the difference between static and non-static members.',
                'Basic',
                'Java Basics',
                'Object-Oriented Programming',
                'direct',
                expected_concepts=['Static Variables', 'Static Methods', 'Instance Variables', 'Class Loading'],
                follow_up_questions=[
                    'When should you use static?',
                    'Can you override a static method?',
                    'What is a static initializer block?'
                ]
            ),

            DynamicQuestion(
                'java_basic_004',
                'What is Inheritance? Explain different types of inheritance supported in Java.',
                'Basic',
                'OOP',
                'Design Patterns Guide',
                'direct',
                expected_concepts=['Single Inheritance', 'Multi-level', 'Hierarchical', 'Multiple Inheritance'],
                follow_up_questions=[
                    'Why doesn\'t Java support multiple inheritance?',
                    'How do interfaces solve the multiple inheritance problem?',
                    'What is method shadowing vs method hiding?'
                ]
            ),
        ]

    @staticmethod
    def get_intermediate_questions() -> List[DynamicQuestion]:
        """Intermediate Java - deeper understanding."""
        return [
            DynamicQuestion(
                'java_intermediate_001',
                'Explain Generics in Java. What is type erasure and why does it exist?',
                'Intermediate',
                'Advanced Java',
                'Java Language Specification',
                'direct',
                expected_concepts=['Type Parameters', 'Type Erasure', 'Bounded Wildcards', 'PECS Principle'],
                follow_up_questions=[
                    'What are bounded type parameters?',
                    'Explain the difference between <? extends T> and <? super T>',
                    'Why can\'t you create an array of generics?',
                    'How does type erasure affect reflection?'
                ],
                version_specific={
                    'Java 5': 'Generics introduced',
                    'Java 10': 'Local variable type inference (var)'
                },
                is_recent=False
            ),

            DynamicQuestion(
                'java_intermediate_002',
                'What is the Functional Programming model in Java? Explain lambda expressions and functional interfaces.',
                'Intermediate',
                'Functional Programming',
                'Modern Java Development',
                'direct',
                expected_concepts=['Lambda', 'Functional Interface', '@FunctionalInterface', 'Method References'],
                follow_up_questions=[
                    'How do lambda expressions relate to anonymous classes?',
                    'What is a method reference and how does it differ from a lambda?',
                    'Explain the SAM (Single Abstract Method) principle',
                    'How do you compose functions in Java?'
                ],
                version_specific={
                    'Java 8': 'Lambda expressions and Stream API introduced',
                    'Java 11': 'Var in lambda expressions'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_intermediate_003',
                'Explain the Stream API in Java. What are intermediate vs terminal operations?',
                'Intermediate',
                'Functional Programming',
                'Modern Java Best Practices',
                'direct',
                expected_concepts=['Stream', 'Intermediate Ops', 'Terminal Ops', 'Lazy Evaluation', 'Collector'],
                follow_up_questions=[
                    'Why use streams over traditional loops?',
                    'What\'s the performance overhead of streams?',
                    'How do you create custom collectors?',
                    'When should you use parallel streams?'
                ],
                version_specific={
                    'Java 8': 'Streams API introduced',
                    'Java 9': 'Enhanced Stream API',
                    'Java 16': 'Improved streaming performance'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_intermediate_004',
                'Explain the principle of SOLID in object-oriented design with Java examples.',
                'Intermediate',
                'Design Principles',
                'Clean Code & Design Patterns',
                'direct',
                expected_concepts=['Single Responsibility', 'Open/Closed', 'Liskov Substitution', 'Interface Segregation', 'Dependency Inversion'],
                follow_up_questions=[
                    'How does dependency injection relate to SOLID?',
                    'Give an example where violating SOLID causes problems',
                    'How do you measure if your design follows SOLID?'
                ]
            ),
        ]

    @staticmethod
    def get_advanced_questions() -> List[DynamicQuestion]:
        """Advanced Java - expert level."""
        return [
            DynamicQuestion(
                'java_advanced_001',
                'Explain the Java Memory Model (JMM). What is the happens-before relationship?',
                'Advanced',
                'Concurrency & Memory',
                'Java Concurrency in Practice',
                'direct',
                expected_concepts=['Memory Model', 'Happens-Before', 'Visibility', 'Atomicity', 'Ordering'],
                follow_up_questions=[
                    'How does volatile relate to the memory model?',
                    'What are the ordering guarantees of synchronized?',
                    'Explain the double-checked locking pattern',
                    'How do you avoid memory leaks in concurrent code?'
                ],
                version_specific={
                    'Java 5': 'New Memory Model introduced',
                    'Java 9': 'Better tool support for memory analysis'
                }
            ),

            DynamicQuestion(
                'java_advanced_002',
                'What are sealed classes? How do they improve pattern matching?',
                'Advanced',
                'Modern Java Features',
                'Java 15+ Features (Recent)',
                'direct',
                expected_concepts=['Sealed Classes', 'Permits', 'Pattern Matching', 'Record Classes'],
                follow_up_questions=[
                    'How do sealed classes enable exhaustive pattern matching?',
                    'What\'s the relationship between sealed classes and records?',
                    'How does this improve code reliability?'
                ],
                version_specific={
                    'Java 15': 'Sealed classes preview',
                    'Java 16': 'Records finalized',
                    'Java 17': 'Sealed classes finalized',
                    'Java 21': 'Pattern matching for switch statements'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_advanced_003',
                'What are virtual threads (Project Loom)? How do they differ from platform threads?',
                'Advanced',
                'Modern Java Features',
                'Java 21 Features (LATEST)',
                'direct',
                expected_concepts=['Virtual Threads', 'Platform Threads', 'Structured Concurrency', 'Coroutines'],
                follow_up_questions=[
                    'How many virtual threads can you create?',
                    'What about virtual thread scheduling?',
                    'How do virtual threads impact existing code?',
                    'When should you use virtual vs platform threads?'
                ],
                version_specific={
                    'Java 19': 'Virtual threads preview',
                    'Java 21': 'Virtual threads finalized'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_advanced_004',
                'Explain records in Java. How do they simplify data classes?',
                'Advanced',
                'Modern Java Features',
                'Java 14+ Features',
                'direct',
                expected_concepts=['Records', 'Compact Constructor', 'Component', 'equals/hashCode/toString'],
                follow_up_questions=[
                    'How do records affect serialization?',
                    'Can you inherit from records?',
                    'What about field initialization in records?',
                    'How do records compare to Lombok?'
                ],
                version_specific={
                    'Java 14': 'Records preview',
                    'Java 15': 'Records second preview',
                    'Java 16': 'Records finalized'
                },
                is_recent=True
            ),
        ]

    @staticmethod
    def get_version_comparison_questions() -> List[DynamicQuestion]:
        """Questions about Java versions - what changed and why."""
        return [
            DynamicQuestion(
                'java_version_001',
                'What are the major differences between Java 8 and Java 17 (LTS)?',
                'Intermediate',
                'Java Versions',
                'Java Release Notes',
                'comparison',
                expected_concepts=['Java 8', 'Java 17', 'Streams', 'Records', 'Sealed Classes', 'Text Blocks'],
                follow_up_questions=[
                    'How does pattern matching improve from 8 to 17?',
                    'What\'s the performance difference?',
                    'Should you migrate from 8 to 17?'
                ],
                version_specific={
                    'Java 8': 'Lambdas, Streams introduced',
                    'Java 9-16': 'Various preview features',
                    'Java 17': 'LTS with finalized features'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'java_version_002',
                'Compare Java 11 (LTS) with Java 21 (LTS) - what changed?',
                'Intermediate',
                'Java Versions',
                'Official Java Documentation',
                'comparison',
                expected_concepts=['Virtual Threads', 'Pattern Matching', 'Records', 'Text Blocks', 'Performance'],
                follow_up_questions=[
                    'Which new features require code changes?',
                    'What\'s the performance improvement?',
                    'Is migration straightforward?'
                ],
                version_specific={
                    'Java 11': 'HTTP/2, Local var in lambdas',
                    'Java 21': 'Virtual threads, Pattern matching'
                },
                is_recent=True
            ),
        ]

    @staticmethod
    def get_trick_questions() -> List[DynamicQuestion]:
        """Tricky questions that reveal deeper understanding."""
        return [
            DynamicQuestion(
                'java_trick_001',
                'What is the output? Explain why.\nList<? extends Number> list = new ArrayList<Integer>();\nlist.add(10); // Does this compile?',
                'Advanced',
                'Generics Tricky',
                'Stack Overflow & Real Interviews',
                'trick',
                expected_concepts=['PECS Principle', 'Bounded Wildcards', 'Covariance', 'Compiler Errors'],
                follow_up_questions=[
                    'Why does the compiler prevent this?',
                    'What if you used <? super Number>?',
                    'How do you fix this?'
                ]
            ),

            DynamicQuestion(
                'java_trick_002',
                'What\'s the difference between == and .equals()? What about null safety?',
                'Intermediate',
                'Object Comparison',
                'Real Interview Gotchas',
                'trick',
                expected_concepts=['Reference Equality', 'Value Equality', 'null', 'NullPointerException'],
                follow_up_questions=[
                    'Can you safely call .equals() on null?',
                    'How do you implement .equals() correctly?',
                    'What about .hashCode()?'
                ]
            ),
        ]


class SeleniumQuestionBank:
    """Latest Selenium interview questions - version-aware."""

    @staticmethod
    def get_version_comparison() -> List[DynamicQuestion]:
        """Questions comparing Selenium 3 vs 4."""
        return [
            DynamicQuestion(
                'selenium_version_001',
                'What are the major differences between Selenium 3 and Selenium 4?',
                'Intermediate',
                'Selenium Versions',
                'Official Selenium Documentation',
                'comparison',
                expected_concepts=['WebDriver W3C Standard', 'Relative Locators', 'CDP', 'Waits', 'Logging'],
                follow_up_questions=[
                    'What is the W3C WebDriver standard?',
                    'How do relative locators improve automation?',
                    'What is Chrome DevTools Protocol (CDP)?',
                    'How do you migrate from Selenium 3 to 4?'
                ],
                version_specific={
                    'Selenium 3': 'Uses JSON Wire Protocol',
                    'Selenium 4': 'W3C WebDriver standard, better DevTools integration'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'selenium_version_002',
                'Explain relative locators in Selenium 4. How are they better than absolute XPath?',
                'Intermediate',
                'Selenium 4 Features',
                'Latest Selenium Best Practices',
                'direct',
                expected_concepts=['Relative Locators', 'above', 'below', 'toLeftOf', 'toRightOf', 'near'],
                follow_up_questions=[
                    'How do relative locators improve test stability?',
                    'When should you use them?',
                    'Can they completely replace XPath?'
                ],
                version_specific={
                    'Selenium 4': 'New feature for UI-based locators'
                },
                is_recent=True
            ),
        ]

    @staticmethod
    def get_common_questions() -> List[DynamicQuestion]:
        """Common Selenium questions asked in interviews."""
        return [
            DynamicQuestion(
                'selenium_common_001',
                'What is Selenium WebDriver? How does it work?',
                'Common',
                'Selenium Basics',
                'Real Interview Questions',
                'direct',
                expected_concepts=['WebDriver', 'Browser Automation', 'JSON Wire Protocol', 'W3C Standard'],
                follow_up_questions=[
                    'What are the different browsers supported?',
                    'How does Selenium communicate with browsers?',
                    'What are the limitations of Selenium?'
                ]
            ),

            DynamicQuestion(
                'selenium_common_002',
                'What is the difference between implicit and explicit waits in Selenium?',
                'Common',
                'Waits & Synchronization',
                'Common Interview Scenario',
                'direct',
                expected_concepts=['Implicit Wait', 'Explicit Wait', 'WebDriverWait', 'ExpectedConditions', 'Synchronization'],
                follow_up_questions=[
                    'When should you use implicit vs explicit waits?',
                    'What is the problem with implicit waits?',
                    'How do you handle AJAX waits?'
                ]
            ),
        ]


class TypeScriptQuestionBank:
    """Latest TypeScript interview questions."""

    @staticmethod
    def get_recent_questions() -> List[DynamicQuestion]:
        """Recent TypeScript questions - latest features."""
        return [
            DynamicQuestion(
                'typescript_recent_001',
                'Explain TypeScript generics and variance. What is covariance and contravariance?',
                'Advanced',
                'Advanced TypeScript',
                'TypeScript Handbook & Real Interviews',
                'direct',
                expected_concepts=['Generics', 'Covariance', 'Contravariance', 'Invariance', 'Type Safety'],
                follow_up_questions=[
                    'How does TypeScript handle variance?',
                    'When do you need to understand variance?',
                    'How do arrays and functions differ in variance?'
                ],
                version_specific={
                    'TypeScript 4.0': 'Improved generic variance handling',
                    'TypeScript 5.0': 'Const type parameters (immutability)'
                },
                is_recent=True
            ),

            DynamicQuestion(
                'typescript_recent_002',
                'What are const assertions in TypeScript? How do they help?',
                'Intermediate',
                'TypeScript Features',
                'Latest TypeScript Releases',
                'direct',
                expected_concepts=['const assertion', 'as const', 'literal types', 'immutability'],
                follow_up_questions=[
                    'How do const assertions differ from regular assertions?',
                    'When should you use them?'
                ],
                version_specific={
                    'TypeScript 3.4': 'const assertions introduced'
                },
                is_recent=True
            ),
        ]


class InteractiveQuestionFlow:
    """Manages follow-up questions and conversational flow."""

    def __init__(self):
        self.conversation_history = []
        self.asked_follow_ups = set()

    def add_to_history(self, role: str, content: str, metadata: Dict = None):
        """Add message to conversation history."""
        self.conversation_history.append({
            'role': role,  # 'interviewer' or 'candidate'
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata or {}
        })

    def get_follow_up_question(self, primary_question: DynamicQuestion, candidate_answer: str) -> str:
        """Generate or select follow-up question based on answer."""
        if not primary_question.follow_up_questions:
            return None

        for follow_up in primary_question.follow_up_questions:
            if follow_up not in self.asked_follow_ups:
                self.asked_follow_ups.add(follow_up)
                return follow_up

        return None

    def generate_probe_question(self, topic: str, depth_level: int) -> str:
        """Generate probing follow-up to go deeper."""
        probes = {
            'architecture': [
                'Can you explain the design decisions behind this?',
                'How would you handle edge cases?',
                'What are the performance implications?',
                'Have you faced any challenges with this approach?',
                'How would you test this?'
            ],
            'performance': [
                'What is the time complexity?',
                'How does this scale?',
                'Have you profiled this?',
                'What would you optimize first?',
                'Any known bottlenecks?'
            ],
            'implementation': [
                'Walk me through your implementation',
                'What libraries or frameworks would you use?',
                'How would you test this thoroughly?',
                'Any gotchas or common mistakes?',
                'How maintainable is this approach?'
            ]
        }

        probe_list = probes.get(topic, probes['architecture'])
        if depth_level < len(probe_list):
            return probe_list[depth_level]
        return probe_list[-1]

    def get_conversation_context(self) -> str:
        """Get formatted conversation context for interviewer."""
        if not self.conversation_history:
            return "No conversation history yet."

        context = "Conversation History:\n"
        for msg in self.conversation_history[-5:]:  # Last 5 messages
            context += f"\n{msg['role'].upper()}: {msg['content']}\n"

        return context


class DynamicQuestionCollector:
    """Collects questions from various sources."""

    def __init__(self):
        self.sources = [
            QuestionSource('Oracle Java Docs', 'https://docs.oracle.com/', 'Java', 'official_docs'),
            QuestionSource('Tech Interview Handbook', 'https://www.techinterviewhandbook.org/', 'General', 'tutorial'),
            QuestionSource('LeetCode Discuss', 'https://leetcode.com/discuss/', 'Coding', 'community'),
            QuestionSource('Stack Overflow', 'https://stackoverflow.com/', 'General', 'Q&A'),
            QuestionSource('YouTube Channels', 'https://www.youtube.com/', 'General', 'video'),
            QuestionSource('Medium Technical Blogs', 'https://medium.com/', 'General', 'blog'),
            QuestionSource('Real Interview Feedback', 'https://www.glassdoor.com/', 'General', 'crowdsourced'),
        ]

    def get_all_java_questions(self) -> List[DynamicQuestion]:
        """Aggregate all Java questions by difficulty."""
        questions = []
        questions.extend(JavaQuestionBank.get_common_questions())
        questions.extend(JavaQuestionBank.get_basic_questions())
        questions.extend(JavaQuestionBank.get_intermediate_questions())
        questions.extend(JavaQuestionBank.get_advanced_questions())
        questions.extend(JavaQuestionBank.get_version_comparison_questions())
        questions.extend(JavaQuestionBank.get_trick_questions())
        return questions

    def get_all_selenium_questions(self) -> List[DynamicQuestion]:
        """Aggregate all Selenium questions."""
        questions = []
        questions.extend(SeleniumQuestionBank.get_common_questions())
        questions.extend(SeleniumQuestionBank.get_version_comparison())
        return questions

    def get_all_typescript_questions(self) -> List[DynamicQuestion]:
        """Aggregate all TypeScript questions."""
        questions = []
        questions.extend(TypeScriptQuestionBank.get_recent_questions())
        return questions

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about question collection."""
        java_q = self.get_all_java_questions()
        selenium_q = self.get_all_selenium_questions()
        typescript_q = self.get_all_typescript_questions()

        return {
            'total_questions': len(java_q) + len(selenium_q) + len(typescript_q),
            'java_questions': {
                'total': len(java_q),
                'common': len([q for q in java_q if q.difficulty == 'Common']),
                'basic': len([q for q in java_q if q.difficulty == 'Basic']),
                'intermediate': len([q for q in java_q if q.difficulty == 'Intermediate']),
                'advanced': len([q for q in java_q if q.difficulty == 'Advanced']),
                'recent': len([q for q in java_q if q.is_recent])
            },
            'selenium_questions': {
                'total': len(selenium_q),
                'version_comparisons': len([q for q in selenium_q if q.question_type == 'comparison'])
            },
            'typescript_questions': {
                'total': len(typescript_q),
                'recent': len([q for q in typescript_q if q.is_recent])
            },
            'sources': len(self.sources)
        }
