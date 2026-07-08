import os
from src import extract_audio

input_path = "input/"
output_path = "output/"
temp_path = "temp/"

video_files = os.listdir(input_path)
extrcted_audio_path = extract_audio.extract(input_path, video_files[0], temp_path)