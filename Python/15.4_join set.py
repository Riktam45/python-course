# using union() method
thisset = {1,3,4,5,7}
thisset1 = {2,6}
thisset2 = thisset.union(thisset1)  # combine two sets
print(thisset2)

# using | operator
thisset3 = {1,3,4,5,7}
set1 = {"bankai","shikai"}
set2 = thisset3 | set1
print(set2)

# join multiple sets into one set
mset1 = {"tin duniya"}
mset2 = {"nouka"}
mset3 = {"sohoj manush"}
mset4 = {"bristi"}
joined_set = mset1.union(mset2, mset3, mset3, mset4)  # combine multiple sets
joined_set1 = mset1 | mset2 | mset3 | mset4  # using | operator to join multiple sets
print(joined_set)
print(joined_set1)


# The | operator only allows to join sets with sets, 
# and not with other data types like the union() method.
# the union() method can exclude any dulpicate items,
# while the | operator will not exclude duplicates.

# and if i want to keep only duplicate them use intersection() method
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)  # keep only items that are present in both sets
print(set3)

# we can use & operator for alternative to intersection()