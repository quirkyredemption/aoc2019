# AoC December 2nd Part 1
# file_path = r"C:\Users\au256765\Desktop\Nyt tekstdokument.txt"

# opcodes = open(file_path, "r").read().split(",")
# opcodes = list(map(int, opcodes))

# opcodes[1] = 12
# opcodes[2] = 2

# for idx, val in enumerate(opcodes):
#     if idx % 4 == 0 or idx == 0:
#         if val == 99:
#             break

#         if val == 1:
#             opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] + opcodes[opcodes[idx + 2]]
#         elif val == 2:
#             opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] * opcodes[opcodes[idx + 2]]

# print(opcodes[0])    

# AoC December 2nd Part 2
# file_path = r"C:\Users\au256765\Desktop\Nyt tekstdokument.txt"

# opcodes = open(file_path, "r").read().split(",")
# opcodes = list(map(int, opcodes))
# opcodes_original = opcodes


# for noun in range(0,100):
#     for verb in range(0,100):
#         opcodes = list(map(int,open(file_path, "r").read().split(",")))
#         # print(opcodes)
        
#         opcodes[1] = noun
#         opcodes[2] = verb

#         # print(opcodes[1], opcodes[2])

#         for idx, val in enumerate(opcodes):
#             # print(idx, val)
#             if idx % 4 == 0 or idx == 0:
#                 if val == 99:
#                     break
                
#                 if val == 1:
#                     opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] + opcodes[opcodes[idx + 2]]
#                 elif val == 2:
#                     opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] * opcodes[opcodes[idx + 2]]

#         if opcodes[0] == 19690720:
#             print(100 * noun + verb)
#             break
#         # print(opcodes)
       
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

wire1_path = r"C:\Users\au256765\Desktop\wire1.txt"
wire2_path = r"C:\Users\au256765\Desktop\wire2.txt"

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

