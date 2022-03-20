class Student:
    def __init__(self, first_name: str, last_name: str, semester: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester

    def promote(self):
        self.semester += 1

    def hello(self):
        return f'Jestem {self.first_name} {self.last_name}, semestr {self.semester}'


george = Student('George', 'Jetson', 1)
print(george.hello())
print(george.first_name, george.last_name)
print("semestr", george.semester)
george.promote()
print('semestr po promocji', george.semester)
print(george.hello())

judy = george
judy.first_name = 'Judy'
print(judy.hello())
print(judy)
print(george.hello())
print(george)
