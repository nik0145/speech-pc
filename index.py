import imp
sr = imp.load_source('speech_recognition', '/home/kolya/.local/lib/python3.8/site-packages/speech_recognition/__init__.py')

import os
import sys
import webbrowser

def talk(word):
    print(word)
    os.system("say "+ word)

talk("Hi")