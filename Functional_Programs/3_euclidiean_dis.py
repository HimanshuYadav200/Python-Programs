import math

def euclid_distance(x1,x2,y1,y2):
    distance=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    return distance


x1=int(input("enter first argument: "))
x2=int(input("enter secind argument: "))
y1=int(input("enter third argument: "))
y2=int(input("enter fourth argument: "))

print(f"euclidean distance is {euclid_distance(x1,x2,y1,y2)}")




