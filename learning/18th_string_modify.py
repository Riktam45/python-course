a = "Hello This python learning is for datascience"
print(a.upper())            # UPPER CASE OF ALL STRING

b = "Hello This Python Learning is For Datascience"
print(b.lower())            # lowercase of all string

c = "Hello This Python Learning is For Datascience"
print(c.replace("Hello","P"))       # replace a string  

# The split() method returns a list where the text between the specified separator becomes the list items.

example_string2 = "python is amazing"        
split_string = example_string2.split()       # default split by spaces
print(split_string)

example_string3 = "one,two,three,four,five"
split_list = example_string3.split(',')
print(split_list)