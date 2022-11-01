from typing import Union, Optional

from fastapi import FastAPI, Form, UploadFile, File

import os

#mutations
from resolver.test.query.test import test
from resolver.whisper.mutation.voice2txt import voice2txt

app = FastAPI()

@app.get("/")
def read_root():
    res = test()
    return res

@app.post('/voice-to-text/voice2txt')
def generate_image_to_image(voice_file: UploadFile = File()):
    is_inputs_folder_exist = os.path.exists(os.path.join(os.getcwd(), 'resources', 'inputs'))
    inputs_folder = os.path.join(os.getcwd(), 'resources', 'inputs')

    if not is_inputs_folder_exist:
        os.mkdir(inputs_folder)

    file_location = os.path.join(inputs_folder, voice_file.filename)

    with open(file_location, "wb+") as file_object:
        file_object.write(voice_file.file.read())

    res = voice2txt(file_location)

    return { "voice2txt": res }