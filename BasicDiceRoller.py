import random
choice=input("you want to rolled dice? enter yes/no:").lower()
if(choice=="yes"):
    number=random.randint(1,6)
    print(f"dice rolled:{number}")
elif(choice=="no"):
    print(f"dice not rolled")
else:
    print("please enter yes/no")