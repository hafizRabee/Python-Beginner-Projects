try:
    def TimeConverter(choice):
      if(choice==1):
       seconds=int(input("enter seconds:"))
       print(f"seconds to minutes:{seconds/60}")
      elif(choice==2):
        minutes=int(input("enter minutes:"))
        print(f"minutes to seconds:{minutes*60}")
      elif(choice==3):
        seconds=int(input("enter seconds:"))
        print(f"seconds to Hours:{seconds/3600}")
      elif(choice==4):
        minutes=int(input("enter minutes:"))
        print(f"minutes to hours:{minutes/60}")
      elif(choice==5):
        hours=int(input("enter hours:"))
        print(f"hours to minutes:{hours*60}")
      elif(choice==6):
        hours=int(input("enter hours:"))
        print(f"hours to seconds:{hours*3600}")
      else:
        print(f"please enter choice 1-6")
    print("\t=========Time Converter=========")
    print("====MENU=======")
    print("1.seconds to minutes")
    print("2.minutes to seconds")
    print("3.seconds to Hours")
    print("4.minutes to hours")
    print("5.hours to minutes")
    print("6.hours to seconds")
    choice=int(input("enter choice:"))
    TimeConverter(choice)
except ValueError:
  print("please enter number")

  

     
