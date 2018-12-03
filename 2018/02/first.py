from collections import Counter

codes = [code.rstrip("\n") for code in open("input.txt")]

counters = [Counter(code) for code in codes]

has_two = len([c for c in counters if 2 in c.values()])
has_three = len([c for c in counters if 3 in c.values()])

print(has_two * has_three)
