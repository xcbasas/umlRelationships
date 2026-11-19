class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return f"Name: {self.name}"

    def get_age(self):
        return f"Age: {self.__age}"

person1 = Person("Xianne", 14)
print(person1.get_name())
print(person1.get_age())