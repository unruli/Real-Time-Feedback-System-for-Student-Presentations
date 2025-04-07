import librosa
import numpy as np
from typing import Dict, List, Tuple

def analyze_pacing(audio_path: str) -> Dict:
    """
    Analyze speech pacing including rate, pauses, and rhythm.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        Dict: Pacing analysis results
    """
    try:
        # Load audio file
        y, sr = librosa.load(audio_path)
        
        # Extract tempo and beat frames
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        
        # Calculate speech rate (words per minute)
        # This is a simplified version - in practice, you'd want to use
        # a more sophisticated method combining with transcription
        speech_rate = tempo * 1.5  # Approximate words per minute
        
        # Detect pauses
        intervals = librosa.effects.split(y, top_db=20)
        pause_durations = []
        
        for i in range(len(intervals) - 1):
            pause_duration = (intervals[i+1][0] - intervals[i][1]) / sr
            if pause_duration > 0.5:  # Only count pauses longer than 0.5 seconds
                pause_durations.append(pause_duration)
        
        # Calculate statistics
        avg_pause_duration = np.mean(pause_durations) if pause_durations else 0
        total_pause_time = sum(pause_durations)
        total_duration = len(y) / sr
        
        return {
            "speech_rate": speech_rate,
            "tempo": tempo,
            "avg_pause_duration": avg_pause_duration,
            "total_pause_time": total_pause_time,
            "total_duration": total_duration,
            "pause_percentage": (total_pause_time / total_duration) * 100 if total_duration > 0 else 0
        }
        
    except Exception as e:
        print(f"Error in pacing analysis: {str(e)}")
        return {
            "speech_rate": 0,
            "tempo": 0,
            "avg_pause_duration": 0,
            "total_pause_time": 0,
            "total_duration": 0,
            "pause_percentage": 0
        } 