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
