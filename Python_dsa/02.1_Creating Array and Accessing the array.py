# 1. Using array module to create an array in Python
import array as arr
my_array = arr.array ('i', [12, 45, 65, 34, 87, 95])
print("Array elements are: ", my_array)

# Accessing the array (using array module) elements using index
print("Accessing the first element of the array: ", my_array[2])    # positive indexing
print("Accessing the last element of the array: ", my_array[-1])    # Negative Indexing
print("Reversed array: ", my_array[::-1])                           # Reversed array


# 2. Using Numpy module to create an array in Python
import numpy as np
my_np_array_1d = np.array([12, 45, 65, 34, 87, 95])
my_np_array_2d = np.array([[2, 4, 6], [3, 5, 7], [1, 8, 9]])
print("Numpy array elements are: ", my_np_array_1d)
print("Numpy 2D array elements are: ", my_np_array_2d)

# Accessing the array (using numpy module) elements using index
# Multi-Dimensional Indexing (Tuple-based)
# Instead of using chained brackets like lists (arr[0][1]), NumPy uses a 
# comma-separated tuple to access rows, columns, and higher dimensions efficiently.
# Syntax: arr[row, column]
print("Accessing the first element of the 1D array: ", my_np_array_1d[2])    # positive indexing
print("Accessing the last element of the 1D array: ", my_np_array_1d[-1])    # Negative Indexing
print("Accessing the first element of the 2D array: ", my_np_array_2d[0, 1])    # positive indexing
print("Accessing the last element of the 2D array: ", my_np_array_2d[-1, -1])    # Negative Indexing
print("Sliced 2D array: ", my_np_array_2d[0:2, 1:3])                           # Multidimensional slicing


# The general syntax for each dimension is [start:stop:step]
# for 2d array the syntax is [row_start:row_stop:row_step, col_start:col_stop:col_step]
# for 3d array the syntax is [dim1_start:dim1_stop:dim1_step, dim2_start:dim2_stop:dim2_step, dim3_start:dim3_stop:dim3_step]

# [row, column]