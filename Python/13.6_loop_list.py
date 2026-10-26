# 1. The Standard for Loop 
loop_list = ["Alpha", "Beta", "Charlie", "Delta"]
for x in loop_list:
    print(x)

loop_list1 = ["A", "B", "C"]
for x in range(len(loop_list1)):
    print(loop_list1[x])

# The output shows the text values because the code uses loop_list1[i], 
# which looks up the actual item at that index position.
# Here is exactly how the print(loop_list1[i]) step translates the index numbers back into the words:
# When i is 0: print(loop_list1[i]) looks up index 0, which outputs apple.
# When i is 1: print(loop_list1[i]) looks up index 1, which outputs banana.
# When i is 2: print(loop_list1[i]) looks up index 2, which outputs cherry.
# If you were to change that line to just print(i), the output would change to the index numbers 0, 1, 2.


# 2. Using enumerate() (To get both Index and Item)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# 3. List Comprehension (Short Syntax)
# Use list comprehension if you want to modify the list items or create a new list in a single line of code
fruits = ["apple", "banana", "cherry"]
loud_fruits = [fruit.upper() for fruit in fruits]       # Capitalizes every item in the list
print(loud_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# 4. Using range(len()) (Looping by Index)
# This approach loops through the list using numeric indices rather than pulling the objects directly.
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

 
#   Method	                            Best Used For	
# for item in list	                Simple, clean data retrieval.	
# for i, item in enumerate(list)	When you need the index and the value.	
# List Comprehension	            Modifying or filtering data quickly.	
# while loop	                    Advanced control (skipping or dynamically altering indices).
