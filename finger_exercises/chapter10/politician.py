from person import Person

class Politician(Person):
    """A Politician is a person who can belong to a political party"""

    def __init__(self, name, party=None):
        super().__init__(name)
        self._party = party

    def get_party(self):
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same party
        or at least one of them does not belong to a party"""

        if self._party == other._party or self._party == None or other._party == None:
            return True
        return False