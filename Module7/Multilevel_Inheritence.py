class Animal:
    # Constructor
    def __init__(self, name):
        self.name = name 
    # To get name
    def getName(self):
        return self.name

# Inherited or sub class (Note Animal in bracket)
class Dog(Animal):
    # Constructor
    def __init__(self, name, age):
        Animal.__init__(self, name)
        self.age = age
    #to get age 
    def getAge(self):
        return self.age

# Inherited or Bub clas (note Dog in bracket)
class pug(Dog):
    # Constructor
    def __init__(self, name, age, color):
        Dog.__init__(self, name, age)
        self.color = color
    #To get color
    def getColor(self):
        return self.color

#Driver code
ob = pug("PugPug", 2, "Brown")
print(ob.getName(),ob.getAge(), ob.getColor())