# List Comprehension
# List comprehension offers a shorter syntax when want to create a new list based on the values of an existing list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged


# Condition
# The condition is like a filter that only accepts the items that evaluate to True
cars = ["car1", "car2", "car3", "car4", "car5"]
new_cars = [y for y in cars if y != "car"]
print(new_cars)


# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
new_list =  [x for x in range(10)]
print(new_list)

# Same example, but with a condition
new_list = [x for x in range(10) if x > 5]
print(new_list)


# Expression
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
Example_list = [x.upper() for x in fruits]
print(Example_list)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
example_set = [x if x != "banana" else "orange" for x in fruits]
print(fruits)