# removing the list python has several methods to remove items from a list
#    1. remove() - removes the first occurrence of a value from the list.
#    2. pop() - removes an item at a specified index and returns it.    
#    3. clear() - removes all items from the list.
#    4. del - deletes an item at a specified index or the entire list.

list1st = ["item1", "item2", "item3", "item4", "item5", "item6"]
list1st.remove("item3")    # using remove() to remove the first occurrence of "item3"
print(list1st)

list2nd = ["crud1", "crud2", "crud3", "crud4", "crud5"]
list2nd.pop(2)    # using pop() to remove the item at index 4 (fifth item)
#list2nd.pop()    # using pop() without any index is always pop the last element in the list    
print(list2nd)

list3rd = ["ele1", "ele2", "ele3", "ele4", "ele5"]
list3rd.clear()    # using clear() to remove all items from the list. but list will still exist
print(list3rd)

list4th = ["item1", "item2", "item3", "item4", "item5"]
del list4th[2]    # using del to remove the item at index 2 (third item)
print(list4th)

list5th = ["item1", "item2", "item3", "item4", "item5"]
del list5th    # using del to delete the entire list
# print(list5th)  # Uncommenting this line will raise an error because the list no longer exists

# Difference of del and pop is that pop() is a method that removes an item and returns its value, 
# while del is a keyword that permanently deletes an item (or slice) without returning anything