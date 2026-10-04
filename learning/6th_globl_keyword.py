def globl_keyword():
    global x                # using this keyword we can create global variable inside a function
    x = "globl_variable"
globl_keyword()

print(x)  # Output: globl_variable
