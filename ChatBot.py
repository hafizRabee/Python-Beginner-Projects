import datetime
import pyjokes
import pyttsx3

joke=pyjokes.get_joke()
engine = pyttsx3.init()

Question=input("enter what you want?").lower()
if(Question=="hello" or Question=="hi"):
    engine.say("Hello! How can i Help You?")
elif(Question=="how are you" or Question=="how are you?"):
    engine.say("I'm great,thanks for asking!")
elif(Question=="what is your name" or  Question=="what is your name?" ):
    engine.say("I am your python chatbot")
elif(Question=="who made you" or  Question=="who made you?" ):
    engine.say("I was created by Hafiz M.Rabee(python Developer)")
elif(Question=="who is hafiz M.Rabee" or  Question=="who is hafiz M.Rabee?" ):
    engine.say(" He is python Developer and he is currently pursuing BSCS Degree from iqra university")
elif(Question=="what is github" or  Question=="what is github?" ):
    engine.say("Github is a platform to store and share code")

elif(Question=="tell me a joke" or  Question=="give me a joke?" ):
    engine.say(joke)
elif(Question=="what is python" or  Question=="what is python?" ):
    engine.say("it is a programming language created by GUIDO VAN ROSSUM")

elif(Question=="thanks" ):
    engine.say("You are welcome!")
elif(Question=="what is the capital of pakistan?" or Question=="what is the capital of pakistan"):
    engine.say("Islamabad")
elif("/0" in Question):
    engine.say("Cant divide by zero")
    
elif("day" in Question or "din" in Question):
    d=datetime.datetime.now().strftime("%A")
    engine.say(d)
elif("tarekh" in Question or "date" in Question):
    d=datetime.date.today().strftime("%B %d, %Y")
    engine.say(d)
elif(Question=="bye" or Question=="goodbye"):
    engine.say("Goodbye! Have a great day!")

elif("what is the factorial" in Question or "what is the factorial?" in Question):
    def factorialcalculator(n):
      fact=1
 
      if(n<0):
        engine.say("please enter greater than or equal to zero")
    
      elif(n==0 or n==1):
        engine.say(f"factorial of {n} is 1")
    
      else:
        for i in range(n,0,-1):
         fact*=i

    
        engine.say(f"factorial of {n} is {fact}")
    try:
      n=int(input("enter a number:"))
      factorialcalculator(n)
    except ValueError:
       engine.say("please enter number")
       
 
else:
   engine.say("Sorry, I don't understand that.")


engine.runAndWait()







     






     



