class Employee:
  pass
  emp_count = 0

emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)

Employee.emp_count += 1 


def showinfo(self):
        return '{} {}, {}'.format(self.first, self.last, self.email)
print(emp1.showinfo())
print("Total Employee:", Employee.emp_count)