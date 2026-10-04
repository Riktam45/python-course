#Variables that are created outside of a function are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside

x = "gLbl_variable"  #global variable

def variables():
    x = "locl_variable"
    print("This is " + x)  #local variables
variables()

print("This is " + x)
