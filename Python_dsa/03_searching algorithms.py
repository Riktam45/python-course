"""
Searching algorithms are foundational tools in Data Structures and Algorithms (DSA) used to check for 
an element's presence or locate its position within a collection.

There are various searching algorithms, each with its own advantages and use cases. 
Some of the most commonly used searching algorithms include:

1. Linear Search: 
    This is the simplest searching algorithm that checks each element in the collection sequentially 
    until the desired element is found or the end of the collection is reached. 
    It has a time complexity of O(n).

2. Binary Search: 
    This algorithm is used on sorted collections. It repeatedly divides the search interval in half, 
    checking the middle element and narrowing down the search range based on comparisons. 
    It has a time complexity of O(log n).
"""

"""
Short note: In programming, -1 is used by universal convention to mean "not found" or "index does not exist."
"""

# 1. Linear Search (Sequential Search)

def linear_search(arr, target):         # Creates a function accepting an array and a target.
    for i in range(len(arr)):           # Generates all valid indices
        if arr[i] == target:            # Compares the current element with the target
            return i                    # Return the index of the target element
    return -1                           # Return -1 if the target element is not found
numbers = [10, 20, 30, 40, 50]              
result = linear_search(numbers, 30)     
print(f"The position of the intended number: {result}")                          # Output: 2 (index of 30 in the list)


# 2. Binary Search (Interval Search)

    # A. Iterative Method (Preferred for Space Efficiency)
    # The iterative path uses a while loop to modify pointers (low and high), 
    # avoiding recursion call-stack overhead (O(1) space complexity)
def binary_search_iterative(arr, target):   # Craete a functuion accepting a array and a target
    low = 0                                 # Start the lower pointer at the first index of the list
    high = len(arr) - 1                     # Start the higher pointer at the last index of the list
    while low <= high:                      # Keep searching as long as the low pointer hasn't passed the high pointer
        mid = (low + high) // 2             # Find the middle position of the current search area
        if arr[mid] == target:              # If the middle item is the target, it found the item
            return mid
        elif arr[mid] < target:             # If the middle item is too small, look in the right half
            low = mid + 1                   # Move the lower pointer past the middle item
        else:
            high = mid - 1                  # Move the higher pointer on the left side of middle item
    return -1                               # Return -1 if the loop finishes and the target is not in the list
numbers = [10, 11, 12, 13, 14, 15]
result = binary_search_iterative(numbers, 13)
print(f"The position of the intended number: {result}")


    # B. Recursive Method
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
numbers = [100, 200, 300, 400, 500]
result = binary_search_recursive(numbers, 500, 0, len(numbers) - 1)
print(f"The position of the intended number: {result}")