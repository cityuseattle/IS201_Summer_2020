# Parent class
class Dog:

    #Class attribute
    species = 'mammal'

    #Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance Method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
    
    #Instance Method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


#Child class (inheritance from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child class (inheritance from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


#Chilf classes inherit attributes and
# behaviors from the parent class
jim = Bulldog('Jim', 12)
print(jim.description())

#Child classes have specific attributes
# and behaviors as well
print(jim.run('slowly'))
