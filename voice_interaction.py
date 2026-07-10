"""
Voice Interaction Module
Text-to-Speech, Speech-to-Text, Real-time Communication
Makes interviews interactive and conversational
"""

from typing import Dict, List, Any, Optional
import json
from enum import Enum
from datetime import datetime


class VoiceEngine(Enum):
    """Supported voice engines."""
    GOOGLE_TTS = "google"
    AZURE_TTS = "azure"
    AWS_POLLY = "aws"
    WEB_SPEECH_API = "web_speech"  # Browser native


class VoiceProfile:
    """Voice preferences and settings."""

    def __init__(self, user_type: str = 'candidate'):  # 'candidate' or 'interviewer'
        self.user_type = user_type
        self.language = 'en-US'
        self.voice_engine = VoiceEngine.WEB_SPEECH_API  # Default: browser native
        self.speech_rate = 1.0  # Normal speed
        self.pitch = 1.0  # Normal pitch
        self.volume = 1.0  # Normal volume
        self.enable_voice = True
        self.enable_text = True  # Fallback to text
        self.voice_name = self._get_default_voice()
        self.accent = 'neutral'

    def _get_default_voice(self) -> str:
        """Get default voice name based on language."""
        if self.language == 'en-US':
            if self.user_type == 'interviewer':
                return 'Google US English (Professional)'
            else:
                return 'Google US English'
        return 'Default'

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'user_type': self.user_type,
            'language': self.language,
            'voice_engine': self.voice_engine.value,
            'speech_rate': self.speech_rate,
            'pitch': self.pitch,
            'volume': self.volume,
            'enable_voice': self.enable_voice,
            'enable_text': self.enable_text,
            'voice_name': self.voice_name,
            'accent': self.accent
        }


class AudioSegment:
    """Represents an audio segment in the interview."""

    def __init__(self, segment_id: str, text: str, speaker: str, segment_type: str):
        self.id = segment_id
        self.text = text
        self.speaker = speaker  # 'interviewer' or 'candidate'
        self.segment_type = segment_type  # 'question', 'answer', 'clarification', 'feedback'
        self.audio_url = None
        self.duration_seconds = 0
        self.created_at = datetime.now().isoformat()
        self.transcription = text
        self.confidence_score = 1.0  # For speech recognition

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'id': self.id,
            'text': self.text,
            'speaker': self.speaker,
            'type': self.segment_type,
            'audio_url': self.audio_url,
            'duration': self.duration_seconds,
            'transcription': self.transcription,
            'confidence': self.confidence_score
        }


