# In Python, you cannot access individual items in a set by referring to an index or a key 
# because sets are unordered and unindexed.

# 1. Check if an Item Exists (Membership Testing)
# Use the in keyword to verify if an item is present inside the set. 
# This returns a boolean value (True or False)
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)

# 2. Loop Through the Set (Iteration)
# Use a for loop to look at or process each item sequentially. Because sets are unordered, 
# the elements will be processed in an unpredictable order.
py_set = {"alpha", "beta", "charlie", "delta"}
for x in py_set:
    print(x)