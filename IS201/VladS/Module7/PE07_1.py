#Declaring a User class
class User:

#Declating a constructor for the class User with 4 parameters
    def __init__(self, first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age

#Declaring a method of User class printing user data     
    def describe_user(self):
        print("First Name: {}".format(self.first_name))
        print("Last Name: {}".format(self.last_name))        
        print("Email: {}".format(self.email))
        print("Age: {}".format(self.age))
        print("\n")
        
#Declaring a method of User class greeting users       
    def greet_user(self):
        print("Hello {}!\n".format(self.first_name))
        
#Creating two user objects by instantiating User class
user1=User("John","Smith","j.smith@company.com",37)
user2=User("Jane","Hopkings","j.hopkings@company.com",25)

#Asking user objects to print their data
user1.describe_user()
user2.describe_user()

#Asking user objects to print greetings for them
user1.greet_user()
user2.greet_user()
