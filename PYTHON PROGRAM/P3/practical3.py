# Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
 print("Largest number is:", a)
elif b >= a and b >= c:
 print("Largest number is:", b)
else:
 print("Largest number is:", c)



# Leap Year Checker
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0
and year % 4 == 0):
 print(year, "is a Leap Year")
else:
 print(year, "is Not a Leap Year")



# Grade Classification
marks = int(input("Enter marks: "))
if marks >= 90:
 print("Grade: A")
elif marks >= 75:
 print("Grade: B")
elif marks >= 50:
 print("Grade: C")
elif marks >= 35:
 print("Grade: D")
else:
 print("Grade: Fail")



# Check Positive, Negative or Zero
num = float(input("Enter a number: "))
if num > 0:
 print("Number is Positive")
elif num < 0:
 print("Number is Negative")
else:
 print("Number is Zero") 

