class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"Name:  {self.name}")

    def show_age(self):
        print(f"Age:  {self.age}")

person1 = Person("Xianne", 14)
person1.show_name()
person1.show_age()