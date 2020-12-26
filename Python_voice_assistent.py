import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
import datetime
import subprocess
import webbrowser

#defs
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

def note(text):
    file_name = str(text)
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def pivot(text):
    pivot='C:\Program Files (x86)\Pivot Animator'
    subprocess.Popen([pivot])

text = get_audio()
# if
WAKE = "robot"
print("Start")
while True:
    print("Listening...")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("yes")
        text = get_audio()
        if "hello" in text:
                speak("hello, how are you?")
        elif "what is your name" in text:
                speak("it is not decided yet")

        NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
        for phrase in NOTE_STRS:
                if phrase in text:
                        speak("What would you like me to write down? ")
                        write_down = get_audio()
                        note(write_down)
                        speak("I've made a note of that.")
        if "break" in text:
            print("breaking")
            break
        Search_strs=["search on Google",'Google','search']
        for phrase in Search_strs:
                if phrase in text:
                    speak('what should I search for you')
                    gsearch=get_audio()
                    webbrowser.open('https://www.google.com/?#q='+gsearch)
        

        Instagram_strs=["open Instagram",'Insta','Instagram']
        for phrase in Instagram_strs:
                if phrase in text:
                    speak('Opening Instagram')
                    gsearch=get_audio()
                    webbrowser.open('https://www.instagram.com')
                    speak('this should do')

        Discord_strs=["open discord",'discord']
        for phrase in Discord_strs:
                if phrase in text:
                    speak('Opening Discord')
                    gsearch=get_audio()
                    webbrowser.open('https://discord.com/channels/@me')
                    speak('this should do')
        
        
        Pivot_STRS = ["pivot", "open pivot"]
        for phrase in Pivot_STRS:
                if phrase in text:
                        speak("Opening Pivot")
                        pivot1 = get_audio()
                        pivot1(pivot)
                        speak("this should Do")