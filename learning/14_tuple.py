#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#Tuples are written with round brackets.
#Create a tuple:
tuplename = ("dd", "ee", "ff")
print(tuplename) 

#tuple items can be duplicated
tuplexample = ("a","a","a","a")
print(tuplexample)

#tuple length
tuple1 = ("vowel", "consonant", "vowel", "consonant")
print(len(tuple1))

#Create a tuple with one item
#To create a tuple with only one item, you have to add a comma after the item, otherwise it will not be treated as a tuple.
tuple2 = ("a",)
print(type(tuple2))

#tuple can be any data type
tuple3 = ("a", 1, 2.5, True)    
print(tuple3)

#tuple() constructor
tuple4 = tuple(("a", "b", "c")) 
print(tuple4)
