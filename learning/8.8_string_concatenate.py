# Because of Python strings are immutable, 
# most concatenation methods create a brand-new string object in memory each time they run


# 1. The + Operator (Best for a few strings)
str1 = "HELLO"
str2 = "WORLD"
c = str1 + str2             # this method cant give space in between them
result = str1 + " " + str2  # this " " method give a space when concatenate strings
print(result)
print(c)

# 2. The join() Method (Best for many strings)
list_of_string = ["Myself", "I", "am", "a", "Python", "Developer"]
result = " ".join(list_of_string) # this method give a space when concatenate strings
result_flat =  "".join(list_of_string) # this method cant give space in between them
print(result)
print(result_flat)

# 3. The % Operator (Old Style)
name = "Ritkam"
age = 23
result = "My name is %s and I am %d years old." % (name, age)
print(result)       

# 4. The format() Method (New Style)
name = "Ritkam"
age = 23            
result = "My name is {} and I am {} years old.".format(name, age)
print(result)

# 5. f-Strings (Best for Python 3.6 and above)
name = "Ritkam" 
age = 23
result = f"My name is {name} and I am {age} years old."
print(result)

# 6. implicit concatenation (Best for a few strings)
result = "My name is " "Ritkam"     # space after first string's quotation gives a spcae time of concatenate 
print(result)
