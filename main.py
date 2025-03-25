from download_video import download_video
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from summarize_transcription import summarize_transcription, save_output

# Define paths
video_url = "https://rr5---sn-qxaelnez.googlevideo.com/videoplayback?expire=1742768607&ei=fzXgZ_KpMuzr7OsPy7fmsAo&ip=128.1.32.123&id=o-ANOmco3RLYX25qkLOOj_NFfB682pRC96XTbBdqIAziOG&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&rms=au%2Cau&bui=AccgBcPNOU1uV2mm2aY4tFTAvzcQ7dpfvPGQuT1HoA-NNxvXJ7pUvbzqHjesQUAF5HsTMx84kAfWPEFp&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Rk3HTiihKMRug0fzhiqPeLMQ&rqh=1&cnr=14&ratebypass=yes&dur=2560.626&lmt=1697753813150378&lmw=1&c=TVHTML5&sefc=1&txp=5438434&n=Zcvrog4fB4hGqw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAK2GahTlfubssZxhvJTPs5n6jMZ1yQ915RTz6k9kz7YOAiBMz-DupAeuGajUDeSDAVwPqIrOy-36CE9-YFDTSazRSQ%3D%3D&title=Product%20Marketing%20Meeting%20(weekly)%202021-06-28&rm=sn-un5y7l&rrc=104,191&fexp=24350590,24350737,24350778,24350827,24350961,24351064,24351146,24351173,24351206,24351229,24351283,24351353,24351395,24351397,24351398,24351468&req_id=ab81238c19e4a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-ci5gup-qxak7e&cms_redirect=yes&cmsv=e&met=1742747418,&mh=1v&mip=223.225.56.147&mm=30&mn=sn-qxaelnez&ms=nxu&mt=1742747070&mv=m&mvi=5&pl=21&tso=0&lsparams=ipbypass,met,mh,mip,mm,mn,ms,mv,mvi,pl,rms,tso&lsig=AFVRHeAwRQIhAK9Go3JDRZhPcSmkesg0tLERKfSblUbhTTUfXM5-GacuAiA2lfbsbb-XP7b5pHaRgqqWTSdtjOIx8tW4YSY6YZNnsA%3D%3D"
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
