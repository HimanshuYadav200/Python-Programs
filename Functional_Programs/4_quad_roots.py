import math

def QuadRoots(a,b,delta):
    root1=(-b+math.sqrt(delta))/(2*a)
    root2=(-b-math.sqrt(delta))/(2*a)
    
    return root1,root2

    

a=int(input("enter coefficient of x**2: "))
b=int(input("enter coefficient of x: "))
c=int(input("enter the constant: "))

delta=b**2-4*a*c

if(delta<0):
    print("no real roots exsist")
else:    
    print(QuadRoots(a,b,delta))