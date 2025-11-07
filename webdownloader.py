from pytubefix import YouTube
from pytubefix.cli import on_progress
import os, re

url = "https://www.youtube.com/watch?v=IaVxNa4lQPI"

yt = YouTube(url, on_progress_callback=on_progress)

def remover_caracteres_errados(title):
    return re.sub(r'[<>:"/\\|?*]', '', title)


ys = yt.streams.get_audio_only()
ys.download(os.path.join(r"C:\Users\wesley\Music"))

print(os.path.join(r"C:\Users\wesley\Music",  remover_caracteres_errados(yt.title)))

# from moviepy.editor import *

# video = VideoFileClip("input.mp4")
# video.audio.write_audiofile("movie_sound.mp3")

