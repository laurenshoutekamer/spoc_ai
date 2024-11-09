import whisper


def transcribe_audio(audio_bytes):
    # Save audio_bytes to a temporary file
    with open("user_feedback.wav", "wb") as f:
        f.write(audio_bytes)

    # Load Whisper model and transcribe
    model = whisper.load_model("base")
    result = model.transcribe("user_feedback.wav")
    return result["text"]
