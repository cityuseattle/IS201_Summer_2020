class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
    
    def describe_user(self):
        print("First Name: {}".format(self.first_name))
        print("Last Name: {}".format(self.last_name))        
        print("Email: {}".format(self.email))
        print("Age: {}".format(self.age))
        print("\n")
        
    def greet_user(self):
        print("Hello {}!\n".format(self.first_name))

user1=User("John","Smith","j.smith@company.com",37)
user2=User("Jane","Hopkings","j.hopkings@company.com",25)

user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()
