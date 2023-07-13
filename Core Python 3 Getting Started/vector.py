class Vector:
    def __init__(self, vals):
        self.vals =vals
    
    def __repr__(self):
        return f'{self.__calss__name__}({repr(self.vals)})'

Vector([1,2,3])