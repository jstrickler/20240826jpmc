from collections import namedtuple

Date = namedtuple("Date", "year month day")

d1 = Date(1972, 5, 22)
print(f"{d1[0] = }")
print(f"{d1.year = }")

d2= Date(1999, 6, 6)
print(f"{d2.day = }")

print(f"{d1._asdict() = }")
print(f"{d1._fields = }")


