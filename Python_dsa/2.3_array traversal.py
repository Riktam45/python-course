# Array traversal means visiting each element of an array from start to end (or end to start) to read, 
# modify, or process the data. In Python, you can use the built-in array module to create homogeneous 
# arrays (arrays storing elements of the same data type in contiguous memory) and 
# traverse them using various loop patterns.
# Moving sequentially from the starting index (lower bound, usually 0) to the ending index (upper bound, n - 1)

#  Array Traversal Methods
    # 1. Direct Element Traversal: Using a for loop to iterate through each element of the array.
import array as arr
my_array = arr.array("i",[1, 2, 3, 4, 5])
print("Direct element traversal:")
for element in my_array:
    print(element, end=" ")     # Setting end="" removes any spacing or newlines entirely

    # 2. Index-Based Traversal: Using a for loop with the range() function to access elements by their index.
print("Index-based traversal:")
for i in range(len(my_array)):
    print(f"Element at index {i}: {my_array[i]}")
# 3. While Loop Traversal: Using a while loop to traverse the array until a certain condition is met.
print("While loop traversal:")
i = 0
while i < len(my_array):
    print(f"Element at index {i}: {my_array[i]}")
    i += 1