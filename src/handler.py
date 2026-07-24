from pathlib import Path

from . import Transcribe, UI, ASS
from . import extract, burn_subtitle, get_resolution

import os
import multiprocessing

class Handle:
    default_font = "fonts/RobotoMono-Medium.ttf"
    
    input_dir = Path("input")
    output_dir = Path("output")
    temp_dir = Path("temp")
    
    videos_data = []
    config = {}
    
    def __init__(self):
        self.create_folders()
        
    def init_UI(self):
        new_ui = UI(Handle.default_font, Handle.input_dir)
        vid_files = new_ui.print_UI()
        
        new_ui.correct_config()
        Handle.config = new_ui.config
        
        return vid_files
    
    def parallel_process_vids(self):
        pass
    
    def process_video(self, video):
        # Extract audio
        audio_path = extract(video, Handle.temp_dir)
        # Clean segments and create transcript data
        new_transcript = Transcribe(audio_path)
        transcript_data = new_transcript.convert()
        # Append transcript data into video
        video["transcript"] = transcript_data
        # Initiate .ass subtitle file
        new_script = ASS(video, Handle.config)
        # Write script and get its path
        path_to_sub = new_script.write_script()
        # Create path 
        font_folder = os.path.dirname(Handle.config["font_style"])
        vid_out = (Path(Handle.output_dir) / video["name"]).as_posix()

        # Final output with subtitle + video.
        burn_subtitle(video["path"], path_to_sub, font_folder, vid_out)
    
    def append_font_data(self, vid_files):
        for video in vid_files:
            width, height = get_resolution(video["path"])
            
            if Handle.config["font_size"] == "auto":
                font = min(width, height) * 0.060
            else:
                font = Handle.config["font_size"]
            
            Handle.videos_data.append(
                {**video, 
                "resX": width,
                "resY": height,
                "font_size": int(font), 
                "transcript": []})
        
    def create_folders(self):
        Handle.input_dir.mkdir(parents=True, exist_ok=True)
        Handle.output_dir.mkdir(parents=True, exist_ok=True)
        Handle.temp_dir.mkdir(parents=True, exist_ok=True)
    
    