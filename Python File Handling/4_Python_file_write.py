# File Write()
# To write files in Python, you use the built-in open() function along with a specific file mode. 
# The safest and most efficient practice is to use the with statement.

# Mode / Option	        Description
# "w"	            Write mode: creates file if missing, truncates (erases) if it exists
# "a"	            Append mode: creates file if missing, writes data always at the end
# "x"	            Exclusive create: creates new file, but fails with FileExistsError if it already exists
# "b"	            Binary flag: used with other modes (e.g., "wb", "ab") for binary files
# "+"	            Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
# encoding=	        Specify text encoding (e.g., "utf-8") when working with text files
# newline=	        Control newline translation in text mode (e.g., "\n")


# 1. Overwrite an existing file
# Opening a file in write mode ("w") clears any existing content before writing new data.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "w", encoding = "utf-8")as file:
    file.write("This line is added through write method!!")
    file.write("Another line is added through write() method")

with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r", encoding="utf-8") as file:
    print(file.read()) 


# 2. Append to an existing file   
# Using "a" mode (append), we can add new data at the end of a file without removing what’s already there.
with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "a", encoding="utf-8")as file:
    file.write("Now this line is added through append method")

with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r", encoding="utf-8") as file:
    print(file.read()) 

# 3. Writing Multiple Lines at Once (writelines)
# You can pass a list of strings directly to writelines(). 
# Note that you must still include the \n line breaks yourself
lines = ["\nFirst Line\n", "Second Line\n", "Third Line\n"]

with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "a", encoding="utf-8")as file:
    file.writelines(lines)

with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 4. Create only if it does not exist
# With "x" mode, Python creates a new file but raises FileExistsError if the file already exists. 
# This prevents accidental overwrites.
try:
    with open("D:\Microsoft One Drive\OneDrive\Desktop\python course\Python File Handling\demo.txt", "x", encoding="utf-8") as f:
        f.write("Created using exclusive mode.\n")
except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")


# 5. Writing to a Binary File
# For non-text data (like images, audio, or other binary content), use binary write mode ("wb"). 
# This treats the file as raw bytes instead of text. 

data = b'\x00\x01\x02\x03\x04'          # Creates a bytes object (raw binary data).
with open("file.bin", "wb") as f:       # Opens file in binary write mode (creates/overwrites).
    f.write(data)               
with open("file.bin", "rb") as f:       # Opens file in binary read mode.
    print(f.read())


