def GCD_LCM(a,b):
  if(a==0 and b==0):
     return "M"

  elif(b==0):
    return a
  elif(a%b==0):
     return b
  else:
     return GCD_LCM(b,a%b)
try:
  print(f"===GCD & LCM Calcuator===")
  a=int(input("enter a:"))
  b=int(input("enter b:"))
  
  Result=GCD_LCM(a,b)
  if(Result=="M"):
    print(f"Not both a and b should be zero")
  else:
    
    print(f"GCD:{Result}")
    print(f"LCM:{a*b//Result}")
except ValueError:
  print("please enter number")

  

