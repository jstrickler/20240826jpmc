class Thing:
    def doit(self):
        print("DO DO DO DO")

class MyList(list, Thing):  # class MyList extends list, dict, ...
    def __getitem__(self, index):   # implement []
        return super().__getitem__(index) * 10

    def append(self, value):
        if len(self) >= 6:
            raise ValueError("this list can only hold 6 items")

class YourList(list):
    def append(self, value):
        super().append(self, value * 5)

data = [1, 2, 3, 'a']

m = MyList(data)
print(f"{m = }")
print(f"{m[0] = }")
print(f"{m[-1] = }")

print(f"{type(list) = }")

print(f"{MyList.mro() = }")
print(f"{YourList.mro() = }")
m.doit()