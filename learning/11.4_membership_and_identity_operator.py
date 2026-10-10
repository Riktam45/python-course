#Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x1 = ["apple", "banana"]
y1 = ["apple", "banana"]
print(x1 is not y1)

#Difference Between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal

#Membership operators are used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits1 = ["apple", "banana", "cherry"]
print("pineapple" not in fruits1)

#Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)