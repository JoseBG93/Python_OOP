class user:
    def __init__(self, name, surname, password, email, phone):
        # public attributes
        self.name = name
        self.surname = surname
        self.password = self.encrypt_password(password)
        self.email = email
        # __ is used to make the phone private
        self.__phone = phone

    def encrypt_password(self, password):
        pass
    
    def verify_password(self):
        pass
    
    def get_phone(self):
        return self.__phone

    def update_phone(self, new_phone):
        self.__phone = new_phone

user1 = user(
    name="John",
    surname="Doe",
    password="123456",
    email="john@example.com",
    phone="1234567890"
)

# __phone is private and can only be accessed through the get_phone and update_phone methods
user1.update_phone(123)
print(user1.get_phone())

