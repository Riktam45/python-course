# To loop through a dictionary in Python, can be iterate over its keys, 
# values, or key-value pairs using a for loop

# Print all key names in the dictionary, one by one:
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
for x in cars:
    print(x)

# 1. Loop Through Key-Value Pairs (Recommended)
# Use the .items() method to extract both the key and the value at the same time.
details = {"Riktam" : "Data Science", "Bittu": "Computer science", "Rik" : "Art"}
for name, role in details.items():
    print(f"User: {name}, Interest : {role}")


# 2. Loop Through Keys Only
# Looping over the dictionary directly defaults to iterating through the keys.
details = {"Riktam" : "Data Science", "Bittu": "Computer science", "Rik" : "Art"}
for name in details:
    print(name)

#  Also use the .keys() method explicitly.
for name in details.keys():
    print(name)

# 3. Loop Through Values Only
# Use the .values() method if you only need the data stored inside the keys.
details = {"Riktam" : "Data Science", "Bittu": "Computer science", "Rik" : "Art"}
for name in details.values():
    print(name)

# Print all values in the dictionary, one by one
# Using Dictionary Directly
# A dictionary itself is iterable. Iterating over it directly returns its keys, 
# which can then be used to access the corresponding values.
cars1 = {
    "brand": "BMW",
    "model": "M4",
    "color": "Blue"  
}
for x in cars1:
    print(cars1[x])