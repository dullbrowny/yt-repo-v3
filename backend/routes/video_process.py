import yt_dlp
#from weaviate_setup import store_in_weaviate
from utils import transcribe_audio, sanitize_filename

def process_video(youtube_url):
    # Example of how you might get the video title from yt-dlp and sanitize the filename
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_title = info_dict.get('title', 'untitled_video')
        sanitized_title = sanitize_filename(video_title)
        
        # Define where the audio will be stored
        audio_file = f"data/transcriptions/{sanitized_title}.mp3"
        #audio_file = f"data/transcriptions/{sanitized_title}"
        
        # Download the video and convert to audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': audio_file,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        #with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #    ydl.download([youtube_url])
    
    # Now proceed with transcription
    transcription = transcribe_audio(audio_file)
    
    # Assuming you extract QA pairs somewhere in your process
    qa_pairs = []  # Placeholder for actual QA pair extraction logic
    
    # Store in Weaviate
    #store_in_weaviate(transcription, qa_pairs)

    return {
        'transcription': transcription,
        'qa_pairs': qa_pairs
    }

