# Find Maximum and Minimum in a List
lst = [12, 45, 7, 89, 23]
print("List:", lst)
print("Maximum Value:", max(lst))
print("Minimum Value:", min(lst))



lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print("Original List:", lst)
print("List after removing duplicates:", unique_lst) 
    


# Sort a List
lst = [34, 12, 56, 78, 23]
print("Original List:", lst)
lst.sort()
print("Ascending Order:", lst)
lst.sort(reverse=True)
print("Descending Order:", lst) 



# Tuple Packing and Unpacking
# Packing
t = (10, 20, 30)
print("Packed Tuple:", t)
# Unpacking
a, b, c = t
print("Unpacked Values: a =", a, ", b =", b, ", c =",
c) 
