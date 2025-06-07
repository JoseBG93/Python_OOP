class baseUser:
    def __init__(self, name, surname, password, phone):
        self.name = name
        self.surname = surname
        self.password = self.encryptPassword(password)
    def encryptPassword(self, password):
        pass
    def verifyPassword(self, password):
        pass