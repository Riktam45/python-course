# Tuple unpacking (also known as multiple assignment or iterable destructuring) allows
# to extract elements from a tuple and assign them to individual variables in a single line.

# 1. Basic Unpacking
cars = ("Audi","BMW", "Chevrolet", "Dodge") # this is packing 
(a,b,c,d) = cars                            # this is unpacking
print(a)
print(b)
print(c)
print(d)

#The number of variables must match the number of values in the tuple, if not, 
# you must use an asterisk to collect the remaining values as a list.

# 2. Extended Unpacking (Using the Asterisk *)
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:
models = ("R8", "M4", "Corvette", "Challenger")
(a,b,*c) = models       
print(a)
print(b)
print(c)

exm_tup = ("some", "words", "are", "written", "for", "example")
(a,b,*c,d) = exm_tup
print(a)
print(b)
print(c)
print(d)

# 3. Ignoring Values (_ Convention)
# use the underscore (_) because Python requires the number of variables on the left side of the assignment 
# to exactly match the number of items in the tuple on the right side.
user_data = ("Riktam", 23, "Engineer", "Kolkata")
name, _, job, _ = user_data         # Only keep name and profession using individual placeholders (_)
print(f"Name: {name}, Job: {job}")
name, *_, city = user_data          # Ignore a large block of values using the star expression (*_)
print(f"Name: {name}, City: {city}")


