print("=======BMI Calculator======")
weight=int(input("enter your weight(KG):"))
height=int(input("enter your height(cm):"))
height=height/100
BMI=weight/(height**2)
if(BMI<18.5):
    print(f"BMI:{BMI} You are underweight")
elif(BMI<25):
    print(f"BMI:{BMI} You are normal")
elif(BMI<30):
    print(f"BMI:{BMI} You are overweight")
else:
    print(f"BMI:{BMI} You are obese")
