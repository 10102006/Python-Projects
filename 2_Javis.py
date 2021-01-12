"""
    Summary
"""

# * Imports
import pyttsx3
from datetime import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
# @ Defining


def Speak(text):
    """
      What is done:
         1. First saying the text given as param
         2. Then waiting a little for the speech to get completed
    """
    engine.say(text)
    engine.runAndWait()


def WishMe():
    """
      What is done:
         1.
    """
    hour = int(datetime.now().hour)

    if hour <= 12 and hour >= 0:
        Speak('Good Morning sir!')
    elif hour <= 18 and hour >= 12:
        Speak('Good Afternoon sir!')
    elif hour <= 24 and hour >= 18:
        Speak('Good Evening sir!')


def TakeCommand():
    """
      What is done:
         1.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    # try:
    print('Recognising..')
    query = r.recognize_google(audio, language='en-in')
    print('User said ' + str(query))

    # except Exception as error:
    #     print(error)
    # print('Say that again..')
    # return 'none'

    # else:
    return str(query).lower()

# ? Execution
# if __name__ == "__main__":
#     WishMe()
