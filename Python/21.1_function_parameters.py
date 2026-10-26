# Parameters
# Parameters are the variables listed inside the parentheses in a function definition.
# They act as placeholders for the values (arguments) that you pass into the function when you call it.

def my_func(fname):     # fname is the argument(single parameters)
    print(fname, "This is parameters ")
my_func("Email")
my_func("Outlook")
my_func("zoho")

# positional parameters
def os_func(OS1,OS2):   # OS1 and OS2 both are arguments(multiple parameters)
    print(f"This is first parameters {OS1} and this is the 2nd parameters {OS2}")
os_func("Linux", "Windows")
os_func("MAC", "Linux")
os_func("Windows", "MAC")

# default parameters
def greet(name, message="Welcome"):
    print(f"{name}, {message}!")
greet("Bob")                      # Output: Welcome, Bob!
greet("Bob", "Good morning")        # Output: Good morning, Bob!



