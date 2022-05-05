import speech_recognition as sr

import pyttsx3



def t2s(command):

    # Initialize the engine

    engine = pyttsx3.init()

    engine.say(command)

    engine.runAndWait()

