class Dog:
    def __init__(self, name, is_neutered):
        self._name = name
        self._is_neutered = is_neutered

    @property
    def name(self):
        return self._name

    @property
    def is_neutered(self):  # getter property
        return self._is_neutered
    
    @is_neutered.setter
    def is_neutered(self, value):  # setter property
        self._is_neutered = value
    
    def bark(self):
        print("Woof! woof!")

d = Dog("Nellie", False)
print(f"{d = }")
print(f"{type(d) = }")
d.bark()
print(f"{d.is_neutered = }")

print(f"{d.name = }")
d.is_neutered = True
print(f"{d.is_neutered = }")

class Thing:
    def __len__(self):
        return 100

t = Thing()
print(f"{t = }")
print(f"{len(t) = }")

class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # name = property(name)

    def __add__(self, other):
        return Animal(self.name[:3] + other.name[:3])

    def __str__(self):
        return f"Animal: {self.name}"

    def __repr__(self):
        return f"Animal('{self.name}')"

a1 = Animal("elephant")
a2 = Animal("wombat")
a3 = Animal("honey badger")
print(f"{a3.name = }")

x = a1 + a2 + a3   #    (a1 + a2) + a3
print(f"{x.name = }")

class Spam:
    """Spam(index)"""
    def __getitem__(self, index):
        return "abc"

    def __repr__(self):
        return "Spam()"


s = Spam()
print(f"{s = }")


print(f"{s[0] = }")
print(f"{s[5] = }")
print(f"{s[99] = }")
print(f"{s['wombat'] = }")

print(a1, a2, a3)
print(f"{a1 = }")
print(f"{a2 = }")
print(f"{a3 = }")


def spam():
    """
    fatty pork meat all ground up
    """

print(spam.__doc__)



