def _is_perfect_length(sequence):
    """true if sequence has length of 2n -1 otherwise false"""
    n = len(sequence)
    return ((n+1) & n==0) and (n != 1)


class LevelOrderIterator:
    
    def __init__(self,sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(f"Sequence of {len(sequence)} does not rep a binary tree of 2-1")
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
    
def _left_child(index):
    return 2 * index +1

def _right_child(index):
    return 2 * index +2


class PreOrderIterator:
    def __init__(self,sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(f"Sequence of {len(sequence)} does not rep a binary tree of 2-1")
        self._sequence = sequence #iterable passed to it
        self._stack = [0] #sets starting point
        
    def __next__(self):
        if len(self._stack) == 0: # checks to see if its at the end of the table
            raise StopIteration
        index = self._stack.pop() #pop off the top item of the stack
        result = self._sequence[index] #

        #preorder push: Push right child first so left child is popped and processed first, last in first out
        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)
            
        _left_child_index = _left_child(index)
        if _left_child_index < len(self._sequence):
            self._stack.append(_left_child_index)
            
        return result

class InOrderIterator:
    def __init__(self,sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(f"Sequence of {len(sequence)} does not rep a binary tree of 2-1")
        self._sequence = sequence #iterable passed to it
        self._stack = [] #sets starting point
        self._index = 0
        
    def __next__(self):
        if (len(self._stack ==0)) and (self._index>= len(self._sequence)):
            raise StopIteration
        
        #Push left children onto the stack while possible
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)
            
        #pop froim stack and process beforeing moving to the right child
        
        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result
    
    def __iter__(self):
        return self

missing = object()

class SkipMissingIterator:
    
    def __init__(self,iterable):
        self._iterator = iter(iterable)
        
    def __next__(self):
        item = next(self._iterator) 
        if item is not missing:
            return item
        
    def __iter__(self):
        return self
