# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed and do not allow duplicate values.
# Sets are written with curly brackets.
# Set items are unchangeable, but you can remove items and add new items.

# Create a set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# set is unordered so, it cannot be sure in which order the items will appear.

thisset1 = {"apple", "banana", "cherry", "apple"}  # duplicates are not allowed
print(thisset1)  # will only show unique items

#in at TRUE value is same as 1 and FALSE value is same as 0
thisset2 = {True, False, 1, 0}  # True and 1 are considered the same value  
print(thisset2)  # will only show unique items, so it will show {True, False}

#set data types
thisset3 = {'apple', 'banana', 'cherry',1, 2, 3, 1.1, 2.2, 3.3, True, False} # can contain different data types
print(thisset3)

#using set() constructor
thisset4 = set(("bus"))  # note the double round-brackets
print(thisset4)  # will show {'b', 'u', 's'} as it is a string and will convert it to a set of characters.
thisset5 = set(("bus", "car", "bike"))  # note the double round-brackets
print(thisset5)  # will show {'bus', 'car', 'bike'} as it is a set of strings.  
