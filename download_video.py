import requests

def download_video(video_url, video_path):
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Raise error if download fails
        with open(video_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print("✅ Video downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"❌ Video download failed: {e}")
        exit()
