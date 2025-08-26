class CustomSet:
    # init can take an iterable argument or no arguments
    # is_empty() method must reflect emptiness if no arguments
        # what object property should is_empty check? underlying data struct: list
    # contains() method must return false when set is empty
        # must return True when set contains value
    # empty set must be a subset of an empty set empty_set()
    # empty set must also be subser of nonempty set
    # nonempty subser must ont be subset of empty set
    def __init__(self, values=[]):
        self._values = []
        for value in values:
            if value not in self._values:
                self._values.append(value)

    def __eq__(self, other):
        if isinstance(other, CustomSet):
            return self.is_same(other)
        return NotImplemented

    def is_empty(self):
        return not self._values

    def contains(self, number):
        return number in self._values

    def is_subset(self, other):
        if isinstance(other, CustomSet):
            if self.is_empty():
                return True
            if other.is_empty():
                return False
            for element in self._values:
                if not other.contains(element):
                    return False
            return True
        return NotImplemented

    def is_disjoint(self, other):
        if isinstance(other, CustomSet):
            if self.is_empty():
                return True
            if other.is_empty():
                return True
            for element in self._values:
                if other.contains(element):
                    return False
        return NotImplemented

    def is_same(self, other):
        if isinstance(other, CustomSet):
            return self.is_subset(other) and other.is_subset(self)
        return NotImplemented

    def add(self, new_value):
        if new_value not in self._values:
            self._values.append(new_value)

    def intersection(self, other):
        new_set = CustomSet()
        if isinstance(other, CustomSet):
            for element in self._values:
                if other.contains(element):
                    new_set.add(element)
            return new_set
        return NotImplemented

    def difference(self, other):
        if isinstance(other, CustomSet):
            new_set = CustomSet()
            for element in self._values:
                if not other.contains(element):
                    new_set.add(element)
            return new_set
        return NotImplemented

    def union(self, other):
        if isinstance(other, CustomSet):
            other_unique = other.difference(self)
            for element in self._values:
                if not other_unique.contains(element):
                    other_unique.add(element)
            return other_unique
        return NotImplemented