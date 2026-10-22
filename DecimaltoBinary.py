def decimaltobinary(num):
  b=bin(num)
  string=str(b)
  
  return string[2:]

num=int(input("enter your decimal:"))
result=decimaltobinary(num)
print(f"binary:{result}")