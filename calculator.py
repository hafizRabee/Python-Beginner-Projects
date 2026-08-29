a=int(input("enter a:"))
b=int(input("enter b:"))
operation=input("enter operation:")
if(operation=="+"):
    print(f"adiidtion:{a+b}")
elif(operation=="-"):
    print(f"subtraction:{a-b}")
elif(operation=="*"):
    print(f"multiplication:{a*b}")
elif(operation=="/"):
    print(f"division:{a/b}")
else:
    print("enter +,-,/,*")
