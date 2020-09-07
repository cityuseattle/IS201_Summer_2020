
import pdb
pdb.set_trace()
def __init__(self,name,cuisine_type):
   self.name = name.title
   self.cuisine_type = cuisine_type

def describe_restaurant(self):
   message = self.name + "its good!" + self.cuisine_type + "."
   print("\n" + message)

def open_restaurant(self):
   message = self.name + "is open 24/7!"
   print("\n" + message)

restaurant = Restaurant('pythons','pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

