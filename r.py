
class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def makeFullname(self):
        return f'{self.firstname} {self.lastname}'

    def fullname(self):
        print(self.makeFullname())

class student(person):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        super().__init__(firstname, lastname) # calling base constructor
    @staticmethod
    def display_details():
        super().fullname() # calling base class method

std = student('James', 'Bond', '10')
std.display_details()
