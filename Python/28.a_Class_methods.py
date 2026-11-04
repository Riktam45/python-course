"""
In Python, a class method is a function that belongs to the entire class, 
not to just one specific object you create from it. Think of the class as a master blueprint and 
objects as individual houses built from it. While a regular method only changes things inside one 
specific house, a class method can change the master blueprint itself. To make one, 
you just put '@classmethod' right above your function, and it automatically gets access to 
the whole class through a special shortcut named 'cls'.
"""

"""
Python classes primarily support three types of methods, 
each serving a different purpose based on whether they need to access individual object data, 
class-wide data, or act independently. 
There are also Special (Dunder) Methods used for specific built-in operations.
"""


# Method Type	    How it's Defined	        First Parameter	        What it Can Access / Modify	            Main Purpose
#
# Instance Method	Regular function            self (points to the     Individual object attributes            General behavior of a single object
#                   definition	                the specific object)	and class variables	                    (e.g., updating user profile info).
#
# Class Method	    Preceded by @classmethod 	cls (points to 	        Class-level variables only; 	        Managing class-wide states or creating 
#                   decorator                   the class itself)       cannot see individual object data       "factory methods" (alternate constructors).
#
# Static Method	    Preceded by @staticmethod 	None (no automatic 	    Nothing from the class or object 	    Utility or helper functions that 
#                   decorator                   first parameter)        unless explicitly passed                logically belong inside the class 
#                                                                       as an argument                          box but don't need its data.

