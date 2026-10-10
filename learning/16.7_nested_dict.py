#Create a dictionary that contain another dictionaries inside it
cars = {
    "car_manufacturer1" : {
        "Brand": "Audi",
        "Model": "A6", 
        "Color": "Red"
    },
    "car_manufacturer2" : {
        "Brand": "BMW",
        "Model": "M4", 
        "Color": "Green"
    },
    "car_manufacturer3" : {
        "Brand": "Chevrolet",
        "Model": "Corvette", 
        "Color": "Black"
    } 
}
print(cars)

# Create separetes dictionaries, then create one dictionary that will contain the other dictionaries inside it
bikes1 = {
    "Brand" : "Truimph",
    "Model" : "Scrambler 800"
}
bikes2 = {
    "Brand" : "Brixton",
    "Model" : "Scrambler 650"
}
bikes3 = {
    "Brand" : "Royal Enfield",
    "Model" : "Bear 650"
}
all_bikes = {
    "bikes1" : bikes1,
    "bikes2" : bikes2,
    "bikes3" : bikes3
}
print(all_bikes)

# access the item in nested dictionary
print(all_bikes["bikes2"]["Model"])  