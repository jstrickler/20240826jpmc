
from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]  # create list of foods with EOL removed from line

counts = Counter(foods)  # initialize Counter object with list of foods

for item, count in sorted(counts.items(), key=lambda e: (-e[1], e[0])):  # iterate over results
    print(item, count)

