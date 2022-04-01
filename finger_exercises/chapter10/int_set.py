class Int_set():
    """an Int_set is a set of integers"""

    def __init__(self):
        """create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """assumes e is an integer.
        Adds e to the set if not already in it"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        returns True if e in _vals, False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer.
        Removes e from _vals. Raises ValueError if e not in _vals"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + " not found.")

    def get_members(self):
        """Returns a list containing the elements of _values."""
        return self._vals[:]

    #def union(self, other):
    def __add__(self, other):
        """other is an Int_set.
        Mutates self so that it contains exactly the elements in self 
        plus the elements in other"""
        
        for e in other.get_members():
            if self.member(e) == False:
                self.insert(e)
        return self._vals[:]

    def __str__(self):
        """String representation of _vals"""
        if self._vals == []:
            return {}
        temp = [str(x) for x in self._vals]
        return "{" + ",".join(temp) + "}"

s = Int_set()
s.insert(3)
s.insert(4)
s2 = Int_set()
s2.insert(4)
s2.insert(5)
s2.insert(6)
print(s.member(3))
print(s) 
print(s2)
print(s + s2)
