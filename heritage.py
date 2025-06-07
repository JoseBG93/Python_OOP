class vehicle:
    # Attributes
    # __init__ is the constructor of the class
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    # Methods
    def accelerate(self, speed):
        self.speed += speed
        return self.speed

    def brake(self, speed):
        self.speed -= speed
        return self.speed

class motorcycle(vehicle):
    def __init__(self, brand, model, speed, year, engine_capacity):
        super().__init__(brand, model, speed, year) # super() is used to call the constructor of the parent class. It makes the motorcycle class inherit from the vehicle class.
        self.engine_capacity = engine_capacity # The motorcycle class inherits from the vehicle class, but has an additional attribute, which is the engine capacity

    def wheelie(self):
        return "The motorcycle is doing a wheelie"

class bus(vehicle):
    def __init__(self, brand, model, speed, year, number_of_seats):
        super().__init__(brand, model, speed, year)
        self.number_of_seats = number_of_seats
    def passengers_max(self, passengers_max):
        return f"Number of passengers: {passengers_max}"

Motorcycle = motorcycle("Honda","A",100,2023, str(1200) + " cc")
#print(Motorcycle.speed)
#print(Motorcycle.wheelie())
#print(Motorcycle.brand)
Bus = bus("Blue","A",100, 1999, 35)
print(Bus.brand)
print(Bus.passengers_max(35))