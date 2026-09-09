print("====Temperature converter====")
print("1.Celsius to fahrenheit")
print("2.Fahremheit to celsius")
print("3.Celsius to Kelvin")
print("4.Fahrenheit to Kelvin")
print("5.Kelvin to Celsius")
print("6.Kelvin to Fahrenheit")

try:
    choice=int(input("enter choice 1/2/3/4/5/6:"))
    if(choice==1):
        Celsius=float(input("enter Celsius temperature:"))
        Fahrenheit=9/5*(Celsius)+32
        print(f"Celsius to fahrenheit:{Fahrenheit}")
    elif(choice==2):
        Fahrenheit=float(input("enter Fahrenheit temperature:"))
        Celsius=5/9*(Fahrenheit-32)
        print(f"Fahrenheit to celsius:{Celsius}")
    elif(choice==3):
        Celsius=float(input("enter Celsius temperature:"))
        Kelvin=Celsius+273.15
        print(f"Celsius to Kelvin:{Kelvin}")
    elif(choice==4):
        Fahrenheit=float(input("enter Fahrenheit temperature:"))
        Celsius=5/9*(Fahrenheit-32)
        Kelvin=Celsius+273.15
        print(f"Fahrenheit to Kelvin:{Kelvin}")
    elif(choice==5):
            Kelvin=float(input("enter Kelvin temperature:"))
            Celsius=Kelvin-273.15
            print(f"Kelvin to Celsius:{Celsius}")
    elif(choice==6):
            Kelvin=float(input("enter Kelvin temperature:"))
            Celsius=Kelvin-273.15
            Fahrenheit=9/5*(Celsius)+32
            print(f"Kelvin to Fahrenheit:{Fahrenheit}")
    else:
        print(f"wrong choice choose (1-6)")
    
except ValueError:
     print(f"please enter your choice 1-6")


