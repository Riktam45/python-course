print(21 == 21)
print(bool("Hello"))
print(bool(15>21))

# in bollean False, None, 0, empty list, empty tuple, empty set, empty dictionary is considered as 'False'

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Functions can Return a Boolean
def myFunction():
    return True
print(myFunction())

def my_function():
    return True
if my_function():
    print("Yes")
else:
    print("No")