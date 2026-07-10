# AI Interview Panelist — Interview Agent

A comprehensive interview simulation system that conducts realistic, structured mock interviews for technical roles.

## Project Structure

```
InterviewAgent/
├── AI_Agent.md              # Full specification & rubrics
├── phase0_intake.py         # PHASE 0: Candidate intake
├── README.md                # This file
└── candidate_intake.json    # Candidate data (generated after Phase 0)
```

## PHASE 0 — INTAKE (Implemented ✓)

Collects essential information from the candidate before the interview begins.

### Running PHASE 0

```bash
python phase0_intake.py
```

### What PHASE 0 Collects

**Required:**
1. **Target Role** — e.g., QA Engineer, Senior QA Engineer, SDET, Backend Developer, etc.
2. **Primary Skill Set(s)** — At least one required (e.g., Playwright, Java, Python, Selenium)
3. **Years of Experience** — Numeric value (e.g., 5, 9.5, 0.5)
4. **Interview Difficulty Level** — Fresher, Basic, Simple, or Hard

**Optional:**
5. **Resume** — Paste text for parsing skills, achievements, and project domains
6. **Self-Ratings** — Rate proficiency (1-5) for each primary skill and framework design (if applicable)

### Output

After successful intake, a `candidate_intake.json` file is created containing all collected data. This is used as input for Phase 1 (interview execution).

### Intake Features

- ✓ Conversational (not a rigid form)
- ✓ Validation at each step
- ✓ Helpful examples and guidance
- ✓ Summary confirmation before proceeding
- ✓ Resume parsing (optional)
- ✓ Self-rating calibration based on experience level
- ✓ Data persistence (JSON export)

---

## PHASE 1 — Interview Execution (Implemented ✓)

Conducts the actual technical interview with sequential, topic-by-topic questions.

### Running PHASE 1

```bash
python phase1_interview.py
```

### What PHASE 1 Does

**Question Delivery:**
- 15-30 questions (scaled to difficulty and experience level)
- Sequential flow by topic (fundamentals → domain-specific → coding → tools → leadership)
- One question at a time
- Up to 2 minutes per answer

**Interview Management:**
- Tracks elapsed time and progress
- Shows progress updates every 5 questions
- Handles skipped/timeout answers gracefully
- Maintains neutral, professional tone
- Silent scoring (no feedback during interview)

**Question Coverage (dynamically selected):**
- Warm-up / Introduction
- Core Domain Fundamentals (SDLC/STLC, QA process for QA roles)
- Testing Types & Methodologies
- Test Planning & Strategy (QA) or Fundamentals (Backend)
- Programming Language (1-2 live coding problems, scaled to skill rating)
- Automation Tool Deep-Dive (Playwright, Selenium, RestAssured, Cypress, etc.)
- Framework Design & Architecture (for Senior/Lead roles)
- CI/CD & DevOps Integration
- Leadership & Program Management (Senior/Lead roles)
- Closing Scenario Question

**Output:**
- `interview_session.json` containing all responses, timing, and hidden scoring
- Ready for Phase 2 analysis

---

## PHASE 2 — Scoring & Analysis (Implemented ✓)

Automatically evaluates all responses and produces comprehensive scoring analysis.

### Running PHASE 2

```bash
python phase2_scoring.py
```

### What PHASE 2 Does

**Response Scoring:**
- Each response scored 0-5 using detailed, question-specific rubrics
- Evaluates correctness, depth, examples, and trade-offs
- Assigns scoring rationale for each answer

**Dimension Ratings (1-5 scale):**
- Technical Depth — mastery of core concepts
- Problem-Solving / Coding Ability — algorithmic thinking, code quality
- Communication Clarity — structure, conciseness, explanation quality
- Confidence & Composure — certainty, pacing, handling difficult questions
- Self-Awareness — honesty of self-assessment vs actual performance
- Leadership & Judgment — (if applicable for Senior/Lead roles)

**Section-wise Performance:**
- Average score per topic section (fundamentals, tools, coding, etc.)
- Performance level classification (Excellent/Strong/Adequate/Weak/Poor)

**Overall Score & Verdict:**
- Weighted overall score (0-100)
- Hiring verdict: Strong Hire / Hire / Hire w/ Reservations / No Hire
- Scoring weights: Technical 50%, Coding 20%, Communication 30% (or 40/20/15/25 for leads)

**Summary Analysis:**
- Top 3-5 strengths (with evidence)
- Top 3-5 improvement areas (with specifics)
- Recommendation based on overall performance

### Output

**`scored_session.json`** containing:
- All responses with assigned scores (0-5)
- Section-wise performance breakdown
- Dimension scores
- Overall score and verdict
- Summary statistics
- Ready for Phase 3 report generation

---

## PHASE 3 — Final Report Generation (Implemented ✓)

Generates professional, comprehensive written interview reports in multiple formats.

### Running PHASE 3

```bash
python phase3_report.py
```

### What PHASE 3 Generates

**Two Professional Report Formats:**
1. **Markdown Report** (`interview_report.md`) — Text format, easy to share
2. **HTML Report** (`interview_report.html`) — Professional styling, print-to-PDF ready

**Report Contents:**
- Candidate summary (role, experience, skills, difficulty)
- Overall score (0-100) and hiring verdict
- Performance dimensions table (6 dimensions, 1-5 scale)
- Question-by-question transcript with scores and rationale
- Section-wise performance breakdown (ranked by performance)
- Key strengths (3-5 evidence-based)
- Areas for improvement (3-5 specific, actionable)
- Communication & presentation feedback
- Recommended study plan (prioritized by weakness)
- Suggested re-attempt difficulty level
- Timeline and resources for preparation

### Output Files

- `interview_report.md` — Clean Markdown text format
- `interview_report.html` — Professional HTML with styling, print-to-PDF capable

### Key Features

✓ Professional formatting with tables and clear hierarchy  
✓ Color-coded performance indicators  
✓ Complete Q&A transcript with expected answers  
✓ Evidence-based strengths and weaknesses  
✓ Actionable improvement guidance  
✓ Print-friendly design with page breaks  
✓ Suitable for personal development or sharing with stakeholders  

---

## Configuration

Edit `AI_Agent.md` to adjust:
- Valid roles and skill sets
- Question banks per role/tool
- Scoring rubrics
- Report templates

---

## Development Notes

This is a **modular, role-agnostic** system:
- Adapts question depth to self-rated skill levels
- Handles QA, Backend, DevOps, Data, and other technical roles
- Scales difficulty from Fresher to Hard
- Framework/tool-agnostic (Playwright, Selenium, RestAssured, etc.)
