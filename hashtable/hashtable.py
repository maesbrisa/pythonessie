class HashTable:

    def __init__(self, number_of_slots=10):
        self._slots = [None] * number_of_slots
        self._length = 0

    def __len__(self):
        return self._length
    
    def __getindex__(self, key):
        return hash(key) % len(self._size)
 
    def __setitem__(self, key, value):
        index = self.__getindex__(key)
        self._size[index] = value
        self._length += 1

    def __getitem__(self, key):
        index = self.__getindex__(key)
        return self._size[index]

    def __delitem__(self):
        index = self.__getindex__(key)
        self._size[index] = None
        self._length -= 1

    def __eq__():
        pass

    def __hash__():
        pass
