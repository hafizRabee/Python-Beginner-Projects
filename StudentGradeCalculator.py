def StudentGradeCalculator(n,totalmarks):
    marks=[]
    for i in range(1,n+1):
         mark=float(input(f"enter marks of  each subject{i}:"))
         marks.append(mark)
    total=sum(marks)
    print(f"total:{total}")
    percentage=(total/totalmarks)*100
    return percentage
try:
   print(f"===Student Grade Calculator===")
   n=int(input("enter total subjects:"))
   totalmarks=int(input("enter total marks:"))
   p=StudentGradeCalculator(n,totalmarks)

   print(f"percentage:{p:.2f}%")
   if p>= 80:
    grade = "A+"
   elif p>= 70:
    grade = "A"
   elif p>= 60:
    grade = "B"
   elif p>= 50:
    grade = "C"
   elif p>= 40:
    grade = "D"
   else:
    grade = "F"
   print(f"Grade:{grade}")
except ValueError:
    print(f"please enter valid ")





     


