class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def displayData(self):
        print('In parent class displayData method')
        print(self.name)
        print(self.age)

class Employee(Person):
    def _init_(self, name, age, id):
        # calling constructor of super class
        super()._init_(name, age)
        self.emId = id

    def displayData(self):
        print('In child class displayData method')
        print(self.name)
        print(self.age)
        print(self.empId)

#Person class object
person = Person('John', 40)
person.displayData()
#Employee class object
emp = Employee('John', 40, 'E005')
emp.displayData()