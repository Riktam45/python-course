# The elif keyword is Python's way of saying "if the previous conditions were not true, 
# then try this condition".
# The elif keyword allows you to check multiple expressions for True 
# and execute a block of code as soon as one of the conditions evaluates to True.

a = 10
b = 21
if b > a:
    print(f"{b} is greater than {a}")
elif a == b:
    print(f"{a} and {b} are same")
elif a > b:
    print(f"{a} is greater than {b}")

# Multiple elif
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
