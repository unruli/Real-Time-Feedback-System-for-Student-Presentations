import webrtcvad
import wave
import collections
import struct
import numpy as np

def detect_voice_activity(audio_path: str) -> dict:
    """
    Detect voice activity in audio file using WebRTC VAD.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        dict: Voice activity statistics
    """
    try:
        # Initialize VAD
        vad = webrtcvad.Vad(3)  # Aggressiveness mode 3
        
        # Read audio file
        with wave.open(audio_path, 'rb') as wf:
            sample_rate = wf.getframerate()
            pcm_data = wf.readframes(wf.getnframes())
            
        # Process audio in 30ms frames
        frame_duration = 30  # ms
        frame_size = int(sample_rate * frame_duration / 1000)
        
        # Calculate statistics
        total_frames = len(pcm_data) // (frame_size * 2)  # 2 bytes per sample
        voice_frames = 0
        
        for i in range(0, len(pcm_data) - frame_size * 2, frame_size * 2):
            frame = pcm_data[i:i + frame_size * 2]
            if len(frame) == frame_size * 2:
                is_speech = vad.is_speech(frame, sample_rate)
                if is_speech:
                    voice_frames += 1
        
        voice_percentage = (voice_frames / total_frames) * 100
        
        return {
            "total_frames": total_frames,
            "voice_frames": voice_frames,
            "voice_percentage": voice_percentage,
            "has_speech": voice_percentage > 0
        }
        
    except Exception as e:
        print(f"Error in voice activity detection: {str(e)}")
        return {
            "total_frames": 0,
            "voice_frames": 0,
            "voice_percentage": 0,
            "has_speech": False
        } 