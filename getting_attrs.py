colors = ['red', 'pink', 'yellow']

def doit(stream):
    if hasattr(stream, 'write'):
        stream.write("some data")
    else:
        raise TypeError("Argument must have a write() method")
print('-' * 60)

print(dir(doit))

x = getattr(doit, '__eq__')
print(f"{x = }")

print(f"{hasattr(doit, '__eq__') = }")

# customer_number
# _
# _my_private_var
# __wombat__
print('-' * 60)

my_list = list()
print(dir(my_list))

my_list.append("Jennifer")

x = my_list[0]
x = list.__getitem__(my_list, 0)
print(f"{x = }")
print(x.__doc__)

# wombat       public name
# _wombat      private name
# __wombat__   predefined name to implement some Python feature
# wombat__     name mangling -- do not use

# def __init__(self, ...)    class initializer (AKA constructor)
#  __init__.py   package initializer
print("\n\n")


class Dog:
    def __init__(self, name):
        self._name = name

    def __call__(self):
        print(f"woof woof my name is {self._name}")

d = Dog("Nellie")
d()



