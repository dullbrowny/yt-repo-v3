import os
import re
import whisper
from transformers import pipeline

def sanitize_filename(filename):
    # Replace any character that is not a letter, number, dot, or underscore with an underscore
    return re.sub(r'[^\w\-_\. ]', '_', filename)

def transcribe_audio(audio_file):
    # Check if the file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(audio_file)

    return result

def generate_qa_pairs(transcription_text):
    qa_model = pipeline("question-generation", model="valhalla/t5-small-qg-hl")
    qa_pairs = qa_model(transcription_text)
    return qa_pairs


