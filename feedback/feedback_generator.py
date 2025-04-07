from typing import Dict
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_feedback(
    transcription: str,
    voice_activity: Dict,
    pacing: Dict,
    filler_words: Dict,
    emotions: Dict
) -> str:
    """
    Generate natural language feedback using GPT-4.
    
    Args:
        transcription (str): Transcribed text
        voice_activity (Dict): Voice activity detection results
        pacing (Dict): Pacing analysis results
        filler_words (Dict): Filler word analysis results
        emotions (Dict): Emotion analysis results
        
    Returns:
        str: Generated feedback
    """
    try:
        # Construct the prompt
        prompt = f"""
        Based on the following presentation analysis, provide constructive feedback 
        to help improve the speaker's presentation skills:

        Transcription: {transcription[:500]}...

        Voice Activity:
        - Total frames: {voice_activity.get('total_frames', 0)}
        - Voice percentage: {voice_activity.get('voice_percentage', 0):.2f}%

        Pacing:
        - Speech rate: {pacing.get('speech_rate', 0):.2f} words per minute
        - Average pause duration: {pacing.get('avg_pause_duration', 0):.2f} seconds
        - Pause percentage: {pacing.get('pause_percentage', 0):.2f}%

        Filler Words:
        - Total filler words: {filler_words.get('total_filler_words', 0)}
        - Filler word percentage: {filler_words.get('filler_percentage', 0):.2f}%
        - Most common fillers: {', '.join([f"{word} ({count})" for word, count in filler_words.get('most_common_fillers', [])])}

        Emotional Analysis:
        - Dominant emotion: {emotions.get('dominant_emotion', 'neutral')}
        - Emotion confidence: {emotions.get('confidence', 0):.2f}

        Please provide specific, actionable feedback in the following areas:
        1. Speech Clarity and Voice
        2. Pacing and Timing
        3. Filler Word Usage
        4. Emotional Delivery
        5. Overall Presentation Effectiveness

        Format the feedback in a clear, constructive manner with specific suggestions for improvement.
        """

        # Generate feedback using GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert presentation coach providing constructive feedback."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error generating feedback: {str(e)}")
        return "Unable to generate feedback at this time. Please try again later." 