print("====Palndrome checker====")
def palindromechecker(n):
  if(n[::-1]==n):
    return 1
  else:
    return 0
n=input("enter sentence/number....:").lower()
result=palindromechecker(n)
if(result==1):
  print(f"{n} is palindrome")
else:
  print(f"{n} is not palindrome")
    