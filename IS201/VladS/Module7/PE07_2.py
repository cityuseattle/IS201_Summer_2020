#This is a root class
class Vehicle:
    def moves(self):
        print("This object moves!")
        
#This is a child of the root class
class Airplane(Vehicle):  
    def flies(self):
        print("This object flies!")
        
#This is grand-child of the root class inheriting from Airplane class
class Boeing747(Airplane):  
    def carries_passengers(self):
        print("This object is a double-decker jet carrying passengers!")

#Instantiating grandchild of the root class and calling methods of all parent classes
plane = Boeing747()
plane.moves()
plane.flies()
plane.carries_passengers()
