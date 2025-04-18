from transformers import pipeline
import torch
import numpy as np
from typing import Dict, List
import os
from dotenv import load_dotenv
import speechbrain as sb

# Load environment variables
load_dotenv()

# Get Hugging Face token from environment variables
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# Initialize emotion classifier
try:
    # Load SpeechBrain emotion recognition model
    emotion_classifier = sb.pretrained.EncoderClassifier.from_hparams(
        source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
        savedir="models/emotion_recognition",
        run_opts={"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )
except Exception as e:
    print(f"Error loading emotion model: {str(e)}")
    emotion_classifier = None

def analyze_emotion(audio_path: str) -> Dict:
    """
    Analyze emotional content of speech using SpeechBrain model.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        Dict: Emotion analysis results
    """
    try:
        if emotion_classifier is None:
            raise Exception("Emotion classifier not initialized")
            
        # Get emotion predictions
        predictions = emotion_classifier.classify_file(audio_path)
        
        # Process predictions
        emotions = {}
        for emotion, score in zip(predictions[1], predictions[0]):
            emotions[emotion] = float(score)
            
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