from collections.abc import MutableSequence, 

class NBasedList(MutableSequence):

    def __init__(self, base, init=None):
        self._base = base
        self._items = list(init) if init else list()
    
    def __getitem__(self, index):
        return self._items[index - self._base]

    def __setitem__(self, index, value):  # x[index] = value
        self._items[index - self._base] = value

    def __delitem__(self, index):  # del x
        del self._items[index - self._base]
    
    def __len__(self):  # len(x)
        return len(self._items)

    def insert(self, index, value):
        self._items.insert(index - self._base, value)

    def __repr__(self):
        return repr(self._items)

print(f"{NBasedList = }")
data = ['apple', 'banana', 'cherry']
nbl = NBasedList(-1, data)
print(f"{nbl = }")

print(f"{nbl[-1] = }")
print(f"{nbl[+1] = }")
