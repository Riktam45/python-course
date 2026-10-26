# String Length
# To find the length of a string in Python, use the built-in len() function. 
# It returns an integer representing the total number of characters in the string, including spaces, punctuation, and special characters

test_string = ("Hello there i am Riktam")
print(len(test_string))         # output is 24 because there are 24 characters in the string including spaces

test_tuple = ("Hello there i am Riktam",)
print(len(test_tuple))          # using , at the end of the tuple to make it a single element tuple so its output is 1

test_tuple2 = (1, 2, 3, 4, "Riktam")
print(len(test_tuple2))         # output is 5 because there are 5 elements in the tuple

test_list = ["Hello there i am Riktam"]
print(len(test_list))           # output is 1 because there is only one element in the list

test_list1 = [1, 2, 3, "Riktam"]
print(len(test_list1))          # output is 4 because there are 4 elements in the list

test_dic = {"Hello there i am Riktam"}
print(len(test_dic))            # output is 1 because there is only one key in the dictionary

test_dic1 = {"a": 2, "b": 3, "c": 4}
print(len(test_dic1))           # output is 3 because there are 3 keys in the dictionary    

test_set = {"Hello there i am Riktam"}
print(len(test_set))            # output is 1 because there is only one element in the set

test_set = {1,2,3,"Riktam"}
print(len(test_set))            # output is 4 because there are 4 elements in the set    

#  Spaces and Punctuation: Every character counts. For instance, " " (a single space) has a length of 1.
#  Empty Strings: An empty string "" has a length of 0.
#  Performance: The len() function runs in O(1) constant time because Python stores the length of the string directly in memory alongside the object

# Python len() with custom objects
class public:
    def __init__(self, name):
        self.name = name
    def __len__(self):      
        return len(self.name)
x = public("Riktam")   
print(len(x))

# __len__ is called dunder(magic) method in Python. It is a special method that allows you to define the behavior of the built-in len() function for your custom objects. 
# When you call len() on an instance of a class that has a __len__ method, Python will invoke that method to determine the length of the object.

