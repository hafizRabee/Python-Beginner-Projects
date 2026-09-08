print("=====senttence speaker")
import pyttsx3
engine = pyttsx3.init()
sentense=input("enter sentense:")
engine.say(sentense)
engine.runAndWait()