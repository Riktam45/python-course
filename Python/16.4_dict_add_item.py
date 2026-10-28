# 1. Direct Assignment (Most Common)
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
cars = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
cars["year"] = 2020
print(cars)

# 2. The .update() Method
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

# 3. The .setdefault() Method
# Use .setdefault() if you want to add a key only if it does not already exist. 
# If the key is already present, the dictionary remains unchanged.
user = {"name": "Riktam", "age": 23}
user.setdefault("country", "IND")           # Adds 'country' because it doesn't exist
user.setdefault("age", 30)                  # Does nothing because 'age' already exists
print(user)



