nums_list=int(input("enter the number of elements in list: "))
list=[]
for i in range(nums_list):
    num=int(input("enter the number to enter into the list: "))
    list.append(num)
    
triples=[]

for i in range(len(list)):
    j=i+1
    for j in range(len(list)):
        k=j+1
        for k in range(len(list)):
            if list[i]+list[j]+list[k]==0:
            
                triples.append([list[i],list[j],list[k]])
               
                
print(triples)                    
    