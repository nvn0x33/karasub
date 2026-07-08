from faster_whisper import WhisperModel

model_size = "small"

def convert(audio_path):
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_path, beam_size=5, word_timestamps=True)
    
    segments = list(segments)
    for segment in segments:
        print(segment)