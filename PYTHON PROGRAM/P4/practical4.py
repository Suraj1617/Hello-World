# Multiplication Table of a Number
num = int(input("Enter a number: "))
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
 print(f"{num} x {i} = {num * i}") 




# Fibonacci Series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
 print(a, end=" ")
 a, b = b, a + b 




# Reverse Digits of a Number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
 digit = num % 10
 rev = rev * 10 + digit
 num //= 10
print("Reversed Number:", rev)





# Sum of Digits of a Number
num = int(input("Enter a number: "))
total = 0
while num > 0:
 digit = num % 10
 total += digit
 num //= 10
print("Sum of Digits:", total) 

