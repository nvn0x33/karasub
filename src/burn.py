import ffmpeg
from pathlib import Path

def burn_subtitle(video_path, ass_path, fontdir_path, video_out):
    ass_path = Path(ass_path).as_posix()
    print(ass_path)
    fontdir_path = Path(fontdir_path).as_posix()
    
    print("Burning stylized ASS subtitles with custom fonts...")
    
    video_stream = ffmpeg.input(video_path)
    audio_stream = video_stream.audio
    
    filter_q = {
        "force_style": 'CollisionCorrection=1,Alignment=2,MarginV=20',
    }
    
    try:
        vid_with_subs = video_stream.video.filter(
            "ass",
            filename=ass_path,
            fontsdir=fontdir_path,
        )
        
        (
            ffmpeg
            .output(vid_with_subs, audio_stream, video_out, vcodec="libx264", acodec="copy")
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
            
        )
        # args = ffmpeg.output(vid_with_subs, audio_stream, video_out).overwrite_output().compile()
        # print(args)
        
        print(f"Success! Final video built at: {video_out}")
        
    except ffmpeg.Error as err:
        print("FFmpeg Error:", err.stderr.decode("utf-8"))
        
    
