# Data can be delete from a Python dictionary using four primary approaches depending on whether want to 
# remove a specific key, retrieve the value while deleting, 
# remove the last item, or clear the dictionary completely.


# Method / Keyword	    Best Used For	                Returns	                Safe from Missing Keys?
# del my_dict[key]	    Deleting a specific key         Nothing                 No (Raises KeyError)
#                                   efficiently.	       	
# my_dict.pop(key,      Safely deleting a key and       The value of the key    Yes (If default is provided)
#         default)	            keeping its value.		
# my_dict.popitem()	    Removing the last-inserted 	    (key, value) tuple	    No (Raises KeyError if empty)
#                                pair (LIFO order)
# my_dict.clear()	    Emptying the entire dictionary	Nothing	                Yes


# 1. The del Statement (Direct Deletion)
my_dict = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
del my_dict["color"]
print(my_dict)
# Warning: If the key does not exist, Python will throw a KeyError


# 2. The .pop() Method (Safe & Flexible)
#  using .pop() is highly recommended because it lets you provide a fallback value (like None) to
#  prevent crashes if a key is missing. It also extracts the value before deleting it
my_dict1 = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
model_value = my_dict1.pop("model")     # in the model_value variable 'A6' is stored after pop operation
print(model_value)


# 3. The .popitem() Method (Remove Last Item)
# This removes and returns the last inserted key-value pair in the dictionary as a tuple (key, value)
my_dict2 = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
print(f"Before using popitem the dictioanry is: {my_dict2}")
last_item = my_dict2.popitem()
print(f"After using popitem the dictioanry is: {my_dict2}")
print(last_item)


# 4. The .clear() Method (Empty Everything)
# It keeps the dictionary object but wipe out all of its data completely
my_dict3 = {
    "brand": "Audi",
    "model": "A6",
    "color": "Red"  
}
my_dict3.clear()
print(my_dict3)