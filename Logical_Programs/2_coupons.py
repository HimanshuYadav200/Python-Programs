import random

disctinct_nums=int(input("enter the number of distinct coupons needed"))
coupons_list=[]

random_num_count=0

for i in range(disctinct_nums):
    coupon_no=random.randint(1,10)
    random_num_count+=1
    
    if(coupon_no not in coupons_list):
        coupons_list.append(coupon_no)
    
print(coupons_list)    
print(f"total random numbers used to generate distinct coupons are {random_num_count}")
    
    
    
