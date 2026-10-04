# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable.
# But there is a workaround. You can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

# Changing values in a tuple by converting it to a list
tuple1 = ("plate", "cup", "bowl", "spoon", "fork", "knife")
listname = (list(tuple1))  # Convert tuple to list
listname[2] = "glass"  # Change the value at index 2    
tuplename = (tuple(listname))  # Convert list back to tuple
print(tuplename)

#using append() method to add an element to the tuple
tuple2 = ("plate", "cup", "bowl", "spoon", "fork", "knife")
listname1 = (list(tuple2))
listname1.append("fridge")
tuplename1 = (tuple(listname1))
print(tuplename1)

#add tuple to tuple
tuple3 = ("plate", "cup", "bowl", "spoon", "fork", "knife")
tuple4 = ("glass",)
tuple3 += tuple4  # Concatenate tuples
print(tuple3)

# tuple is immutable, so you cannot change the value of an element directly. 
# so if you want to remove the value of an element, you have to convert it to a list, 
# remove the value, and convert it back to a tuple.

# Removing an element from a tuple by converting it to a list
tuple5 = ("plate", "cup", "bowl", "spoon", "fork", "knife")
listname2 = (list(tuple5))  # Convert tuple to list
listname2.remove("bowl")  # Remove the value "bowl"
tuplename2 = (tuple(listname2))  # Convert list back to tuple
print(tuplename2)

# delete th ewhole tuple
tuple6 = ("plate", "cup", "bowl", "spoon", "fork", "knife")
del tuple6
print(tuple6)  # This will raise an error because tuple6 is deleted