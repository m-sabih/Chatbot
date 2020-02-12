# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:18:00 2020

@author: sabih
"""

import webbrowser
import pyowm
import speech_recognition as sr
cmd1 = ['open browser', 'open google','google']
cmd2 = ['open youtube', 'youtube']
cmd3 = ['tell me the weather', 'weather', 'what about the weather']
CONVERSING = True

r = sr.Recognizer()
mic = sr.Microphone() 

while CONVERSING:
    print("what do you want to open")
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    with mic as source:
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
    try:
        cmd=r.recognize_google(audio)
    except sr.RequestError:
        print("API unavailable")
        cmd="no"
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        cmd="no"
        
        
    if cmd in cmd1:
        print("opening google")
        webbrowser.open('www.google.com')
    elif cmd in cmd2:
        print("opening youtube")
        webbrowser.open('www.youtube.com')
    elif cmd in cmd3:
        owm = pyowm.OWM('0708e28f0e3d4b2357549e2ec5993999')
        observation = owm.weather_at_place('Lahore,pk')
        w = observation.get_weather()
        temp=w.get_temperature('celsius')
        print(temp)
        temp=str(temp['temp'])
        print("" + temp + " celcius")
        #print(" Celcius")
    else:
        webbrowser.open_new('www.google.com/search?q=' + cmd)
    
