def SimpleIntrest(P,R,T):
    return P*(R/100)*T
try:
    P=float(input("enter Principal amount:(P)"))
    R=float(input("enter  Annual interest rate in %(like 100):(R)"))
    T=float(input("enter Time duration in years:(T)"))
    Result=SimpleIntrest(P,R,T)
    print(f"SI:{Result:.2f}")
except ValueError:
    print("please enter valid numeric")
