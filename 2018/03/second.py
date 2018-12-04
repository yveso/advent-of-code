def split_line(line):
    main_split = line.split("@")
    left_side = main_split[0].rstrip().lstrip("#")
    right_side = main_split[1]
    split = right_side.split(":")
    start_point = [int(x) for x in split[0].split(",")]
    square = [int(x) for x in split[1].split("x")]
    return {
        "id": left_side,
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
                fabric[point] = [line["id"]]
            else:
                fabric[point].append(line["id"])

for line in lines:
    points = []
    for y in range(line["height"]):
        for x in range(line["width"]):
            points.append((line["x"] + x, line["y"] + y))
    found_it = all([len(fabric[p]) == 1 for p in points])
    if found_it:
        print(line["id"])
        break
