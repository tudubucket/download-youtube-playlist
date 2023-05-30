import youtube_dl
import os

# Specify the YouTube playlist ID
playlist_id = "PLV2M9Tvv_Ru7PS05zvBNhAfW8_FMK4G0f"

# Specify the URL of the YouTube playlist
playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"

# Create a directory to save the downloaded files
output_dir = f"playlist-output-{playlist_id}"
os.makedirs(output_dir, exist_ok=True)

# Configure the options for downloading audio
ydl_opts = {
    'format': 'bestaudio/best',
    'restrict-filenames': True, # set to false if the playlist have videos that contain invalid string/character
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'/{output_dir}/%(title)s.%(ext)s',
    'ignoreerrors': True,
}

# Create a YouTube downloader instance
ydl = youtube_dl.YoutubeDL(ydl_opts)

# Extract information about the playlist
playlist_info = ydl.extract_info(playlist_url, download=False)

# Iterate over the playlist's entries and download the audio
for video_info in playlist_info['entries']:
    if video_info:
        video_url = video_info['webpage_url']
        ydl.download([video_url])
