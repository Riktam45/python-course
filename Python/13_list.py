#Lists are used to store multiple items in a single variable.

#Lists are one of the four built-in data types in Python used to store collections of data, 
# the other three are Tuple, Set, and Dictionary, all with different qualities and usage.

#Lists are created using square brackets [].

car = ["BMW", "Volvo", "Ford"]
print(car)

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["sack" , "chest", "box", "bag"]
print(len(thislist))                             #length of list

newitem = ["biology", "chemistry", "physics", "maths"]
number = [1, 2, 3, 4, 5]                            #list can be any data type
bool = ["True", "False"] 
mix = ["apple", 1, 2.5, True]
print(newitem)                 #list can contain different data types
print(number)   
print(bool)
print(mix)   

mylsit = ['a','b','c','d']
print(type(mylsit))             # return the type of python colection array(list[],set{},tuple(),dictionary{})