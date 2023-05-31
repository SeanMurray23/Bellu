
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

employee1 = Employee("Jin", 38 , "developer", 1200)
employee2 = Employee("Laura", 44, "tester", 1000)

Employee.increase_salary(employee2, 20)
employee2.info()