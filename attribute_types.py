class vehicle:
    colour = "blue"
    # Class attributes: these are attributes that are shared by all instances of the class
    def __init__(self, wheels, brand, speed, year):
        self.wheels = wheels
        self.brand = brand
        self.speed = speed
        self.year = year
      # Methods
    def accelerate(self, speed):
        self.speed += speed
        return self.speed
    def brake(self, speed):
        self.speed -= speed
        return self.speed

class Car(vehicle):
    # Instance attributes: these are attributes that are specific to each instance of the class
    def __init__(self, wheels, brand, speed, year, model):
        super().__init__(wheels, brand, speed, year)
        self.model = model

class Motorcycle(vehicle):
    def __init__(self, wheels, brand, speed, year):
        super().__init__(wheels, brand, speed, year)
    
car = Car(4, "Toyota", 120, 2020, "Corolla")
motorcycle = Motorcycle(2, "Honda", 150, 2022)

# Method 1: Using f-strings
print(f"Car details: wheels={car.wheels}, brand={car.brand}, speed={car.speed}, model={car.model}")

# Method 2: Using vars() to get all instance attributes
print("\nAll car attributes:", vars(car))

# Method 3: Using __dict__ to get all instance attributes
print("\nAll motorcycle attributes:", motorcycle.__dict__)

# Method 4: Using getattr() in a loop for specific attributes
attributes_to_print = ['wheels', 'brand', 'speed', 'model']
print("\nSelected car attributes:")
for attr in attributes_to_print:
    print(f"{attr}: {getattr(car, attr)}")

# Attributes (and methods) can be accessed and modified using the dot notation.
# Data attributes are variables that are associated with an instance of a class. It's like a copy of the class attribute.
print("\n--------------------------------")
vehicle.colour = "red"
print(car.colour)
