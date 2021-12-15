with open("./input_13.txt") as fin:
    dots = set()
    while True:
        line = fin.readline().strip()
        if line == "":
            break
        dots.add(tuple([int(i) for i in line.split(",")]))
    folds = []
    while True:
        line = fin.readline().strip()
        if line == "":
            break

        fold = line[len("fold along "):]
        if fold[0] == "y":
            folds.append((0, int(fold[2:])))
        else:
            folds.append((int(fold[2:]), 0))

def reflect(point, line):
    if line[0] != 0:
        return (2*line[0] - point[0], point[1])
    return (point[0], 2*line[1] - point[1])


new_dots = set()
fold = folds[0]

for dot in dots:
    if fold[0] != 0:
        if dot[0] > fold[0]:
            new_dots.add(reflect(dot, fold))
        else:
            new_dots.add(dot)

    else:
        if dot[1] > fold[1]:
            new_dots.add(reflect(dot, fold))
        else:
            new_dots.add(dot)


ans = len(new_dots)
print(ans)