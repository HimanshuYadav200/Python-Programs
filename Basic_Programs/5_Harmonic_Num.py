#nth harmonic number , harmonic number=n*reciprocal(HM on n numbers) ,HM= n/(1/n1+1/n2+1/n3+...+1/n)
num=int(input("Enter the number"))
i=1
harmonic_num=0
while(i<num):
    harmonic_num=harmonic_num+1/i
    i+=1
print(f"{num}th harmonic number is {harmonic_num}")    