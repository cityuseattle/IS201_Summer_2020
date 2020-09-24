class Animal:
    def _init_(self):
        self.str1 = "Dog"
        print("Base1")
        
class Color:
    def _init_(self):
        self.str2 = "Black"
        print("Base2")

class Dog(Animal, Color):
    def _init_(self):
        # Calling contructors of Animlas and Color
        Animal._init_(self)
        Color._init_(self)
        print("Derived")

    def printStat(self):
        print(self.str2, self.str1)

ob = Dog()
ob.printStat()