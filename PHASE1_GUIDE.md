# PHASE 1 — Interview Execution Guide

## Quick Start

After completing PHASE 0 intake, run the interview:

```bash
python phase1_interview.py
```

## What to Expect

### Duration
- **45 minutes** (simulated, not real-time)
- Questions scaled to your difficulty level and experience

### Question Count
- **Fresher/Basic:** 15-20 questions
- **Simple:** 20-25 questions  
- **Hard:** 25-30 questions

### Interview Flow

```
1. Introduction & Warm-up (1 question)
   ↓
2. Domain Fundamentals (2-3 questions)
   - SDLC/STLC, QA process, definitions
   ↓
3. Testing Types & Methodologies (2-3 questions)
   - Smoke vs Sanity, Functional vs Non-functional, etc.
   ↓
4. Test Planning & Strategy (1-2 questions)
   - Risk-based prioritization, estimation
   ↓
5. Programming Language & Coding (2-3 questions)
   - Conceptual + 1-2 live coding problems
   ↓
6. Automation Tools (2-3 questions)
   - Playwright, Selenium, RestAssured, etc.
   ↓
7. Framework Design & CI/CD (1-2 questions)
   - Architecture, scaling, DevOps integration
   ↓
8. Leadership (if applicable) (1-2 questions)
   - Team dynamics, mentoring, conflict resolution
   ↓
9. Closing Scenario (1 question)
```

## Answering Questions

### Format
- I'll ask **one question at a time**
- You have up to **2 minutes** to answer
- Type your response and press Enter twice when done
- Or type `skip` / `pass` / `next` to skip a question

### Tips
- **Be thorough but concise.** 2-3 minutes is ideal.
- **Explain your reasoning.** Show your thought process.
- **Use examples** when possible (real projects, scenarios).
- **For coding questions:** Explain your approach before/while coding.
- **If you don't know:** It's okay to say "I don't know" or "skip" — better than guessing.

### Progress Tracking
- Every 5 questions, I'll show progress: questions answered, time elapsed
- You can see remaining time for the interview

## Scoring (Silent)

I'm scoring silently during the interview:
- **0** = No answer / skipped
- **1** = Attempted but fundamentally incorrect
- **2** = Partially correct, major gaps
- **3** = Correct core concept, minor gaps
- **4** = Correct, well-explained, minor gaps
- **5** = Correct, precise, includes nuance and real-world trade-offs

**No feedback or scoring is shared during the interview.**

## After the Interview

Your responses and scoring are saved to `interview_session.json`.

Next step: Run **PHASE 2** to generate your detailed report with:
- Per-question scores and rationale
- Strengths and improvement areas
- Overall score /100 and hiring verdict
- Recommended resources and next steps

```bash
python phase2_scoring.py
```

---

## Example Question Flow

```
Q1: Walk me through your background and current role.
→ You answer (2-3 min)
→ ✓ Got it. Next question.

Q2: What is the difference between SDLC and STLC?
→ You answer (1-2 min)
→ ✓ Got it. Next question.

...

Q6: Write a function to reverse a string. Explain your approach.
→ You explain your approach first
→ Then write code
→ ✓ Got it. Next question.

...

📊 Progress: 5/20 answered | 15.2 min elapsed

Q15: Describe your testing strategy for a critical payment feature in 2 days.
→ You answer (2-3 min)
→ ✓ Got it. Next question.

...

INTERVIEW COMPLETE
Questions Asked: 20
Questions Answered: 18
Questions Skipped: 2
Total Time: 44.5 minutes
```

---

## Troubleshooting

### "I need to go back to a previous question"
- Not possible during the interview (sequential flow).
- Review and revise in the final report (Phase 3).

### "I forgot what I was going to say"
- You can ask me to repeat the question.
- I'll clarify once, briefly.

### "I want to change my answer to Q5"
- Not possible during the interview.
- You can note this in the final report or for discussion after.

### "I'm running out of time"
- Interview runs for ~45 minutes.
- If time is up, I'll notify and we'll wrap up.
- Remaining questions will be marked as skipped.

---

## Best Practices

✓ **Do:**
- Read the question carefully before answering
- Think for a few seconds before speaking
- Provide specific examples
- Explain trade-offs and considerations
- Admit when you don't know something

✗ **Don't:**
- Rush through answers
- Give vague, generic responses
- Overstate your expertise
- Ramble without structure
- Get defensive if unsure

---

## Ready?

Start the interview anytime:

```bash
python phase1_interview.py
```

Good luck! 🚀
