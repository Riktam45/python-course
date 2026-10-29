# In Python, you cannot access individual items in a set by referring to an index or a key 
# because sets are unordered and unindexed collections


# 1. Check if an Item Exists (Membership Testing)
access_set = {1,2,3,4,5,6,7,8,9,10}
print(5 in access_set)
# the output will show in TRUE and FALSE
# or
if 5 in access_set:
    print("5 is present in the set")      # checking if an item present in the set


# 2. Iterate Over the Items (Looping)
access_set1 = {1,2,3,4,5,6,7,8,9,10}
for x in access_set1:
    print(x)


# 3. checking if an item not present in the set
access_set1 = {1,2,3,4,5,6,7,8,9,10}
print(5 not in access_set1)
# the output will show in TRUE and FALSE


   