from pathlib import Path
from src import extract, Transcribe, UI
from src import get_resolution

# Some folder paths
input_dir = "input"
output_dir = "output"
temp_dir = "temp"
font = "fonts/RobotoMono-Medium.ttf"

# Main video data
videos_data = []

def append_font_data():
    for video in vid_files:
        if new_ui.config["font_size"] == "auto":
            width, height = get_resolution(video["path"])
            size = min(width, height) * 0.085
            
            videos_data.append({**video, "font_size": size, "transcript": {}})
            
        else:
            videos_data.append({**video, "font_size": new_ui.config["font_size"], "transcript": {}})
        
            
# pseudo code testings
new_ui = UI(font, input_dir)

vid_files = new_ui.print_UI()
new_ui.correct_config()

print(new_ui.config)
append_font_data()

# DATA:
# new_ui.config = configurations for colors, font style and font size
# vid_files = an array of dicts containing video name and its path
# videos_data = an array of dicts containing video name, its path, font_size and empty transcript dictionary to later append data into.
    
# Testing for 1 video only for now.
extracted_audio_path = extract(vid_files[0]["path"], temp_dir)
print(extracted_audio_path)
transcript = Transcribe(extracted_audio_path)

# TODO: calculate font size after obtaining video resolution
#       clean and refactor the transcribed segments into usable form

# NEXT: Write .ass file using the segments and config details and burn it into the video.