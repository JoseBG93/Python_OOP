# Class example
class User():
    # Data (attributes)
    # Each instance of the class will have these attributes
    # Each class's method must have self as the first parameter
    # __init__ is the constructor of the class
    def __init__(self, name, surname, email, password, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.phone = phone

    # Methods (functions)
    def encrypt_password(self):
        return 'encrypting password'

    def verify_password(self):
        return 'verifying password'

# Create instances of the User class
print('USER 1')
user1 = User(
    name='Jose',
    surname='Garcia',
    email='jose@gmail.com',
    password='123456',
    phone='1234567890'
)
print(user1.name, user1.surname, user1.email, user1.password, user1.phone, '\n', user1.encrypt_password(), '\n', user1.verify_password())

print('USER 2')
user2 = User(
    name='Maria',
    surname='Lopez',
    email='maria@gmail.com',
    password='654321',
    phone='0987654321'
)
print(user2.name, user2.surname, user2.email, user2.password, user2.phone, '\n', user2.encrypt_password(), '\n', user2.verify_password())


