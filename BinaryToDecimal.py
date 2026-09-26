def BinaryToDecimal(n):
  if set(n) <= {"0", "1"}:
    result=0
    for i in range(len(n),0,-1):
      pow=len(n)-i
      X=int(n[i-1])
      result+=X*((2)**pow)
    print(result)
  else:
   print("binary only contain 0/1")

try:
  print("Note:This program accepts only non-negative binary integers containing 0s and 1s. Negative numbers and floating-point values are not supported.")
  n=input("enter binary:")
  BinaryToDecimal(n)
except ValueError:
  print("please enter Valid binary number")






  
