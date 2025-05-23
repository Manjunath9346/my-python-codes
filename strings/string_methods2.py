def trim(str):
    return str.strip()


def exists(str, x):
    s = str.find(x)
    return s


def titleIt(str):
    n = str.title()
    return n


def casesSwap(str):
    if str.islower():
        m = str.upper()
        return m
    elif str.isupper():
        p = str.lower()
        return p
print(trim("  hello  "))
print(exists("hello", "llo"))
print("hello")
print("hello")
