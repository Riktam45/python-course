# Python errors can be broadly categorized into four main 
# groups depending on when they happen and what causes them: 
# i. Syntax errors, 
# ii. Exceptions (Runtime errors), 
# iii. Logical errors, and 
# iv. System errors

# and this types also breaks into 6 steps:
# • 1. Syntax Error → Category: Syntax Errors (Missing colons, unclosed brackets).
# • 5. Indentation Error → Category: Syntax Errors (A special type of syntax error caused by bad spacing).
# • 2. NameError → Category: Exceptions (Calling a variable before creating it).
# • 3. TypeError → Category: Exceptions (Trying to add text to a number).
# • 4. FileNotFoundError → Category: Exceptions (Trying to open photos.txt when it doesn't exist).
# • 6. ZeroDivisionError → Category: Exceptions (Dividing any number by 0).


""" 
1. Syntax Error
What it means: When broke the grammatical rules of the Python language. 
Python cannot even begin to run the script because it doesn't understand the structure.  
    example: -->
            if 5 > 3
                print("Five is greater than three")
"""

"""
2. Indentation Error
What it means: A specific type of syntax error. Python relies on spaces/tabs to know which lines of 
code belong inside loops, functions, or conditions. If the spacing is uneven, it breaks.
    example -->
            def welcome():
            print("Welcome to Python!")  # Missing indentation here
"""

"""
3. NameError
What it means: When trying to use a variable, function, or object that 
Python does not recognize because it hasn't been created yet.
    example -->
            variable = "Alex"
            print(variabl)  # Typo: missed the 'e' in username
"""

"""
4. TypeError
What it means: When trying to perform an operation on data types that 
don't mix (like combining words with mathematical numbers).
    example -->
            age = 25
            message = "I am " + age + " years old."  # Cannot add text and numbers together     
"""

"""
5. FileNotFoundError
What it means: User told Python to open, read, or manipulate a file on your computer, 
but Python looked for it and couldn't find it.
    example -->
            with open("my_secrets.txt", "r") as file:
                content = file.read()   # if no file named "my_secrets.txt" in the system
"""

"""
6. ZeroDivisionError
What it means: When trying to attempting a mathematical calculation that divides a number by zero, 
which is mathematically impossible.
    example -->
            total_score = 100
            players = 0
            average = total_score / players
"""
