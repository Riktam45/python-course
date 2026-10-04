# Logical operators are used to combine conditional statements. Python has three logical operators:
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# and operator
a = 20
b = 10
c = 40
if a > b and b > c:
    print("a is bigger")
else:
    print("a is not bigger")

# or operator
x = 10
y = 20
z = 30
if x > y or z > x:
    print("because of or it print")

# not
a1 = 33
b1 = 200
if not a1 > b1:
  print("a is NOT greater than b")