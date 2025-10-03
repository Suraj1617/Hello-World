# Factorial Function
def factorial(n):
 result = 1
 for i in range(1, n+1):
 result *= i
 return result
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


# Fibonacci Function
def fibonacci(n):
 fib_list = []
 a, b = 0, 1
 for _ in range(n):
 fib_list.append(a)
 a, b = b, a + b
 return fib_list
terms = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci(terms)) 



# Prime Number Checker Function
def is_prime(n):
 if n <= 1:
 return False
 for i in range(2, int(n**0.5)+1):
 if n % i == 0:
 return False
 return True
num = int(input("Enter a number: "))
if is_prime(num):
 print(num, "is a Prime Number")
else:
 print(num, "is Not a Prime Number")




 # Calculator Functions
def add(a, b):
 return a + b
def subtract(a, b):
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 if b != 0:
 return a / b
 else:
 return "Division by zero not allowed"
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y)) 
