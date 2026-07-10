import ffmpeg
from pathlib import Path
from .utils import rm_extension

def extract(vid_file, out_dir):
    # Create audio path with same name as video file
    audio_path = Path(out_dir) / (rm_extension(vid_file["name"]) + ".mp3")
    audio_path = audio_path.as_posix()

    print(audio_path)
    
    # Create references to input video and output video
    input_vid = ffmpeg.input(vid_file["path"])
    out_audio = ffmpeg.output(input_vid.audio, audio_path)
    
    # Output the audio
    ffmpeg.run(out_audio, overwrite_output=True)
    
    # Return the audio path
    return audio_path