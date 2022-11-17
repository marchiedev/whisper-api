import whisper
import os

model = whisper.load_model("base")
result = model.transcribe(os.path.join(os.getcwd(), 'resources', 'saltwaterroom.mp4'))
print(result["segments"])