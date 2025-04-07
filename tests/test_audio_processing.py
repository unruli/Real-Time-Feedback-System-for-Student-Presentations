import unittest
import os
import numpy as np
from audio_processing.transcriber import transcribe_audio
from audio_processing.vad import detect_voice_activity
from audio_processing.pacing import analyze_pacing
from audio_processing.filler_words import detect_filler_words
from audio_processing.emotion import analyze_emotion
from utils.helpers import convert_audio_format, get_audio_duration, normalize_audio

class TestAudioProcessing(unittest.TestCase):
    def setUp(self):
        # Create a test audio file path
        self.test_audio_path = "assets/sample_audio/test.wav"
        
    def test_transcribe_audio(self):
        if os.path.exists(self.test_audio_path):
            result = transcribe_audio(self.test_audio_path)
            self.assertIsInstance(result, str)
            
    def test_detect_voice_activity(self):
        if os.path.exists(self.test_audio_path):
            result = detect_voice_activity(self.test_audio_path)
            self.assertIsInstance(result, dict)
            self.assertIn('voice_percentage', result)
            
    def test_analyze_pacing(self):
        if os.path.exists(self.test_audio_path):
            result = analyze_pacing(self.test_audio_path)
            self.assertIsInstance(result, dict)
            self.assertIn('speech_rate', result)
            
    def test_detect_filler_words(self):
        test_text = "Um, like, you know, this is a test."
        result = detect_filler_words(test_text)
        self.assertIsInstance(result, dict)
        self.assertIn('total_filler_words', result)
        
    def test_analyze_emotion(self):
        if os.path.exists(self.test_audio_path):
            result = analyze_emotion(self.test_audio_path)
            self.assertIsInstance(result, dict)
            self.assertIn('dominant_emotion', result)
            
    def test_convert_audio_format(self):
        if os.path.exists(self.test_audio_path):
            output_path = "temp/test_converted.wav"
            result = convert_audio_format(self.test_audio_path, output_path)
            self.assertTrue(result)
            self.assertTrue(os.path.exists(output_path))
            
    def test_get_audio_duration(self):
        if os.path.exists(self.test_audio_path):
            duration = get_audio_duration(self.test_audio_path)
            self.assertIsInstance(duration, float)
            self.assertGreater(duration, 0)
            
    def test_normalize_audio(self):
        if os.path.exists(self.test_audio_path):
            data, sr = normalize_audio(self.test_audio_path)
            self.assertIsInstance(data, np.ndarray)
            self.assertIsInstance(sr, int)
            self.assertGreater(sr, 0)

if __name__ == '__main__':
    unittest.main() 