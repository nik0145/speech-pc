#! /usr/bin/env python
# -*- coding: utf-8 -*-
import imp
import speech_recognition as sr 
import os
import sys
import webbrowser

def talk(word):
    print(word)
    os.system("spd-say \""+ word+"\"")
talk("I listen to you master")
def onStart():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold=4000
    with sr.Microphone() as source:
        
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source,phrase_time_limit=2)
        except sr.WaitTimeoutError:
            talk("I do not understand you")
            words = onStart()
    try:
        words = recognizer.recognize_google(audio, language = "ru-RU").lower()
    except sr.UnknownValueError:
        talk("I do not understand you")
        words = onStart()
    return words

def onCheckPhrase(value):
    # сделать из этого конфиг
    print("вы сказали",value)
    if 'включи музыку' in value:
        url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'
        webbrowser.open(url)
    elif 'стоп' in value:    
        sys.exit()
    elif 'браузер' in value:    
        os.system("firefox")
    elif 'выключи компьютер' in value:    
        os.system("sudo shutdown -h now")
       
    elif 'запустить tracker' in value:  
        #  os.system("gnome-terminal --e \"bash -c \"sudo /usr/share/AppStaff/AppStaff.sh ; exec bash\"\"")
        os.system("gnome-terminal -- bash -c \"sudo /usr/share/AppStaff/AppStaff.sh; exec bash\"")
    elif 'привет' in value:    
        talk("hi")
        

while True:
    onCheckPhrase(onStart())