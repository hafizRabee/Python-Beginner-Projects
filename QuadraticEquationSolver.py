def quadraticEquation(a,b,c):
    discriminant1=(b**2 -4*a*c)
 
    if(a==0):
        print(f"a should not be zero ")
    elif(discriminant1<0):
    
        discriminant2=(-discriminant1)**0.5 # for real and imaginary roots
        result1=-b/(2*a)
        result2=discriminant2/(2*a)
        print(f"X1={result1}+{result2}i")
        print(f"X2={result1}-{result2}i")
      
    else:
       discriminant2=discriminant1**0.5 # for real roots
       result1=(-b+discriminant2)/(2*a)
       result2=(-b-discriminant2)/(2*a)
       print(f"X1={result1},X2={result2}")
try:
    print(f"===Quadratic Equation Solver===")
    a=int(input("enter coefficient of x²(a):"))
    b=int(input("enter  x(b):"))
    c=int(input("enter c:"))
    quadraticEquation(a,b,c)
except ValueError:
  print("pleae enter number")




