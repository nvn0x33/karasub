import ffmpeg
from pathlib import Path
from .utils import rm_extension

def extract(inp_dir, vid_file, out_dir):
    vid_path = Path(inp_dir) / vid_file
    vid_path = vid_path.as_posix()
    
    audio_path = Path(out_dir) / (rm_extension(vid_file) + ".mp3")
    audio_path = audio_path.as_posix()

    print(audio_path)
    
    input_vid = ffmpeg.input(vid_path)
    out_audio = ffmpeg.output(input_vid.audio, audio_path)
    
    ffmpeg.run(out_audio, overwrite_output=True)
    
    return audio_path