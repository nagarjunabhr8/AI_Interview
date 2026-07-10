# Test Guide: Verify Different Questions on Each Interview

## ✅ Web App is Running Fresh!

**Status:** Server active on port 5000  
**All caches cleared:** YES  
**Question bank:** ExpandedQuestionBank (150+ questions, randomized)

---

## 🧪 Test Procedure

Follow these exact steps to verify different questions appear:

### **Test 1: Run First Interview**

1. Open browser: `http://localhost:5000`
2. Click "Start Interview"
3. Fill out Phase 0 (intake form):
   - Role: "Senior QA Engineer"
   - Skills: "Playwright, Java, Python"
   - Experience: "8"
   - Difficulty: "Hard"
   - Click continue

4. Click "Start Interview" button

5. **IMPORTANT: Take Note of the Questions**
   - Read the first 5 questions carefully
   - Write down the first question exactly
   - Example: "Walk me through your background..." or "Tell me about your most significant project..."

6. Answer 3-5 questions (doesn't matter what you answer)

7. Skip remaining questions (click "Skip Question")

8. Go through Phase 2 and Phase 3 (scoring and reports)

**SAVE: Note the first question from Interview 1**

---

### **Test 2: Run Second Interview (Different Browser Tab)**

1. Open a NEW browser tab or window
2. Go to: `http://localhost:5000`
3. Click "Start Interview"
4. Fill out Phase 0 with SAME information:
   - Role: "Senior QA Engineer"
   - Skills: "Playwright, Java, Python"  
   - Experience: "8"
   - Difficulty: "Hard"

5. Click "Start Interview"

6. **COMPARE: Check if first question is DIFFERENT**
   - Is the first question different from Interview 1?
   - If YES: ✅ System is working!
   - If NO: See troubleshooting below

7. Look at the first 5-10 questions

8. You should notice DIFFERENT questions compared to Interview 1

---

### **Test 3: Run Third Interview (Further Confirmation)**

Repeat Test 2 again to confirm even more variety

---

## ✅ Expected Results

### Interview 1 First Questions Might Be:
```
1. "Walk me through your background and current role..."
2. "What is the difference between SDLC and STLC?"
3. "Explain Smoke, Sanity, and Regression testing..."
4. "How do you estimate testing effort..."
5. "Write a function to reverse a string..."
```

### Interview 2 First Questions Should Be:
```
1. "Tell me about your most significant project..."  (DIFFERENT)
2. "Explain the testing activities in different SDLC phases..." (DIFFERENT)
3. "When would you use Integration vs System vs UAT testing..." (DIFFERENT)
4. "How do you prioritize when time is limited..." (DIFFERENT)
5. "Find the missing number in an array..." (DIFFERENT)
```

### Interview 3 Should Be:
```
1. "What are your career goals for the next 3-5 years?" (DIFFERENT AGAIN)
2. "Describe the V-model in software testing..." (NEW)
3. "Explain API testing vs UI testing..." (NEW)
4. And so on...
```

---

## 🔍 What to Look For

### ✅ Signs It's Working
- Question wording is **completely different** each interview
- Questions cover the **same topics** but from different angles
- Some questions appear in one but not the other
- Structure changes (different order of topics)

### ❌ Signs It's NOT Working
- Exact same questions in same order
- Verbatim wording repeats
- All 18-20 questions are identical

---

## 🛠️ Troubleshooting

### If Still Seeing Same Questions:

#### Option 1: Hard Browser Refresh
```
Ctrl + Shift + Delete  (Clear all cache and cookies)
Then close ALL browser tabs to localhost:5000
Open fresh: http://localhost:5000
```

#### Option 2: Try Different Browser
- Try Chrome, Firefox, Edge, or Safari
- Use Private/Incognito mode
- This rules out browser caching issues

#### Option 3: Verify Expanded Question Bank is Loaded
Run this in PowerShell:
```powershell
cd d:\AutomationEdge\InterviewAgent
python -c "from question_bank_expanded import ExpandedQuestionBank; qb = ExpandedQuestionBank('Senior QA Engineer', 'Hard', ['Playwright'], 8, {}); print(f'Total questions available: {len(qb.all_questions)}'); questions = qb.get_questions_for_interview(); print(f'Questions for this interview: {[q[\"question\"][:50] for q in questions[:3]]}')"
```

This will show if the expanded question bank has 150+ questions.

#### Option 4: Restart Everything
```powershell
# Stop the server (if running)
Ctrl + C  (in PowerShell window)

# Kill any remaining Python
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Clear cache
cd d:\AutomationEdge\InterviewAgent
Get-ChildItem -Recurse -Filter "__pycache__" -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force

# Start fresh
python web_app.py
```

---

## 📊 Question Pool Information

Current question pool should have:
- **Total questions:** 150+
- **Hard difficulty questions:** 80+
- **Possible question sets:** Thousands
- **Questions per interview:** 25-30

This means:
- Very unlikely to see repeats
- Each interview should be unique
- High diversity of topics

---

## 📝 Example Test Results

### Good Results
```
Interview 1 Questions:
1. Walk me through your background...
2. What is the difference between SDLC and STLC...
3. Explain the difference between Verification and Validation...

Interview 2 Questions:
1. Tell me about your most significant project...
2. Explain the testing activities in different SDLC phases...
3. What is the difference between Functional and Non-Functional testing...

Status: ✅ DIFFERENT - System working correctly!
```

### Bad Results
```
Interview 1 Questions:
1. Walk me through your background...
2. What is the difference between SDLC and STLC...
3. Explain the difference between Verification and Validation...

Interview 2 Questions:
1. Walk me through your background...  (SAME!)
2. What is the difference between SDLC and STLC...  (SAME!)
3. Explain the difference between Verification and Validation...  (SAME!)

Status: ❌ SAME - System not working, see troubleshooting
```

---

## 🎯 Quick Checklist

- [ ] Web app is running (http://localhost:5000 works)
- [ ] Completed Interview 1, noted first question
- [ ] Completed Interview 2, noted first question
- [ ] First question is **DIFFERENT** between interviews
- [ ] Multiple questions are different
- [ ] Confusion, topics covered are similar but questions are different

---

## 📞 Still Having Issues?

If you're STILL seeing the same 18 questions exactly:

1. **Take a screenshot** of the questions from both interviews
2. **Check browser console** (F12 → Console tab) for any errors
3. **Verify file dates**: 
   - question_bank_expanded.py should exist and be recent
   - web_app.py should have recent timestamp
4. **Check process ID**: Should be a new Python process each time

---

## ✅ Expected Outcome

After running this test, you should see:
- ✅ Each interview has different questions
- ✅ Topics are similar but questions vary
- ✅ No repetition across interviews
- ✅ Random selection is working
- ✅ System is functioning correctly

**Run the test now and report back!** Let me know if questions are different or still the same. 🚀
