#In Python, you can access dictionary values using square brackets [] or the .get() method.

# 1. Accessing a Single Value
# Square Brackets []: Fastest method, but raises a KeyError if the key is missing.
# .get() Method: Safer method; returns None (or a custom default) if the key doesn't exist instead of crashing.

my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
print(my_dict["model"])
print(my_dict.get("brand"))
print(my_dict.get("year"))  # Output: None
print(my_dict.get("year", "Not provided"))  # Output: Not Provided (custom default)

# 2. Checking if a Key Exists
my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
if "name" in my_dict:
    print(my_dict["name"])


# 3. Accessing Keys, Values, and Items
# another method for accessing the element usnig key
my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
print(my_dict.get("color"))
x = my_dict.keys()
print(x)            # can be this -- print(my_dict.keys()) 


# Values() method will return a list of all the values in the dictionary.
bikes = {
    "brand": "ducati",
    "model": "scrambler 800",
    "color": "browm"  
}
y = bikes.values()
print(y)

# 4. Using 'in' Operator 
sample_dict2 = {'Name': "Ritkam", 'Age': 23}  
for key in sample_dict2:       # looping through each key
    print(key, sample_dict2[key])


# Add a new item to the original dictionary
bikes["year"] = 2024
print(y)

