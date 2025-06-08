    # Getter is used to get the value of the attribute
    # Setter is used to set the value of the attribute

# Base class for all users
class baseUser:
    def __init__(self, name, surname, password):
        self._name = name
        self._surname = surname
        self.__password = self.encryptPassword(password)
        print(f"User created with password hash: {self.__password}")

    def encryptPassword(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        hashed = hash(password)
        print(f"Password '{password}' hashed to: {hashed}")
        return hashed

    def verifyPassword(self, password):
        hashed_input = hash(password)
        print(f"Verifying password '{password}'")
        print(f"Input hash: {hashed_input}")
        print(f"Stored hash: {self.__password}")
        return hashed_input == self.__password

    def changePassword(self, old_password, new_password):
        print("\nAttempting to change password...")
        print(f"Checking old password: '{old_password}'")
        
        # First verify the old password
        if not self.verifyPassword(old_password):
            print("Password verification failed!")
            raise ValueError("Current password is incorrect")
        
        print("Old password verified successfully!")
        
        # Validate new password
        if len(new_password) < 8:
            raise ValueError("New password must be at least 8 characters long")
        
        # Update the password
        self.__password = self.encryptPassword(new_password)
        print(f"Password changed successfully! New hash: {self.__password}")
        return True

  
    # A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
    
    # Getter and Setter for name
    @property 
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self._name = value
        
    # Getter and Setter for surname
    @property
    def surname(self):
        return self._surname
        
    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise ValueError("Surname must be a string")
        if len(value) < 2:
            raise ValueError("Surname must be at least 2 characters")
        self._surname = value

    # Read-only property for password (no setter)
    @property
    def password(self):
        raise AttributeError("Password cannot be read directly")

user1 = baseUser("Jose", "Burguera", "password123")
print(user1.name)
print(user1.surname)
