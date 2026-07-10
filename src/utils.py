import os, ffmpeg
from pathlib import Path

def get_resolution(video_path):
    probe = ffmpeg.probe(video_path)
    video_stream = next(s for s in probe["streams"] if s["codec_type"] == "video")
    return video_stream["width"], video_stream["height"]

def rm_extension(file_name):
    file_name = file_name.split(".")
    file_name.pop()
    
    return ".".join(file_name)

def RGB_to_BGR(hex="#FFGGHH"):
    hex = hex.upper().strip("#")
    
    # format example: {\c&H0000FF&}
    new_hex = f"&H{hex[4:6]}{hex[2:4]}{hex[0:2]}&"
    
    return new_hex

def get_vid_files(target_dir):
    supported_exts = [".mp4", ".mkv", ".m4v", ".mov"]
    found_files = []
    
    for item in os.listdir(target_dir):
        _, ext = os.path.splitext(item)

        if ext in supported_exts:
            path = (Path(target_dir) / item).as_posix()
            found_files.append({"name": item, "path": path})
            
    return found_files