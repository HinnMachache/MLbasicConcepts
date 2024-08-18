class Robots:
    Three_laws = (
        """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
        """A robot must obey the orders given to it by human beings, except where such orders would conflict with the 
        First Law.""",
        """A robot must protect its own existence as long as such protection does not conflict with the First or Second
         Law."""
    )

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year


class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print(f"this class is about {cls._class_info}!")


class Dog(Pet):
    _class_info = "Dog Pet"


class Cat(Pet):
    _class_info = "Cat"


class Person:
    _population = 0

    def __init__(self, name):
        self.name = name
        Person._population += 1

    def del_user(self):
        print(f"User {self.name} Deleted")
        Person._population -= 1

    @classmethod
    def attendance(cls):
        print(f"Total Attendance : {Person._population}")
