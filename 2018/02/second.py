codes = [code.rstrip("\n") for code in open("input.txt")]

commons = None

for i, code in enumerate(codes):
    others = codes[:i] + codes[i + 1:]
    for other in others:
        difference = sum([0 if x == y else 1 for x, y in zip(code, other)])
        if difference == 1:
            commons = (code, other)

answer = "".join([l1 for l1, l2 in zip(commons[0], commons[1]) if l1 == l2])

print(answer)
