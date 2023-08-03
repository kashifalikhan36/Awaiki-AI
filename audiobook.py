from gtts import gTTS

class AudioBook():
    def __init__(self):
        pass

    def text_to_speech(self, text):
        output_file="C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\ebook_and_audiobook\\output.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(output_file)
        print(f"Text converted to speech and saved as {output_file}")