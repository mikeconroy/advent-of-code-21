import copy

f = open("input", "r")

coordinates = dict()
foldInstructions = []
for line in f.readlines():
    if ("fold along x" in line):
        foldInstruction = ("x", int(line.strip().split("=")[1]))
        foldInstructions.append(foldInstruction)
    elif ("fold along y" in line):
        foldInstruction = ("y", int(line.strip().split("=")[1]))
        foldInstructions.append(foldInstruction)
    elif (line.strip() != ""):
        x,y = line.strip().split(",")
        coordinates[(int(x), int(y))] = True

def foldUp(foldLine):
    for point in copy.deepcopy(coordinates):
        # Only operate on the point if it is above(below) the fold line.
        x = point[0]
        y = point[1]
        if(y > foldLine):
            # New Y = difference between Fold line & Y
            newY = foldLine - (y - foldLine)
            coordinates[(x, newY)] = True
            # Remove all points below the fold line.
            coordinates.pop(point)

def foldLeft(foldLine):
    for point in copy.deepcopy(coordinates):
        # Only operate on the point if it is above(below) the fold line.
        x = point[0]
        y = point[1]
        if(x > foldLine):
            # New X = difference between Fold line & X
            newX = foldLine - (x - foldLine)
            coordinates[(newX, y)] = True
            coordinates.pop(point)

def part1():
    if(foldInstructions[0][0] == "x"):
        foldLeft(foldInstructions[0][1])
    else:
        foldUp(foldInstructions[0][1])
    return len(coordinates)

print("PART 1:", part1())