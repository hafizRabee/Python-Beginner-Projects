i=4
while i>=1:
    try:
       CORRECTPIN=6590683
       PIN=int(input("enter your PIN:"))
       if(PIN!=CORRECTPIN):
            print(f"please enter valid pin")
            print(f"{i-1} attempts left")
            i=i-1 
       elif(PIN==CORRECTPIN):
            print(f"Succeed!")  
            break
   
    except ValueError:
        print(f"please enter PIN in numbers")
   
    





