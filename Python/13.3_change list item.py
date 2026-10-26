# Change list item in Python
unchanged_list = ["siko", "peso", "selolya", "plama"]
unchanged_list[1] ="espo"               #this replace a specific item , here the second item is reaplaced
print(unchanged_list)

#change a range of items
ranged_elements = ["ele1", "ele2", "ele3", "ele4", "ele5", "ele6", "ele7", "ele8"]
ranged_elements[2:7] = ["new1", "new2"]    #this change the second to seventh item
print(ranged_elements)

# insert an item into existing element without changing the element with using insert().
inserted_list = ["pencil", "pen", "eraser"]
inserted_list.insert(1, "marker")  #this insert a new item at the second position
print(inserted_list)

# insert an item at last using append()
append_list = ["apple", "banana", "cherry"]
append_list .append("orange")    #this append a new item at the end of the list.
print(append_list)

# merge two list using extens()
existing_list = ["item1", "item2", "item3"]
new_list = ["item4", "item5"]
existing_list.extend(new_list)  #this merge two list
print(existing_list)


# Difference between apeend and insert 
# append() always adds a single item to the very end of the list. Takes exactly 1 argument (item)
# insert() allows to add an item at any specified index (position) within the list. Takes exactly 2 arguments (index, item)
