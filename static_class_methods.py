class MyClass:
    class_attribute = 10

    def __init__(self, colour): # This is the constructor method.
        self.colour = colour
    
    @staticmethod # This is a decorator that tells Python to treat the method as a static method. It doesn't take 'self' as an argument. It has no access to the instance or the class.
    def static_method(colour): # This is a static method.
        print(f"This is a static method of the colour {colour}")

    @classmethod # This is a decorator that tells Python to treat the method as a class method. It takes 'cls' as an argument. It has access to the class but not the instance.
    def class_method(cls):
        print(cls.__name__) # 'cls' is the class itself, like 'self' is the instance itself.
        print("This is a class method with the class attribute", cls.class_attribute)

my_class = MyClass("red")
print("My favourite colour is", my_class.colour)
MyClass.static_method("blue") 
MyClass.class_method()