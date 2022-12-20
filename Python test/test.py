from gtts import gTTS
from pygame import mixer

def text_to_speech(text: str):
    # Create a gTTS object and get the audio data
    tts = gTTS(text=text, lang='en')
    audio_data = tts.get_audio()

    # Play the audio using pygame
    mixer.init()
    mixer.music.load(audio_data)
    mixer.music.play()

# Convert the text "Hello, World!" to speech and play it
text_to_speech("Hello, World!")
