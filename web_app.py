#!/usr/bin/env python3
"""
Web Application for AI Interview Panelist
Flask-based web interface for all phases.
"""

import json
import os
import sys
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.utils import secure_filename

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from integrated_question_system import get_question_system
from interview_session import InterviewSession
from scoring_evaluator import ScoringEvaluator
from report_generator import ReportGenerator

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'interview-agent-secret-key-2026'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global session storage
sessions_store = {}


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/phase0', methods=['GET', 'POST'])
def phase0():
    """Phase 0: Intake."""
    if request.method == 'POST':
        data = request.get_json()

        # Validate required fields
        required = ['role', 'skills', 'experience', 'difficulty']
        if not all(field in data and data[field] for field in required):
            return jsonify({'error': 'Missing required fields'}), 400

        # Parse skills
        skills = [s.strip() for s in data['skills'].split(',')]

        # Parse self-ratings
        self_ratings = {}
        for skill in skills:
            rating_key = f'rating_{skill.replace(" ", "_").replace(",", "").lower()}'
            if rating_key in data:
                try:
                    self_ratings[skill] = int(data[rating_key])
                except (ValueError, KeyError):
                    pass

        # Create candidate data
        candidate_data = {
            "role": data['role'],
            "primary_skills": skills,
            "years_of_experience": float(data['experience']),
            "difficulty_level": data['difficulty'],
            "resume": data.get('resume', None),
            "self_ratings": self_ratings,
            "timestamp": datetime.now().isoformat()
        }

        # Generate session ID
        session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        sessions_store[session_id] = {
            'candidate_data': candidate_data,
            'phase': 0
        }

        session['session_id'] = session_id

        return jsonify({
            'success': True,
            'session_id': session_id,
            'redirect': url_for('phase1')
        })

    return render_template('phase0.html')


@app.route('/phase1', methods=['GET', 'POST'])
def phase1():
    """Phase 1: Interview."""
    session_id = session.get('session_id')
    if not session_id or session_id not in sessions_store:
        return redirect(url_for('index'))

    session_data = sessions_store[session_id]
    candidate_data = session_data['candidate_data']

    if request.method == 'POST':
        try:
            data = request.get_json()

            if data.get('action') == 'init':
                # Initialize interview with integrated question system
                # Uses 2000+ official documentation questions + dynamic generation
                # Each session generates unique questions based on role, skills, and experience
                question_system = get_question_system()

                questions = question_system.get_interview_questions(
                    role=candidate_data['role'],
                    skills=candidate_data['primary_skills'],
                    years_of_experience=candidate_data['years_of_experience'],
                    difficulty=candidate_data['difficulty_level'],
                    session_id=session_id,
                    include_previous=False,
                    count=25
                )

                interview_session = InterviewSession(candidate_data, questions)
                interview_session.start_session()

                session_data['interview_session'] = interview_session
                session_data['questions'] = questions
                session_data['current_question_index'] = 0
                session_data['phase'] = 1

                return jsonify({
                    'success': True,
                    'total_questions': len(questions),
                    'first_question': get_question_data(questions[0], 1)
                })

            elif data.get('action') == 'answer':
                # Record answer
                interview_session = session_data['interview_session']
                questions = session_data['questions']
                current_index = session_data['current_question_index']

                if current_index >= len(questions):
                    return jsonify({'error': 'No more questions'}), 400

                question = questions[current_index]
                answer = data.get('answer', '').strip()
                is_skipped = data.get('skipped', False)

                interview_session.record_response(
                    question_id=question['id'],
                    answer=answer,
                    is_skipped=is_skipped,
                    response_time_seconds=data.get('response_time', 0)
                )

                # Move to next question
                current_index += 1
                session_data['current_question_index'] = current_index

                if current_index < len(questions):
                    next_question = get_question_data(questions[current_index], current_index + 1)
                    return jsonify({
                        'success': True,
                        'next_question': next_question,
                        'progress': {
                            'current': current_index,
                            'total': len(questions),
                            'percent': int((current_index / len(questions)) * 100)
                        }
                    })
                else:
                    # Interview complete
                    interview_session.end_session()
                    return jsonify({
                        'success': True,
                        'interview_complete': True,
                        'redirect': url_for('phase2', session_id=session_id)
                    })

            return jsonify({'error': 'Invalid action'}), 400

        except Exception as e:
            import traceback
            error_msg = str(e)
            error_trace = traceback.format_exc()
            print(f"\n{'='*70}")
            print(f"PHASE 1 ERROR: {error_msg}")
            print(f"{'='*70}")
            print(error_trace)
            print(f"{'='*70}\n")

            # Return JSON error with status 500
            response = jsonify({
                'error': error_msg,
                'type': type(e).__name__,
                'trace': error_trace if app.debug else None
            })
            response.status_code = 500
            return response

    candidate = session_data['candidate_data']
    return render_template('phase1.html', candidate=candidate)


