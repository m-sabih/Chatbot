# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:20:06 2019

@author: sabih
"""

import random
import datetime
import webbrowser
import pyowm
import pyttsx3
import speech_recognition as sr
CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','hey','wassup','yo']
questions = ['how are you?','how are you','how are you doing?','how are you doing']
responses = ['Okay','I am fine']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
que1 = ['who made you', 'who created you','who made you?', 'who created you?']
ans1 = ['I was created by Sabih', 'Sabih', 'A really great guy who i never got to know','what do you mean? i am also a human! silly question']
que2 = ['what time is it', 'what is the time', 'time','what time is it?', 'what is the time?', 'time?']
que3 = ['who are you', 'what is your name','who are you?', 'what is your name?','whats your name']
ans3=  ['I am a bot','i am anything you want me to be']
que4 = ['what is your color', 'what is your colour', 'your color', 'your color?','what is you favourite colour', 'what is your favourite color']
ans4 = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
que5 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
ans5 = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd1 = ['open browser', 'open google','google']
cmd2 = ['open youtube', 'youtube']
cmd3 = ['tell me the weather', 'weather', 'what about the weather']
cmd4 = ['exit', 'close', 'goodbye','bye','quit']
cma4 = ['see you soon?','bye, take care','bye']
cmd5 = ['thank you','you are nice']
ans = ['youre welcome', 'glad i could help you']

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
name = input()
print("Hello "+name+" how may i help you?")
engine.say("Hello "+name+" how may i help you?")
engine.runAndWait()

while CONVERSING:
    r = sr.Recognizer()
    mic = sr.Microphone()    
    lang = 'en-US'
    speed = .1
    userInput = input(">>> " + name +": ").lower()
    print(">>> " + name +": ")
    time = datetime.datetime.now()
    
    
    
    if userInput in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
        memory.append((userInput,random_greeting))
    elif userInput in questions:
        random_response = random.choice(responses)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in verifications:
        random_response = random.choice(validations)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in que1:
        random_response = random.choice(ans1)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in que2:
        print("Current date and time : ")
        print(time.strftime("The time is %H:%M"))
        memory.append((userInput,time.strftime("The time is %H:%M")))
        engine.say(time.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif userInput in que3:
        random_response = random.choice(ans3)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in que4:
        random_response = random.choice(ans4)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in que5:
        random_response = random.choice(ans5)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif userInput in cmd1:
        engine.say("opening google")
        engine.runAndWait()
        webbrowser.open('www.google.com')
        memory.append(userInput)
    elif userInput in cmd2:
        engine.say("opening youtube")
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
        memory.append(userInput)
    elif userInput in cmd3:
        owm = pyowm.OWM('0708e28f0e3d4b2357549e2ec5993999')
        observation = owm.weather_at_place('Lahore,pk')
        w = observation.get_weather()
        temp=w.get_temperature('celsius')
        engine.say(temp)
        engine.runAndWait()
        temp=str(temp['temp'])
        print("" + temp + " celcius")
        #print(" Celcius")
        memory.append((userInput,temp))
    elif userInput in cmd4:
        random_response = random.choice(cma4)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
        CONVERSING=False
        print('\n')
    elif 'sure' in userInput:
        response = "Sure about what?"
        memory.append(('sure',response))
        engine.say(response)
        engine.runAndWait()
        print(response)
    elif 'why' in userInput:
        response = "What why?"
        memory.append(('why',response))
        engine.say(response)
        engine.runAndWait()
        print(response)        
    elif userInput in cmd5:
        random_response = random.choice(ans)
        memory.append((userInput,random_response))
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)        
    else:
        print("I did not understand what you said")        
        engine.say("I did not understand what you said")
        engine.say("Do you want to search it in google? yes or no")
        engine.runAndWait()
#        res = input("Do you want to search it in google? yes/no" + "\n")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            res=r.recognize_google(audio)
        except sr.RequestError:
            print("API unavailable")
            res="no"
        except sr.UnknownValueError:
            print("Unable to recognize speech")
            res="no"
        if res=='yes':
            webbrowser.open_new('www.google.com/search?q=' + userInput)            
        
for conversations in memory:
	print(conversations)