class Animal:   #this is a base class

    #Constructor
    def __init__(self,name):
        self.name = name

    #To get name
    def getName(self):
        return self.name

#Inherited or subclass (note Animal in brackets) - this is a child class
class Dog(Animal):  

    #Constructor
    def __init__(self,name,age):
        Animal.__init__(self,name)
        self.age = age

    #To get age
    def getAge(self):
        return self.age

#Inherited or subclass (note Dog in brackets) - this is a grandchild class
class pug(Dog):

    #Constructor
    def __init__(self, name, age, color):
        Dog.__init__(self, name, age)
        self.color = color

    #To get color
    def getColor(self):
        return self.color

#Driver code
ob = pug("PugPug", 2, "Brown")
print(ob.getName(), ob.getAge(), ob.getColor())
