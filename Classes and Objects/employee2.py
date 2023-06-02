from datetime import date

class Employee:  
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def increarse_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
class Tester(Employee):
    def run_tests(self):
        print(f"Testing started by {self.name}....")
        print("Tests  are done")

class Developer(Employee):
    def __init__(self,name,age,salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
        
    def increarse_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus
        

employee1 = Tester("Lauren", 33, 1000)
employee2 = Developer("Bob", 38, 1000)

employee1.increarse_salary(20)
employee2.increarse_salary(20, 30)

print(employee1.salary)
print(employee2.salary)