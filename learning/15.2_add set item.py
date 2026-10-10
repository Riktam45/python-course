#once a set set is created it can not be changed, but you can add new items to it.
thisset = {"apple", "banana", "cherry"}
thisset.add("komola lebu")  # add a new item to the set
print(thisset)

#add sets
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)  # add items from set2 to set1
set2.update(set1)  # add items from set1 to set2
print(set1)
print(set2)

#add iterable
thisset1 = {"nouka", "gari", "sob"}
thislist = ["komola lebu", "murgi", "goru"]
thisset1.update(thislist)  # add items from list to set
print(thisset1)  # will show {'gari', 'goru', 'komola lebu', 'murgi', 'nouka', 'sob'}
