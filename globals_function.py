import mymodule
import sys

mymodule.count = 10

mymodule.ham()

x = 5   # global variable

def eggs():
    print(f"{x = }")
    animal = "hen"   # local variable

class Toast:
    SPREAD = "honey"

print(f"{mymodule.ANIMAL = }")

g = globals()
print(f"{g = }")

print(f"{g['x'] = }")
g['x'] = 22
print(f"{x = }")

# def print(*args):
#     sys.stdout.write("HA HA HA\n")

g['color'] = 'blue'
print(f"{color = }")

# local -> nonlocal -> global -> builtin

g['bark'] = lambda: print("woof woof")

bark()

def main():
    n = doom()
    gloom(n)

def doom():
    name = "Srini"
    return name

def gloom(name):
    print(f"{name = }")
    
# def dont():
#     global x  # EVIL EVIL EVIL EVIL
#     x = 10

# def iwouldnt():
#     print(f"{x = }")

# dont()
# iwouldnt()







