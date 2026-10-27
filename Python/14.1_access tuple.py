# Accessing elements in a tuple
tuple1 = ("plate", "cup", "bowl","spoon", "fork", "knife")
print(tuple1[4])

# negetive indexing 
tuple2 = ("plate", "cup", "bowl","spoon", "fork", "knife")  # in negative last element (most rightest) is '-1' 
print(tuple2[-3])

# range of indexes
tuple3 = ("plate", "cup", "bowl","spoon", "fork", "knife")
print(tuple3[1:4])  # from index 1 to index 3 (4 is not included)

#range of negetive indexes
tuple4 = ("plate", "cup", "bowl","spoon", "fork", "knife")  
print(tuple4[-5:-2])  # from index -5 to index -3 (-2 is not included)

# range index without starting index
# it will start from the beginning of the tuple
tuple5 = ("plate", "cup", "bowl","spoon", "fork", "knife")
print(tuple5[:4])

# range index without ending index
# it will end at the last element of the tuple
tuple6 = ("plate", "cup", "bowl","spoon", "fork", "knife")
print(tuple6[5:])  # from index 2 to the end of the tuple

# Looping / iteration
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
for index, fruit in enumerate(fruits):  # Loop with index tracking
    print(f"Index {index}: {fruit}")