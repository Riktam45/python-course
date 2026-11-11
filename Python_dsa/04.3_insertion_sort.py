# insertion sort
# Builds the sorted list one item at a time by inserting elements into their correct position

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
numbers = [564,323,24,646,7,37,9]
insertion_sort(numbers)
print(numbers)


"""
Line-by-Line Breakdown

# for i in range(1, len(arr))   --> Starts an outer loop from index 1 (the second element) to the end of the 
#                                   list. The element at index 0 is assumed to be already sorted on its own.

# key = arr[i]  --> Stores the current element being examined in a variable called key so it is not 
#                   lost when other elements shift over its position.

# j = i - 1 --> Sets a pointer j to the index immediately to the left of key 
#               (the end of the already-sorted portion).

# while j >= 0 and key < arr[j] --> Starts an inner loop that runs as long as j has not passed the 
#                                   start of the list (j >= 0) and key is smaller than the element at arr[j].

# arr[j + 1] = arr[j]   --> Shifts the larger element at arr[j] one position to the right 
#                           (j + 1) to make room for key.

# j -= 1    --> Moves the pointer j one step to the left to check the next previous element in the sorted portion

# arr[j + 1] = key  --> Places key into the empty spot left behind once the while loop stops.
"""

"""

Step-by-Step Execution Dry Run

1. Initial List: [564, 323, 24, 646, 7, 37, 9]
2. Pass i = 1 (key = 323):
	• Compare 323 with 564 (j = 0). Since 323 < 564, 564 shifts right to index 1.
	• Loop ends (j = -1). Insert 323 at index 0.
	• List becomes: [323, 564, 24, 646, 7, 37, 9]
3. Pass i = 2 (key = 24):
	• Compare 24 with 564 (j = 1) and 323 (j = 0). Both are greater than 24, so both shift right.
	• Loop ends (j = -1). Insert 24 at index 0.
	• List becomes: [24, 323, 564, 646, 7, 37, 9]
4. Pass i = 3 (key = 646):
	• Compare 646 with 564 (j = 2). Since 646 < 564 is false, the while loop does not run.
	• Insert 646 back at index 3 (j + 1). No change.
	• List becomes: [24, 323, 564, 646, 7, 37, 9]
5. Pass i = 4 (key = 7):
	• Compare 7 with 646, 564, 323, and 24. All four are greater than 7, so all shift one spot right.
	• Loop ends (j = -1). Insert 7 at index 0.
	• List becomes: [7, 24, 323, 564, 646, 37, 9]
6. Pass i = 5 (key = 37):
	• 646, 564, and 323 are greater than 37 and shift right.
	• Loop stops at j = 1 because 37 is not less than 24. Insert 37 at index 2 (j + 1).
	• List becomes: [7, 24, 37, 323, 564, 646, 9]
7. Pass i = 6 (key = 9):
	• 646, 564, 323, 37, and 24 are greater than 9 and shift right.
	• Loop stops at j = 0 because 9 is not less than 7. Insert 9 at index 1 (j + 1).
	• List becomes: [7, 9, 24, 37, 323, 564, 646]
"""