# Swap two numbers without using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before Swapping: a =", a, " b =", b)
a = a + b
b = a - b
a = a - b
print("After Swapping: a =", a, " b =", b)



# Simple Interest and Compound Interest
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))
# Simple Interest
si = (p * r * t) / 100
# Compound Interest
ci = p * ((1 + r/100) ** t) - p
print("Simple Interest =", si)
print("Compound Interest =", ci)



# Area and Perimeter of Circle
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
perimeter = 2 * math.pi * radius
print("Area of Circle =", area)
print("Perimeter of Circle =", perimeter)



# Temperature Conversion Celsius ↔ Fahrenheit
choice = int(input("Enter 1 for Celsius → Fahrenheit,2 for Fahrenheit → Celsius: "))
if choice == 1:
 c = float(input("Enter Temperature in Celsius: "))
 f = (c * 9/5) + 32
 print("Temperature in Fahrenheit =", f)
elif choice == 2:
 f = float(input("Enter Temperature in Fahrenheit:"))
 c = (f - 32) * 5/9
 print("Temperature in Celsius =", c)
else:
 print("Invalid Choice!") 





 

