from pathlib import Path
from src import extract, Transcribe, UI, ASS
from src import get_resolution
import json

# Some folder paths
input_dir = "input"
output_dir = "output"
temp_dir = "temp"
font = "fonts/RobotoMono-Medium.ttf"

# Main video(s) data
videos_data = []

# TODO: If possible create a class for video_data with methods append font data and append transcript in future.
def append_font_data():
    for video in vid_files:
        width, height = get_resolution(video["path"])
        
        if new_ui.config["font_size"] == "auto":
            # size = min(width, height) * 0.085
            size = min(width, height) * 0.060
            
            font = size
        else:
            font = new_ui.config["font_size"]
        
        videos_data.append(
            {**video, 
             "resX": width,
             "resY": height,
             "font_size": int(font), 
             "transcript": []})
        
def read_transcript():
    path = "temp/transcript.json"
    data = None
    
    with open (path, "r") as file:
        data = json.load(file)
        
    return data
        
            
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

# CHECKPOINT 1:
# extracted_audio_path = extract(vid_files[0], temp_dir) # Done
# CHECKPOINT 2:
# transcript = Transcribe("temp/vidssave.com The Pursuit Of Happiness - Job interview - Inspirational Movie Scenes Ep. 6 480p.mp3") # Done

transcript = read_transcript()
# Only 1 video for now for testing. It's the final data of a video.
videos_data[0]["transcript"] = transcript

#-----------------------------------# NOW WE HAVE THE DATA WE NEED TO WRITE .ASS FILE #-----------------------------------#

script = ASS(videos_data[0], new_ui.config)

# TODO: calculate font size after obtaining video resolution            [Done]
#       clean and refactor the transcribed segments into usable form    [Done]

#       Write .ass file using the segments and config details and burn it into the video. [Done]

#       Refactor the main code where class is called.
#       Burn the subtitle file into the video file.
#       Allow user to adjust the percentage of the font size instead of actual font size.
#       Add threading feature to allow multiple video files at once.