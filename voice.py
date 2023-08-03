from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)
    print(f"Text converted to speech and saved as {output_file}")

if __name__ == "__main__":
    # Replace 'Your desired text here' with the text you want to convert to speech
    desired_text = "Your desired text here"
    output_file = "output.mp3"  # Output file name (default: output.mp3)

    text_to_speech(desired_text, output_file)
