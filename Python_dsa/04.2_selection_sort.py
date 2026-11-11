# c. Selection sort
# Selection sort works by repeatedly finding the minimum element from 
# the unsorted portion of the list and moving it to the beginning

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index holds the minimum value
        min_idx = i
        
        # Scan the remaining unsorted elements
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(data))


"""
# min_idx = i   --> Assumes that the current index i holds the minimum value in the remaining unsorted portion.

# for j in range(i + 1, n)  --> The inner loop. It scans all the subsequent elements from index 
#                               i + 1 to the end of the list (n - 1) to search for a smaller value.

# if arr[j] < arr[min_idx] --> Compares the element at the current inner index j with the element at min_idx.

# min_idx = j   --> If a smaller element is found at index j, updates min_idx to point to j.

# arr[i], arr[min_idx] = arr[min_idx], arr[i]   --> Swaps the smallest element found (arr[min_idx]) with 
#                                                   the first element of the unsorted section (arr[i]).
"""

"""
Step-by-Step Execution Dry Run

1. Initial List: [64, 25, 12, 22, 11]

2. Pass i = 0 (min_idx starts at 0 / value 64):
	• Inner loop scans 25, 12, 22, 11 and finds 11 at index 4 is the smallest.
	• Swap arr[0] (64) with arr[4] (11).
	• List becomes: [11, 25, 12, 22, 64]

3. Pass i = 1 (min_idx starts at 1 / value 25):
	• Inner loop scans 12, 22, 64 and finds 12 at index 2 is the smallest.
	• Swap arr[1] (25) with arr[2] (12).
	• List becomes: [11, 12, 25, 22, 64]

4. Pass i = 2 (min_idx starts at 2 / value 25):
	• Inner loop scans 22, 64 and finds 22 at index 3 is the smallest.
	• Swap arr[2] (25) with arr[3] (22).
	• List becomes: [11, 12, 22, 25, 64]

5. Pass i = 3 (min_idx starts at 3 / value 25):
	• Inner loop scans 64; 25 remains the smallest in this slice. No change.
	• List becomes: [11, 12, 22, 25, 64]
    
6. Pass i = 4:
	• Reaches the last element; sorting is complete.
"""