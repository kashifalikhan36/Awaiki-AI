from gtts import gTTS

class AudioBook():
    def __init__(self):
        pass

    def text_to_speech(self, text):
        output_file="./ebook_and_audiobook/input.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(output_file)
        print(f"Text converted to speech and saved as {output_file}")