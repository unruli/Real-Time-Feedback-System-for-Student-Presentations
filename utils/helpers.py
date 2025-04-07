import os
import soundfile as sf
import numpy as np
from typing import Tuple

def convert_audio_format(input_path: str, output_path: str, target_sr: int = 16000) -> bool:
    """
    Convert audio file to WAV format with target sample rate.
    
    Args:
        input_path (str): Path to input audio file
        output_path (str): Path to save converted audio file
        target_sr (int): Target sample rate (default: 16000)
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Read audio file
        data, sr = sf.read(input_path)
        
        # Convert to mono if stereo
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)
        
        # Save as WAV with target sample rate
        sf.write(output_path, data, target_sr)
        return True
        
    except Exception as e:
        print(f"Error converting audio format: {str(e)}")
        return False

def get_audio_duration(audio_path: str) -> float:
    """
    Get duration of audio file in seconds.
    
    Args:
        audio_path (str): Path to audio file
        
    Returns:
        float: Duration in seconds
    """
    try:
        data, sr = sf.read(audio_path)
        return len(data) / sr
    except Exception as e:
        print(f"Error getting audio duration: {str(e)}")
        return 0.0

def normalize_audio(audio_path: str) -> Tuple[np.ndarray, int]:
    """
    Normalize audio file to have consistent volume levels.
    
    Args:
        audio_path (str): Path to audio file
        
    Returns:
        Tuple[np.ndarray, int]: Normalized audio data and sample rate
    """
    try:
        # Read audio file
        data, sr = sf.read(audio_path)
        
        # Convert to mono if stereo
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)
        
        # Normalize
        data = data / np.max(np.abs(data))
        
        return data, sr
        
    except Exception as e:
        print(f"Error normalizing audio: {str(e)}")
        return np.array([]), 0 