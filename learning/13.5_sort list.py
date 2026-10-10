# List objects have a sort() method that will sort the list alphanumerically, ascending
# or descending, and in place. The sort() method modifies the original list and does not return a new list.

# sort the list alphabatically, ascending.
list1st = ["v","f","r","t","a","n"]
list1st.sort()  # Sorts the list in place.
print(list1st)

# sort the list alphabatically, descending.
list2nd = ["v","f","r","t","a","n"] 
list2nd.sort(reverse=True)  # Sorts the list in place in descending order.
print(list2nd)

#sort the list numerically, ascending.
list3rd = [65,346,23,12,55,6,89]
list3rd.sort()
print(list3rd)  # Sorts the list in place in ascending order.

#sort the list numerically, descending.
list4th = [65,346,23,12,55,6,89]
list4th.sort(reverse = True)
print(list4th)  # Sorts the list in place in descending order.