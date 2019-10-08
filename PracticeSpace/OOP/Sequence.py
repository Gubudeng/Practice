from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collection.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence;False outherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return the leftmost index at which val is found(or raise Valueerror)"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        return ValueError('Value not in sequence.')

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
