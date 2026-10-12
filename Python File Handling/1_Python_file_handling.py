"""
File handling refers to the process of performing operations on a file, such as 
creating, opening, reading, writing closing it and delete files permanently on users storage system through a programming interface. 
It involves managing the data flow between the program and the file system on the storage device, 
ensuring that data is handled safely and efficiently.
"""

"""
The most effective and safest way to interact with files is by using the built-in with open() statement, 
which automatically closes the file after processing to prevent resource leaks.
"""

# Core File Modes
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode, { open(filename, mode) } 
# There are four different methods (modes) for opening a file:
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

# Syntax to open a file
f = open("file_name.txt")

f = open("file_name2.txt", "r")
print(f)

f = open("file_path", mode = "r", encode = None)
print(f)

# Best Practice: The with Statement
# While you can manage files manually by assigning the open() function to a variable 
# and ending with .close(), the community consensus on Stack Overflow emphasizes using 
# the with statement (Context Manager) instead.

# 1. Read the entire file
with open("file_name.txt", "r", encoding = "utf-8") as file:    # encoding: The text encoding used to decode or encode the file (highly recommended to set as 'utf-8' for text files).
    content_val = file.read
    print(content_val)


# The with statement automatically closes the file when the code block finishes, 
# preventing resource leaks and data corruption even if an error occurs


# 2. Reading a file line-by-line (Memory Efficient)
with open("large_dataset.txt", "r", encoding = "utf-8") as file:
    for line in file:
        print(line.strip())     # .strip() removes trailing newlines


# 3. writing to a file
with open("dataset.txt", "r", encoding = "utf-8") as file:
    file.write("Hello Wold")
    file.write("Writing File Handling logic in Python.")
    

