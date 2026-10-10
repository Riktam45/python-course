#Python has two built-in methods that you can use on tuples.
# 1. count() method
# 2. index() method

# count() method returns the number of times a specified value appears in a tuple.
tuple1 = ("plate", "cup", "bowl", "spoon", "fork", "knife", "plate")    
count_plate = tuple1.count("plate")  # Count occurrences of "plate"
print(f"The value 'plate' appears {count_plate} times in the tuple.")   

# index() method returns the index of the first occurrence of a specified value in a tuple.
index_fork = tuple1.index("fork")  # Get index of "fork"
print(f"The index of 'fork' in the tuple is {index_fork}.") 