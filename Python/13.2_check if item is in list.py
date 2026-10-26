# To check if an item exists in a Python list, the most common and efficient way is to use the in keyword. 
# It returns True if the item is present and False otherwise.


# 1. Check for a Single Item
# Use an if statement with the in operator
list_items = ["module 1", "module 2", "module 3", "module 4"]
if "module 2" in list_items:
    print("module 2 is in the list")
else:
    print("certain module isnt in the list, please check the list")

# 2. Check for Multiple Items (All or Any)
# If need to check whether multiple items exist in a list, 
# converting the list to a set provides the best performance.

# Scenario	            Code Example	                       Explanation
# Check if ALL      set(items).issubset(my_list)            Returns True only if every target 
#   items exist		                                            item is in the main list.
# Check if ANY      not set(items).isdisjoint(my_list)      Returns True if at least one 
#   item exists		                                            target item is found.

my_list = ["apple", "banana", "cherry", "date"]
targets = ["apple", "cherry"]
if set(targets).issubset(my_list):                      # 1. Check if ALL target items are present
    print("All target items are in the list.")                                                 
if not set(targets).isdisjoint(my_list):                # 2. Check if AT LEAST ONE target item is present
    print("At least one target item is in the list.")



