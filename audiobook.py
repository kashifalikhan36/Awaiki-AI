from gtts import gTTS
from pydub import AudioSegment

class AudioBook():
    def __init__(self):
        pass

    def text_to_speech(self, text):
        output_file="./ebook_and_audiobook/input.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(output_file)
        print(f"Text converted to speech and saved as {output_file}")

    def audio_editor(self,text):
        def add_background_effect(original_audio_path, background_effect_path, output_file_path):
            original_audio = AudioSegment.from_file(original_audio_path, format="mp3")
            background_effect = AudioSegment.from_file(background_effect_path, format="mp3")

            # Adjust the duration of the background effect to match the original audio
            desired_duration = len(original_audio)
            background_effect = background_effect[:desired_duration]

            # Mix the two audio segments together with the desired volume levels
            mixed_audio = original_audio.overlay(background_effect, position=0, gain_during_overlay=-20)

            # Export the mixed audio to a new file
            mixed_audio.export(output_file_path, format="mp3")

        # Example usage
        original_audio_path = "./ebook_and_audiobook/input.mp3"
        background_effect_path = "path_to_background_effect.mp3"
        output_file_path = "output_file_path.mp3"

        add_background_effect(original_audio_path, background_effect_path, output_file_path)
