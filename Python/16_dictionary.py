# A Python dictionary is a built-in data structure that stores data in key-value pairs.

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
print(my_dict)

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key : value pairs, and can be referred to by using the key name.
my_dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "color": "Red"
}
print(my_dict["brand"])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key


# Iterating Through Dictionaries
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
for fruit in inventory:       # Loop through keys only (default behavior)
    print(fruit)
for count in inventory.values():    # Loop through values only
    print(count)
for fruit, count in inventory.items():    # Loop through both keys and values simultaneously
    print(f"We have {count} {fruit}.")

