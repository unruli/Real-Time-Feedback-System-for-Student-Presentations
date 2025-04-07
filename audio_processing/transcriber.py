import whisper
import os

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe audio file to text using OpenAI's Whisper model.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        str: Transcribed text
    """
    try:
        # Load the Whisper model
        model = whisper.load_model("base")
        
        # Transcribe the audio
        result = model.transcribe(audio_path)
        
        return result["text"]
    except Exception as e:
        print(f"Error in transcription: {str(e)}")
        return "" 