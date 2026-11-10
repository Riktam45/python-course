# Searching using the .index() -->

def linear_search_index(arr, target):
    try:
        # .index() performs a sequential search and returns the first matching index
        return arr.index(target)
    except ValueError:
        # Return -1 if the target element is not found in the list
        return -1

# Example usage:
my_list = [10, 23, 45, 70, 11, 15]

# Case 1: Element is in the list
target_1 = 70
result_1 = linear_search_index(my_list, target_1)
print(f"Element {target_1} found at index: {result_1}")  # Output: 3

# Case 2: Element is not in the list
target_2 = 99
result_2 = linear_search_index(my_list, target_2)
print(f"Element {target_2} result: {result_2}")          # Output: -1
