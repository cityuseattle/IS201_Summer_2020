class Student:
    def __init__(self, id, age): #self - a default parameter, id and age are additional parameters.\
        #_init__ - a constructor method used for making ('instantiating') objects from a class.
        
        self.id = id #id and age are attributes  (variables accessible through instances)
        self.age = age

std1 = Student(1,20)
std2 = Student(1,20)
print(std1) #std 1 and std 2 are two unique objects; each of them is stored in a separate location in memory
print(std2)
print("This student's ID is " + str(std1.id) + ". He is " + str(std1.age) + " years old.")

#def __init__(self): is an example of a default constructor
#def __init__ (self, id, age): is an example of a parameterized constructor

#__init__ method (constructor) is not required by every class, but is a good tool to have \
#when you create objects from a class and want them to have common characteristics. 

class A: 
    pass