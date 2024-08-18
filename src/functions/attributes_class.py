from src.classes.class_attributes import Robots, Pet, Cat, Dog, Person

for number, attribute in enumerate(Robots.Three_laws):
    print(str(number + 1) + ": " + attribute)

Pet.about()
Cat.about()
Dog.about()

Person.attendance()
jane = Person("jane")
peter = Person("Peter")
Person.attendance()
jane.del_user()
Person.attendance()