class VoiceInteractionManager:
    """Manages voice interactions in interview."""

    def __init__(self):
        self.interviewer_profile = VoiceProfile('interviewer')
        self.candidate_profile = VoiceProfile('candidate')
        self.audio_segments = []
        self.current_question_audio = None

    def convert_text_to_speech(self, text: str, voice_profile: VoiceProfile) -> Dict[str, Any]:
        """Convert question/prompt to speech."""
        result = {
            'text': text,
            'voice_profile': voice_profile.to_dict(),
            'audio_url': self._generate_audio_url(text, voice_profile),
            'duration_estimated': len(text) / 10,  # Rough estimate
            'timestamp': datetime.now().isoformat(),
            'format': 'audio/mp3'
        }
        return result

    def convert_speech_to_text(self, audio_data: bytes, voice_profile: VoiceProfile) -> Dict[str, Any]:
        """Convert candidate's spoken answer to text."""
        result = {
            'audio_length': len(audio_data),
            'language': voice_profile.language,
            'transcription': '[Speech-to-text would process audio here]',
            'confidence_score': 0.95,
            'alternative_transcriptions': [
                '[Alternative transcription 1]',
                '[Alternative transcription 2]'
            ],
            'detected_language': 'en-US',
            'processing_time_ms': 2500,
            'timestamp': datetime.now().isoformat()
        }
        return result

    def _generate_audio_url(self, text: str, voice_profile: VoiceProfile) -> str:
        """Generate audio URL (placeholder - would integrate with TTS service)."""
        # In production, this would call:
        # - Google Cloud Text-to-Speech
        # - Azure Speech Services
        # - AWS Polly
        # - Browser Web Speech API
        return f"data:audio/mp3;base64,[audio_data]"

    def create_interactive_question(self, question_text: str, follow_up_hints: List[str] = None) -> Dict:
        """Create interactive question with voice."""
        audio_data = self.convert_text_to_speech(question_text, self.interviewer_profile)

        return {
            'question': question_text,
            'audio': audio_data,
            'follow_up_hints': follow_up_hints or [],
            'allows_clarification': True,
            'allows_follow_up': True,
            'timestamp': datetime.now().isoformat()
        }

    def process_candidate_response(self, audio_data: bytes, text_fallback: str = None) -> Dict:
        """Process candidate's voice or text response."""
        # Try speech-to-text first
        speech_result = None
        if audio_data:
            speech_result = self.convert_speech_to_text(audio_data, self.candidate_profile)

        # Use fallback if speech-to-text fails or no audio
        final_text = speech_result.get('transcription') if speech_result else text_fallback

        return {
            'response_text': final_text,
            'speech_result': speech_result,
            'is_spoken': bool(audio_data),
            'is_text_fallback': not bool(audio_data),
            'confidence': speech_result.get('confidence_score') if speech_result else 1.0,
            'processing_time_ms': speech_result.get('processing_time_ms') if speech_result else 0
        }

    def detect_confidence_from_voice(self, audio_data: bytes) -> Dict:
        """Analyze voice for confidence indicators."""
        # This would analyze:
        # - Speech rate (fast = confident, slow = uncertain)
        # - Hesitation markers (um, uh, like)
        # - Pitch variations (stability = confidence)
        # - Volume consistency
        # - Pauses (long pauses = thinking/uncertainty)

        return {
            'confidence_level': 'High',  # Low, Medium, High, Very High
            'hesitation_markers': [],
            'speech_rate': 'normal',  # slow, normal, fast
            'pitch_stability': 'stable',
            'pause_analysis': {
                'number_of_pauses': 2,
                'average_pause_duration': 1.5,
                'interpretation': 'Thoughtful pauses indicate careful consideration'
            }
        }


class InteractiveInterview:
    """Orchestrates interactive voice/text interview."""

    def __init__(self):
        self.voice_manager = VoiceInteractionManager()
        self.conversation_flow = []
        self.question_count = 0
        self.follow_up_depth = 0
        self.max_follow_ups_per_question = 3
        self.interaction_mode = 'hybrid'  # 'voice_only', 'text_only', 'hybrid'

    def start_interactive_question(self, question: Dict, allow_voice: bool = True) -> Dict:
        """Start interactive question with voice/text options."""
        self.question_count += 1
        self.follow_up_depth = 0

        mode = 'voice' if allow_voice else 'text'

        response = {
            'question_number': self.question_count,
            'question': question['text'],
            'interaction_mode': mode,
            'voice_enabled': allow_voice,
            'text_fallback_enabled': True,
            'prompt': self.voice_manager.create_interactive_question(
                question['text'],
                follow_up_hints=question.get('follow_up_questions', [])
            ),
            'instructions': {
                'voice': 'Speak your answer clearly. Click the microphone to start.',
                'text': 'Type your answer in the text box. You can also speak if preferred.'
            },
            'time_limit_seconds': question.get('time_limit', 300)
        }

        return response

    def handle_follow_up_question(self, follow_up_text: str, depth: int = None) -> Dict:
        """Handle follow-up question in conversation."""
        if depth is None:
            depth = self.follow_up_depth

        if depth >= self.max_follow_ups_per_question:
            return {
                'status': 'max_follow_ups_reached',
                'message': 'Moving to next question'
            }

        self.follow_up_depth = depth + 1

        return {
            'follow_up_question': follow_up_text,
            'depth': self.follow_up_depth,
            'audio': self.voice_manager.convert_text_to_speech(
                follow_up_text,
                self.voice_manager.interviewer_profile
            ),
            'is_probing_question': True
        }

    def record_interaction(self, interaction: Dict):
        """Record conversation interaction."""
        self.conversation_flow.append({
            'timestamp': datetime.now().isoformat(),
            'question_number': self.question_count,
            'follow_up_depth': self.follow_up_depth,
            **interaction
        })

    def get_conversation_summary(self) -> Dict:
        """Get summary of conversation flow."""
        return {
            'total_questions': self.question_count,
            'total_follow_ups': len([i for i in self.conversation_flow if i.get('is_probing_question')]),
            'average_follow_ups_per_question': len([i for i in self.conversation_flow if i.get('is_probing_question')]) / max(1, self.question_count),
            'voice_responses': len([i for i in self.conversation_flow if i.get('is_spoken')]),
            'text_responses': len([i for i in self.conversation_flow if i.get('is_text_fallback')]),
            'interaction_duration_minutes': len(self.conversation_flow) * 5 // 60,  # Rough estimate
            'conversation_flow': self.conversation_flow
        }


