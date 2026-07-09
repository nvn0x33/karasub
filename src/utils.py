import os

def rm_extension(file_name):
    file_name = file_name.split(".")
    file_name.pop()
    
    return ".".join(file_name)

def get_vid_files(target_dir):
    supported_exts = [".mp4", ".mkv", ".m4v", ".mov"]
    found_files = []
    
    for item in os.listdir(target_dir):
        _, ext = os.path.splitext(item)

        if ext in supported_exts:
            found_files.append(item)
            
    return found_files