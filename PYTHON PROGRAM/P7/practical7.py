
# Union, Intersection, and Difference of Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Set A:", A)
print("Set B:", B)
print("Union:", A | B) # or A.union(B)
print("Intersection:", A & B) # or A.intersection(B)
print("Difference (A-B):", A - B) 



# Remove Duplicates from a List using Set
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print("Original List:", lst)
print("List after removing duplicates:", unique_lst)



# Student Record Using Dictionary
student = {
 "Name": "Alice",
 "Roll No": 101,
 "Marks": 95
}
print("Student Record:")
for key, value in student.items():
 print(key + ":", value)



# Word Frequency Count
text = "hello world hello python"
words = text.split()
freq = {}
for word in words:
 if word in freq:
 freq[word] += 1
 else:
 freq[word] = 1
print("Word Frequency:")
for word, count in freq.items():
 print(word + ":", count) 
