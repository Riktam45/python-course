# 2. Standard DSA Sorting Algorithms


# a. Bubble sort
    # Repeatedly compares adjacent items (from left to right) and swaps them if they are in the wrong order, 
    # pushing the largest item to the end in each pass

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
numbers = [324,43,42,13,5,672,74,23]    
bubble_sort(numbers)
print(numbers)


# without function 
mylist = [324,43,42,13,5,672,74,23] 
n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)


# b. Modified Bubble sort

def modified_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
                swapped = True
        if not swapped:  # Optimization if array is already sorted
            break
    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)
modified_bubble_sort(numbers)
print("Sorted list:", numbers)


# Without function
mylist = [64, 34, 25, 12, 22, 11, 90]
n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break
print(mylist)

"""
1. Function Setup
"def bubble_sort(arr)" --> This defines a function named bubble_sort that accepts a list called arr.
"n = len(arr)"         --> This stores the total number of items in the list inside the variable n

2. The Outer Loop (Tracking Passes)
"for i in range(n - 1)" --> This loop controls how many full passes we make through the list
## We use n - 1 because once you sort n - 1 elements, the final remaining element is automatically 
    in its correct spot. For a list of 4 items (n = 4), you only need 3 passes (range(3), 
    which runs for i = 0, 1, 2) to guarantee the entire list is sorted.

"swapped = False"       --> Before starting a new pass, we assume the list is already       
                            sorted by setting this flag to False.
## We assume the list is sorted at the start of each pass so we can detect the exact moment 
#   the list finishes sorting and stop early. Without this assumption, the code would blindly 
#   keep running empty passes even after every number is already in the right place.

3. The Inner Loop (Comparing and Swapping)
"for j in range(0, n - i - 1)" -->  This loop steps through the unsorted part of the list from left to right. 
                                    We subtract i because after each pass, the largest items are already 
                                    locked into place at the end. We subtract 1 so j + 1 never goes past 
                                    the end of the list.

"if arr[j] > arr[j + 1]"        --> This checks if the current item (arr[j]) is larger than the item right 
                                    next to it (arr[j + 1]).

"arr[j], arr[j + 1] = arr[j + 1], arr[j]" --> If the left item is larger, this line swaps their positions in place.

"swapped = True"                --> Because we had to make a swap, we update the flag to True to 
                                    show the list was not fully sorted yet.

4. Early Exit and Return
"if not swapped" --> Once the inner loop finishes a full pass, this checks if swapped is still False.

"break"          --> If zero swaps happened during that pass, the list is completely sorted, 
                     so we stop the outer loop early to save time.

"return arr"     --> Once the loops finish, the function returns the newly sorted list.


"""
