import time
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import os

def take_command():

    r = sr.Recognizer()
    fs = 16000
    seconds = 5

    print("Listening... Speak now")
    time.sleep(1)

    try:
        # record audio
        audio_data = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        write("voice.wav", fs, audio_data)

        print("Recording saved")

        # check file exists
        if not os.path.exists("voice.wav"):
            print("Audio file not created")
            return "none"

        # read audio
        with sr.AudioFile("voice.wav") as source:
            audio = r.record(source)

        print("Recognizing...")

        voice_data = r.recognize_google(audio)
        voice_data = voice_data.lower()

        print("You said:", voice_data)

        return voice_data

    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none"

    except sr.RequestError:
        print("Internet connection error")
        return "none"

    except Exception as e:
        print("Error:", e)
        return "none"


# for testing this file alone
if __name__ == "__main__":
    take_command()