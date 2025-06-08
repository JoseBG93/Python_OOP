class Pet:
    def __init__(self, animal, name, age, toy):
        self.animal = animal
        self.name = name
        self.age = age
        self.toy = toy
    def greet(self):
        print(f"Hello, my pet is a {self.animal} called {self.name}")
    def tell_age(self):
        print(f"{self.name} is {self.age} years old")
    def tell_race(self):
        print(f"{self.name} is a {self.race}")
    def play(self):
        print(f"{self.name} loves playing with a {self.toy}")
  
    
class dog(Pet):
    def __init__(self, animal, name, age, race, toy):
        super().__init__(animal, name, age, toy)
        self.race = race
    def greet(self):
        super().greet()
    def tell_age(self):
        super().tell_age()
    def tell_race(self):
        super().tell_race()
    def play(self):
        super().play()

 
class my_dog(dog):
    def __init__(self, animal, name, age, race, toy):
        super().__init__(animal, name, age, race, toy)
        self.race = race
    def greet(self):
        super().greet()
    def tell_age(self):
        super().tell_age()
    def tell_race(self):
        super().tell_race()
    def play (self):
        super().play()

m_dog = my_dog("dog", "Max", 5, "Labrador", "ball")
m_dog.greet()
m_dog.play()
m_dog.tell_age()
m_dog.tell_race()

class cat(Pet):
    def __init__(self, animal, name, age, toy):
        super().__init__(animal, name, age, toy)
    def play(self):
        super().play()
    def greet(self):
        super().greet()
    def tell_age(self):
        super().tell_age()
print("--------------------------------" + "\n")

m_cat = cat("cat", "Whiskers", 3, "yarn")
m_cat.greet()
m_cat.play()
m_cat.tell_age()