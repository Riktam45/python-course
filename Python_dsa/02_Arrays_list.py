"""
What is an Array?
    An array is a data structure that stores multiple elements in an ordered collection.
    For example, imagine storing the marks of five students:
    marks = [85, 90, 78, 95, 88]   Instead of creating five separate variables, we store all five values in one collection.
    Each element has an index (position):
      85        90        78        95      88
    Index 0   Index 1   Index 2   Index 3   Index 4

Three Ways to Handle "Arrays" in Python
    1. Python Lists 
    It can hold mixed (heterogeneous) data types (integers, strings, and floats all together)
        ex - my_list = [1, 2, 3, "Hello", 4.5]

    2. Python Arrays from the array module)
    if requires true homogeneous array (where every element must be the exact same type) then 
    needed this native python array module. It is more efficient than lists for large arrays of numeric data.
        ex - import array
             my_array = array.array('i', [1, 2, 3, 4, 5])       # 'i' is signed integer

    3. NumPy Arrays (from the NumPy library)
    For advanced mathematical calculations, matrix manipulation, and processing massive datasets 
    it is better to use NumPy arrays. It is more efficient than lists and native arrays for large datasets.
        ex - import numpy as np
             my_numpy_array = np.array([1, 2, 3, 4, 5])

Common Type Codes for Native Arrays
    'b': Signed character (1 byte)
    'B': Unsigned character (1 byte)
    'u': Unicode character (2 bytes)
    'h': Signed integer (2 bytes)
    'H': Unsigned integer (2 bytes)
    'i': Signed integer (4 bytes)
    'I': Unsigned integer (4 bytes)
    'l': Signed long integer (4 bytes)
    'L': Unsigned long integer (4 bytes)
    'q': Signed long long integer (8 bytes)
    'Q': Unsigned long long integer (8 bytes)
    'f': Floating-point number (4 bytes)
    'd': Double-precision floating-point number (8 bytes)


Creating an Array in Python with Array Module

    import array as arr     # in here the 'arr' can be anything just to make it easy to use
    variable_name = arr.array('typecodes', [elements])       

Array methods:
    1. append() - Adds an element to the end of the array.
    2. insert() - Inserts an element at a specified index.
    3. remove() - Removes the first occurrence of a specified element.
    4. pop() - Removes and returns the element at a specified index (default is the last element).
    5. index() - Returns the index of the first occurrence of a specified element.
    6. count() - Returns the number of occurrences of a specified element.
    7. reverse() - Reverses the order of elements in the array.
    8. extend() - Appends elements from another array or iterable to the end of the array.
    9. buffer_info() - Returns a tuple containing the memory address and size of the array.
    10. typecode() - Returns the type code of the array.
    11. fromlist() - Creates an array from a list.
    12. tolist() - Converts the array to a list.

Array vs Python List
    Feature	                Traditional fixed-size array	        Python List
    Size	                Fixed	                                Dynamic
    Resizing	            Usually requires a new allocation	    Automatically resizes
    Element types	        Usually homogeneous	                    Can contain mixed types
    Indexing	            O(1)	                                O(1)
    Insertion at beginning	O(n)	                                O(n)
"""