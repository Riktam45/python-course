# Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement
try:
    print(x)
except:
    print("X is not defined")       # x is not defined so the except block is executed


# Many Exceptions
try:
    print(x)
except NameError:           # NameError is Python Built-in Exceptions Reference
    print("X is not defined")
except:
    print("something is wrong")


# Else
# can use the else keyword to define a block of code to be executed if no errors were raised
try:
    print("Hello")      # In this example, the try block does not generate any error
except:
    print("This is except")
else:
    print("This is else")


# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("this is except")
finally:
    print("This is finally")


# Python Built-in Exceptions Reference
"""
Exception	            Description
ArithmeticError	        Raised when an error occurs in numeric calculations
AssertionError	        Raised when an assert statement fails
AttributeError	        Raised when attribute reference or assignment fails
Exception	            Base class for all exceptions
EOFError	            Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	    Raised when a floating point calculation fails
GeneratorExit	        Raised when a generator is closed (with the close() method)
ImportError	            Raised when an imported module does not exist
IndentationError	    Raised when indentation is not correct
IndexError	            Raised when an index of a sequence does not exist
KeyError	            Raised when a key does not exist in a dictionary
KeyboardInterrupt	    Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError	            Raised when errors raised cant be found
MemoryError	            Raised when a program runs out of memory
NameError	            Raised when a variable does not exist
NotImplementedError	    Raised when an abstract method requires an inherited class to override the method
OSError	                Raised when a system related operation causes an error
OverflowError	        Raised when the result of a numeric calculation is too large
ReferenceError	        Raised when a weak reference object does not exist
RuntimeError	        Raised when an error occurs that do not belong to any specific exceptions
StopIteration	        Raised when the next() method of an iterator has no further values
SyntaxError	            Raised when a syntax error occurs
TabError	            Raised when indentation consists of tabs or spaces
SystemError	            Raised when a system error occurs
SystemExit	            Raised when the sys.exit() function is called
TypeError	            Raised when two different types are combined
UnboundLocalError	    Raised when a local variable is referenced before assignment
UnicodeError	        Raised when a unicode problem occurs
UnicodeEncodeError	    Raised when a unicode encoding problem occurs
UnicodeDecodeError	    Raised when a unicode decoding problem occurs
UnicodeTranslateError	Raised when a unicode translation problem occurs
ValueError	            Raised when there is a wrong value in a specified data type
ZeroDivisionError	    Raised when the second operator in a division is zero
"""