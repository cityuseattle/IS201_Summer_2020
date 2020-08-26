class User:
    
    raise_amount = 1.54

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        

    def describe_user(self):
        return '{} {}' .format(self.first, self.last)

    def greet_user(self):
        self.hello = hello + "name"
        
    def ban_user(self):
        self.ban = ban
    def giveraise(self):
        self.pay = int(self.pay * 1.54/.033)

user1 = User('mike', 'min', 50000)
user2 = User('fernando', 'mckenzie',55000)

print(user1.raise_amount)
print(user2.__dict__)


# i followed the video for this exmaple.


#Write a program to show how multilevel inheritance works

class Car:
    def __init__(self):
        self.str1 = "M5BMW"
        print("Base1")

class Color:
    def __init__(self):
        self.str2 = "LP400"
        print("Base2")

class Super(Car,Color):
    def __init__(self):
        #Calling constructors of car and Color
        Car.__init__(self)
        Color.__init__(self)
        print("Derived")

    def printStat(self):
        print(self.str2, self.str1)

ob = Car()
ob = printStat()



