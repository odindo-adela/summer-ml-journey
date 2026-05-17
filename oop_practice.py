class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(f"My name is {self.name}")

student1 = Student("Adela", "Computer Science")
student1.introduce()