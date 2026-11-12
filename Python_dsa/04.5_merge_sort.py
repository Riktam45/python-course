# Merge Sort (Divide & Conquer)

# Recursively splits the array in half, sorts each half, and merges them back together.

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1  
    return arr
numbers = [3,8,6,9,1,5]
list = merge_sort(numbers)
print(list)

"""

Line-by-Line Code Breakdown

• def merge_sort(arr): Defines the recursive function that accepts a list named arr.
• if len(arr) > 1: Checks if the list has more than one element. If it has 0 or 1 item, it is already sorted and skips straight to the return statement.
• mid = len(arr) // 2 Finds the middle index using floor division so the list can be split cleanly.
• left = arr[:mid] Slices the first half of the list into a new sub-list called left.
• right = arr[mid:] Slices the second half of the list into a new sub-list called right.
• merge_sort(left) Recursively calls the function to split and sort the left half completely.
• merge_sort(right) Recursively calls the function to split and sort the right half completely.
• i = j = k = 0 Initializes three index pointers to 0. Pointer i tracks left, j tracks right, and k tracks the main arr.
• while i < len(left) and j < len(right): Loops as long as both left and right still have unmerged elements.
• if left[i] < right[j]: Compares the current front items of both halves to find the smaller value.
• arr[k] = left[i] Places the smaller item from left into the current position of arr.
• i += 1 Moves the left pointer forward by one step.
• else: Runs when right[j] is smaller than or equal to left[i].
• arr[k] = right[j] Places the smaller item from right into the current position of arr.
• j += 1 Moves the right pointer forward by one step.
• k += 1 Moves the main arr pointer forward after placing an item.
• while i < len(left): Copies any leftover elements from left into arr once right is completely empty.
• while j < len(right): Copies any leftover elements from right into arr once left is completely empty.
• return arr Returns the sorted list back to the caller.
"""

"""
Step-by-Step Execution Dry Run

1. Initial Call (Root Level)

• Input: [3, 8, 6, 9, 1, 5] (Length: 6)
• Split: mid = 3
	• left = [3, 8, 6]
	• right = [9, 1, 5]
• Action: Pauses to completely sort left ([3, 8, 6]).

2. Sorting the Left Branch ([3, 8, 6])

• Call 2A: merge_sort([3, 8, 6]) (Length: 3)
	• Split: mid = 1 -> left = [3], right = [8, 6]
• Call 2B (Base Case): merge_sort([3]) has length 1, so it returns [3].
• Call 2C: merge_sort([8, 6]) (Length: 2)
	• Split: mid = 1 -> left = [8], right = [6]
	• Base Cases: [8] and [6] return immediately.
	• Merge 2C: Compares 8 and 6. Places 6 first, then 8. Returns [6, 8].
• Merge 2A: Merges left = [3] and right = [6, 8].
	• Compares 3 vs 6 -> places 3.
	• left is now empty, so the cleanup loop copies 6 and 8.
	• Returns [3, 6, 8] back to Step 1.

3. Sorting the Right Branch ([9, 1, 5])

• Call 3A: merge_sort([9, 1, 5]) (Length: 3)
	• Split: mid = 1 -> left = [9], right = [1, 5]
• Call 3B (Base Case): merge_sort([9]) has length 1, so it returns [9].
• Call 3C: merge_sort([1, 5]) (Length: 2)
	• Split: mid = 1 -> left = [1], right = [5]
	• Base Cases: [1] and [5] return immediately.
	• Merge 3C: Compares 1 and 5. Places 1 first, then 5. Returns [1, 5].
• Merge 3A: Merges left = [9] and right = [1, 5].
	• Compares 9 vs 1 -> places 1.
	• Compares 9 vs 5 -> places 5.
	• right is now empty, so the cleanup loop copies 9.
	• Returns [1, 5, 9] back to Step 1.

4. Final Merge (Root Level)

Now Step 1 merges left = [3, 6, 8] and right = [1, 5, 9] into arr:
• Compare 3 vs 1: 1 is smaller -> arr = [1, ...]
• Compare 3 vs 5: 3 is smaller -> arr = [1, 3, ...]
• Compare 6 vs 5: 5 is smaller -> arr = [1, 3, 5, ...]
• Compare 6 vs 9: 6 is smaller -> arr = [1, 3, 5, 6, ...]
• Compare 8 vs 9: 8 is smaller -> arr = [1, 3, 5, 6, 8, ...]
• Cleanup: left is empty, so 9 is copied to the end.
• Final Output: [1, 3, 5, 6, 8, 9]
"""