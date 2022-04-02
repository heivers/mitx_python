import datetime

class Person():
    
    def __init__(self, name):
        """Assumes name a string. Create a person."""
        self._name = name
        try:
            last_blank = name.rindex(" ")
            self._last_name = name[last_blank:]
        except:
            self._last_name = name
        self._birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Assumes birthday is of type datetime.date
        Sets self's birthday to birthdate"""
        self._birthday = birthdate
    
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Assume other a Person
        Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparision is based on last
        names, but if these are teh smae full names are compared"""

        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name

"""
me = Person("Bart Heerkens")
wife = Person("Joanna Heerkens")
her = Person("Madonna")
singer = Person("Lady Gaga")

wife.set_birthday(datetime.date(1976, 3, 22))
me.set_birthday(datetime.date(1976, 4,3))

print(wife.get_name(), "is", wife.get_age(), "days old.")
print(me.get_name(), "is", me.get_age(), "days old.")
"""