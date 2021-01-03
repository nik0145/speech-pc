#! /usr/bin/env python
# -*- coding: utf-8 -*-
import imp
import speech_recognition as sr 
import os
import sys
import webbrowser

def talk(word):
    print(word)
    os.system("say "+ word)

talk("ДДарова?")

def command():
    r = sr.Recognizer()
    r.energy_threshold=4000
    with sr.Microphone() as source:
        print("Базарь")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        wordss = r.recognize_google(audio, language = "ru-RU")
        print("Вы сказали "+ wordss.lower() )
    except sr.UnknownValueError:
        talk("не понятно")
    return wordss
command()