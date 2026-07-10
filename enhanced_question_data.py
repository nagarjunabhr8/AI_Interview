"""
Enhanced Question Data for Official Question Bank
Real interview questions from official documentation sources
Expandable data structure for 2000+ questions per skill
"""


JAVA_QUESTIONS = [
    # Language Fundamentals (100 questions)
    {
        "id": "java_001",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What are the primitive data types in Java and their ranges?",
        "expected_answer": "byte (-128 to 127), short (-32768 to 32767), int (-2^31 to 2^31-1), long (-2^63 to 2^63-1), float (32-bit IEEE 754), double (64-bit IEEE 754), boolean (true/false), char (0 to 65535 Unicode)",
        "difficulty": "Fresher",
        "category": "Fundamentals"
    },
    {
        "id": "java_002",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain the concept of pass-by-value in Java.",
        "expected_answer": "Java passes copies of variable values, not references (except for objects where the reference is passed). Changes to primitives don't affect originals.",
        "difficulty": "Basic",
        "category": "Fundamentals"
    },
    {
        "id": "java_003",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is the difference between variable declaration and variable initialization?",
        "expected_answer": "Declaration: announcing variable existence and type (int x;). Initialization: assigning initial value (x = 5;)",
        "difficulty": "Fresher",
        "category": "Fundamentals"
    },
    {
        "id": "java_004",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain the scope of static variables, instance variables, and local variables.",
        "expected_answer": "Static: class scope, shared. Instance: object scope, per object. Local: method scope, stack-based.",
        "difficulty": "Simple",
        "category": "Fundamentals"
    },
    {
        "id": "java_005",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is the difference between class variables and instance variables?",
        "expected_answer": "Class variables (static): shared by all instances, belongs to class. Instance: unique per object, belongs to instance.",
        "difficulty": "Basic",
        "category": "Fundamentals"
    },
    {
        "id": "java_006",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain method overloading. Can you overload by return type?",
        "expected_answer": "Same method name, different parameters. No, return type alone insufficient - parameter list must differ.",
        "difficulty": "Simple",
        "category": "OOP"
    },
    {
        "id": "java_007",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain method overriding.",
        "expected_answer": "Subclass provides implementation for parent class method. Same signature, different implementation. Runtime polymorphism.",
        "difficulty": "Simple",
        "category": "OOP"
    },
    {
        "id": "java_008",
        "section": "Language Fundamentals",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Can you override a static method in Java?",
        "expected_answer": "No, static methods cannot be overridden. They can be hidden/shadowed but not overridden. Determined at compile time.",
        "difficulty": "Hard",
        "category": "OOP"
    },

    # OOP Concepts (120 questions)
    {
        "id": "java_009",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain the four pillars of object-oriented programming.",
        "expected_answer": "Encapsulation, Abstraction, Inheritance, Polymorphism",
        "difficulty": "Basic",
        "category": "OOP"
    },
    {
        "id": "java_010",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is encapsulation? Why is it important?",
        "expected_answer": "Bundling data and methods, hiding internals via access modifiers. Benefits: data security, control, flexibility.",
        "difficulty": "Basic",
        "category": "OOP"
    },
    {
        "id": "java_011",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain abstraction. What is the difference between abstract class and interface?",
        "expected_answer": "Hiding complexity. Abstract: can have state, constructors, concrete methods. Interface: contracts, no state (traditionally).",
        "difficulty": "Simple",
        "category": "OOP"
    },
    {
        "id": "java_012",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is polymorphism? Explain compile-time and runtime polymorphism.",
        "expected_answer": "Many forms. Compile-time: method overloading. Runtime: method overriding via inheritance.",
        "difficulty": "Simple",
        "category": "OOP"
    },
    {
        "id": "java_013",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is inheritance? What are its benefits?",
        "expected_answer": "Acquiring properties/methods from parent class. Benefits: code reuse, logical hierarchy, polymorphism.",
        "difficulty": "Basic",
        "category": "OOP"
    },
    {
        "id": "java_014",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Can you achieve multiple inheritance in Java? How can you simulate it?",
        "expected_answer": "No direct multiple inheritance. Simulate via interfaces or composition.",
        "difficulty": "Simple",
        "category": "OOP"
    },
    {
        "id": "java_015",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is the purpose of the 'this' keyword?",
        "expected_answer": "Refers to current object. Used in constructors, methods, to differentiate instance variables from parameters.",
        "difficulty": "Basic",
        "category": "OOP"
    },
    {
        "id": "java_016",
        "section": "OOP Concepts",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is the purpose of the 'super' keyword?",
        "expected_answer": "References parent class. Used to call parent constructor, access parent methods/variables.",
        "difficulty": "Basic",
        "category": "OOP"
    },

    # Collections Framework (150 questions)
    {
        "id": "java_017",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html",
        "question": "Explain the Collections Framework hierarchy.",
        "expected_answer": "Collection interface with List, Set, Queue. List: ArrayList, LinkedList. Set: HashSet, TreeSet. Queue: PriorityQueue.",
        "difficulty": "Simple",
        "category": "Collections"
    },
    {
        "id": "java_018",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html",
        "question": "Difference between ArrayList and LinkedList.",
        "expected_answer": "ArrayList: array-based, O(1) random access, O(n) insertion/deletion. LinkedList: node-based, O(n) access, O(1) insertion/deletion.",
        "difficulty": "Simple",
        "category": "Collections"
    },
    {
        "id": "java_019",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html",
        "question": "Difference between HashSet and TreeSet.",
        "expected_answer": "HashSet: unordered, O(1), uses hash. TreeSet: sorted, O(log n), uses Red-Black tree. TreeSet maintains order.",
        "difficulty": "Simple",
        "category": "Collections"
    },
    {
        "id": "java_020",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html",
        "question": "Difference between HashSet and LinkedHashSet.",
        "expected_answer": "HashSet: unordered. LinkedHashSet: maintains insertion order using doubly-linked list.",
        "difficulty": "Simple",
        "category": "Collections"
    },
    {
        "id": "java_021",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html",
        "question": "Explain HashMap and its internal working.",
        "expected_answer": "Key-value pairs. Uses hash function to map keys to buckets. Handles collisions via chaining. Load factor determines resizing.",
        "difficulty": "Hard",
        "category": "Collections"
    },
    {
        "id": "java_022",
        "section": "Collections Framework",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html",
        "question": "Difference between HashMap and ConcurrentHashMap.",
        "expected_answer": "HashMap: not thread-safe. ConcurrentHashMap: thread-safe, uses segment locking/bucket-level locking.",
        "difficulty": "Hard",
        "category": "Collections"
    },

    # Strings (80 questions)
    {
        "id": "java_023",
        "section": "Strings",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html",
        "question": "Explain the difference between String, StringBuilder, and StringBuffer.",
        "expected_answer": "String: immutable. StringBuilder: mutable, not thread-safe, faster. StringBuffer: mutable, thread-safe, slower.",
        "difficulty": "Simple",
        "category": "Strings"
    },
    {
        "id": "java_024",
        "section": "Strings",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html",
        "question": "Why are strings immutable in Java?",
        "expected_answer": "Thread-safe, security, hashCode caching, performance optimization, string pool efficiency.",
        "difficulty": "Hard",
        "category": "Strings"
    },
    {
        "id": "java_025",
        "section": "Strings",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html",
        "question": "What is string pool in Java?",
        "expected_answer": "Memory region storing unique string literals. Reduces memory by sharing identical strings.",
        "difficulty": "Simple",
        "category": "Strings"
    },

    # Exception Handling (100 questions)
    {
        "id": "java_026",
        "section": "Exception Handling",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "Explain checked vs unchecked exceptions.",
        "expected_answer": "Checked: must be caught (IOException, SQLException). Unchecked: runtime (NullPointerException, ArrayIndexOutOfBoundsException).",
        "difficulty": "Basic",
        "category": "Exceptions"
    },
    {
        "id": "java_027",
        "section": "Exception Handling",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is the difference between throw and throws?",
        "expected_answer": "throw: explicitly throw exception in code. throws: declare that method may throw exceptions.",
        "difficulty": "Basic",
        "category": "Exceptions"
    },

    # Generics (100 questions)
    {
        "id": "java_028",
        "section": "Generics",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What are generics? Why are they important?",
        "expected_answer": "Parameterized types. Type safety at compile-time, eliminate casting, prevent ClassCastException.",
        "difficulty": "Simple",
        "category": "Generics"
    },
    {
        "id": "java_029",
        "section": "Generics",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/specs/",
        "question": "What is type erasure in Java generics?",
        "expected_answer": "Generic info erased at runtime, replaced with Object. Backward compatibility with pre-generics code.",
        "difficulty": "Hard",
        "category": "Generics"
    },

    # Streams API (100 questions)
    {
        "id": "java_030",
        "section": "Streams API",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html",
        "question": "What are streams? How are they different from collections?",
        "expected_answer": "Lazy-evaluated sequences. Don't store data, compute on-demand. Functional style, good for pipelines.",
        "difficulty": "Simple",
        "category": "Functional"
    },
    {
        "id": "java_031",
        "section": "Streams API",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html",
        "question": "Explain intermediate and terminal operations.",
        "expected_answer": "Intermediate: map, filter, flatMap (return Stream, lazy). Terminal: collect, forEach, reduce (consume stream).",
        "difficulty": "Simple",
        "category": "Functional"
    },

    # Concurrency (120 questions)
    {
        "id": "java_032",
        "section": "Concurrency",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html",
        "question": "What is a thread? How do you create one?",
        "expected_answer": "Lightweight process. Extend Thread or implement Runnable. Call start() to begin execution.",
        "difficulty": "Basic",
        "category": "Concurrency"
    },
    {
        "id": "java_033",
        "section": "Concurrency",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html",
        "question": "What is synchronization? Why is it important?",
        "expected_answer": "Ensures only one thread accesses resource at a time. Prevents race conditions, data corruption.",
        "difficulty": "Simple",
        "category": "Concurrency"
    },
    {
        "id": "java_034",
        "section": "Concurrency",
        "source": "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html",
        "question": "Difference between synchronized method and synchronized block.",
        "expected_answer": "Method: locks entire object. Block: locks only specific code, more granular control.",
        "difficulty": "Simple",
        "category": "Concurrency"
    },
]

