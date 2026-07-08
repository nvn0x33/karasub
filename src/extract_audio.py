import ffmpeg
from pathlib import Path

def extract(inp_dir, vid_file, out_dir):
    audio_path = Path(out_dir) / (rm_extension(vid_file) + ".mp3")
    audio_path = audio_path.as_posix()

    print(audio_path)
    
    input_vid = ffmpeg.input(inp_dir+vid_file)
    out_audio = ffmpeg.output(input_vid.audio, audio_path)
    
    ffmpeg.run(out_audio, overwrite_output=True)
    
    return audio_path
    
def rm_extension(file_name):
    file_name = file_name.split(".")
    file_name.pop()
    
    return ".".join(file_name)