"""
To read files in Python, the best practice is to use the with open() statement. 
This approach automatically ensures the file is closed properly after you are finished, 
preventing resource leaks and data corruption.
"""

# Method 1
f = open("demo.txt")
print(f.read())         

# Method 2 (with keyword)
with open("demo.txt")as file:
    print(file.read())

# Method 3 Read Only Parts of the File
with open("demofile.txt") as file:
  print(file.read(5))


#  most common ways to read a file, depending on needs

# 1. Raed the entire file at once
# Use .read() to pull the entire content of the file into a single string.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", mode = "r", encoding = "utf-8") as file:
    content_val = file.read()
    print(content_val)

# 2. Read line by line (memory efficient)
# If you are dealing with large files, looping directly over the file object is the best option. 
# It loads only one line into memory at a time.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r") as file:
    for line in file:
        print(line.strip())

# 3. Read all lines into a list
# Use .readlines() if you want to capture every line as an individual string element inside a Python list.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r")as file:
    lines = file.readlines()
    print(lines)        #  # Output: ['Line 1\n', 'Line 2\n', ...]

    
# 4. Read One Specific Line
# Use .readline() to fetch just a single line. Calling it multiple times moves sequentially through the file.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
print(first_line)
print(second_line)


# Common File Reading Methods Summary

#   Method	            Output Type	                        Best Used For
# .read()	            String	                    Reading smaller files entirely into memory.
# for line in file:	    String (per iteration)	    Processing large files without high memory usage.
# .readlines()	        List of strings	            Storing all lines separately to manipulate or index them later.
# .readline()	        String	                    Reading a file incrementally or fetching the very first line.
