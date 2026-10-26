# Directly Loop Through Characters
# If you only need to access each character, you can iterate over the string directly
my_string = "Ritkam"
for x in my_string:
    print(x)

for x in "Sarkar":
    print(x)


# Loop with Index and Character (enumerate)
my_string = "Bittu"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")

#  Loop Through Words Instead of Characters
sentence = "This is a sample sentence"
for word in sentence.split():       # the split() function splits the sentence into words
    print(word)
