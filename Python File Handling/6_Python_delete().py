# To delete a file in Python, you do not use a delete() function, as no built-in method by 
# that exact name exists for file objects. Instead, you use os.remove()or pathlib.Path.unlink()

# 1. Using the os Module (Traditional)
# The built-in os.remove() function deletes a file permanently. 
# It is best practice to check if the file exists first using os.path.exists() to prevent a FileNotFoundError
import os
file_path = "example.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("The file does not exist.")


# 2. Using the pathlib Module (Modern Approach)
# The pathlib module offers an object-oriented approach. In Python 3.8+, 
# you can pass missing_ok=True to automatically ignore the error if the file is already gone
from pathlib import Path
file = Path("example.txt")
# Deletes the file; suppresses error if it doesn't exist
file.unlink(missing_ok=True)
print("File handled successfully.")


# 3. Handling Permissions and Other Exceptions
import os
try:
    os.remove("protected_file.txt")
    print("File deleted.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied. The file might be open elsewhere.")
except OSError as e:
    print(f"Error occurred: {e.strerror}")      # In Python, strerror is a built-in property of exception objects (like OSError)
                                                # that provides the human-readable error message corresponding to the system error code.


# 4. To delete an entire folder, use the os.rmdir() method:
import os
directory_path = "my_empty_folder"
# 1. Check if the path exists and is actually a directory
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # 2. Check if the directory is empty
    if not os.listdir(directory_path):
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' removed successfully.")
    else:
        print(f"Error: '{directory_path}' is not empty.")  
else:
    print(f"Error: The directory '{directory_path}' does not exist.")

