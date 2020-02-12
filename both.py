# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:15:29 2020

@author: sabih
"""


import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
r = sr.Recognizer()
mic = sr.Microphone()  

engine.say("What is your name")
engine.runAndWait()
if not isinstance(r, sr.Recognizer):
    raise TypeError("`recognizer` must be `Recognizer` instance")
if not isinstance(mic, sr.Microphone):
    raise TypeError("`microphone` must be `Microphone` instance")
with mic as source:
     r.adjust_for_ambient_noise(source)
     audio = r.listen(source)
try:
    name=r.recognize_google(audio)
except sr.RequestError:
    print("API unavailable")
    name="User"
except sr.UnknownValueError:
    print("Unable to recognize speech")
    name="User"
    
print("Hello "+name+" how may i help you?")
engine.say("Hello "+name+" how may i help you?")
engine.runAndWait()
