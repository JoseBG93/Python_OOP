from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class baseUser(ABC):
    def __init__(self, name, surname, email, password, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = self.encryptPassword(password)
        self.phone = phone
    
    @abstractmethod
    def encryptPassword(self, password):
        pass
    
    @abstractmethod
    def verifyPassword(self, password):
        pass

class concretUser(baseUser):
    def encryptPassword(self, password):
        return encrypt(password,"secret") # "encrypt" is the imported cryptocode's function, and "secret" is just a token that encrypts our password.
    def verifyPassword(self, password):
        desencrypted_password = decrypt(self.password, "secret") # "decrypt" is the other imported cryptocode's function.
        return desencrypted_password == password

user1 = concretUser(
    name="Jose", 
    surname=" Burguera", 
    email="jlburguera@gmail.com",
    password="test", 
    phone=123456,
    )

print(user1.password)
print(user1.verifyPassword("test"))