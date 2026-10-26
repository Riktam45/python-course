# Python provides a rich set of built-in string methods to manipulate, format, search, and validate text. 
# Because strings in Python are immutable, these methods never modify the original string; instead, 
# they always return a new value


# 1. Case Conversion & Formatting

# Method	                Description	                                            Example
# lower()	            Converts all characters to lowercase.	           "PyThOn".lower() → "python"
# upper()	            Converts all characters to uppercase.	           "python".upper() → "PYTHON"
# capitalize()	        Capitalizes the first character 
#                           and lowercases the rest.	                   "hello WORLD".capitalize() → "Hello world"
# title()	            Capitalizes the first letter of every word.	       "hello world".title() → "Hello World"
# swapcase()	        Flips uppercase to lowercase and vice versa.	   "PyThOn".swapcase() → "pYtHoN"
# casefold()	        An aggressive lowercase helper for uniform, 
#                           case-insensitive matching.	                   "Riktam".casefold() → "riktam"
# center(width, fill)	Centers the string padded by a 
#                           specified character.	                       "Hi".center(6, "-") → "--Hi--"
# zfill(width)	        Pads the left side of a string with 
#                           zeros to a set width.	                       "42".zfill(4) → "0042"

x3 = "I am a student"
y3 = x3.center(400)      #Returns a centered string with a specified width
print(y3)

# 2. Searching & Counting
# Python provides several built-in string methods to effectively search for substrings and count their frequencies.

# i. Counting Substrings
# string.count(substring, start, end)
# Returns the number of non-overlapping occurrences of a substring.
text  = "Riktam Riktam"
print(text.count("am"))
print(text.count("Riktam"))     
print(text.count("Riktam", 0, 4)) # The sliced part of the string Python searches in is text[0:4], which equals "Rikt". The full word "Riktam" cannot fit inside a 4-character window, so Python finds 0 occurrences.

# ii. Searching for Substring Locations
# Python offers two main pairs of methods to find where a substring is located: find() / rfind() and index() / rindex().
# string.find(substring, start, end)
text = "Find the needle from a heystack"
print(text.find("needle"))
print(text.find("Gold"))        # output is -1 because it didnt find "Gold" on string

# string.rfind(substring, start, end)
# Searches from right to left (from the end of the string) and returns the index of the last occurrence. Returns -1 if not found.
numbers = "one two one three"
print(numbers.find("one"))   # Output: 0 (first occurrence)
print(numbers.rfind("one"))  # Output: 8 (last occurrence)
 
# string.index(substring, start, end) & string.rindex()
# Identical to find() and rfind(), but they throw a ValueError if the substring isn't found. Use these when a missing substring means an error in your program logic
text = "Python"
print(text.index("yt"))     # y start from 1 index

 
#Summary Comparison Table

# Method	Direction	    Returns If Found	        Returns If Missing	    Best Used For
# count()	Left to Right	Total occurrences (int)	        0	                Frequency metrics
# find()	Left to Right	Index of 1st match (int)	    -1	                Safe location lookups
# rfind()	Right to Left	Index of last match (int)	    -1	                Locating trailing patterns
# index()	Left to Right	Index of 1st match (int)	Raises ValueError	    Strict index requirements
