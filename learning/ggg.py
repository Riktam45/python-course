file_path = r"D:\Games\New folder\anime.txt"

vowels = "aeiouAEIOU"
count = 0

with open(file_path, 'r') as file:
    for char in file.read():
        if char in vowels:
            count += 1

print(count)