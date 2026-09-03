try:
    year=int(input("enter year:"))
    if((year%4==0 and year%100!=0) or year%400==0):
      print(f"{year} is a leap year")
    else:
      print("not a leap year")
except ValueError:
   print(f"pease enter year")
