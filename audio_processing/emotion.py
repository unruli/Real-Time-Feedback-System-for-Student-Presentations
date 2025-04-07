from transformers import pipeline
import torch
import numpy as np
from typing import Dict, List

# Initialize emotion classifier
try:
    emotion_classifier = pipeline(
        "audio-classification",
        model="audeering/wav2vec2-large-robust-12-ft-emotion",
        device=0 if torch.cuda.is_available() else -1
    )
except Exception as e:
    print(f"Error loading emotion model: {str(e)}")
    emotion_classifier = None

def analyze_emotion(audio_path: str) -> Dict:
    """
    Analyze emotional content of speech using Wav2Vec2 model.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        Dict: Emotion analysis results
    """
    try:
        if emotion_classifier is None:
            raise Exception("Emotion classifier not initialized")
            
        # Get emotion predictions
        predictions = emotion_classifier(audio_path)
        
        # Process predictions
        emotions = {}
        for pred in predictions:
            emotions[pred['label']] = pred['score']
            
        # Get dominant emotion
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])
        
        # Calculate emotion distribution
        total_score = sum(emotions.values())
        emotion_distribution = {
            emotion: (score / total_score * 100) 
            for emotion, score in emotions.items()
        }
        
        return {
            "dominant_emotion": dominant_emotion[0],
            "confidence": dominant_emotion[1],
            "emotion_distribution": emotion_distribution,
            "all_emotions": emotions
        }
        
    except Exception as e:
        print(f"Error in emotion analysis: {str(e)}")
        return {
            "dominant_emotion": "neutral",
            "confidence": 0.0,
            "emotion_distribution": {},
            "all_emotions": {}
        } 