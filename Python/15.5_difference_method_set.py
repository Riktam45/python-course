# In Python, the set.difference() method returns a new set containing elements that 
# exist only in the first set and not in the specified target sets.
# it evaluates what is unique to the left-hand set by completely filtering out any overlapping elements.


# 1. Basic Syntax
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result1 = set_a.difference(set_b)   # Method 1: Using the .difference() method
print(result1)

result2 = set_a - set_b     # Method 2: Using the - operator
print()

# Note: Order matters! If you swap them (set_b.difference(set_a)), the output will be {5, 6}


# 2. Comparing Multiple Sets
a = {1, 2, 3, 4}
b = {3, 4}
c = {5, 6}
print(a.difference(b, c))  # Removes elements found in either b or c from a
