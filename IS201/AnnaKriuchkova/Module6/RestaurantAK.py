"""A class that can be used to represent a restaurant."""
class Restaurant():
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type = " "):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return restaurant's name and cuisine type it serves."""
        return f"Restaurant {self.restaurant_name.title()} serves {self.cuisine_type}."
        
    def open_restaurant(self):
        """Return a message indicating that the restaurant is open."""
        return f"Welcome to {self.restaurant_name.title()}! We are now open!"
        

#Creating three instances of a class Restaurant

restaurant_1 = Restaurant("la parisiene", "French pastry")
restaurant_2 = Restaurant("jade garden", "dim sum")
restaurant_3 = Restaurant("vito", "Italian cuisine")

#Displaying them to the user by calling describe_restaurant()

print(restaurant_1.describe_restaurant())
print(restaurant_2.describe_restaurant())
print(restaurant_3.describe_restaurant())
