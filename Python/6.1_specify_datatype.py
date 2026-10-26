# Setting the Specific Data Type
# we can specify the dattypes in te variables

x1 = str("Hello World")                         # str is a string data type
x2 = int(20)	                                # int is an integer data type (2)
x3 = float(20.5)		                        # float is a floating point data type (2.0)
x4 = complex(1j)		                        # complex numeric data type used for mathematical complex numbers, or complex/composite data structures like lists, tuples, and dictionaries that store collections of data
x5 = list(("apple", "banana", "cherry"))		# list is a built-in data structure used to store an ordered, mutable (changeable) collection of items
x6 = tuple(("apple", "banana", "cherry"))	    # tuple is a built-in sequence data type used to store an ordered, unchangeable (immutable) collection of items
x7 = range(6)	                                # range is a built-in function that generates a sequence of integers
x8 = dict(name="John", age=36)	                # dict is a built-in data structure that stores data in key-value pairs
x9 = set(("apple", "banana", "cherry"))	        # set is a built-in data structure used to store an unordered collection of unique items
x10 = frozenset(("apple", "banana", "cherry"))	# frozenset is a built-in data type that represents an immutable, unordered collection of unique elements
x11 = bool(5)	                                # bool is a boolean data type
x12 = bytes(5)	                                # bytes is an immutable sequence of integers ranging from 0 to 255, used primarily to handle raw binary data
x13 = bytearray(5)	                            # bytearray is a built-in mutable sequence of integers ranging from 0 to 255
x14 = memoryview(bytes(5))	                    # memoryview is a  built-in data type that provides a zero-copy, memory-efficient way to access and slice the internal data of an object without replicating it in memory
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)
print(x11)
print(x12)
print(x13)
print(x14)
