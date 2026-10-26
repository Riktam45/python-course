# A heterogeneous list in Python is a list that contains elements of different data types 
# (such as integers, strings, floats, booleans, or even other lists and tuples) within the same collection

# Unlike many programming languages where arrays require all elements to be of the exact same type, 
# Python lists are heterogeneous by default.

# Why are Python lists heterogeneous?
# Python lists do not store the actual values directly in a contiguous block of memory. 
# Instead, they store a collection of memory references (pointers) that point to the actual objects. 
# Because every reference pointer is the same size, the objects they point to can be of any data type.

# 1. Creating a Heterogeneous List
mixed_list = ["Riktam", 23, 9.46, True, (1, 2)]
for item in mixed_list:
    print(f"Elements : {item} | Type : {type(item)}")


# 2. Filtering or Splitting by Data Type
# When working with heterogeneous lists, you often need to isolate specific types using isinstance()
data = [12, "apple", 23, "banana", 42, "cherry"]
strings = [x for x in data if isinstance(x, str)]
numbers = [x for x in data if isinstance(x, (int, float))]
print("Strings:", strings)
print("Numbers:", numbers)

