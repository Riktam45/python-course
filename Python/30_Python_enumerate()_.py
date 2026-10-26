# The enumerate() function in Python is a built-in function that allows you to loop through 
# an iterable (like a list, tuple, or string) while automatically keeping track of the 
# index (or count) of each item.
# enumerate() generates the index every time the loop runs, 
# but it only shows up in code if explicitly ask to see it.

# Instead of manually maintaining a counter variable or using range(len(sequence)), 
# enumerate() wraps the iterable and yields pairs containing the index and the value as a tuple.

""" syntax
 enumerate(iterable, start = 0)   
"""
# iterable: Any object that supports iteration (e.g., lists, strings, tuples, dictionaries).
# start (optional): The number from which the counter begins. It defaults to 0.

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)


names = ['Ritkam', 'Sarkar']
for i, name in enumerate(names):
    print(name)  # <--- The index exists, but it is not shown here


names = ['Riktam', 'Sarkar']
for item_pair in enumerate(names):
    print(item_pair)  # <--- Shows both together(index and iterate output)


# Customizing the Starting Index
tasks = ['Write code', 'Debug', 'Deploy']
for position, task in enumerate(tasks, start=1):
    print(f"Task {position}: {task}")


# Converting to a List of Tuples
colors = ['red', 'green', 'blue']
print(list(enumerate(colors)))
# Output: [(0, 'red'), (1, 'green'), (2, 'blue')]

