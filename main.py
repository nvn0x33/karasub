from pathlib import Path
from src import extract, Transcribe, UI
from src import get_resolution


input_dir = "input"
output_dir = "output"
temp_dir = "temp"
font = "fonts/RobotoMono-Medium.ttf"

vid_font_sizes = []

def get_font_size():
    # font size = min(width, height) * 0.085 // formula
    # Every video's font size is auto for now.
    
    if new_ui.config["font_size"] == "auto":
        for video in vid_files:
            width, height = get_resolution(video["path"])
            size = min(width, height) * 0.085
            
            vid_font_sizes.append({"font_size": size, "video": video["name"]})
            
# pseudo code testings
new_ui = UI(font, input_dir)
vid_files = new_ui.print_UI()
new_ui.correct_config()

print(new_ui.config)
get_font_size()
print(vid_font_sizes)
    

# extracted_audio_path = extract(vid_files[0]["path"], temp_dir)
# print(extracted_audio_path)
# transcript = Transcribe(extracted_audio_path)

# TODO: calculate font size after obtaining video resolution
#       clean and refactor the transcribed segments into usable form

# NEXT: Write .ass file using the segments and config details and burn it into the video.