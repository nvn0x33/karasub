import os
from src import extract, Transcribe, UI
from src import get_vid_files

# font size = min(width, height) * 0.085 // formula

input_dir = "input"
output_dir = "output"
temp_dir = "temp"
font = "fonts/RobotoMono-Medium.ttf"

video_files = get_vid_files(input_dir)

# pseudo code testings

new_ui = UI(font)

# extracted_audio_path = extract(input_dir, video_files[0], temp_dir)
# print(extracted_audio_path)
# transcript = Transcribe(extracted_audio_path)