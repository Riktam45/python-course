# A 2D list in Python is essentially a list of lists. 
# It is commonly used to store grid-based or tabular data like matrices, spreadsheets, or game boards

# 1. Creating a 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

# 2. Dynamically with List Comprehension
# To initialize a grid of a specific size (e.g., 3 rows and 4 columns) with default values, use a list comprehension.
# As consensus on Stack Overflow notes, using nested list comprehensions is the cleanest and 
# safest way to initialize an empty 2D list or one filled with a default value (like zeros):

rows = 3
cols = 4
matrix1 = [[0 for _ in range(cols)] for _ in range(rows)]        # Creates a 3x4 matrix filled with zeros
print(matrix1)

# Avoid [[0]*cols]*rows

# 3. Accessing and Modifying Elements
# access specific values using double index brackets: matrix[row][column].

matrix2 = [
    [10, 20, 30],
    [40, 50, 60]
]
print(matrix2[1])            # print the entire row 
print(matrix2[1][2])         # Access the element in row 1, column 2 (60)
matrix2[0][1] = 99           # Modify the element in row 0, column 1
print(matrix2)


# 4. Iterating Through a 2D List
matrix3 = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in matrix3:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row


# 4. Common Operations
# Add a new row: Use .append() to add an entire sublist to the end.
matrix.append([10, 11, 12])
print(matrix)

# add an element to an existing row: Target the specific row index first
matrix[0].append(4)  # Adds 4 to the end of the first row
print(matrix)