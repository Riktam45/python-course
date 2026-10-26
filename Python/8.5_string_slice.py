# Python string slicing allows you to extract a specific portion (a substring) from a string. 
# Because strings in Python are immutable, slicing does not modify the original text—it returns a completely new string.
# string[start:stop:step]

import string


a = "Abracadabra"
print(a[2:7])       # in slicing start from 2 so start with 2 numbered charecter and end in 6th charecter  
                    # because 7 is end point so it didnt print the 7th charecter   
b = "super Upper"
print(b[:5])        # slicing from start

c = "super Upper"
print(c[5:])        # slicing to end

# in negative indexing last(most right sided) charecter is condsider as -1 then value is get bigger
# from right to left like -5 -4 -3 -2 -1

d = "Abracadabra"   
print(d[-5:-2])     

# in negative indexing printing the charecters from right to left so, the starting point(-2) is skipped 
# and then start print to the ending point with print the end point charecter(-5)
print(d[-4:])

# In Python, slicing only applies directly to sequence data types like strings, lists, and tuples 
# because they are ordered and indexed. 
# Sets and dictionaries do not support slicing because they are unordered collections.
# However, you can still extract a slice of data from sets or dictionaries by converting their keys, values, or items into a list or tuple first.


# Slicing with Lists 
list_slice = [1, 2, 3, 4, 5, 6]
print(list_slice[2:5])
print(list_slice[::-1])  # Reversing the list using slicing

# Slicing with tuples
tuple_slice = (10, 20, 30, 40, 50)
print(tuple_slice[1:4])
print(tuple_slice[::-1])  # Reversing the tuple using slicing

# Slicing with Sets (Indirect via Conversion)
set_slicing ={100, 20, 45, "Riktam"}
set_to_list = list(set_slicing)   # convert set to list
print(set_to_list[:])  # it gives random output because set is unordered and the order of elements in the list may vary each time you run the code

# Slicing with Dictionaries (Indirect via View Objects)
dictionary_slicing = {'a': "Ritkam", 'b': 23, 'c': 9.46}
dict_to_list1 = list(dictionary_slicing.keys())  # Convert keys to list
dict_to_list2 = list(dictionary_slicing.values())  # Convert values to list
dict_to_list3 = list(dictionary_slicing.items())  # Convert items to list of tuples
print(dict_to_list1[0:2])  # Slicing the converted list of keys
print(dict_to_list2[1:3])  # Slicing the converted list of values
print(dict_to_list3[0:2])  # Slicing the converted list of items

# s[start:stop]       piece of string

# s[:stop]            beginning → stop

# s[start:]           start → end

# s[:]                whole string

# s[start:stop:step]  slice with jumps

# s[::2]              every second character

# s[-1]               last character

# s[-2]               second-last character

# s[-3:]              last 3 characters

# s[:-1]              everything except last

# s[1:]               everything except first

# s[::-1]              reverse string