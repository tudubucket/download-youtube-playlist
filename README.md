
# Simple Youtube Playlist Downloader (.mp3)

#### [Checkout my playlist here, if you want 😋](https://www.youtube.com/playlist?list=PLV2M9Tvv_Ru7PS05zvBNhAfW8_FMK4G0f)
#### [My Discord server 😋😋😋😋](https://ankita.tudubucket.workers.dev/discord)

#### reason i made this shit python file:
- i dont want to spend couple of years just only to download a playlist that have over 500 videos on y2mate
- some shit website (actually they're nice) won't download videos that have copyright, or they will load the playlist to first 200 videos only
- i want to listen to some music when my location encountered outage
- i want some cul logs while the code running 😎



#### what this code have:
- 32769 variables
- download up to any number of videos in playlist, not limited
- very slow code, need commits to fix these shits if you can
- bad englist in readme

### 1. Requirements (for ~~noob~~ beginners)

- python: [Download](https://www.python.org/downloads/) | [Installation Guide](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
- pip: [Installation Guide](https://phoenixnap.com/kb/install-pip-windows)
- `youtube-dl` python package: run this command on Terminal/PowerShell/Command Prompt/Windows + R keystroke: `pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"` (see [this](https://github.com/ytdl-org/youtube-dl/issues/32180) if you are wondering why i am not doing `pip install youtube-dl` instead)
- ffmpeg: [Download](https://ffmpeg.org/download.html) | [Installation Guide](https://www.wikihow.com/Install-FFmpeg-on-Windows)
- your brain

### 2. Download the playlist
#### Step-by-step guide:

1. Get the youtube playlist ID: 
`https://www.youtube.com/playlist?list=abcdef`, the ID will be `abcdef`, for example

2. Open the python file, change the variable `playlist_id` in line 5 to your youtube playlist ID

3. Run the python file:
Open Terminal, type `python C:\path\to\file\download-youtube-playlist.py`

4. Waiting, 1 video about 2 minutes length will take about 3 - 5 seconds

5. Have fun with your playlist, the result will be inside the folder named `playlist-output-{playlist_id}`, right inside the path where you put the python file




