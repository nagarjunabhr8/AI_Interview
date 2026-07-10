#!/usr/bin/env python3
"""
Diagnostic script to identify Phase 1 errors
"""

import sys
import json

print("\n" + "="*70)
print("PHASE 1 ERROR DIAGNOSTIC")
print("="*70)

# Test 1: Import checks
print("\n1. Checking imports...")
try:
    from integrated_question_system import get_question_system
    print("   OK: integrated_question_system")
except Exception as e:
    print(f"   ERROR: integrated_question_system - {e}")
    sys.exit(1)

try:
    from dynamic_question_generator import DynamicQuestionGenerator
    print("   OK: dynamic_question_generator")
except Exception as e:
    print(f"   ERROR: dynamic_question_generator - {e}")
    sys.exit(1)

try:
    from interview_session import InterviewSession
    print("   OK: interview_session")
except Exception as e:
    print(f"   ERROR: interview_session - {e}")
    sys.exit(1)

# Test 2: Initialize question system
print("\n2. Initializing question system...")
try:
    system = get_question_system()
    print("   OK: Question system initialized")
except Exception as e:
    print(f"   ERROR: {e}")
    sys.exit(1)

# Test 3: Generate questions
print("\n3. Testing question generation...")
try:
    questions = system.get_interview_questions(
        role='Senior QA Engineer',
        skills=['java', 'playwright'],
        years_of_experience=8.5,
        difficulty='Hard',
        session_id='test_session',
        include_previous=False,
        count=25
    )
    print(f"   OK: Generated {len(questions)} questions")
    if questions:
        q = questions[0]
        print(f"   Sample: {q.get('question', 'N/A')[:60]}...")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Create interview session
print("\n4. Testing interview session...")
try:
    candidate_data = {
        'role': 'Senior QA Engineer',
        'primary_skills': ['java', 'playwright'],
        'years_of_experience': 8.5,
        'difficulty_level': 'Hard',
        'resume': None,
        'self_ratings': {},
        'timestamp': '2026-07-10T00:00:00'
    }
    session = InterviewSession(candidate_data, questions[:5])
    session.start_session()
    print("   OK: Interview session created and started")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Web app route simulation
print("\n5. Testing web app routes...")
try:
    from web_app import app
    client = app.test_client()

    # Phase 0
    resp = client.post('/phase0', json={
        'role': 'Senior QA Engineer',
        'skills': 'Java, Playwright',
        'experience': '8',
        'difficulty': 'Hard'
    })
    if resp.status_code == 200:
        print("   OK: Phase 0 route working")
    else:
        print(f"   ERROR: Phase 0 returned {resp.status_code}")
        print(f"   Response: {resp.get_data(as_text=True)[:200]}")
        sys.exit(1)

    # Phase 1 init
    resp = client.post('/phase1', json={'action': 'init'})
    if resp.status_code == 200:
        data = resp.get_json()
        if 'success' in data and data['success']:
            print("   OK: Phase 1 init route working")
            print(f"   Generated questions: {data.get('total_questions')}")
        else:
            print(f"   ERROR: Phase 1 returned error - {data.get('error')}")
            sys.exit(1)
    else:
        print(f"   ERROR: Phase 1 returned {resp.status_code}")
        print(f"   Content-Type: {resp.content_type}")
        print(f"   Response: {resp.get_data(as_text=True)[:500]}")
        sys.exit(1)

except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*70)
print("ALL DIAGNOSTICS PASSED")
print("="*70)
print("\nSystem Status: READY")
print("\nTo use the system:")
print("  1. Run: python web_app.py")
print("  2. Open: http://localhost:5000")
print("  3. Complete Phase 0 (intake form)")
print("  4. Click 'Start Interview' to begin Phase 1")
print("\n" + "="*70 + "\n")
