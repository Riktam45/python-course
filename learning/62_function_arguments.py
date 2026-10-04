# Arguments are the actual values or data passed into a function when call it

# Keyword Arguments
# can send arguments with the key = value syntax.
def cars(brand, model):
    print("I have a", brand)
    print("and the model is",model)
cars(brand = "lexus", model = "Ls350")

#passing different data types
# can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#Sending a list as an argument:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Sending a dictionary as an argument:
def my_function1(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function1(my_person)

#default arguments
def power(base, exponent=2):
    return base ** exponent
print(power(5))     # Uses default exponent (5^2) -> Outputs: 25
print(power(5, 3))  # Overrides default exponent (5^3) -> Outputs: 125

