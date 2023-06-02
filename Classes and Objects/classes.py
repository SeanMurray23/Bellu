
class Employee:
    min_wage = 1000
    
    @classmethod
    def change_min_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("We Broke")
        cls.min_wage = new_wage
        
    @classmethod
    def new_emp(cls,name,dob):
        now = date.today()
        age = now.year - dob.year - ((now.month,now.day)< (dob.month, dob.day))
        return cls(name, age, cls.min_wage)
    
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None
    
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
    
    @salary.setter
    def salary(self, salary):
        if salary > Employee.min_wage:
            raise ValueError(f'Min Wage is {Employee.min_wage}')
        self._annual_salary = None
        self._salary = salary
        
    @property
    def anaual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary
        
    
        
employee1 = Employee("Jin", 38 , "developer", 1200)
employee2 = Employee("Laura", 44, "tester", 1000)

Employee.increase_salary(employee2, 20)

print(employee2)
print(str(employee2))
print(repr(employee2))

employee3 = employee1 + employee2
print(employee3)