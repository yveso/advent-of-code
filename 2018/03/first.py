def split_line(line):
    right_side = line.split("@")[1]
    split = right_side.split(":")
    start_point = [int(x) for x in split[0].split(",")]
    square = [int(x) for x in split[1].split("x")]
    return {
        "x": start_point[0],
        "y": start_point[1],
        "width": square[0],
        "height": square[1]
    }


lines = [split_line(line.rstrip("\n")) for line in open("input.txt")]
fabric = {}

for line in lines:
    for y in range(line["height"]):
        for x in range(line["width"]):
            point = (line["x"] + x, line["y"] + y)
            if point not in fabric:
                fabric[point] = 1
            else:
                fabric[point] += 1

print(len([key for key, value in fabric.items() if value > 1]))
