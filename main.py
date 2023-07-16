import os
import pytube
import time
from moviepy.editor import *

def download_youtube_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    return video.default_filename

def convert_to_mp3(video_filename, output_directory):
    video = VideoFileClip(video_filename)
    mp3_filename = os.path.splitext(video_filename)[0] + ".mp3"
    mp3_filepath = os.path.join(output_directory, mp3_filename)
    mp3_filepath = mp3_filepath.replace(" ", "_")
    audio = video.audio
    audio.write_audiofile(mp3_filepath)
    video.close()
    return mp3_filepath

def convert_to_mp4(video_filename, output_directory):
    mp4_filename = os.path.splitext(video_filename)[0] + ".mp4"
    mp4_filepath = os.path.join(output_directory, mp4_filename)
    mp4_filepath = mp4_filepath.replace(" ", "_")
    os.rename(video_filename, mp4_filepath)
    return mp4_filepath

def get_file_size(filepath):
    return os.path.getsize(filepath) / (1024 * 1024)

def main():
    youtube_url = input("Enter YouTube video URL: ")
    output_directory = input("Enter the output directory for the files: ")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    video_filename = download_youtube_video(youtube_url)

    start_time = time.time()
    mp3_filepath = convert_to_mp3(video_filename, output_directory)
    mp3_size = get_file_size(mp3_filepath)
    mp3_creation_time = time.time() - start_time

    start_time = time.time()
    mp4_filepath = convert_to_mp4(video_filename, output_directory)
    mp4_size = get_file_size(mp4_filepath)
    mp4_creation_time = time.time() - start_time

    print(f"MP3 file '{mp3_filepath}' created successfully!")
    print(f"MP3 File Size: {mp3_size:.2f} MB")
    print(f"MP3 Creation Time: {mp3_creation_time:.2f} seconds\n")
    print(f"MP4 file '{mp4_filepath}' created successfully!")
    print(f"MP4 File Size: {mp4_size:.2f} MB")
    print(f"MP4 Creation Time: {mp4_creation_time:.2f} seconds")

if __name__ == "__main__":
    main()
