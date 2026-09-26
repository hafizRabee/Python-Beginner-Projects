def Fibonacci_generator(n):
  li=[0,1]
  if(n<0):
      print("please enter number greater than or equal to zero")
  elif(n==0):
    print("")
  elif(n==1):
    print("0")
  elif(n==2):
    print("0,1")
  else:
    for i in range(n-2):
      
      li.append(li[i]+li[i+1])
    sequence=",".join(map(str,li))
    print(sequence)
try:
 n=int(input("enter n:"))
 Fibonacci_generator(n)
except ValueError:
    print("please enter valid number ")