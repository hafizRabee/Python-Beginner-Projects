def futuredayfinder(currentdate,futuredate,today):
  Days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  result=futuredate-currentdate
  if(result<0):
    print("this is only work within  the same month")
  elif(today not in Days):
    print("please enter valid day")
  else:
    day=Days.index(today)
    final=Days[(day+result)%7]
    print(f"Day at {futuredate} will be:{final}")

currentdate=int(input("enter today date:"))
futuredate=int(input("enter futuredate:"))
today=input("enter today day:").lower()

futuredayfinder(currentdate,futuredate,today)

  