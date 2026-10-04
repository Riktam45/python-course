# Adding an item to the dictionary is done by using a new index key and assigning a value to it
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
cars["year"] = 2020
print(cars)

# The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs
bikes = {
    "brand": "ducati",
    "model": "scrambler",
    "color": "browm"  
}
bikes.update({"version":800})
print(bikes)