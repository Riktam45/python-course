#An escape character is a backslash \ followed by the character you want to insert.

txt = "We are the so-called \"Vikings\" from the north."
print(txt)                                   # \"" -- double quote

txt = 'It\'s alright.'
print(txt)                                   # \' -- single quote

txt = "This will insert one \\ (backslash)."    
print(txt)                                   # \\ -- backslash

txt = "Hello\nWorld!"
print(txt)                                   # \n -- new line

txt = "Hello\tWorld!"
print(txt)                                   # \t -- tab

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)                                   # \b -- backspace




