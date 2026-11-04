# Adding Attributes in a Derived Class
# When a child class inherits from a parent, it can also define its own unique properties.
# To do this, we add the __init__() function to the child class.
# We must use super().__init__() first to keep the parent's properties, then define the new ones.


# Parent class
class Vehicle:                                  
    def __init__(self, brand, model):
        self.brand = brand                      # Parent class attribute
        self.model = model                      # Parent class attribute

# Derived Class
class ElectricCar(Vehicle):                     # child class inherits from parent class (Vehicle)
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)          # inherit properties from the parent 
        self.battery = battery                  # add unique child attribute
        
    def ex(self):
        print(self.brand, self.model, "has a", self.battery, "battery")

# Usage
my_ev = ElectricCar("Tesla", "Model 3", "75 kWh")

print(my_ev.brand)                              # prints inherited attribute (Tesla)
print(my_ev.battery)                            # prints child specific attribute (75 kWh)
my_ev.ex()                                      # prints the combined output