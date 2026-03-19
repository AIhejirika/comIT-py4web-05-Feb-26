class Animal:
    species = "Mammals"

    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs

    def talk(self):
        print("Animal sound")


class Dog(Animal):

    def __init__(self, name, number_of_legs, breed):
        super().__init__(name, number_of_legs)
        self.breed = breed

    def talk(self):
        print("Woof!")


# create object
dog1 = Dog("Buddy", 4, "Labrador")

# display attributes
print(dog1.name)
print(dog1.breed)
print(dog1.species)

# call method
dog1.talk()