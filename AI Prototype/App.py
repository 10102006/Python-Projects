"""
  Overview>

"""

# @ Imports
import pyttsx3

# Initialising the engine for the pyttsx3
engine = pyttsx3.init()

# voices = engine.getProperty("voices") # @ For getting voices

# * Changing the voice of the speaker
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# * Defining

# Saying some thing
engine.say("Hello world!")
engine.runAndWait()  # ! Important

# ? Implementation
if __name__ == "__main__":
    #  [print(voice.id) for voice in voices] # @ For finding voices
    pass
