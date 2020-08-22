class User: 
    """An attempt to create a user"""

    def __init__(self, first_name, last_name, DOB, city, country):
        """Initialize attributes to describe a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.DOB = DOB
        self.city = city.title()
        self.country = country.title()
        self.email = first_name + "_" + last_name + '@outlook.com'
      
    def describe_user(self):
        """Display user information"""
        return "Name: {} {}  Date of birth: {} Location: {}, {}  Email: {}".format(self.first_name, 
        self.last_name, self.DOB, self.city, self.country, self.email)

    def greet_user(self):
        """Greet the user"""
        return "\nWelcome to your profile, {}!".format(self.first_name)

#create two instances of users
user1 = User('anna', 'kriuchkova', '07/24/1994','Seattle', 'unites states')
user2 = User('vitalina', 'savenko', '04/05/1993', 'kharkov', 'ukraine')

#call describe_user() and greet_user() for both instances
print(user1.describe_user(), user1.greet_user())
print(user2.describe_user(), user2.greet_user())


