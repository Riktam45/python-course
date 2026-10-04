x = "C_language"     # This is global variable

def MyFunc():
    global x        # now using this "global" keyword, I make "x" is a global variable
    x = "Python_language"  #assignin new values because it is now a global variable
MyFunc()

print("This is " + x)   # so here the global keyword's variable is placed 