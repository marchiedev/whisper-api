import argparse
import os
from moviepy.editor import *
import librosa

def extract_voice_from_music(mp3_file_name: str):
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # take filename argument
    parser.add_argument("--file_name", type=str, default="saltwaterroom.mp4", help="mp4 file name")

    args = parser.parse_args()

    # read mp4 video
    video = VideoFileClip(os.path.join(os.getcwd(), "resources", args.file_name))

    mp3_file_name =  args.file_name.split('.')[0] + '.mp3'

    # convert mp4 to mp3
    video.audio.write_audiofile(os.path.join(os.getcwd(), "resources", mp3_file_name))

    # extract voice fron mp3 music
    extract_voice_from_music(mp3_file_name) # ??