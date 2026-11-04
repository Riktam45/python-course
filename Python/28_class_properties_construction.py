
# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.class person
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Riktam", 23)
print(p1.name)
print(p1.age)

# Access Properties
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
pq = car("Lexux", "Ls")
print(pq.brand)
print(pq.model)


# Modify Properties
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
pq = car("Lexux", "Ls")
print(pq.brand)
print(pq.model)
pq.model = "ES"
print(pq.model)

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects
class Humans:
    species = "humans"              # class properties
    def __init__(self, name):
        self.name = name            # instance properties
p1 = Humans("Ritkam")
p2 = Humans("Bittu")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Modifying Class Properties
class simple:
    def __init__(self,name):
        self.name = name
mod = simple("Riktam")
print(mod.name)
mod.name = "Bittu"
print(mod.name)
mod.age = 23    # Add new properties
mod.bg = "B"    # Add new properties
print(mod.age)      
print(mod.bg)       

