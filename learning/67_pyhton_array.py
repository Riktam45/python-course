# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# This shows how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library

# Array
# An array is a special variable, which can hold more than one value at a time
# if a list of items (a list of car names, for example), storing the cars in single variables could look like this:
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# However, what if want to loop through the cars and find a specific one? And what if had not 3 cars, but 300?
# The solution is an array!
# An array can hold many values under a single name, and you can access the values by referring to an index number.


# Access the Elements of an Array
cars = ["Ford", "GMC", "Jeep"]
x = cars[0]
print(x)

# Modify the value of the first array item
cars[0] = "Toyota"
print(cars)

# Length of an Array
cars = ["Ford", "GMC", "Jeep"]
x = len(cars)
print(x)

# Looping Array Elements
for i in cars:
    print(i)

# Adding Array Elements
cars.append("Nissan")       # always put the element in the last position
print(cars)

# use insert to add on custom positions
cars.insert(1,"Lamborghini")    # list_name.insert(index, elemnts)
print(cars)

# Removing Array Elements
# pop() method to remove an element from the array
cars.pop(2)
print(cars)

# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list