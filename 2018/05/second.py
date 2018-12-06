import string

with open("input.txt") as f:
    polymer = f.read()

polymer = polymer.rstrip("\n")

all_units = [
    {"unit": a,
     "polymer": "".join(filter(lambda x: x.lower() != a, polymer))}
    for a in string.ascii_lowercase]


def is_same_type(x: str, y: str) -> bool:
    return x.upper() == y.upper()


def is_different_polarity(x: str, y: str) -> bool:
    if x == x.upper():
        return y == y.lower()
    else:
        return y == y.upper()


def parse(poly: str, i: int):
    current, next = poly[i], poly[i+1]
    if(is_same_type(current, next) and is_different_polarity(current, next)):
        return poly[:i] + poly[i+2:]
    else:
        return poly


def colapse(p):
    polymer = p
    i = 0
    while i < len(polymer)-1:
        last = polymer[:]
        polymer = parse(polymer, i)
        if last == polymer:
            i += 1
        else:
            i = max(0, i-1)
    return polymer


minimal = len(polymer)
bad_unit = ""

for u in all_units:
    new_minimal = len(colapse(u.get("polymer")))
    if new_minimal < minimal:
        minimal = new_minimal
        bad_unit = u.get("unit")

print(bad_unit, minimal)
