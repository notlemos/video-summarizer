from pytubefix import YouTube
import os

def baixar_audio(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    output_path = "audios"
    os.makedirs(output_path, exist_ok=True)
    audio_path = audio.download(output_path=output_path, filename=f"{yt.title}.mp4")

    return f'{yt.title}.mp4'