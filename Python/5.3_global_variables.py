#Variables that are created outside of a function are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside

x = "Riktam"
def myfunc():
    print(x)
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

x = "gLbl_variable"  #global variable
def variables():
    x = "locl_variable"
    print("This is " + x)  #local variables
variables()
print("This is " + x)

# 'Global" keyword
def myfunc2():
    global x
    x = "Riktam"    # This variable is now global and can be used by everyone
    print(x)
myfunc2()

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
global_variable = "awesome"
def myfunc():
  global global_variable
  global_variable = "fantastic"     # global_variable's value is updated beacuse of using global key word
myfunc()
print("Python is " + global_variable)

