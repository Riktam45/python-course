# In Python, f-strings (Formatted String Literals) are the modern, standard, and preferred way to format strings. 
# Introduced in Python 3.6, they are more concise and faster than older methods
# the older methods are - 
# i. .format() method, 
# ii. '%' operator,

age = 22
txt = f"MY name is bittu and my age is {age}"        #the f function can combine string value and int value
print(txt)

example_variable = 69
txt1 = f"The moon says doing {example_variable}"     #this is place holder {example_variable}
print(txt1)

price = 58
txt2 = f"This product is cost of {price:.2f}"        #this is for float number and it will show 2 decimal places because of .2f
print(txt2)                                         

txt3 = f"placeholder can sum of 20 + 10 = {20+10} in the python"
print(txt3)                                          #A placeholder can contain Python code, like math operations

# the  .format() method 
name = "Ritkam"
age = 23
print("Hello, {} I am {} years old".format(name, age))  # positional placeholder

# Operator (Legacy)
name = "Bittu"
age = 12
print("Yo i am %s and my age is %s" %(name, age))

# Format Specifier	    Description	                        Example	                Output
# ":.2f"	Round a float to 2 decimal places	            f"{3.14159:.2f}"	    '3.14'
# ":,"	    Add comma separators to large numbers	        f"{1000000:,}"	        '1,000,000'
# ":0>5"	Pad with zeros to a width of 5 (right-aligned)	f"{42:0>5}"	            '00042'
# ":%"	    Convert a fraction into a percentage	        f"{0.25:%}"	            '25.000000%'
# ":b / :x" Convert an integer to binary or hexadecimal	    f"{10:b}" / f"{10:x}"	'1010' / 'a'