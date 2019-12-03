# AoC December 2nd Part 1
file_path = "INSERT PATH"

opcodes = open(file_path, "r").read().split(",")
opcodes = list(map(int, opcodes))

opcodes[1] = 12
opcodes[2] = 2

for idx, val in enumerate(opcodes):
    if idx % 4 == 0 or idx == 0:
        if val == 99:
            break

        if val == 1:
            opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] + opcodes[opcodes[idx + 2]]
        elif val == 2:
            opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] * opcodes[opcodes[idx + 2]]

print(opcodes[0])    

# AoC December 2nd Part 2
file_path = "INSERT PATH"

opcodes = open(file_path, "r").read().split(",")
opcodes = list(map(int, opcodes))
opcodes_original = opcodes


for noun in range(0,100):
    for verb in range(0,100):
        opcodes = list(map(int,open(file_path, "r").read().split(",")))
      
        opcodes[1] = noun
        opcodes[2] = verb

         for idx, val in enumerate(opcodes):
            if idx % 4 == 0 or idx == 0:
                if val == 99:
                    break
                
                if val == 1:
                    opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] + opcodes[opcodes[idx + 2]]
                elif val == 2:
                    opcodes[opcodes[idx + 3]] = opcodes[opcodes[idx + 1]] * opcodes[opcodes[idx + 2]]

        if opcodes[0] == 19690720:
            print(100 * noun + verb)
            break
