try:
    print("===permutation & combination===")
    n=int(input("Total number of items in the set:(n):"))
    r=int(input("enter Number of items you pick and arrange:(r):"))
    if(n<0 or r<0):
        print(f" n and r should be greater than or equal to zero")
        
    elif(n<r):
        print(f"n should be greater than or equal to r")
    else:
        fact1=1
        for i in range(n,0,-1):
            fact1*=i           #n!
        result=n-r
        fact2=1
        for j in range(result,0,-1):
            fact2*=j                #(n-r)!
        fact3=1
        for K in range(r,0,-1):
            fact3*=K           #r!
        
        permutation=fact1//fact2
        combination=fact1//(fact2*fact3)
        
        print(f"permutation:{permutation}")
        print(f"combination:{combination}")

    
except ValueError:
    print(f"not valid")
#permutaion=n!/(n-r)!
#combination=n!/(n-r)!*r!