import os
from src import extract
from src import Transcribe
from src import utils

# font size = min(width, height) * 0.085 // formula

input_path = "input"
output_path = "output"
temp_path = "temp"

video_files = utils.find_vid_files(input_path)
print(video_files)

# pseudo code testings
# extracted_audio_path = extract(input_path, video_files[0], temp_path)
# transcript = Transcribe(extracted_audio_path)