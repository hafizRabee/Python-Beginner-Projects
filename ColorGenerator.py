import random
colors=["red","pink","purple","yellow","brown","white","gold","navy","silver","gray","black","green","teal","violet","maroon","orange"]
while True:
    choice=input("you want to generate color? enter yes/no:").lower()
    if(choice=="yes"):
        print(f"color:{random.choice(colors)}")
    elif(choice=="no"):
        print(f"exist")
        break
    else:
        print(f"please enter yes/no")
