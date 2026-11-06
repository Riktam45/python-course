# 1. Using the Built-in array Module
import array as arr
my_array = arr.array ('i', [12, 45, 65, 34, 87, 95])
print("Array elements are: ", my_array)

# A. In-Place Value Updates (Index & Slicing)
    # Single Element Update: Modify an item directly by its index.
my_array[2] = 100  # Update the value at index 2    
print("Updated array elements are: ", my_array)

    # Slice Update: Replace a segment of the array
my_array[1:4] = arr.array('i', [100, 100, 100, 100])  # Update values from index 1 to 3
print("Updated array elements after slice update are: ", my_array)

"""
heres a catch, when you update a standard slice of an array, the number of new elements in the 
slice must match the number of elements being replaced. Otherwise it increase or 
decrease the size of the array, because of dynamically resizing. And dont forget the typecode in the time of 
updating the slice, it should be same as the original array typecode.
"""

# B. Structural Updates (Adding/Removing Elements)
    # Appending: Add an element to the very end of the array
my_array.append(200)  # Append 200 to the end of the array
print("Array elements after appending 200: ", my_array)

    # Inserting: Inject an element at a designated index position.
my_array.insert(2, 300)  # Insert 300 at index 2
print("Array elements after inserting 300 at index 2: ", my_array)

    # Removing: Eliminate the first occurrence of a specified value.
    # Remove : only remove the first occurrence of element in the array (left to right) and other 
    # elemnts are right shifted to fill the gap
my_array.remove(100)  
print("Array elements after removing the first occurrence of 100: ", my_array)

    # Extending: Append multiple elements from another iterable array.
my_array.extend(arr.array('i', [4, 5, 6]))  # Extend the array with new elements at the end
print("Array elements after extending with [4, 5, 6]: ", my_array)


