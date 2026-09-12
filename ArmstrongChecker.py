def armstrongchecker(n):
  num=list(n)
  listsum=0
  length=len(num)
  
  for k in num:
    listsum=listsum+(int(k)**length)
  if(listsum==int(n)):
    print("armstrong")
  else:
    print("not armstrong")
n=input("enter n:")
armstrongchecker(n)
