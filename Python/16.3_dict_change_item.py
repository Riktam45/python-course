# change the value of a specific item by referring to its key name
bikes = {
    "brand": "ducati",
    "model": "scrambler 800",
    "color": "browm"  
}
bikes["color"] = "yellow"
print(bikes)

#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
cars.update({"color":"White"})
print(cars)