import pygame
import time
from flask import Flask, request

app = Flask(__name__)

# Initialize pygame
pygame.init()

# List of audio files to play
audio_files = [
    "sounds/1.mp3",
    "sounds/2.mp3",
    "sounds/3.mp3",
    "sounds/4.mp3",
    "sounds/5.mp3",
    "sounds/6.mp3",
    "sounds/7.mp3",
    "sounds/8.mp3",
    "sounds/9.mp3",
    "sounds/10.mp3",
    "sounds/11.mp3",
    "sounds/12.mp3",
    "sounds/13.mp3",
    "sounds/14.mp3",
    "sounds/15.mp3",
    "sounds/16.mp3",
    "sounds/17.mp3",
    "sounds/18.mp3",
    "sounds/19.mp3",
    "sounds/20.mp3",
    # Add paths to all your audio files
]

# Function to play audio files with intervals
def play_audio_files_with_interval(audio_files, interval):
    for file in audio_files:
        try:
            # Load and play the audio file
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()

            # Wait for the audio to finish
            while pygame.mixer.music.get_busy():
                pass

            # Pause for the specified interval
            time.sleep(interval)
        except pygame.error:
            print(f"Error playing {file}")

@app.route('/run-code', methods=['GET'])
def run_code():
    audio_index = request.args.get('audio', type=int) - 1  # Adjust for 0-based index
    if 0 <= audio_index < len(audio_files):
        play_audio_files_with_interval([audio_files[audio_index]], interval=5)
        return "Code execution triggered."
    else:
        return "Invalid audio index."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
