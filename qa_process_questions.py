"""
QA Process / Agile Testing Question Bank
Process, metrics, and scenario-based questions covering Agile QA practice -
asked regardless of the candidate's technical stack, since every QA/dev
role in an Agile team needs to reason about process.
"""

import random
from typing import Dict, List


QA_PROCESS_QUESTIONS: List[Dict] = [
    {
        "id": "qa_proc_001",
        "question": "What are the key QA metrics you track in an Agile project (e.g., escaped defects, automation pass rates)?",
        "expected_answer": "Escaped defects, defect density, automation pass/fail rate, test coverage, defect leakage, mean time to detect/resolve, sprint velocity impact.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_002",
        "question": "How do you differentiate between defect priority and severity?",
        "expected_answer": "Severity is the technical/functional impact of the defect on the system; priority is the business urgency of fixing it. A cosmetic bug can be high priority for a demo but low severity.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_003",
        "question": "How do you decide which tests to automate first?",
        "expected_answer": "Prioritize high-value, repetitive, stable, regression-prone tests using risk-based criteria: business criticality, frequency of execution, stability of the feature, and manual execution cost.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_004",
        "question": "What is your approach to handling 'flaky' automated tests?",
        "expected_answer": "Quarantine the flaky test, investigate root cause (timing/waits, test data, environment), fix or rewrite with proper synchronization, track flakiness rate before re-enabling in the pipeline.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_005",
        "question": "What do you do if a developer delivers a build late in the sprint?",
        "expected_answer": "Communicate risk to the team immediately, re-prioritize testing to focus on critical paths first, negotiate scope or timeline with the Scrum Master/PO, consider carrying over to the next sprint rather than skipping testing.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_006",
        "question": "How do you manage regression testing when sprint cycles are only two weeks long?",
        "expected_answer": "Maintain a prioritized, automated regression suite; run a risk-based subset per sprint rather than the full suite; use CI to run regression continuously rather than only at sprint end.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_007",
        "question": "What if a user story is accepted into a sprint, but the acceptance criteria are vague or missing?",
        "expected_answer": "Raise it during backlog refinement or sprint planning before commitment; if discovered mid-sprint, clarify with the Product Owner immediately and document agreed criteria before testing proceeds.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_008",
        "question": "Can you share an experience where you had to raise a QA impediment?",
        "expected_answer": "STAR-style answer: situation blocking testing (environment down, missing test data, unclear requirements), action taken to escalate/resolve, and the outcome/impact on the sprint.",
        "difficulty": "Advanced",
        "category": "behavioral",
    },
    {
        "id": "qa_proc_009",
        "question": "What is Shift-Left testing, and how have you implemented it in an Agile team?",
        "expected_answer": "Shift-Left means involving QA earlier in the SDLC - reviewing requirements/stories, writing test cases during grooming, pairing with developers on unit/component tests, so defects are caught before code is 'done'.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_010",
        "question": "How do you approach testing when requirements change mid-sprint?",
        "expected_answer": "Reassess impact on already-written test cases and in-progress execution, communicate risk/timeline impact to the team, update test cases to reflect new requirements before continuing execution.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_011",
        "question": "What is continuous testing, and how does it relate to Continuous Integration (CI)?",
        "expected_answer": "Continuous testing runs automated tests at every stage of the pipeline (build, integration, deployment) to get fast feedback; CI triggers these test suites automatically on every commit/merge.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_012",
        "question": "What is a 'Spike' in Agile, and how can QA use it?",
        "expected_answer": "A Spike is a timeboxed research/investigation story used to reduce uncertainty (technical or functional) before committing to full implementation. QA can use spikes to evaluate test tools, feasibility of automation, or unclear requirements.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_013",
        "question": "How do you handle incomplete user stories or late builds at the end of a sprint?",
        "expected_answer": "Flag the risk early, prioritize smoke/critical-path testing over full coverage, recommend not accepting the story if quality can't be verified, and carry over remaining work rather than rubber-stamping it.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_014",
        "question": "How does Agile testing differ from traditional (Waterfall) testing?",
        "expected_answer": "Agile testing is continuous and integrated throughout short iterations with close developer collaboration; Waterfall testing is a distinct phase after development completes, with less flexibility to adapt to change.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_015",
        "question": "What is your role as a QA in the daily stand-up meeting?",
        "expected_answer": "Report testing progress/blockers, flag defects or environment issues affecting the sprint, coordinate with developers on retesting priorities, keep updates concise and focused on impediments.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_016",
        "question": "Can you explain the difference between a Sprint Review and a Sprint Retrospective?",
        "expected_answer": "Sprint Review demonstrates completed work to stakeholders and gathers feedback on the product; Sprint Retrospective is an internal team discussion on how to improve process, collaboration, and ways of working.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_017",
        "question": "How do you estimate testing efforts (e.g., using Planning Poker techniques)?",
        "expected_answer": "Break stories into testable scenarios, factor in complexity/risk/unknowns, use relative estimation techniques like Planning Poker with the team to converge on story points or effort.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_018",
        "question": "What does a flat line in the middle of a sprint burndown chart indicate?",
        "expected_answer": "No work was completed/reported during that period - could indicate a blocker, the team working on a large task without checking in progress, or stories not being updated.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_019",
        "question": "How can a QA use a burndown chart to plan their testing cycle?",
        "expected_answer": "Track how quickly stories move to 'ready for test' to anticipate testing workload distribution, spot bottlenecks early, and avoid a pile-up of testing work at sprint end.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_020",
        "question": "What is the difference between Velocity and Capacity?",
        "expected_answer": "Velocity is the average amount of work (story points) a team historically completes per sprint; capacity is the actual available working time/effort for the upcoming sprint accounting for leave, holidays, etc.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_021",
        "question": "Which metrics do you use to measure the effectiveness of your automation suite?",
        "expected_answer": "Pass/fail rate trend, flakiness rate, execution time, maintenance cost (time to fix failing tests), defect detection rate, and coverage of critical paths.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_022",
        "question": "What is 'Defect Leakage' and how do you calculate it?",
        "expected_answer": "Defects that escape to production/UAT despite testing. Calculated as: (Defects found in production) / (Defects found in production + Defects found in testing) x 100.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_023",
        "question": "What is the difference between Smoke Testing and Sanity Testing?",
        "expected_answer": "Smoke testing is a broad, shallow check that a build is stable enough to test further; sanity testing is a narrow, deeper check that a specific fix/feature works as expected after a change.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_024",
        "question": "How do you execute Regression Testing within a tight 2-week sprint?",
        "expected_answer": "Rely on an automated regression suite run continuously in CI, prioritize a risk-based subset for manual spot checks, and avoid manually re-running the entire suite every sprint.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_025",
        "question": "What is Exploratory Testing, and why is it vital in Agile?",
        "expected_answer": "Simultaneous learning, test design, and execution without predefined scripts - critical in Agile because requirements and time are limited, and it uncovers issues scripted tests miss.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_026",
        "question": "Can you explain the Testing Pyramid and how you apply it?",
        "expected_answer": "A large base of fast unit tests, a smaller layer of integration/API tests, and a thin top layer of slow UI/end-to-end tests - balances speed, cost, and confidence in the test suite.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_027",
        "question": "What is Risk-Based Testing, and how do you prioritize test cases under it?",
        "expected_answer": "Focus testing effort on areas with the highest probability of failure and highest business impact, prioritizing critical-path and high-risk features over low-impact edge cases when time is constrained.",
        "difficulty": "Intermediate",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_028",
        "question": "A developer says, 'It works on my machine.' How do you respond?",
        "expected_answer": "Investigate environment differences (config, data, dependencies, OS), reproduce with exact steps and logs/screenshots, push for a shared/consistent environment (containers) to eliminate this class of issue.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_029",
        "question": "The Product Owner wants to release a feature with a known high-severity bug. What do you do?",
        "expected_answer": "Clearly communicate the risk and impact with data/evidence, document the decision and get explicit sign-off if they proceed, propose a mitigation (feature flag, hotfix plan) rather than silently agreeing or blocking unilaterally.",
        "difficulty": "Advanced",
        "category": "scenario",
    },
    {
        "id": "qa_proc_030",
        "question": "How do you handle a situation where developers constantly deliver code on the last day of the sprint?",
        "expected_answer": "Raise it as a process issue in retrospective, propose earlier code-complete deadlines or mid-sprint check-ins, advocate for smaller stories that can be delivered and tested incrementally.",
        "difficulty": "Advanced",
        "category": "scenario",
    },
    {
        "id": "qa_proc_031",
        "question": "What do you do if you find a major bug 2 hours before a production deployment?",
        "expected_answer": "Immediately report with severity/impact and reproduction steps, recommend hold vs. go decision to the team with evidence, evaluate hotfix/rollback feasibility rather than staying silent to avoid delaying release.",
        "difficulty": "Advanced",
        "category": "scenario",
    },
    {
        "id": "qa_proc_032",
        "question": "If a user story has zero acceptance criteria, would you still test it? How would you approach it?",
        "expected_answer": "Push back during refinement to get criteria defined; if forced to test anyway, derive implicit criteria from the story description, related stories, and stakeholder conversation, and document assumptions explicitly before testing.",
        "difficulty": "Advanced",
        "category": "scenario",
    },
    {
        "id": "qa_proc_033",
        "question": "How do you write effective bug reports that developers can act on without back-and-forth?",
        "expected_answer": "Clear title, exact reproduction steps, expected vs actual result, environment/build details, severity, screenshots/logs, and isolating the minimal steps to reproduce.",
        "difficulty": "Basic",
        "category": "fundamentals",
    },
    {
        "id": "qa_proc_034",
        "question": "How do you balance manual exploratory testing against automated test execution in a sprint?",
        "expected_answer": "Automate stable, repetitive regression scenarios to free up time; use manual/exploratory testing for new features, usability, and edge cases automation can't easily cover.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
    {
        "id": "qa_proc_035",
        "question": "Two team members disagree on whether a behavior is a bug or works as designed. How do you resolve it?",
        "expected_answer": "Refer back to the acceptance criteria/requirements documentation as the source of truth; if ambiguous, get clarification from the Product Owner rather than the team debating opinions.",
        "difficulty": "Intermediate",
        "category": "scenario",
    },
]


def get_qa_process_questions(count: int) -> List[Dict]:
    """Select `count` random QA process questions for the interview."""
    pool = random.sample(
        QA_PROCESS_QUESTIONS, min(count, len(QA_PROCESS_QUESTIONS))
    )

    questions = []
    for q in pool:
        questions.append({
            "id": q["id"],
            "question": q["question"],
            "expected_answer": q["expected_answer"],
            "section": "QA Process",
            "difficulty": q["difficulty"],
            "category": q["category"],
        })
    return questions
