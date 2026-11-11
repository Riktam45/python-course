# Quick Sort (Divide & Conquer)
# Picks a "pivot" element and partitions the array so that smaller elements go left and larger elements go right

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [34, 436, 37, 65, 9, 36, 347, 67, 77, 62, 99]
arr = quicksort(arr)
print(arr)

"""

Line-by-Line Code Breakdown

• def quicksort(arr)    --> Defines the recursive function that accepts a list named arr.

• if len(arr) <= 1  --> Checks the base case to see if the list has 0 or 1 items.

• return arr    --> Returns the list immediately if the base case is met, since a 1-item or empty 
                    list is already sorted.

• pivot = arr[len(arr) // 2]    --> Selects the middle element of the current list as the comparison benchmark. 
                                    The // operator performs floor division to ensure a whole number index.

• left = [x for x in arr if x < pivot]  --> Uses list comprehension to gather all elements strictly smaller 
                                            than the pivot.

• middle = [x for x in arr if x == pivot]   --> Gathers all elements equal to the pivot, which cleanly handles 
                                                duplicate numbers.

• right = [x for x in arr if x > pivot]     --> Gathers all elements strictly larger than the pivot.

• return quicksort(left) + middle + quicksort(right)    --> Recursively sorts the left and right lists, 
                                                            then joins all three parts together in sorted order.

• arr = [34, 436, 37, 65, 9, 36, 347, 67, 77, 62, 99] Initializes the unsorted list of 11 integers.

• arr = quicksort(arr) Starts the sorting process and saves the final sorted list back into arr.

• print(arr) Displays the sorted result in the console.
"""

"""
Step-by-Step Execution Dry Run


1. Initial Call (Root Level)

• Input: [34, 436, 37, 65, 9, 36, 347, 67, 77, 62, 99] (Length: 11)
• Pivot: Index 11 // 2 = 5, which is 36.
• Partitioning:
	• left: [34, 9]
	• middle: [36]
	• right: [436, 37, 65, 347, 67, 77, 62, 99]
• Action: Pauses to sort left ([34, 9]).

2. Sorting the Left Branch ([34, 9])

• Call 2A: quicksort([34, 9]) (Length: 2)
	• Pivot: Index 2 // 2 = 1, which is 9.
	• Partitioning: left = [], middle = [9], right = [34].
• Call 2B (Base Case): quicksort([]) returns [].
• Call 2C (Base Case): quicksort([34]) returns [34].
• Combine 2A: [] + [9] + [34] returns [9, 34] back to Step 1.

3. Sorting the Right Branch ([436, 37, 65, 347, 67, 77, 62, 99])

• Call 3A: quicksort([436, 37, 65, 347, 67, 77, 62, 99]) (Length: 8)
	• Pivot: Index 8 // 2 = 4, which is 67.
	• Partitioning:
		• left: [37, 65, 62]
		• middle: [67]
		• right: [436, 347, 77, 99]
Sub-branch 3A-Left ([37, 65, 62]):
• Call 3B: quicksort([37, 65, 62]) (Length: 3)
	• Pivot: Index 3 // 2 = 1, which is 65.
	• Partitioning: left = [37, 62], middle = [65], right = [].
• Call 3C: quicksort([37, 62]) (Length: 2)
	• Pivot: Index 2 // 2 = 1, which is 62.
	• Partitioning: left = [37], middle = [62], right = [].
	• Base Cases: [37] and [] return immediately.
	• Combine 3C: [37] + [62] + [] returns [37, 62].
• Combine 3B: [37, 62] + [65] + [] returns [37, 62, 65].
Sub-branch 3A-Right ([436, 347, 77, 99]):
• Call 3D: quicksort([436, 347, 77, 99]) (Length: 4)
	• Pivot: Index 4 // 2 = 2, which is 77.
	• Partitioning: left = [], middle = [77], right = [436, 347, 99].
• Call 3E: quicksort([436, 347, 99]) (Length: 3)
	• Pivot: Index 3 // 2 = 1, which is 347.
	• Partitioning: left = [99], middle = [347], right = [436].
	• Base Cases: [99] and [436] return immediately.
	• Combine 3E: [99] + [347] + [436] returns [99, 347, 436].
• Combine 3D: [] + [77] + [99, 347, 436] returns [77, 99, 347, 436].
Combine 3A: [37, 62, 65] + [67] + [77, 99, 347, 436] returns [37, 62, 65, 67, 77, 99, 347, 436] back to Step 1.

4. Final Combination

• Combine Step 1: left + middle + right
• [9, 34] + [36] + [37, 62, 65, 67, 77, 99, 347, 436]
• Final Output: [9, 34, 36, 37, 62, 65, 67, 77, 99, 347, 436]
"""