class AbstractCollection:

    def __init__(self,source_collection=None):
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __add__(self, other):
        """ Overloads the + operator. Returns a new Bag containing the contents of self and other """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def is_empty(self):
        """Return True if len(self) ==0, False otherwise"""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self"""
        return self._size

    def count(self, item):
        """ Returns a count of how many times 'item' appears in self """
        result = 0
        for i in self:
            if i == item:
                result += 1
        return result