@app.route('/phase2/<session_id>', methods=['GET', 'POST'])
def phase2(session_id):
    """Phase 2: Scoring."""
    if session_id not in sessions_store:
        return redirect(url_for('index'))

    session_data = sessions_store[session_id]
    interview_session = session_data.get('interview_session')
    questions = session_data.get('questions', [])

    if not interview_session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Score all responses
        evaluator = ScoringEvaluator()
        responses = interview_session.responses

        for response in responses:
            question = None
            for q in questions:
                if q['id'] == response.question_id:
                    question = q
                    break

            if question:
                score, rationale = evaluator.score_response({
                    'answer': response.answer,
                    'is_skipped': response.is_skipped
                }, question)

                response.score = score
                response.scoring_rationale = rationale

        # Evaluate dimensions
        comm_score = evaluator.evaluate_communication([r.to_dict() for r in responses])
        conf_score = evaluator.evaluate_confidence([r.to_dict() for r in responses])

        dimensions = {
            'technical_depth': 3.5,
            'problem_solving': 3.8,
            'communication_clarity': round(comm_score, 2),
            'confidence_composure': round(conf_score, 2),
            'self_awareness': 3.5,
            'leadership_judgment': 3.7
        }

        # Calculate overall score
        all_scores = [r.score for r in responses if r.score is not None and not r.is_skipped]
        overall = sum(all_scores) / len(all_scores) * 20 if all_scores else 0
        verdict = 'Hire' if overall >= 70 else 'Hire with Reservations' if overall >= 55 else 'No Hire'

        # Build analysis
        analysis = {
            'scored_responses': [r.to_dict() for r in responses],
            'section_analysis': {},
            'dimension_scores': dimensions,
            'overall_score': overall,
            'hiring_verdict': verdict,
            'summary': {
                'total_questions': len(questions),
                'answered_questions': sum(1 for r in responses if not r.is_skipped),
                'skipped_questions': sum(1 for r in responses if r.is_skipped),
                'response_rate_percent': int((sum(1 for r in responses if not r.is_skipped) / len(responses)) * 100) if responses else 0,
                'strengths': ['Strong technical foundation', 'Good problem-solving skills'],
                'weaknesses': ['Communication clarity', 'Some knowledge gaps'],
                'recommendation': f'Overall Score: {overall:.1f}/100'
            }
        }

        scored_session = {
            'candidate': session_data['candidate_data'],
            'session_metadata': {
                'session_start': interview_session.session_start_time.isoformat() if interview_session.session_start_time else None,
                'session_end': interview_session.session_end_time.isoformat() if interview_session.session_end_time else None,
                'elapsed_time_minutes': interview_session.get_elapsed_time_minutes()
            },
            'analysis': analysis
        }

        session_data['scored_session'] = scored_session
        session_data['phase'] = 2

        return jsonify({
            'success': True,
            'analysis': analysis,
            'redirect': url_for('phase3', session_id=session_id)
        })

    return render_template('phase2.html', session_id=session_id)


@app.route('/phase3/<session_id>', methods=['GET'])
def phase3(session_id):
    """Phase 3: Reports."""
    if session_id not in sessions_store:
        return redirect(url_for('index'))

    session_data = sessions_store[session_id]
    scored_session = session_data.get('scored_session')

    if not scored_session:
        return redirect(url_for('index'))

    # Generate reports
    generator = ReportGenerator(scored_session)
    markdown_report = generator.generate_markdown_report()
    html_report = generator.generate_html_report()

    analysis = scored_session['analysis']

    return render_template('phase3.html',
                         session_id=session_id,
                         analysis=analysis,
                         markdown_report=markdown_report,
                         html_report=html_report)


@app.route('/api/report/<session_id>/<format>')
def get_report(session_id, format):
    """Get report in specified format."""
    if session_id not in sessions_store:
        return jsonify({'error': 'Session not found'}), 404

    session_data = sessions_store[session_id]
    scored_session = session_data.get('scored_session')

    if not scored_session:
        return jsonify({'error': 'No report available'}), 404

    generator = ReportGenerator(scored_session)

    if format == 'markdown':
        return generator.generate_markdown_report(), 200, {'Content-Type': 'text/plain'}
    elif format == 'html':
        return generator.generate_html_report(), 200, {'Content-Type': 'text/html'}
    else:
        return jsonify({'error': 'Invalid format'}), 400


@app.route('/api/download/<session_id>/<format>')
def download_report(session_id, format):
    """Download report file."""
    if session_id not in sessions_store:
        return jsonify({'error': 'Session not found'}), 404

    session_data = sessions_store[session_id]
    scored_session = session_data.get('scored_session')

    if not scored_session:
        return jsonify({'error': 'No report available'}), 404

    generator = ReportGenerator(scored_session)

    if format == 'markdown':
        content = generator.generate_markdown_report()
        filename = f'interview_report_{session_id}.md'
    elif format == 'html':
        content = generator.generate_html_report()
        filename = f'interview_report_{session_id}.html'
    else:
        return jsonify({'error': 'Invalid format'}), 400

    response = app.make_response(content)
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'text/plain' if format == 'markdown' else 'text/html'

    return response


def get_question_data(question, question_number):
    """Format question for API response."""
    return {
        'number': question_number,
        'id': question['id'],
        'section': question['section'],
        'question': question['question'],
        'category': question.get('category', 'general')
    }


@app.template_filter('markdown')
def markdown_filter(text):
    """Simple markdown to HTML conversion."""
    if not text:
        return ''

    # Convert markdown headers
    text = text.replace('# ', '<h1>').replace('\n<h1>', '</h1>\n<h1>')
    text = text.replace('## ', '<h2>').replace('\n<h2>', '</h2>\n<h2>')

    # Add closing tags
    if '<h1>' in text:
        text += '</h1>'
    if '<h2>' in text:
        text += '</h2>'

    return text


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500


if __name__ == '__main__':
    print("\n" + "="*70)
    print("  AI INTERVIEW PANELIST - WEB APPLICATION")
    print("="*70 + "\n")

    print("Starting server...")
    print("Open your browser and go to: http://localhost:5000")
    print("\nServer is running on http://0.0.0.0:5000")
    print("="*70 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
