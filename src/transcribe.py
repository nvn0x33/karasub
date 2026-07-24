from faster_whisper import WhisperModel
import json

class Transcribe:
    model_size = "medium"
    model = None
    
    def __init__(self):
        Transcribe.model = WhisperModel(Transcribe.model_size, device="cpu", compute_type="int8")
        

    def convert(self, audio_path):
        segments, _ = Transcribe.model.transcribe(audio_path, beam_size=5, word_timestamps=True)
    
        segments = list(segments)
        return self.clean_segments(segments)
        
    def clean_segments(self, segments):
        
        if not segments:
            raise ValueError("Error: segments is corrupted or empty.")
        
        transcript = []
        
        for segment in segments:
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
            
        # self.save_transcript(transcript)
        return transcript
            
    def save_transcript(self, transcript):
        with open ("temp/transcript.json", "a") as file:
            json.dump(transcript, file)
        