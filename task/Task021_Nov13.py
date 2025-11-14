"""
Create a Person class where we will have five attributes and five behaviors.
Make sure that each type of function is used, and I want you to also create
the print function, which will print all the instance variable values.
"""

class Person:
    def __init__(self):
        self.name = "Archana"
        self.age = 31
        self.height = "5 ft"
        self.weight = 53
        self.eye_color = "Black"

    def person_name(self):
        return self.name

    def person_age(self):
        return self.age

    def person_height(self):
        return self.height

    def person_weight(self):
        return self.weight

    def person_eye_color(self):
        return self.eye_color

person = Person()
print(person.person_name())
print(person.person_age())
print(person.person_height())
print(person.person_weight())
print(person.person_eye_color())
