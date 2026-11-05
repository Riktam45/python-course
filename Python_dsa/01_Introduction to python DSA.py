"""
What is Python DSA?
    It is a branch of computer science that focuses on the study of data structures and algorithms 
    using the Python programming language. Data structures are ways of organizing and storing 
    data in a computer so that it can be accessed and modified efficiently. 
    Algorithms are step-by-step procedures or formulas for solving problems.

Examples of Data Structures:
    Array / List	    Numbered storage compartments
    Linked List	        Chain of connected links
    Stack	            Stack of plates
    Queue	            People standing in a line
    Tree	            Family tree
    Graph	            Road network
    Hash Table	        Dictionary lookup 

Where the Data Structure Resides ?
    A data structure resides in computer memory or storage—specifically in primary memory (RAM) while 
    a program is actively running, or in secondary storage (such as SSDs or hard drives) 
    when saved persistently.

Classification of Data Structures:
    1. Linear Data Structures: Data elements are arranged in a sequential manner.
       Examples: Array, Dynamic array, List, Linked List, Stack, Queue, Deque, Priority Queue
    2. Non-Linear Data Structures: Data elements are not arranged in a sequential manner.
       Examples: AVL, Tree, Graph, Hash Table, B-Tree

What is an Algorithm?
    An algorithm is a step-by-step linguistic representation of procedure or formula for solving a problem.

What are the different types of algorithms?
    rute Force	            Try possible solutions directly
    Searching	            Find a particular element
    Sorting	                Arrange elements in order
    Recursion	            Solve a problem through smaller versions of itself
    Divide and Conquer	    Divide, solve and combine
    Greedy	                Make locally optimal choices
    Backtracking	        Explore possibilities and undo choices
    Dynamic Programming	    Reuse results of overlapping subproblems
"""
# some basic examples of data structures and algorithms in Python

# Problem 1: Find the sum of numbers
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total = total + num
print("Sum:", total)

# logic: 
# total = 0, 
# total = 0 + 10, 
# total = 10 + 20, 
# total = 30 + 30, 
# total = 60 + 40, 
# total = 100 + 50, 
# total = 150


# Problem 2: Find the largest number
numbers = [12, 45, 23, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)

# logic:
# largest = 12, 
# largest = 45, 
# largest = 67, 
# largest = 67, 
# largest = 67

# Problem 3: Count even numbers
numbers = [12, 45, 23, 67, 34]
count = 0
for num in numbers:
    if num % 2 == 0:
        count = count + 1
print("Count of even numbers:", count)

# logic:
# count = 0,
# count = 1,
# count = 1,
# count = 1,
# count = 2

