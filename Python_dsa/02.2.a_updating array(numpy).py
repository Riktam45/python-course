# 2. Using the numpy Library
# NumPy handles multidimensional ndarray structures. Because NumPy arrays have a fixed memory size, 
# structural changes (like inserting or appending) are not directly supported. 
# Instead, you need to create a new array with the desired modifications.

import numpy as np
my_np_array_1d = np.array([12, 45, 65, 34, 87, 95])
my_np_array_2d = np.array([[2, 4, 6], [3, 5, 7], [1, 8, 9]])
print("Numpy array elements are: ", my_np_array_1d)
print("Numpy 2D array elements are: ", my_np_array_2d)

# A. Value Updates by Index & Slicing
    # Direct Index Assignment: Change single elements in 1D or multi-dimensional space
my_np_array_1d[2] = 100                     # Update the value at index 2
my_np_array_2d[1, 1] = 200                  # Update the value at row 1, column 1
print("Updated 1D array elements are: ", my_np_array_1d)
print("Updated 2D array elements are: ", my_np_array_2d)

    # Slice Assignment: Update a whole subset or a full axis simultaneously.
my_np_array_1d[1:4] = [1, 2, 3]          # Update values from index 1 to 3
my_np_array_2d[:, 0] = [100, 200, 300]      # Update the first column of the 2D array
my_np_array_2d[:, 2] = [10, 20, 30]      # Update the last column of the 2D array
my_np_array_2d[2, 1] = 20                   # Update the value at row 2, column 1
print("Updated 1D array elements after slicing are: ", my_np_array_1d)
print("Updated 2D array elements after slicing are: ", my_np_array_2d)

# [20] and 20 are different. [20] is a list with one element, while 20 is an integer. 
# When you assign [20] to a slice of a NumPy array, it will replace the selected elements with the 
# contents of the list. In contrast, assigning 20 will set all selected elements to the integer value 20

# B. Structural Alterations (Returns a New Array)
    # Appending: Append elements to the end
my_np_array_1d = np.append(my_np_array_1d, [40, 50])
      # Append a new row to the 2D array  
print("1D array after appending: ", my_np_array_1d)
print("2D array after appending: ", my_np_array_2d)

    # Inserting: Insert elements at a specific index
my_np_array_1d = np.insert(my_np_array_1d, 2, [15, 25])  # Insert values at index 2
my_np_array_2d = np.insert(my_np_array_2d, 1, [[10, 20, 30]], axis=0)  # Insert a new row at index 1
print("1D array after inserting: ", my_np_array_1d)
print("2D array after inserting: ", my_np_array_2d)

""" 
axis=0: Tells NumPy to insert this data horizontally as a row, pushing the existing row at index 1 
 1. For a 2D Array (Rows and Columns)
 • Use axis=0 to insert a row.
 • Use axis=1 to insert a column.

 2. For a 3D Array (Depth, Rows, Columns)
 • axis=0: Inserts a whole new 2D matrix/slice along the depth.
 • axis=1: Inserts a new row across all slices.
 • axis=2: Inserts a new column across all slices.

 instead of 1d (flattened array) every dth array need the axis parameter otherwise it raises a value error.
"""

    
 