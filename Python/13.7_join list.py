# Join list is convert a list of strings into a single string or merge two separate lists into one.
#there are several ways to join two lists in Python
# append() method
# + operator
# extend() method
# insert() method   

# 1. Combine Two Lists into One List

#join two lists using + operator
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d" ]
list3 = list1 + list2
print(list3)

#join two lists using extend() method
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d" ]
list1.extend(list2) 
print(list1)

# 2. Join a List of Strings into One String
words = ["Python", "is", "fun"]
print(" ".join(words))     # Join with spaces (Output: Python is fun)
print(", ".join(words))    # Join with commas (Output: Python, is, fun)
print("".join(words))      # Join with no space (Output: Pythonisfun)

#  Every element in the list must be a string. If your list contains numbers, 
# you must convert them first using - map(str, your_list)
numbers = [1, 2, 3]
print(",".join(map(str, numbers)))  # Output: 1,2,3






