# pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.say("My name is Krishna")
engine.runAndWait()