# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:41:03 2020

@author: sabih
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:20:06 2019

@author: sabih
"""

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)


engine.say("What is your name")
engine.runAndWait()
name=input("What is your name" + "\n")
print("Hello "+name+" how may i help you?")
engine.say("Hello "+name+" how may i help you?")
engine.runAndWait()