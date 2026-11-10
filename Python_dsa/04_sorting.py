"""
What is soritng?
    Sorting algorithms are fundamental to Data Structures and Algorithms (DSA) because they arrange data in a 
    specific order (usually ascending or descending). This makes searching faster (e.g., enabling binary search) 
    and helps optimize many downstream operations like finding duplicates or filtering.

In Python, sorting is divided into two primary approaches: 
    1. Built-in Sorting Techniques: 
        Python's built-in sorting uses Timsort, a highly optimized hybrid 
        algorithm that combines Merge Sort and Insertion Sort.

    2. Standard DSA Sorting Algorithms:

"""

# 1. Built-in Sorting Techniques
# a. list.sort() (In-Place Sorting)
    # The .sort() method can only be applied to a list
    # Modifies the original list directly and returns None. It is highly efficient because it 
    # does not allocate extra memory for a new list.

chars = ['b', 'a', 'c']
chars.sort()
print(chars)                # charecters can be sorted as alphabetically order

nums = [56, 32, 237, 48, 1]
nums.sort()
print(nums)

# b. sorted() (Returns a New List)
    # Leaves the original iterable unchanged and returns a completely new sorted list. 
    # It can accept any iterable type, strings, tuples, dictionaries, sets, and including lists

chars = ['charlie', 'alpha', 'beta']        # list(chars)
new_chars = sorted(chars)
print(new_chars)                            # in a string alphabatically order the very first letter

nums = [38, 46, 33, 38, 553, 48]            # list(nums)
new_nums = sorted(nums)
print(new_nums)

my_tuple = (5, 1, 4, 3)                     # tuples
sorted_tuple = tuple(sorted(my_tuple)) 
print(sorted_tuple)                         # sorted() returns a list; cast it back to a tuple

my_set = {5, 1, 4, 3}                       # sets
sorted_list = sorted(my_set) 
print(sorted_list)                          # Sets are unordered. Sorting them produces a sorted list.

my_dict = {'b': 2, 'a': 4, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))      # Sort by Keys (Default)
print(sorted_by_keys)  # Output: {'a': 4, 'b': 2, 'c': 1}

# Sort by Values (Using a lambda function)
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'c': 1, 'b': 2, 'a': 4}


"""
Summary of sorted() behavior:

• list  -->  Returns a new sorted list
• tuple -->  Returns a new sorted list (which you can convert back using tuple())
• set   -->  Returns a new sorted list
• dict  -->  Returns a new sorted list of the keys (or pairs, if you use .items())
"""

# Custom Customizations (reverse and key)
# Both tools accept two optional parameters:
# reverse=True: Sorts elements in descending order
# key: Accepts a function (often a lambda expression) to customize sorting logic

# Descending order
items = [4, 2, 7]
items.sort(reverse=True) 
print(items)                        # [7, 4, 2]

# Custom sorting by length of strings using key
words = ["banana", "apple", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)                 # Output: ['kiwi', 'apple', 'banana']

