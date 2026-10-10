#Logical operators are used to combine conditional statements
x = 5
print(x > 0 and x > 9)      # This is AND gate logic x>0 = True(1), x>9 = False(0) so, 1 * 0 = 0(false)

x1 = 8
print(x1 < 10 or x == 6)    # This is OR gate logic x1<10 = True(1), x1==6 = False(0) so, 1 + 0 = 1(true)

x2 = 21
print(not(x2 > 30 and x2 > 10)) # x2>30 = false(0), x2>10 = True(1), 0 * 1 = 0 and complement(not) = 1(true)