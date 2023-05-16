class Flight:

    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError(f"No Air Line code in {number}")
        self._number = number
    
    def number(self):
        return self._number
    
