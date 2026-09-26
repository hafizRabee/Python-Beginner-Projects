def BinaryToDecimal(n):
  
  result=0
  for i in range(len(n),0,-1):
    pow=len(n)-i
    X=int(n[i-1])
    result+=X*((2)**pow)
  print(result)

try:
  print("Note:This program works only with non-negative integers and does not accept negative or floating-point numbers.")
  n=input("enter bnary:")
  BinaryToDecimal(n)
except ValueError:
  print("please enter Valid binary number")






  