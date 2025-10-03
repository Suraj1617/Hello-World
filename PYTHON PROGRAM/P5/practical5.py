# Reverse a String and Count Vowels
s = input("Enter a string: ")
rev = s[::-1]
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Reversed String:", rev)
print("Number of Vowels:", count)



# Palindrome String Checker
s = input("Enter a string: ")
if s == s[::-1]:
 print("The string is a Palindrome")
else:
 print("The string is Not a Palindrome") 




# Frequency of Characters
s = input("Enter a string: ")
freq = {}
for char in s:
 if char in freq:
 freq[char] += 1
 else:
 freq[char] = 1
print("Character Frequency:")
for char, count in freq.items():
 print(f"{char}: {count}")




 # Substring Search
s = input("Enter the main string: ")
sub = input("Enter substring to search: ")
if sub in s:
 print(f"'{sub}' is present in the string")
else:
 print(f"'{sub}' is not present in the string") 
