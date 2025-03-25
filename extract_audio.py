import os

def extract_audio(video_path, audio_path="audio.wav"):  # Now it accepts 2 arguments
    cmd = f"ffmpeg -y -i {video_path} -vn -acodec pcm_s16le -ar 16000 -ac 1 {audio_path}"
    os.system(cmd)
    
    if os.path.exists(audio_path):
        print(f"✅ Audio extracted successfully as '{audio_path}'!")
    else:
        print("❌ Audio extraction failed!")

    return audio_path  # Returning the path for further use
