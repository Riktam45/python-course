# In Python, there is no direct create() function for file handling. 
# Instead, you use the built-in open() function with specific mode parameters to create a file.

# The 3 Ways to Create a File
# You can create a file by passing one of the following modes as the second argument to open():
# Mode	Behavior	Use Case
# "x"	Exclusive Creation: Creates a new file. If the file already exists,                 Use this when you want to avoid accidentally 
#           the program fails with an error (FileExistsError).	                                overwriting existing data.
# "w"	Write Mode: Creates a new file if it doesn't exist.                                 Use this when you want a fresh file
#           If the file already exists, it completely overwrites the old content.	            every time you run the script.
# "a"	Append Mode: Creates a new file if it doesn't exist. If the file already exists,    Use this for logging or adding information
#           it keeps the old content and appends new data to the end.	                        over time without erasing previous data.


# 1. Creating and Writing a File (Using "w") [ using open() ]
# This creates the file or blanks it out if it already exists.
file_path = "new_file.txt"             
with open(file_path, 'w') as file:      # Open the file in write mode 
    # Write content to the file 
    file.write("Hello, this is a new text file created using open() function.") 
print(f"File '{file_path}' created successfully.")

# 2. Safely Creating a File (Using "x")
# This will crash if the file is already created, protecting your data.
try:
    with open("new_file.txt", "x") as file:
        file.write("This file is brand new!")
    print("File created successfully.")
except FileExistsError:
    print("Error: The file already exists.")


# 3. Creating and Appending to a File (Using "a")
# This creates the file if it's not created, or safely adds lines to the bottom if it exists.
with open("log.txt", "a") as file:
    file.write("Adding a new line to the log.\n")
print("Line successfully added to log.txt!")
