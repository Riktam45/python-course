# Scope
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def local():
    a = 300
    print(a)
local()

def local1():
    b = 200
    def inside_local():
        print(b)
    inside_local()
    print(b)
local1()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

c = "Bankai"
def glo_scope():
    print(c)
glo_scope()
print(c)

# naming variable
# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope (outside the function)
# and one available in the local scope (inside the function):
d = "Riktam"
def glo_loco_scope():
    d = "Sarkar"
    print(d)
glo_loco_scope()
print(d)

# Global Keyword
# If we need to create a global variable, but are stuck in the local scope, 
# we can use the global keyword.
# The global keyword makes the variable global.
def glo_key():
    global e
    e = 86
glo_key()
print(e)

f = "Python"
def glo_key1():
  global f
  f = "Programming"
glo_key1()  # here only the prgramming is print because using the global keyword both f variable is global,
print(f)    # so f is updated with "programming" from "python"


# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)