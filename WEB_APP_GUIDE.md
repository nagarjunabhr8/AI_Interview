# Web Application Guide — AI Interview Panelist

## 🚀 Server Status: RUNNING ✅

**Application:** AI Interview Panelist Web Application  
**Status:** Active and Running  
**Port:** 5000  
**Process ID:** 32880  

---

## 🌐 Access Your Application

### From Your Local Computer
Open your web browser and navigate to:

```
http://localhost:5000
```

### From Another Computer on Your Network
```
http://192.168.0.108:5000
```

### From Internet (if exposed)
```
http://<your-ip-address>:5000
```

---

## 📋 Complete Interview Workflow

### Step 1: Home Page
- **URL:** `http://localhost:5000`
- **What you'll see:** Welcome page with features overview
- **Action:** Click "🚀 Start Interview" button

### Step 2: Phase 0 - Intake
- **URL:** `http://localhost:5000/phase0`
- **What you do:**
  1. Select your target role (e.g., Senior QA Engineer)
  2. Enter primary skills (comma-separated, e.g., Playwright, Java, Python)
  3. Enter years of experience (e.g., 8.5)
  4. Select difficulty level (Fresher, Basic, Simple, or Hard)
  5. (Optional) Paste your resume
  6. Rate your skills (1-5 scale)
  7. Click "Continue to Interview"

### Step 3: Phase 1 - Interview
- **URL:** `http://localhost:5000/phase1`
- **What you do:**
  1. Click "Start Interview" to begin
  2. Read each question carefully
  3. Type your answer (up to 2 minutes per question)
  4. Click "Submit Answer" to move to next question
  5. Or click "Skip Question" if you need to pass
  6. Answer all questions (or skip as needed)
  7. Auto-advances to Phase 2 when complete

### Step 4: Phase 2 - Scoring (Automatic)
- **URL:** `http://localhost:5000/phase2/<session_id>`
- **What happens:**
  - System automatically scores your responses
  - Evaluates 6 dimensions (technical, communication, coding, etc.)
  - Calculates overall score (0-100)
  - Determines hiring verdict
  - Auto-advances to Phase 3

### Step 5: Phase 3 - Reports
- **URL:** `http://localhost:5000/phase3/<session_id>`
- **What you see:**
  - Overall score and verdict
  - Performance dimensions (6-scale breakdown)
  - Section-wise performance (with rankings)
  - Strengths and weaknesses identified
  - Full transcript (markdown format)
  - Professional HTML report

**Download Options:**
- Download Markdown report (text format)
- Download HTML report (professional format, print to PDF)
- Start New Interview (go back to Phase 0)

---

## 💡 Testing Scenarios

### Test 1: Quick Run (3-5 minutes)
1. Go to Phase 0
2. Select: Senior QA Engineer, Playwright/Java, 8.5 yrs, Hard
3. Go to Phase 1
4. Answer 2-3 questions briefly
5. Skip remaining questions
6. See automatic scoring and report

### Test 2: Full Interview (30-45 minutes)
1. Complete all phases with full answers
2. Practice realistic interview scenario
3. Review detailed feedback and recommendations

### Test 3: Multiple Interviews
1. Run Phase 0-3 for different roles
2. Compare different difficulty levels
3. See how scores vary by role and difficulty

---

## 🎯 Features to Test

- ✅ **Responsive Design** — Works on desktop, tablet, mobile
- ✅ **Role Adaptation** — Different questions for different roles
- ✅ **Difficulty Scaling** — Questions scale to your level
- ✅ **Smart Scoring** — Intelligent evaluation of responses
- ✅ **Real-time Progress** — See your progress as you answer
- ✅ **Professional Reports** — Markdown and HTML formats
- ✅ **Print to PDF** — Print HTML report as PDF for sharing
- ✅ **Session Management** — Multiple independent sessions
- ✅ **Error Handling** — Graceful error messages
- ✅ **Mobile Friendly** — Works on all devices

---

## 📊 Key Sections to Test

### Phase 0 Tests
- Test role selection dropdown
- Test skill input (comma-separated)
- Test experience number input
- Test difficulty selection
- Test skill rating inputs (should appear after skills entered)
- Test form validation (required fields)
- Test form submission

### Phase 1 Tests
- Test question display
- Test answer input
- Test timer functionality
- Test progress bar
- Test skip functionality
- Test submit functionality
- Test question navigation
- Test elapsed time tracking

### Phase 2 Tests
- Test automatic scoring progress
- Test step-by-step visualization
- Test smooth transition to Phase 3

### Phase 3 Tests
- Test score card display
- Test dimension cards (should show 6 dimensions)
- Test performance table
- Test tab switching (Markdown ↔ HTML)
- Test Markdown report formatting
- Test HTML report rendering in iframe
- Test download buttons
- Test "Start New Interview" button

---

## 🛠️ Troubleshooting

### Page doesn't load
- **Problem:** Cannot access localhost:5000
- **Solution:** 
  1. Check if Flask is running (should see "Running on..." message)
  2. Make sure port 5000 is not in use
  3. Try refreshing the page (F5)

### Forms not submitting
- **Problem:** "Submit" button doesn't work
- **Solution:**
  1. Check browser console for errors (F12)
  2. Make sure all required fields are filled
  3. Try a different browser
  4. Clear browser cache and cookies

### Reports not displaying
- **Problem:** Reports appear blank
- **Solution:**
  1. Refresh the page
  2. Try the HTML view vs Markdown view
  3. Check that you completed Phase 1 with responses

### Scoring seems wrong
- **Problem:** Scores don't match expectations
- **Solution:**
  1. This is expected - scoring is based on actual content analysis
  2. Review the scoring rationale for each question
  3. Re-answer with different content to see different scores

---

## 📝 Browser Recommendations

- **Chrome:** Fully supported ✅
- **Firefox:** Fully supported ✅
- **Safari:** Fully supported ✅
- **Edge:** Fully supported ✅
- **Mobile Safari:** Fully supported ✅
- **Mobile Chrome:** Fully supported ✅

---

## 🔧 Advanced Features

### Session Persistence
- Each interview creates a unique session ID
- Session data stored in memory during server uptime
- Can access reports multiple times

### Report Export
- Markdown format for text editors
- HTML format for professional presentation
- Print to PDF directly from browser

### Multi-user Testing
- Multiple users can run interviews simultaneously
- Each gets their own session
- No interference between sessions

---

## 🎓 Sample Test Inputs

### For Quick Testing:
```
Role: QA Engineer
Skills: Playwright, Java
Experience: 5
Difficulty: Simple
```

### For Comprehensive Testing:
```
Role: Senior QA Engineer
Skills: Playwright, Java, Python, Selenium
Experience: 8.5
Difficulty: Hard
Resume: (paste a sample resume)
```

### For Leadership Role Testing:
```
Role: Lead QA Engineer
Skills: Playwright, Python
Experience: 12
Difficulty: Hard
```

---

## 📞 Support

If you encounter issues:

1. **Check the console** (F12 in browser)
2. **Verify server is running** (check PowerShell output)
3. **Try a different browser**
4. **Clear cache and cookies**
5. **Refresh the page**
6. **Restart the server** (Ctrl+C and run web_app.py again)

---

## ✅ Ready to Test!

Your AI Interview Panelist web application is fully functional and ready for comprehensive testing.

**Start your first interview:**
```
http://localhost:5000
```

Enjoy your testing! 🚀
