import ffmpeg
from pathlib import Path

def burn_subtitle(video_path, ass_path, fontdir_path, video_out):
    ass_path = Path(ass_path).as_posix()
    fontdir_path = Path(fontdir_path).as_posix()
    
    print("Burning stylized ASS subtitles with custom fonts...")
    
    video_stream = ffmpeg.input(video_path)
    audio_stream = video_stream.audio
    
    try:
        vid_with_subs = video_stream.video.filter(
            "subtitles",
            filename=ass_path,
            fontsdir=fontdir_path
        )
        
        (
            ffmpeg
            .output(vid_with_subs, audio_stream, video_out)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"Success! Final video built at: {video_out}")
        
    except Exception as err:
        print(err.stderr.decode("utf-8"))
        
    
