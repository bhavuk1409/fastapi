from download_video import download_video
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from summarize_transcription import summarize_transcription, save_output

# Define paths
video_url = "https://ohio.stream-io-cdn.com/1366698/video/recordings/default_845d68a8-6696-41c2-b38a-445bf6b903d0/rec_default_845d68a8-6696-41c2-b38a-445bf6b903d0_720p_1741788578656.mp4?Expires=1744142544&Signature=VtZbRURcx7pLWCTgcWs0C5CEplIEcp2VqHB58Xh-oRIhlg-seDI-7zKrqPrMICGF~yo3ggluQPEKrSZzCZXuNouGlx7VTyRG~2UnuAeT1F0KE9b-HhZ5mpmJE8CZ0GPQltVsN49tu~PCiRW2xeFgoYveUv1ZZa42LVwr3Yk2urbKzUgZ5WAElvWVYJDxQg3SP64xxHrRDw-zPvxgiBZDYMQA4DMsy0Er30GTf0cHkgB6KTGJ007cA6XJKF173Qn0ZzAMtIeZDSsHDT52hEy9TA0jRsDlQBOWr9tWNTbv7Ydpb2LH8QQEV-7GMzXx4FlGjJ2fe1snYXpiQa9FwCziFA__&Key-Pair-Id=APKAIHG36VEWPDULE23Q"
video_path = "video.mp4"
audio_path = "audio.wav"
output_text_path = "output.txt"

# Execute steps in order
download_video(video_url, video_path)
extract_audio(video_path, audio_path)
transcript = transcribe_audio(audio_path)
summary = summarize_transcription(transcript)
save_output(transcript, summary, output_text_path)

print("✅ Process completed successfully!")
