# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, 
# and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

things = ["chair","table","desk","laptop","mobile"] # list
for x in things:
    print(x)

# Looping Through a String
for y in "Asomyphormensiniaclotoforeblit":
    print(y)

# break Statement
bikes = {"scrambler","chopper","bobber","retro"}   # set(unordered)
for z in bikes:
    if z == "chopper":
        break
    print(z)

# continue Statement
cars = ("impala", "mustang", "charger", "plymouth")
for a in cars:
    if a == "charger":
        continue
    print(a)

# range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for x1 in range(10):
    print(x1)

# The range() function defaults to 0 as a starting value, 

for x2 in range(2,8):
    print(x2)

# however it is possible to specify the starting value by adding a parameter: range(2, 8), 
# which means values from 2 to 6 (but not including 8)

# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for y1 in range(0,100,20):
    print(y1)
