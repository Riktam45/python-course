# Check if a substring or character exists inside a string
# Use the in operator, which is the most Pythonic and efficient way to check for membership.


# 1 method is to use the in operator, 
# which is the most Pythonic and efficient way to check for membership. 
# It returns True if the substring or character is found in the string, and False otherwise.
txt = "The best feeling is to be happy"
print("best" in txt)


# 2 method is to use the find() method, 
# which returns the index of the first occurrence of the substring or character in the string. 
# If the substring or character is not found, it returns -1.
any_variable = "lied on vivid of the darkness"
if "do" in any_variable:
    print("yes, checked string is present")
else:
    print("no, checked string is not present")


# 3 method is to use the index() method, which is similar to find() 
# but raises a ValueError if the substring or character is not found. 
# It returns the index of the first occurrence of the substring or character in the string.
try:
    index = any_variable.index("do")
    print(f"Substring found at index: {index}") 
except ValueError:
    print("Substring not found")