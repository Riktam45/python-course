# for diplaying all items the set
access_set = {1,2,3,4,5,6,7,8,9,10}
for x in access_set:
    print(x)

#checking if an item present in the set
access_set1 = {1,2,3,4,5,6,7,8,9,10}
print(5 in access_set1)
# the output will show in TRUE and FALSE

#checking if an item not present in the set
access_set1 = {1,2,3,4,5,6,7,8,9,10}
print(5 not in access_set1)
# the output will show in TRUE and FALSE

#checking if an item present in the set
if 5 in access_set1:
    print("5 is present in the set")    