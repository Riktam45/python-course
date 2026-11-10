# Numpy Traversal array

    # 1. Advanced Multi-Dimensional Traversal (np.nditer)
import numpy as np
matrix = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Traversing the array:")
for element in np.nditer(matrix):
    print(element)

    # 2. Index & Value Traversal (np.ndenumerate)
val = np.array([[10, 20, 30],[12, 22, 32]])
print("Indexed Traversing array:")
for index, value in np.ndenumerate(val):
    print(f"Index: {index}, Value: {value}")

    # 3. Iterating with np.ndindex
print("Iterating with np.ndindex:")
for index in np.ndindex(val.shape):
    print(f"Index: {index}, Value: {val[index]}")