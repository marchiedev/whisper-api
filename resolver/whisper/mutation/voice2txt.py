import whisper
import os

def voice2txt(file_location, return_type):
    model = whisper.load_model("base")
    result = model.transcribe(file_location)
    res = result[return_type if return_type else "text"]
    return res