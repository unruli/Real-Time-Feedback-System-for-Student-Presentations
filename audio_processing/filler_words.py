from typing import Dict, List
import re

# Common filler words to detect
FILLER_WORDS = {
    'um': 0,
    'uh': 0,
    'like': 0,
    'you know': 0,
    'sort of': 0,
    'kind of': 0,
    'basically': 0,
    'literally': 0,
    'actually': 0,
    'so': 0,
    'well': 0,
    'right': 0,
    'okay': 0,
    'now': 0,
    'just': 0
}

def detect_filler_words(transcription: str) -> Dict:
    """
    Detect and count filler words in the transcribed text.
    
    Args:
        transcription (str): Transcribed text
        
    Returns:
        Dict: Statistics about filler word usage
    """
    try:
        # Initialize counters
        filler_counts = FILLER_WORDS.copy()
        total_words = len(transcription.split())
        
        # Convert to lowercase for case-insensitive matching
        text = transcription.lower()
        
        # Count occurrences of each filler word
        for filler in filler_counts.keys():
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(filler) + r'\b'
            count = len(re.findall(pattern, text))
            filler_counts[filler] = count
        
        # Calculate total filler words
        total_fillers = sum(filler_counts.values())
        
        # Calculate filler word percentage
        filler_percentage = (total_fillers / total_words * 100) if total_words > 0 else 0
        
        # Get most common filler words
        most_common = sorted(
            [(word, count) for word, count in filler_counts.items() if count > 0],
            key=lambda x: x[1],
            reverse=True
        )
        
        return {
            "total_filler_words": total_fillers,
            "filler_percentage": filler_percentage,
            "total_words": total_words,
            "filler_counts": filler_counts,
            "most_common_fillers": most_common[:5]  # Top 5 most used filler words
        }
        
    except Exception as e:
        print(f"Error in filler word detection: {str(e)}")
        return {
            "total_filler_words": 0,
            "filler_percentage": 0,
            "total_words": 0,
            "filler_counts": FILLER_WORDS,
            "most_common_fillers": []
        } 