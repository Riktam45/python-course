my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
print(my_dict["model"])

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

# Add a new item to the original dictionary
bikes["year"] = 2024
print(y)

