values = [line.rstrip("\n") for line in open("input.txt")]

sum = sum([int(x) for x in values])

print(sum)
