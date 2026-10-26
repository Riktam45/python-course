# In Python, iteration, iterable, and iterator are distinct but tightly coupled components of the Python Iterator Protocol. 
# This protocol governs how for loops, list comprehensions, and data streams traverse collections efficiently.

# The Three Core Concepts: 
# a. Iteration:- is the process or act of looping through a collection of items one by one.
# b. Iterable:- is the object that can be looped over (e.g., a list, tuple, string, or dict). 
#       It implements the __iter__() method, which produces an iterator when called.
# c. Iterator:- is the agent or stateful object that actually performs the traversal. 
#       It keeps track of its current position and produces the next value via the __next__() method.


# 
#  Term	        What it is	                                            Key Method(s)	            Example
# Iterable	A collection or sequence that you can loop over.        	__iter__() or          [1, 2, 3] (List),
#               It contains data but doesn't track traversal state.	    __getitem__()           "abc" (String)

# Iterator	A stateful object that fetches elements one at a time.      __next__() and          Output of iter([1, 2, 3])
#               It tracks where it currently is in the sequence.	    __iter__()	    
#         
# Iteration	The process of executing a block of code                    Handled by for or while loops.
#               repeatedly for each item.		                                                The execution of the loop itself


# # 1. ITERABLE: A standard list containing data
my_fruits = ["apple", "banana", "cherry"]
# 2. ITERATOR: Created by passing the iterable to iter()
fruit_iterator = iter(my_fruits)
# 3. ITERATION: Fetching items one by one using next()
print(next(fruit_iterator))  # Outputs: apple
print(next(fruit_iterator))  # Outputs: banana
print(next(fruit_iterator))  # Outputs: cherry
# If you call next() again, it raises StopIteration because the items ran out
# print(next(fruit_iterator))

# The Standard for Loop
numbers = [10, 20, 30]
for num in numbers:     # Standard iteration
    print(num)

# The Manual "Behind-the-Scenes" Method
numbers = [10, 20, 30]
iterator = numbers.__iter__()       # 1. The loop calls __iter__() to get the iterator object
while True:                         # 2. The loop repeatedly calls __next__() to fetch values
    try:
        num = iterator.__next__()   # This is the exact method the for loop calls each cycle
        print(num)
    except StopIteration:
        break                       # 3. The loop catches this exact error to exit cleanly
