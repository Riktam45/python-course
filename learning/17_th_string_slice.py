a = "Abracadabra"
print(a[2:7])       # in slicing start from 2 so start with 2 numbered charecter and end in 6th charecter  
                     # because 7 is end pointso it didnt print the 7th charecter   
b = "super Upper"
print(b[:5])        # slicing from start

c = "super Upper"
print(c[5:])        # slicing to end

# in negative indxing last(most right sided) charecter is condsider as -1 then value is get bigger
# from right to left like -5 -4 -3 -2 -1 

d = "Abracadabra"   
print(d[-5:-2])     

# in negative indexing printing the charecters from right to left so, the starting point(-2) is skipped 
# and then start print to the ending point with print the end point charecter(-5)

print(d[-4:])