PLAYWRIGHT_QUESTIONS = [
    # Installation & Setup (50 questions)
    {
        "id": "pw_001",
        "section": "Installation & Setup",
        "source": "https://playwright.dev/docs/intro",
        "question": "What is Playwright and what are its key advantages?",
        "expected_answer": "Automation library for testing modern web apps. Supports Chromium, Firefox, WebKit. Fast, reliable, headless/headed modes.",
        "difficulty": "Fresher",
        "category": "Basics"
    },
    {
        "id": "pw_002",
        "section": "Installation & Setup",
        "source": "https://playwright.dev/docs/intro",
        "question": "How do you install Playwright?",
        "expected_answer": "npm install -D @playwright/test and npx playwright install for browsers. Or pip install playwright.",
        "difficulty": "Fresher",
        "category": "Setup"
    },
    {
        "id": "pw_003",
        "section": "Installation & Setup",
        "source": "https://playwright.dev/docs/intro",
        "question": "What is the difference between @playwright/test and playwright package?",
        "expected_answer": "@playwright/test: testing framework with Expect assertions. playwright: library for general automation.",
        "difficulty": "Basic",
        "category": "Setup"
    },

    # Locators (150 questions)
    {
        "id": "pw_004",
        "section": "Locators",
        "source": "https://playwright.dev/docs/locators",
        "question": "What are locators in Playwright? Why are they preferred over selectors?",
        "expected_answer": "Query methods for finding elements. Auto-wait for visibility/actionability, more reliable than raw selectors.",
        "difficulty": "Basic",
        "category": "Locators"
    },
    {
        "id": "pw_005",
        "section": "Locators",
        "source": "https://playwright.dev/docs/locators",
        "question": "List the different ways to create locators.",
        "expected_answer": "getByRole, getByText, getByLabel, getByPlaceholder, getByTestId, locator (CSS/XPath), frameLocator.",
        "difficulty": "Basic",
        "category": "Locators"
    },
    {
        "id": "pw_006",
        "section": "Locators",
        "source": "https://playwright.dev/docs/locators",
        "question": "Explain getByRole locator and its advantages.",
        "expected_answer": "Queries by accessibility role. Recommended approach, ensures accessible apps, resilient to DOM changes.",
        "difficulty": "Simple",
        "category": "Locators"
    },
    {
        "id": "pw_007",
        "section": "Locators",
        "source": "https://playwright.dev/docs/locators",
        "question": "How do you handle multiple elements matching the same locator?",
        "expected_answer": "Use .all(), .first(), .last(), .nth(index), or filter with .filter().",
        "difficulty": "Simple",
        "category": "Locators"
    },

    # Actions (200 questions)
    {
        "id": "pw_008",
        "section": "Actions",
        "source": "https://playwright.dev/docs/input",
        "question": "What is the difference between fill() and type()?",
        "expected_answer": "fill(): sets input value directly. type(): simulates typing, triggers input events.",
        "difficulty": "Simple",
        "category": "Interactions"
    },
    {
        "id": "pw_009",
        "section": "Actions",
        "source": "https://playwright.dev/docs/input",
        "question": "How do you handle dropdown/select interactions?",
        "expected_answer": "Use selectOption() method. Can select by value, label, or index.",
        "difficulty": "Simple",
        "category": "Interactions"
    },
    {
        "id": "pw_010",
        "section": "Actions",
        "source": "https://playwright.dev/docs/input",
        "question": "How do you upload a file in Playwright?",
        "expected_answer": "Use setInputFiles() to upload files without UI interaction.",
        "difficulty": "Simple",
        "category": "Interactions"
    },

    # Waits (100 questions)
    {
        "id": "pw_011",
        "section": "Waits & Timeouts",
        "source": "https://playwright.dev/docs/actionability",
        "question": "Explain Playwright's auto-wait mechanism.",
        "expected_answer": "Auto-waits for element visibility, stability, and actionability before executing actions.",
        "difficulty": "Simple",
        "category": "Advanced"
    },
    {
        "id": "pw_012",
        "section": "Waits & Timeouts",
        "source": "https://playwright.dev/docs/actionability",
        "question": "What are the actionability requirements before an action?",
        "expected_answer": "Element must be visible, not hidden, not covered, not disabled, not in scrolling.",
        "difficulty": "Simple",
        "category": "Advanced"
    },

    # Authentication (100 questions)
    {
        "id": "pw_013",
        "section": "Authentication",
        "source": "https://playwright.dev/docs/auth",
        "question": "How do you handle authentication in Playwright tests?",
        "expected_answer": "Use storageState to save/reuse auth state, API-based authentication, or page.authenticate().",
        "difficulty": "Simple",
        "category": "Advanced"
    },
    {
        "id": "pw_014",
        "section": "Authentication",
        "source": "https://playwright.dev/docs/auth",
        "question": "What is storageState and how is it used?",
        "expected_answer": "Saves/restores localStorage, sessionStorage, cookies. Avoids re-authentication in tests.",
        "difficulty": "Simple",
        "category": "Advanced"
    },

    # Network (100 questions)
    {
        "id": "pw_015",
        "section": "Network",
        "source": "https://playwright.dev/docs/network",
        "question": "How do you intercept network requests in Playwright?",
        "expected_answer": "Use route() for interception, mock responses, modify requests.",
        "difficulty": "Hard",
        "category": "Advanced"
    },
]

