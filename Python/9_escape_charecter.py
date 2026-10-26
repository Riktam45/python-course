# An escape sequence is a sequence of characters that starts with a backslash (\) 
# followed by a specific character or numbers. 
# It tells Python to treat that part of the string as a special character (like a tab or newline) 
# or as a literal text shortcut instead of its normal meaning

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




