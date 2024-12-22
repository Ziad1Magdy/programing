class Person:
    def __init__(self, name): 
        self.name = name

    def getName(self):  
        return self.name

    def isEmployee(self): 
        return False

class Employee(Person):
    def isEmployee(self):  
        return True

person = Person("ziad")  
print(person.getName(), person.isEmployee())  # ziad False

emp = Employee("magdy")  
print(emp.getName(), emp.isEmployee())  # magdy True


print("##############################################")


class Person:
    def __init__(self, name, idnumber):  
        self.name = name
        self.idnumber = idnumber

    def display(self):  
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, departement):  
        self.salary = salary
        self.departement = departement
        Person.__init__(self, name, idnumber)

a = Employee('ziad', 886012, 200000, "syber_security")
a.display()  
