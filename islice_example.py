from itertools import islice

with open('DATA/alice.txt') as alice_in:
    lines = islice(alice_in, 500, 550)

    for line in lines:
        print(line, end="")