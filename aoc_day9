class IntCodeComputer:
    def __init__(self, program, setting):
        self.code = program
        if not setting == None:
            self.inputs = [setting]
        else:
            self.inputs = []
        self.index = 0
        self.relative_base = 0
        self.output = []

    def get_opcode(self):
        return self.code[self.index] % 100
    
    def get_modes(self):
        mode1 = (self.code[self.index] // 100) % 10
        mode2 = (self.code[self.index] // 1000) % 10
        mode3 = (self.code[self.index] // 10000) % 10
        return mode1, mode2, mode3

    def get_parameter(self, opcode):
        mode1, mode2, mode3 = self.get_modes()
        parameter1, parameter2, parameter3 = None, None, None

        if opcode in (1, 2, 7, 8):
            parameter1 = self.index + 1 if mode1 == 1 else (self.code[self.index + 1] + self.relative_base if mode1 == 2 else self.code[self.index + 1])
            parameter2 = self.index + 2 if mode2 == 1 else (self.code[self.index + 2] + self.relative_base if mode2 == 2 else self.code[self.index + 2])
            parameter3 = self.index + 1 if mode3 == 1 else (self.code[self.index + 3] + self.relative_base if mode3 == 2 else self.code[self.index + 3])
        elif opcode in (3, 4, 9):
            parameter1 = self.index + 1 if mode1 == 1 else (self.code[self.index + 1] + self.relative_base if mode1 == 2 else self.code[self.index + 1])
        elif opcode in (5, 6):
            parameter1 = self.index + 1 if mode1 == 1 else (self.code[self.index + 1] + self.relative_base if mode1 == 2 else self.code[self.index + 1])
            parameter2 = self.index + 2 if mode2 == 1 else (self.code[self.index + 2] + self.relative_base if mode2 == 2 else self.code[self.index + 2])
    
        return parameter1, parameter2, parameter3
    
    def extend_memory(self, extension):
        memory_need = (extension - len(code)) + 1
        self.code += [0] * memory_need

    def run(self, inputs):
        if not inputs == None:
            self.inputs += inputs

        while self.index < len(self.code):
            opcode = self.get_opcode()
            parameter1, parameter2, parameter3 = self.get_parameter(opcode)

            for parameter in (parameter1, parameter2, parameter3):
                if parameter is not None:
                    if parameter > len(self.code):
                        self.extend_memory(parameter)

            if opcode == 1:
                self.code[parameter3] = self.code[parameter1] + self.code[parameter2]
            elif opcode == 2:
                self.code[parameter3] = self.code[parameter1] * self.code[parameter2]
            elif opcode == 3:
                self.code[parameter1] = self.inputs.pop(0)
            elif opcode == 4:
                self.output.append(self.code[parameter1])
            elif opcode == 5:
                self.index = self.code[parameter2] if self.code[parameter1] != 0 else self.index + 3
            elif opcode == 6:
                self.index = self.code[parameter2] if self.code[parameter1] == 0 else self.index + 3
            elif opcode == 7:
                self.code[parameter3] = int(self.code[parameter1] < self.code[parameter2])
            elif opcode == 8:
                self.code[parameter3] = int(self.code[parameter1] == self.code[parameter2])
            elif opcode == 9:
                self.relative_base += self.code[parameter1] 
            else:
                assert opcode == 99
                return self.output

            if opcode in (1, 2, 7, 8):
                self.index += 4
            elif opcode in (3, 4, 9):
                self.index += 2

if __name__ == "__main__":
    code = [int(x) for x in open("input_day9.txt", "r").read().split(",")]
    boost1 = IntCodeComputer(code, None)
    part1 = boost1.run([1])
    print(f"Password is {part1[0]}")
    boost2 = IntCodeComputer(code, 2)
    part2 = boost2.run([1])
    print(f"Coordinates is {part2[0]}")
