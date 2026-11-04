# 1. Instance Methods
# These are the most common methods you write in Python. 
# They automatically receive the specific object instance (self) as their first argument.

class Student:
    def __init__(self, name, grade):
        self.name = name       # Instance variable
        self.grade = grade     # Instance variable

    # This is an instance method
    def display_info(self):
        # Uses 'self' to access specific object properties
        return f"Student: {self.name}, Grade: {self.grade}"

# Usage
student1 = Student("Alice", "A")
print(student1.display_info())  # Output: Student: Alice, Grade: A


# 2. Class Methods
# Class methods are bound to the class rather than its objects. 
# They are marked with the @classmethod decorator and accept cls as the first argument.

class Student:
    school_name = "Hogwarts"   # Class variable shared by all instances

    def __init__(self, name):
        self.name = name

    # This is a class method
    @classmethod
    def change_school(cls, new_school):
        # Uses 'cls' to modify the shared class variable
        cls.school_name = new_school

# Usage (You can call it directly on the Class itself)
Student.change_school("Durmstrang")
print(Student.school_name)  # Output: Durmstrang


# 3. Static Methods
# Static methods are not bound to the class or its objects. 
# They are marked with the @staticmethod decorator and do not receive any automatic first argument.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Call static methods directly using the class name (no instance required)
print(Calculator.add(5, 10))       # Output: 15
print(Calculator.is_even(8))       # Output: True
