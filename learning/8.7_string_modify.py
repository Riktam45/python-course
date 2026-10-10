# In Python, strings are immutable, meaning you cannot alter them in place. 
# Any operation that modifies a string actually returns a new string


a = "Hello This python learning is for datascience"
print(a.upper())            # UPPER CASE OF ALL STRING
print(a.lower())            # lowercase of all string
print(a.title())            # Title Case Of All String
print(a.capitalize())       # Capitalize the first letter of the string


b = "Hello This Python Learning is For Datascience"
print(b.replace("Hello","P"))       # replace the string "Hello" with "P" 

c = "Hello This Python Learning is For Datascience"
print(c.replace("Hello","P").replace("Learning","Training"))  # replace multiple strings        


# The split() method returns a list where the text between the specified separator becomes the list items.
example_string2 = "python is amazing"        
split_string = example_string2.split()       # default split by spaces
print(split_string)

example_string3 = "one,two,three,four,five"
split_list = example_string3.split(',')
print(split_list)

# Modifying by Index (Slicing)
# Because you cannot do text[0] = 'Y', you must slice the string and concatenate the new character
string = "RIKTAM"
change = string[:3] + 'Y' + string[4:]  # Replace the located charecter character with 'Y'
print(change)

# locating the string
# the string is "RIKTAM" and the method is - string[:3] + 'Y' + string[4:] so, 
# R   I   K   T   A   M
# 0   1   2   3   4   5
# string[:3] (Before index 3): Grabs indices 0, 1, and 2 → "RIK"
# 'Y' (At index 3): The new character replacing the old one.
# string[4:] (After index 3): Grabs index 4 to the end → "AM"
# Putting them all together gives you "RIYAM".

# Converting to a List
# If you need to make multiple complex modifications, turn the string into a list, alter the items, and join it back together.
text = "RIKTAM"
turn_to_list = list(text)
turn_to_list[3] = 'Y'   # modify the 4th character (index 3) to 'Y'
turn_to_list.append('!')  # append '!' at the end of the list
print(turn_to_list)