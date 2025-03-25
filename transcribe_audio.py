import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Adjust model size as needed
    try:
        result = model.transcribe(audio_path)
        transcript = result.get("text", "")
        print("\n📝 Transcription Completed:")
        print(transcript)
        return transcript
    except Exception as e:
        print(f"❌ Transcription failed: {e}")
        exit()
