try:
    print("===Welcome To EvenOdd Checker===")
    number=int(input("enter a number:"))
    if(number%2==0):
      print(f"{number} is even")
    else:
      print(f"{number} is odd")
except ValueError:
   print(f"please enter Valid number")


