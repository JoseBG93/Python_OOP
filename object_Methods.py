class vehicle:
    # Class attributes: these are attributes that are shared by all instances of the class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
      # Methods
      # We use self to refer to the object itself, so we can access its attributes.
    def accelerate(speed): # A method that doesn't have 'self' as an argument is a function.
        print (speed)
    def brake(self, speed): 
       self.speed -= speed
       print(self.speed)

car1 = vehicle("Toyota", "Corolla")
print(f"Brand: {car1.brand} \nModel: {car1.model}")

# Difference between a method and a function:
# A method is a function that is associated with an object.
# A function is not associated with an object.

# When we create an instance of a class and call a method, the instance is implicitly passed as the first argument to the method.
# That's why we use self in the method definition. We don't need to pass self when we call the method.
# We can also access the attributes of the instance using the instance name.
car1.brake(20)

car1.accelerate(10) # Here we are calling the function accelerate, not the method accelerate.
# When we run this, we get an error because the function accelerate doesn't have a self argument,
# so we can't access the attributes of the instance.
# To fix this, we need to define accelerate as a method by adding self as the first argument, or we can call it as a function.
vehicle.accelerate(10) # This works because we are calling the function accelerate, not the method accelerate.
vehicle.brake(10) # In this case, this doesn't work because we are calling the method brake, not the function brake. We need to pass 'self' as the first argument.
# To fix this, we must pass the instance as the first argument.
vehicle.brake(car1, 10)