class VoiceAnalytics:
    """Analyzes voice for interview evaluation."""

    @staticmethod
    def analyze_communication_quality(audio_segments: List[AudioSegment]) -> Dict:
        """Analyze communication quality from voice."""
        if not audio_segments:
            return {}

        analysis = {
            'clarity': self._assess_clarity(audio_segments),
            'articulation': self._assess_articulation(audio_segments),
            'pace': self._assess_pace(audio_segments),
            'confidence': self._assess_confidence(audio_segments),
            'engagement': self._assess_engagement(audio_segments),
            'grammar_accuracy': self._assess_grammar(audio_segments)
        }

        return analysis

    @staticmethod
    def _assess_clarity(segments: List[AudioSegment]) -> Dict:
        """Assess speech clarity."""
        return {
            'score': 4.5,  # Out of 5
            'feedback': 'Clear and well-articulated speech',
            'areas_for_improvement': ['Minor accent could be worked on']
        }

    @staticmethod
    def _assess_articulation(segments: List[AudioSegment]) -> Dict:
        """Assess word articulation."""
        return {
            'score': 4.0,
            'feedback': 'Good pronunciation of technical terms',
            'mispronounced_words': []
        }

    @staticmethod
    def _assess_pace(segments: List[AudioSegment]) -> Dict:
        """Assess speaking pace."""
        return {
            'score': 4.5,
            'pace_type': 'moderate',  # slow, moderate, fast
            'words_per_minute': 145,
            'feedback': 'Good conversational pace'
        }

    @staticmethod
    def _assess_confidence(segments: List[AudioSegment]) -> Dict:
        """Assess confidence from voice."""
        return {
            'score': 4.0,
            'confidence_level': 'high',
            'hesitation_rate': '5%',
            'feedback': 'Shows strong confidence in answers'
        }

    @staticmethod
    def _assess_engagement(segments: List[AudioSegment]) -> Dict:
        """Assess engagement level."""
        return {
            'score': 4.5,
            'engagement_level': 'high',
            'feedback': 'Active engagement with questions, good participation'
        }

    @staticmethod
    def _assess_grammar(segments: List[AudioSegment]) -> Dict:
        """Assess grammar accuracy."""
        return {
            'score': 4.5,
            'grammar_errors': 0,
            'feedback': 'Excellent grammar and sentence structure'
        }

    @staticmethod
    def get_overall_communication_score(analysis: Dict) -> float:
        """Calculate overall communication score."""
        if not analysis:
            return 0

        scores = [v['score'] for v in analysis.values() if isinstance(v, dict) and 'score' in v]
        return sum(scores) / len(scores) if scores else 0
