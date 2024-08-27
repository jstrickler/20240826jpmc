from itertools import chain

a = [1, 2, 3]
b = [5, 8, 19]
c = [22, 85, 9, -1, 0, 45]

for value in chain(a, b, c):
    print(value, end=" ")
print("\n")

d = [['a', 'b', 'c'], ['de', 'e', 'f']]

for value in chain.from_iterable(d):
    print(value, end="/")
print("\n")



