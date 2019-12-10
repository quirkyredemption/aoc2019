asteriod_map = [list(line.strip()) for line in open("input.txt", "r")]
asteriod_total = [item for sublist in asteriod_map for item in sublist].count("#")
map_width = len(asteriod_map)
map_height = len(asteriod_map[0])


def neighboor_asteroid(x, y):
    

for i in range(map_width):
    for j in range(map_height):
        if asteriod_map == "#":
