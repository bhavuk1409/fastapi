from transformers import pipeline

def summarize_transcription(transcript):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    try:
        summary = summarizer(transcript, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
        print("\n📄 Summary:")
        print(summary)
        return summary
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
        exit()

def save_output(transcript, summary, output_text_path):
    try:
        with open(output_text_path, "w", encoding="utf-8") as f:
            f.write("📜 Transcription:\n")
            f.write(transcript + "\n\n")
            f.write("📄 Summary:\n")
            f.write(summary)
        print("✅ Output saved in output.txt")
    except IOError as e:
        print(f"❌ Failed to save output: {e}")
