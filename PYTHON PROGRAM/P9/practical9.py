# Using math Module
import math
# Area of Circle
radius = 7
area = math.pi * radius ** 2
print("Area of Circle:", area)
# Square Root
num = 49
print("Square Root of", num, "is",
math.sqrt(num))
# Trigonometry
angle = 30 # degrees
radians = math.radians(angle)
print(f"Sine({angle}) =",
math.sin(radians))
print(f"Cosine({angle}) =",
math.cos(radians))



# Using random Module
import random
dice_roll = random.randint(1, 6)
print("Dice Rolled: ", dice_roll)





# Using datetime Module
import datetime
current_time = datetime.datetime.now()
print("Current Date & Time:", current_time)



# user_module.py
def greet(name):
 return f"Hello, {name}!"
# main.py
import user_module
name = input("Enter your name: ")
print(user_module.greet(name))
