import whisper
import os

def voice2txt(file_location):
    model = whisper.load_model("base")
    result = model.transcribe(file_location)
    res = result["text"]
    return res