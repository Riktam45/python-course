#there are several ways to join two lists in Python
# append() method
# + operator
# extend() method
# insert() method   

#join two lists using + operator
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d" ]
list3 = list1 + list2
print(list3)

#join two lists using extend() method
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d" ]
list1.extend(list2) 
print(list1)




