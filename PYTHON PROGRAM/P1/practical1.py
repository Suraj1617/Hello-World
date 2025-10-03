print("hello world!")

num = int(input("Enter a number: "))
if num % 2 == 0:
 print(num, "is Even")
else:
 print(num, "is Odd")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
 fact *= i
print("Factorial of", num, "is", fact) 

