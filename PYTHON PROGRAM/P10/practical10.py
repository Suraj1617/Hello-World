# Write and Read from a Text File
# Writing to file
with open("example.txt", "w") as file:
 file.write("Hello World!\nWelcome to
Python Programming.")
# Reading from file
with open("example.txt", "r") as file:
 content = file.read()
 print("File Content:\n", content)




# Count Lines, Words, Characters
with open("example.txt", "r") as file:
 content = file.read()
lines = content.split("\n")
words = content.split()
chars = len(content)
print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Number of Characters:", chars)




# Copy Content from One File to Another
with open("example.txt", "r") as source:
 content = source.read()
with open("copy.txt", "w") as dest:
 dest.write(content)
print("Content copied to copy.txt successfully.")




# Exception Handling for Division by Zero
try:
 a = int(input("Enter numerator: "))
 b = int(input("Enter denominator: "))
 result = a / b
 print("Result:", result)
except ZeroDivisionError:
 print("Error: Division by zero is not allowed!") 
