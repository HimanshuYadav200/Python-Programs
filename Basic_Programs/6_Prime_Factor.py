
import math

def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
     
    return True    


number=int(input("enter the number: "))

list=[]
for i in range(2,number+1):
    if number%i==0:
        list.append(i)
        
for i in list:
    if(check_prime(i)):
        print(i)  
        
        

            
    