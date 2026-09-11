def prime(n):
  if(n<2):
    return -1
  root=int((n**0.5)+1)
  
  for i in range(2,root,1):
    if(n%i==0):
      return 1    
  else:
      return 0
n=int(input("enter n:"))
result=prime(n)
if(result==1):
  print("not prime")
elif(result==0):
  print("prime")
else:
  print("please enter greater than or equal to 2")