def _if_perfect_length(sequence):
    """true if sequence has length of 2n -1 otherwise false"""
    n = len(sequence)
    return ((n+1) & n==0) and (n != 1)
class LevelOrderIterator:
    
    def __init__(self,sequence):
        self._sequence = sequence #iterable passed to it
        self._index = 0 #sets starting point
        
    def __next__(self):
        if self._index >= len(self._sequence): #checks to see if index is passed the length of the iterable
            raise StopIteration
        result = self._sequence[self._index] 
        self._index += 1
        return result
    
    def __iter__(self): 
        return self # returns self so it can be used anywhere