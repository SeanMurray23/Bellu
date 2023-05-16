class Flight:
    """Flight stuff
    """

    def __init__(self,number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No Air Line code in {number}")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid Airlone code {number}")
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid Airline code {number}") 
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        
        
    def aircraft_model(self):
        return self._aircraft.model()
    
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]    
class Aircraft:
    
    def __init__(self,registion,model,num_rows,num_seats_per_row):
        self._registion = registion
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registion
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return(range(1, self._num_rows + 1),
               "ABCDEFGHJK"[:self._num_seats_per_row])