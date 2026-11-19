class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return f"Name: {self.name}"

    def get_age(self):
        return f"Age: {self.__age}"

#get_age can access the private attribute __age.

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def teach(self):
        print(f"{self.name} is teaching")

student1 = Student("Xianne", 14)
print(student1.get_name())
print(student1.get_age())
student1.study()


teacher1 = Teacher("Ms. Moira", 30)
print(f"\n{teacher1.get_name()}")
print(teacher1.get_age())
teacher1.teach()