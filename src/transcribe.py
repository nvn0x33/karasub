from faster_whisper import WhisperModel

class Transcribe:
    model_size = "small"
    
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.convert()

    def convert(self):
        model = WhisperModel(self.model_size, device="cpu", compute_type="int8")
        segments, _ = model.transcribe(self.audio_path, beam_size=5, word_timestamps=True)
        
        segments = list(segments)
        # for segment in segments:
        #     print(segment)