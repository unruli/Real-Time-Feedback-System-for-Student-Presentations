import streamlit as st
import os
from dotenv import load_dotenv
from audio_processing.transcriber import transcribe_audio
from audio_processing.vad import detect_voice_activity
from audio_processing.pacing import analyze_pacing
from audio_processing.filler_words import detect_filler_words
from audio_processing.emotion import analyze_emotion
from feedback.feedback_generator import generate_feedback
from utils.helpers import convert_audio_format

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Student Presentation Feedback System",
    page_icon="🎤",
    layout="wide"
)

def main():
    st.title("🎤 Student Presentation Feedback System")
    st.write("Upload your presentation audio for real-time feedback and analysis.")

    # File uploader
    audio_file = st.file_uploader("Upload your audio file", type=['wav', 'mp3', 'm4a'])

    if audio_file:
        # Save the uploaded file temporarily
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.getbuffer())

        # Process the audio
        with st.spinner("Analyzing your presentation..."):
            # Transcribe audio
            transcription = transcribe_audio("temp_audio.wav")
            
            # Analyze different aspects
            voice_activity = detect_voice_activity("temp_audio.wav")
            pacing_analysis = analyze_pacing("temp_audio.wav")
            filler_words = detect_filler_words(transcription)
            emotions = analyze_emotion("temp_audio.wav")
            
            # Generate feedback
            feedback = generate_feedback(
                transcription=transcription,
                voice_activity=voice_activity,
                pacing=pacing_analysis,
                filler_words=filler_words,
                emotions=emotions
            )

            # Display results
            st.subheader("Analysis Results")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("### Speech Clarity")
                st.write(filler_words)
                
                st.write("### Pacing Analysis")
                st.write(pacing_analysis)
            
            with col2:
                st.write("### Emotional Analysis")
                st.write(emotions)
                
                st.write("### Voice Activity")
                st.write(voice_activity)
            
            st.subheader("Detailed Feedback")
            st.write(feedback)

        # Clean up
        os.remove("temp_audio.wav")

if __name__ == "__main__":
    main() 