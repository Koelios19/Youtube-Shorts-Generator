import time
import FactTeller as ft
import whisper_timestamped as whisper

def transcribe():
    audio =  whisper.load_audio("facts.mp3")
    model = whisper.load_model("tiny", device="cpu")
    result = whisper.transcribe(model, audio, language="en")
    return result
