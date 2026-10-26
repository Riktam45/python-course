fruits = ["apple", "banana", "cherry"]
print(fruits[1])                   #accessing the second item in the list, Because index starts from 0.

print(fruits[-1])                  #accessing the last item in the list, -1 refers to the last item.

# negetive indexing

print(fruits[-2])                  #accessing the second last item in the list, -2 refers to the second last item.

# Range of indexes
elements = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(elements[2:5])              #accessing items from index 2 to 4 (5 is not included).

print(elements[:4])               #accessing items from the start to index 3 (4 is not included).

print(elements[2:])               #accessing items from index 2 to the end of the list.

#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item.
#Remember that the item in index 4 is NOT included.

# Negetative indexing with range
print(elements[-6:-2])            #accessing items from the second item to the second last item.

#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

# Accessing Nested List
# If a list contains other lists, use multiple sets of square brackets to drill down into the sub-lists.
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0])        # whole inner list
print(matrix[1][0])     # accessing the inner list element