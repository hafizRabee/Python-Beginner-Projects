print("===Factorial Calculator===")
def factorialcalculator(n):
  fact=1
 
  if(n<0):
    print("please enter greater than or equal to zero")
    
  elif(n==0 or n==1):
    print(f"factorial of {n} is 1")
    
  else:
    for i in range(n,0,-1):
       fact*=i

    print(f"factorial of {n} is {fact}")
n=int(input("enter a number:"))
factorialcalculator(n)
