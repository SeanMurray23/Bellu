
class Employee:
    def __init__(self):
        self.__dict__['name'] = "Ji-soon"
        self.__dict__['age'] = "38"
        self.__dict__['position'] = "developer"
        self.__dict__['salary'] = "1200"
        

e = Employee()

print(e.name)