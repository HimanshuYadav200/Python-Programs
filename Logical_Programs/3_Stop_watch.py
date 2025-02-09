import time

def Start_time():
    start=time.time()
    return start
    
def Stop_time():
    end=time.time()
    return end
    
user_instruction_to_start=input("Start the watch or not, enter yes/no: ")

if(user_instruction_to_start=="yes"):
   begin_time= Start_time()
    
user_instruction_to_end=input("Stop the watch or not, enter yes/n: ")    

if(user_instruction_to_end=="yes"):
    end_time=Stop_time()
    
print(f"time elapsed is {end_time-begin_time}")    

                