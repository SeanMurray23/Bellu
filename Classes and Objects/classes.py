
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
           
    
    def __add__(self, other_employee):
        return Employee("New", self.age + other_employee.age, "dev", 2000)
    
    @property
    def salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary > 1000:
            raise ValueError('Min Wage is $1000')
        self._salary = salary
        
    
        
employee1 = Employee("Jin", 38 , "developer", 1200)
employee2 = Employee("Laura", 44, "tester", 1000)

Employee.increase_salary(employee2, 20)

print(employee2)
print(str(employee2))
print(repr(employee2))

employee3 = employee1 + employee2
print(employee3)