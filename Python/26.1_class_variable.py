# In Python, a class variable is a variable that is declared inside a class but 
# outside any instance methods or the __init__ constructor. Unlike instance variables, 
# which hold data unique to each object, class variables are shared by all instances of that class.

class Dog:
    species = "Canine"      # Class Variable (Shared by all instances of Dog)
    def __init__(self, name):
        self.name = name    # Instance Variable (Unique to each instance of Dog)
# 1. Access using the Class name (Best practice)
print(Dog.species)  # Output: Canine    
# 2. Access using an Instance
buddy = Dog("Buddy")
print(buddy.species)  # Output: Canine
print(buddy.name)     # Output: Buddy


# code number 2 with class variable, accessing the class variables, modifying the class variables
class Car:    
    car_segment = "Muscle"  # <-- Class Variable (Shared by all)

    def __init__(self, name):
        self.name = name  # <-- Instance Variable (Unique to each)

# --- 1. ACCESSING THE CLASS VARIABLE ---
print("--- 1. Initial Values ---")
# Recommended: Access via Class name
print(f"Class level segment: {Car.car_segment}")  # Output: Muscle

# Access via instances
car1 = Car("Mustang")
car2 = Car("Camaro")
print(f"Car 1's segment: {car1.car_segment}")  # Output: Muscle
print(f"Car 2's segment: {car2.car_segment}")  # Output: Muscle


# --- 2. MODIFYING VIA CLASS NAME (Changes it for everyone) ---
print("\n--- 2. Modifying via Class Name ---")
Car.car_segment = "Sports Car"  # This changes the class variable for all instances
print(f"Class level segment: {Car.car_segment}")  # Output: Sports Car

print(f"Class level segment: {Car.car_segment}")  # Output: Sports Car
print(f"Car 1's segment: {car1.car_segment}")  # Output: Sports Car
print(f"Car 2's segment: {car2.car_segment}")  # Output: Sports Car

# --- 3. MODIFYING VIA INSTANCE (Creates a local copy / Shadowing) ---
print("\n--- 3. Modifying via Instance ---")
# This ONLY changes it for car1, creating a unique instance variable
car1.car_segment = "Luxury Car"  # This creates a new instance variable for car1
print(f"Car 1's segment: {car1.car_segment}")  # Output: Luxury Car
print(f"Car 2's segment: {car2.car_segment}")  # Output: Sports   Car (Unchanged)

print(f"Car 1's segment: {car1.car_segment}")  # Output: Luxury Car
print(f"Car 2's segment: {car2.car_segment}")  # Output: Sports Car

print(f"Class level segment: {Car.car_segment}")  # Output: Sports Car
