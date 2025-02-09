import random


flip_turns=int(input("Enter number of times to flip a coin :"))
head_count=0
tail_count=0
while(flip_turns>0):
    if(flip_turns>0):
        value=random.random()
        if(value<0.5):
            print("tails")
            tail_count+=1
        else:
            print("heads")      
            head_count+=1
    flip_turns-=1 
    
total_turns=head_count+tail_count    
if(total_turns!=0):
    
    head_percentage=(head_count/total_turns)*100
    tail_percentage=(tail_count/total_turns)*100    
    
print(f" head percentage is {head_percentage}")
print(f"tails percentage is {tail_percentage}")    

