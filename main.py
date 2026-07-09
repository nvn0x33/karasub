import os, src

# font size = min(width, height) * 0.085 // formula

input_path = "input"
output_path = "output"
temp_path = "temp"

video_files = os.listdir(input_path)

# pseudo code testings
extracted_audio_path = src.extract(input_path, video_files[0], temp_path)
src.convert(extracted_audio_path)