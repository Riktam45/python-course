# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.
# The else statement provides a default action when none of the previous conditions are true

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Else Without Elif
a1 = 200
b1 = 30
if b1 > a1:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Complete If-Elif-Else Chain
temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")