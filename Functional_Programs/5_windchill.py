import math

def WindChill(temperature,speed):
    if(temperature>50 and (speed>120 or speed<3)):
        wind=35.74+0.6215*temperature+(0.4275*temperature-35.75)*(math.pow(speed,0.16))
        
        return wind

temperature=int(input("enter the temperature: "))
speed=int(input("enter the speed: "))

print(f"wind speed is {WindChill(temperature,speed)}")



