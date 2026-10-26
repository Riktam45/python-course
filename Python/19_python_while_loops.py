# Python has two primitive loop commands:
# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
    print(i)
    i += 1          # remember to increment i, or else the loop will continue forever.

# the break statement we can stop the loop even if the while condition is true
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

# the continue statement we can stop the current iteration, and continue with the next
k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k)

## infinite loop
    # k = 0
    # while k < 6:
    # print(k)
    # if k == 3:
    #     continue
    # k += 1
## The "Trapped" Iteration (k = 3)Check Condition: The loop checks while k < 6. 
# Since 3 < 6, it enters the loop.Print: It runs print(k), so 3 is printed to the screen.
# If Statement: It checks if k == 3. This is true.The Continue Hit: The code hits continue.
# Because continue means "stop this turn right now and jump back to the top of the while loop", 
# the computer immediately jumps back up to line 2 (while k < 6:).


    