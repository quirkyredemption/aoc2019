# AoC December 3nd Part 1

def to_condinates(direction, pre_coord):
    coords = []
    # print(direction, pre_coord)
    if direction[0] == "R":
        for steps in range(1, int(direction[1:]) + 1):
            coords.append(((pre_coord[0] + steps), pre_coord[1]))
    if direction[0] == "L":
        for steps in range(1, int(direction[1:]) + 1):
            coords.append(((pre_coord[0] - steps), pre_coord[1]))       
    if direction[0] == "U":
        for steps in range(1, int(direction[1:]) + 1):
            coords.append((pre_coord[0],(pre_coord[1] + steps)))          
    if direction[:1] == "D":
        for steps in range(1, int(direction[1:]) + 1):
            coords.append((pre_coord[0],(pre_coord[1] - steps)))                  

    return coords

wire1_path = "insert path"
wire2_path = "insert path"

wire1 = open(wire1_path, "r").read().split(",")
wire2 = open(wire2_path, "r").read().split(",")

wire1_coordinates = [(0,0)]
wire2_coordinates = [(0,0)]

for idx, wire in enumerate(wire1):
    coord = []
    coord = to_condinates(wire, wire1_coordinates[len(wire1_coordinates)-1])
    wire1_coordinates += coord

for idx, wire in enumerate(wire2):
    coord = []
    coord = to_condinates(wire, wire2_coordinates[len(wire2_coordinates)-1])
    wire2_coordinates += coord

intersections = list(set(wire1_coordinates) & set(wire2_coordinates))
man_dists = []
for intersect in intersections:
    if intersect == (0,0):
        continue
    man_dists.append(abs(intersect[0]) + abs(intersect[1]))
    
man_dists.sort()
print(man_dists[0])

steps = []
for intersection in intersections:
    step = wire1_coordinates.index(intersection) + wire2_coordinates.index(intersection)
    steps.append(step)

steps.sort()
print(steps[0])
