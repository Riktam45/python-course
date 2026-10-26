cars = ("Audi","BMW", "Chevrolet", "Dodge") # this is packing 
(a,b,c,d) = cars                            # this is unpacking
print(a)
print(b)
print(c)
print(d)

#The number of variables must match the number of values in the tuple, if not, 
# you must use an asterisk to collect the remaining values as a list.

#If the number of variables is less than the number of values, 
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
