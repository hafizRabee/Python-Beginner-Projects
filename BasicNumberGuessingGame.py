import random
userchoice=int(input("enter choice:"))
computerchoice=random.randint(1,50)
if(userchoice>computerchoice):
    print("TOO HIGH!")
elif(userchoice<computerchoice):
    print("TOO LOW!")
elif(userchoice==computerchoice):
    print(" CONGRATES YOUR GUESS CORRECT!")
else:
    print("please enter number")
