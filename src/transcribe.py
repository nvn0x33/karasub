from faster_whisper import WhisperModel

class Transcribe:
    model_size = "small"
    model = None
    
    def __init__(self, audio_path):
        self.audio_path = audio_path
        Transcribe.model = WhisperModel(Transcribe.model_size, device="cpu", compute_type="int8")
        
        self.convert()

    def convert(self):
        segments, _ = Transcribe.model.transcribe(self.audio_path, beam_size=5, word_timestamps=True)
    
        segments = list(segments)
        self.clean_segments(segments)
        
    def clean_segments(self, segments):
        
        if segments is None or len(segments) < 1:
            raise ValueError("Error: segments is corrupted or empty.")
        
        transcript = []
        
        for segment in segments:
            print(segment.id, segment.start, type(segment.start))
            words = []
            
            for raw_word in segment.words:
                word_data = {
                    "word": raw_word.word.strip(),
                    "start": float(f"{raw_word.start:.2f}"),
                    "end": float(f"{raw_word.end:.2f}")
                }
                words.append(word_data)
                
            data = {
                "id": int(segment.id),
                "start": float(f"{segment.start:.2f}"),
                "end": float(f"{segment.end:.2f}"),
                "text": segment.text.strip(),
                "words": words
            }
            
            transcript.append(data)
        # transcript = [
		#     {
        #         "id": "segment_1",
        #         "start": 11.29,
        #         "end": 12.1,
        #         "text": ' Chris Gardner' (strip it),
        #         "words": [
        #             {"word": "Chris", "start": 12.1, "end": 12.1},
        #             {"word": "Chris", "start": 12.1, "end": 12.58},
        #             ...
        #         ]
        #     }
        # ]
        