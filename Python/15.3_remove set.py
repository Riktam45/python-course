# using remove() methhod
thisset = {1, 2, 3, 4, 5}
thisset.remove(3)  # remove item 3 from the set
print(thisset)
#If the item to remove does not exist, remove() will raise an error.

#using discard() method
thisset1 = {1, 2, 3, 4, 5}
thisset1.discard(4) # remove item 4 from the set
print(thisset1)
#If the item to remove does not exist, discard() will NOT raise an error

# using clear() method
thisset2 = {1, 2, 3, 4, 5}
thisset2.clear()  # remove all items from the set
print(thisset2)  # this will print an empty set
# the output of this will be set() which is an empty set
#This set() is just Python’s official way of representing an empty set. 
# Remember, {} is for an empty dictionary—so set() is used instead to make it crystal clear that you're dealing with a set.

# using del() method
thisset3 = {1, 2, 3, 4, 5}
del thisset3  # delete the set completely
# print(thisset3)  # this will raise an error because the set no longer exists