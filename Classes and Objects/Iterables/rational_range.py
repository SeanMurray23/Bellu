from  fractions import Fraction

class RationalRange:
    
    def __init__(self, start, stop, num_steps):
        if num_steps != int(num_steps):
            raise ValueError('Not Right dude')
        if num_steps < 1:
            raise ValueError('Dont be negative')
        self._start = Fraction(start)
        self._num_steps = num_steps
        self._step = Fraction(stop - start, num_steps)
        
    def __getitem__(self, index):
        if not ( 0 <= index < self._num_steps):
            raise IndexError
        return self._start + index * self._step
    
    
        