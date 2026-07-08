import os
from src import extract_audio
from src import transcribe

input_path = "input/"
output_path = "output/"
temp_path = "temp/"

video_files = os.listdir(input_path)

# pseudo code testings
extracted_audio_path = extract_audio.extract(input_path, video_files[0], temp_path)
transcribe.convert(extracted_audio_path)