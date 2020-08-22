#Illustrating multilevel inheritance 
class CityUEmployee: 
    """An attempt to create a general CityU employee (parent class)"""

    def __init__ (self, first_name, last_name, id, position):
        """Initialize attributes to describe an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position

    def display_user(self):
        """Display general employee data."""
        return "Name: {} {} Employee ID: {} Current position: {}".format(self.first_name, self.last_name, 
        self.id, self.position)


class Faculty(CityUEmployee): 
    """An attempt to create a faculty (CityU Employee child class)"""

    def __init__(self, first_name, last_name, id, position, courses_taught):
        """Initialize attributes from CityUEmployee parent class and new Faculty attribute."""
        CityUEmployee.__init__(self, first_name, last_name, id, position)
        self.courses_taught = courses_taught
        
    def teaching_experience(self):
        """Display faculty's teaching experience"""
        return "This instructor has taught previously the following courses: {}".format(self.courses_taught)
        

class AdminFaculty(Faculty):
    """An attempt to create an administrative faculty (CityU Employee grandchild class)"""

    def __init__(self, first_name, last_name, id, position, courses_taught):
        """Initialize attributes from Faculty parent class"""
        Faculty.__init__(self, first_name, last_name, id, position, courses_taught)
       
    def determine_workload(self, taught_wc):
        """Determine whether an admin faculty has fulfilled within compensation requirement."""
        if taught_wc < 3:
            return ("W/C requirement is not fulfilled.")
        if taught_wc >= 3: 
            return ("W/C requirement is fulfilled.")

#create an instance of the AdminFaculty class 
faculty = AdminFaculty('James', 'Brown', '89567413', 'Administrative faculty', 'IS 505')

#checking whether functions from CityUEmployee, Faculty, and AdminFaculty are called in successfully
print(faculty.display_user())
print(faculty.teaching_experience())
print(faculty.determine_workload(2))
