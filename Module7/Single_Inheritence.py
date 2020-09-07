# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer/ Instance attributes 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    #instace method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #instance method
    def speak(self, sound):
        return "{} say {}".format(self.name, sound)    


#Child class (inherits from Dog class)
class RusselTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child classes inherit attributes and 
#behaviors from the parent class 
jim = Bulldog("jim",12)
print(jim.description())
sam = RusselTerrier("sam",10)
print(sam.description())

#child classes have specific attributes 
# and behaviors as well
print(jim.run("slowly"))
print(sam.run("all the times"))
