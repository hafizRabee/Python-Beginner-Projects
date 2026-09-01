import random
userchoice=input("enter your choice:")
choices=["snake","water","gun"]
computerchoice=random.choice(choices)
if(userchoice==computerchoice):
    print(f"congratulations YOU WIN!")
elif(userchoice not in choices):
    print(f"plese enter eiter snake/water/gun")
else:
    print(f"computer win!")
