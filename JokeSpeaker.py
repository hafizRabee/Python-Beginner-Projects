print("=====JokeSpeaker====")
import pyjokes
import pyttsx3
jokes=pyjokes.get_joke()
engine = pyttsx3.init()
engine.say(jokes)
engine.runAndWait()
