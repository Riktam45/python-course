# The ternary operator allows to assign one value if a condition is true, and another if it is false
# The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.
num = 3
x = "Weekend" if num > 5 else "Workday"
print(x) 

# The ternary operator can be used instead of elif in longer if statements
num = 0
x = "Good" if num == 8 else "Bad" if num == 9 else "worst" if num == 7 else "Great"
print(x)