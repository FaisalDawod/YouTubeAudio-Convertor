import os
from pytube import YouTube

# Output PATH
OUTPUT_FOLDER = 'D:/YouTube Audios'

# Define the bitrate for the downloaded FLAC audio files
BITRATE = '320k'  # Set the desired bit-rate (e.g., 320kbps for high quality)

VIDEO_URL = input("Enter YouTube URL audio: ")

yt = YouTube(VIDEO_URL)

# Get the best audio stream (you can customize this based on your quality preferences)
audio_stream = yt.streams.filter(only_audio=True, file_extension='webm').first()

# Download the audio file in FLAC format with the specified bit-rate
audio_stream.download(output_path=OUTPUT_FOLDER)
# Rename the downloaded file with the video title and .flac extension
output_file_path = audio_stream.download(output_path=OUTPUT_FOLDER)
output_file_name = yt.title + ".flac"
os.rename(output_file_path, os.path.join(OUTPUT_FOLDER, output_file_name))

# Print a message to the user
print("Audio file downloaded successfully!")
