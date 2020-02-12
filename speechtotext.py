# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:45:32 2020

@author: sabih
"""

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()  

print("what is your name")
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