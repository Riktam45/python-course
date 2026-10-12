# Closing a File
# The close() method in Python file handling terminating an open file stream, 
# flushes any unwritten data from buffers to disk, and frees up critical system resources.

# If you are not using the with statement, you must write a close statement in order to close the file:
f = open("demo.txt")
print(f.read())
f.close()

# Once closed, trying to perform operations like read() or write() on the object will raise a ValueError
# 1. Manual File Closing
file = ("demo.txt", "w")        # # Opening a file for writing
file.write("Hello, World!")     # a operation
print(file)
file.close()                    # Explicitly closing the file


# 2. Best Practice: Automatic Closing with with
# The modern and standard way to handle files in Python is using the with statement (also known as a context manager). 
# It automatically closes the file as soon as the block of code finishes, even if an error or exception occurs
with open("example.txt", "r") as file:  # The file is safely closed the moment you indent back out
    content = file.read()
    print(content)
# No need to call file.close() here!


# 3. Safe Manual Closing (Try/Finally)
# If you cannot use a with statement for some reason, you should wrap manual file closing inside 
# a try...finally block. This guarantees that close() runs even if the file processing throws an error midway
file = open("example.txt", "r")
try:
    content = file.read()
finally:
    file.close()        # This block executes no matter what happens in try


# How to Check if a File is Closed
file = open("example.txt", "r")
print(file.closed)  # Returns False
file.close()
print(file.closed)  # Returns True


# Checking File Properties
f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)
f.close()
print("Is Closed?", f.closed)


# Handling Exceptions When Closing a File
# It's important to handle exceptions to ensure that files are closed properly, 
# even if an error occurs during file operations. Here, the finally block ensures 
# the file is closed even if an error occurs.
try:
    with open("geek.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:      # except FileNotFoundError: This is part of a try...except block. 
                                    # It listens specifically for a missing file error raised inside a preceding try block.
                                    # as e: This stores the actual exception object (the system's error message details) inside a variable named e
    print("Error:", e)              # print("Error:", e): This prints the word "Error:" followed by the specific details of the missing file error stored in e 