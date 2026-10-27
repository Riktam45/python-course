# 1. Direct Assignment (Most Common)
# Access the existing key using square brackets [] and assign it a new value.
# change the value of a specific item by referring to its key name
bikes = {
    "brand": "ducati",
    "model": "scrambler 800",
    "color": "browm"  
}
bikes["color"] = "yellow"
print(bikes)


# 2. Using the .update() Method
# The update() method is ideal if you want to change multiple items at once. 
# It accepts another dictionary or an iterable of key-value pairs

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
cars.update({"color":"White"})
print(cars)