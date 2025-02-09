
import random
stake=int(input("enter the stake amount: "))
goal=int(input("enter the goal: "))
times_to_bet=int(input("enter how many times to bet: "))
loss_count=0
win_count=0
total_bets=times_to_bet

while(times_to_bet>0):
    if(random.choice([0,1]))==1:
        stake+=1
        win_count+=1
    else:
        stake-=1    
        loss_count+=1
        
    times_to_bet-=1

if(total_bets>0):
    loss_percentage=(loss_count/total_bets)*100
    win_percentage=(win_count/total_bets)*100

print(f"loss percentage is {loss_percentage}")
print(f"win percentage is {win_percentage}") 
        
        
        
