print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")
choice=int(input("enter your choice 1/2/3:"))
if(choice==1):
    celcius=float(input("enter celcius temperature:"))
    Fahrenheit=9/5*(celcius)+32
    print(f"celsius to fahrenheit:{Fahrenheit}")

elif(choice==2):
    KM=float(input("enter kilometers:"))
    Miles=KM*0.621371
    print(f"Kilometers to Miles:{Miles}")
elif(choice==3):
    KG=float(input("enter kilograms:"))
    pounds=KG*2.205
    print(f"kilograms to pounds:{pounds}")