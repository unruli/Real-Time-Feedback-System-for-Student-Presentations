import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Audio Processing Settings
SAMPLE_RATE = 16000
CHUNK_SIZE = 1024
MAX_AUDIO_DURATION = 600  # 10 minutes in seconds

# Voice Activity Detection Settings
VAD_AGGRESSIVENESS = 3
MIN_SPEECH_DURATION = 0.5  # seconds
MIN_SILENCE_DURATION = 0.5  # seconds

# Filler Word Detection
COMMON_FILLER_WORDS = [
    'um', 'uh', 'like', 'you know', 'sort of',
    'kind of', 'basically', 'literally', 'actually',
    'so', 'well', 'right', 'okay', 'now', 'just'
]

# Emotion Detection Settings
EMOTION_MODEL = "audeering/wav2vec2-large-robust-12-ft-emotion"
EMOTION_THRESHOLD = 0.5

# Feedback Generation Settings
GPT_MODEL = "gpt-4"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

# File Paths
TEMP_DIR = "temp"
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

# Create necessary directories
for directory in [TEMP_DIR, UPLOAD_DIR, OUTPUT_DIR]:
    os.makedirs(directory, exist_ok=True) 