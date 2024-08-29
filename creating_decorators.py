import logging
from functools import wraps
from datetime import datetime

logging.basicConfig(
    filename="deco.log",
    level=logging.DEBUG,
)

def spooky(func):
    return 100

@spooky
def spam():
    pass
# spam = spooky(spam)

x = spam
print(f"{x = }")


def log_timestamp(orig_function):
    
    @wraps(orig_function)
    def replacement(*args, **kwargs):
        logging.debug("Function %s called at %s", orig_function.__name__, datetime.now().ctime())
        result = orig_function(*args, **kwargs)
        return result

    replacement.ts = datetime.now().ctime()

    return replacement

@log_timestamp
def ham():
    print("calling ham()")
# ham = log_timestamp(ham)

def toast():
    print("calling toast")

@log_timestamp
def eggs(color):
    print(f"calling {color} eggs")

ham()
ham()
eggs("blue")
toast()
eggs("green")
ham()
print(f"{ham.__name__ = }")
print(f"{toast.__name__ = }")
print(f"{eggs.__name__ = }")

print(f"{ham.ts = }")
