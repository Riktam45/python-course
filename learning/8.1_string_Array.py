# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character (char) data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.


# How Strings Mimic Arrays
# Because strings behave like sequences, you can interact with them using standard array-like syntax:
# Indexing: You can grab individual characters using square brackets, starting at 0.
# Slicing: You can extract a specific segment or substring from the string.
# Iteration: You can loop through the characters one by one.
# Length: The len() function returns the total number of characters.


text = "Python"
print(text[0])       # Accessing characters (Indexing)
print(text[0:4])     # Extracting parts (Slicing)
print(len(text))     # Finding length

# Immutability
text = "Python"
# This will throw a TypeError:
text[0] = "J"  # it gives an error because strings are immutable, meaning it cannot be changed their content after creation.