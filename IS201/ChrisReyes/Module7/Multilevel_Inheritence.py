class Animal:
    # Constructor
    def _init_(self, name):
        self.name = name
    
    # To get name
    def getName(self):
        return self.name
# Inherited or Sub class (Nte Animal in bracket)
class Dog(Animal):
    # Constructor
    def _init_(self, name, age):
        Animal._init_(self, name)
        self.age = age
    # To get name
    def getAge(self):
        return self.age

    # Inherited or Sub class (NOte Dog in bracket)
    class pug(Dog):
        # Constructor
        def _init_(self, name, age, color):
            Dog._init_(self, name, age)
            self.color = color
        # To get color
        def getColor(self):
            return self.color
# Driver code
ob = pug("PugPug", 2, "Brown")
print(ob.getName(), ob.getAge(), ob.getColor())