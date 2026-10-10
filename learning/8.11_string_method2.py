# 3. Splitting and Joining
# The split() and join() methods are built-in string manipulation tools used to 
# break text apart into a list and stitch a list back together into text

# i. The split() Method
# The split() method divides a string into a list of smaller pieces called substrings based on a chosen separator or delimiter.
# Syntax: string.split(separator, maxsplit)
# Default behavior: If you leave the separator blank, it splits the text at any whitespace (spaces, tabs, or newlines).
text = "Riktam Sarkar, will Graduate in 2027"
print(text.split())         # Split by individual words (Default)
print(text.split(","))      # it makes two different string using split ','
print(text.split("will Graduate"))      # Split by a specific word
print(text.split("G"))      # Split by a specific letter

# ii. join() mehtod
# The join() method does the exact opposite: it glues a collection of text items together from 
# an iterable (like a list) into a single unified string.
# Syntax: separator.join(list)
# Important rule: Every item in the list must be a string, or Python will raise a type error.
words = ["Data", "Science", "Python"]
sentence = " ".join(words)
print(sentence)

# 4. Replacing and Modifying

# i. Replacing Substrings: .replace()
# The replace() method swaps out a target substring with a new one.
# Syntax: string.replace(old, new, count)
# old: The text you want to find.
# new: The text you want to insert.
# count (Optional): The maximum number of replacements to make (defaults to all occurrences)

text = "apple, banana, apple, cherry"
new_text = text.replace("apple", "orange")  # Replace all occurrences
limited_text = text.replace("apple", "orange", 1)   # replace only the first occurance
print(new_text)         
print(limited_text)

# ii. Modifying Text case
# Modifying Text Case
# Python provides built-in methods to easily change the capitalization of a string.

# Method	        What it does	                            Example	                Output
# .upper()	        Converts all characters to uppercase	"python".upper()	        "PYTHON"
# .lower()	        Converts all characters to lowercase	"PyThOn".lower()	        "python"
# .capitalize()	    Capitalizes only the first letter of 
#                       the string	                        "hello world".capitalize()	"Hello world"
# .title()	        Capitalizes the first letter of 
#                       every word	                        "hello world".title()	    "Hello World"
# .swapcase()	    Flips uppercase to lowercase and 
#                       vice versa	                        "PyThOn".swapcase()	        "pYtHoN"

# text.removeprefix(prefix): Removes a specific starting text from a string if it is there. 
#       If the string does not start with that prefix, it leaves the string alone.
# text.removesuffix(suffix): Removes a specific ending text from a string if it is there. 
#       If the string does not end with that suffix, it leaves the string alone.
# text.zfill(width): Pads a string on the left with zero (0) digits until it reaches your chosen total length (width). 
#       If the string is already as long as or longer than the width, it changes nothing.