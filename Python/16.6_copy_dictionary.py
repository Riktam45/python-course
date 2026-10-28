# cannot copy a dictionary simply by typing dict2 = dict1, because:dict2 will only be a reference to dict1, 
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy()

# Shallow Copy (For flat dictionaries)
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
c_cars = cars.copy()
print(c_cars)

# Another way to make a copy is to use the built-in function dict()
cars1 = {
    "brand": "BMW",
    "model": "M4",
    "color": "Blue"  
}
d_cars = dict(cars1)
print(d_cars)
