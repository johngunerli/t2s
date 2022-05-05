# Python program to translate

# speech to text and text to speech



import speech_recognition as sr

import pyttsx3

from greeters import greeters
from curses import curses

from SpeakText import t2s
from op import open_site
from op import search_site
import time



# Initialize the recognizer

r = sr.Recognizer()

print("Welcome! How may I assist you?")



while(1):


    # Exception handling to handle

    # exceptions at the runtime

    try:


        # use the microphone as source for input.

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)


            # listens for the user's input

            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2)

            MyText = MyText.lower()


            # this is for us to check what the user said

        value_of_greeters = greeters(MyText)

       	value_of_curses = curses(MyText)

        value_of_open =0

        value_of_search=0

        if 'open' in MyText:

            value_of_open = open_site(MyText)

        else:

        	value_of_search = search_site(MyText)
        

        # if the functions return nonzero, then say I did not understand

        if value_of_greeters != 0 and value_of_curses != 0 and value_of_open != 0 and value_of_search != 0:
           t2s("I did not understand what you said")

           print("What i understood was", MyText)

    except sr.UnknownValueError:    

        print("error, please run again.")