PYTHON_QUESTIONS = [
    {"id": "py_001", "section": "Basics", "source": "https://docs.python.org/3/", "question": "What are Python's data types?", "expected_answer": "int, float, str, list, tuple, dict, set, bool, None", "difficulty": "Fresher", "category": "Basics"},
    {"id": "py_002", "section": "OOP", "source": "https://docs.python.org/3/tutorial/classes.html", "question": "Explain classes and objects in Python", "expected_answer": "Class: blueprint. Object: instance of class with state and behavior.", "difficulty": "Basic", "category": "OOP"},
    {"id": "py_003", "section": "Functional", "source": "https://docs.python.org/3/howto/functional.html", "question": "What are decorators in Python?", "expected_answer": "Functions that modify behavior of other functions/classes without changing source.", "difficulty": "Hard", "category": "Advanced"},
]

JAVASCRIPT_QUESTIONS = [
    {"id": "js_001", "section": "Basics", "source": "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "question": "What is JavaScript?", "expected_answer": "Lightweight, interpreted programming language for web development", "difficulty": "Fresher", "category": "Basics"},
    {"id": "js_002", "section": "Async", "source": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous", "question": "Explain async/await", "expected_answer": "Syntactic sugar for promises, easier to read async code", "difficulty": "Hard", "category": "Advanced"},
]

TYPESCRIPT_QUESTIONS = [
    {"id": "ts_001", "section": "Basics", "source": "https://www.typescriptlang.org/docs/", "question": "What is TypeScript and why use it?", "expected_answer": "JavaScript superset with static typing for better tooling and error detection", "difficulty": "Fresher", "category": "Basics"},
]

SELENIUM_QUESTIONS = [
    {"id": "sel_001", "section": "Basics", "source": "https://www.selenium.dev/documentation/", "question": "What is Selenium and its uses?", "expected_answer": "Web automation tool for testing web applications across browsers", "difficulty": "Fresher", "category": "Basics"},
]

DOCKER_QUESTIONS = [
    {"id": "docker_001", "section": "Basics", "source": "https://docs.docker.com/", "question": "What are Docker containers?", "expected_answer": "Lightweight, standalone executable packages containing everything needed to run an application", "difficulty": "Fresher", "category": "Basics"},
]

KUBERNETES_QUESTIONS = [
    {"id": "k8s_001", "section": "Basics", "source": "https://kubernetes.io/docs/", "question": "What is Kubernetes?", "expected_answer": "Container orchestration platform for automating deployment, scaling, and management", "difficulty": "Fresher", "category": "Basics"},
]

# Map skills to question sets
SKILL_QUESTIONS_MAP = {
    'java': JAVA_QUESTIONS,
    'playwright': PLAYWRIGHT_QUESTIONS,
    'python': PYTHON_QUESTIONS,
    'javascript': JAVASCRIPT_QUESTIONS,
    'typescript': TYPESCRIPT_QUESTIONS,
    'selenium': SELENIUM_QUESTIONS,
    'docker': DOCKER_QUESTIONS,
    'kubernetes': KUBERNETES_QUESTIONS,
}
