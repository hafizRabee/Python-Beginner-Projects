print("1.celcius to fahrenheit")
print("2. Fahrenheit to celcius")
choice=int(input("enter your choice:"))
if(choice==1):
    Celcius=float(input("enter celcius temperature:"))
    Fahrenheit=9/5*(Celcius)+32
    print(f"celcius to fahrenheit:{Fahrenheit}")
elif(choice==2):
    Fahrenheit=float(input("enter Fahrenheit temperature:"))
    Celcius=5/9*(Fahrenheit-32)
    print(f"Fahrenheit to celcius:{Celcius}")
    