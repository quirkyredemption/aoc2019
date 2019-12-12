import numpy as np
import matplotlib.pyplot as plt

class IntCodeComputer:
    def __init__(self, program, setting, continue_prog):
        self.code = program
        if not setting == None:
            self.inputs = [setting]
        else:
            self.inputs = []
        self.index = 0
        self.relative_base = 0
        self.prog_continue = continue_prog
        self.saved_index = 0
        
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
        memory_need = (extension - len(self.code)) + 1
        self.code += [0] * memory_need

    def run(self, inputs):
        if not inputs == None:
            self.inputs += inputs
        
        self.output = []
        
        if self.prog_continue:
            self.index = self.saved_index

        while self.index < len(self.code):
            opcode = self.get_opcode()
            parameter1, parameter2, parameter3 = self.get_parameter(opcode)
            for parameter in (parameter1, parameter2, parameter3):
                if parameter is not None:
                    if parameter >= len(self.code):
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
                return self.output, True

            if opcode in (1, 2, 7, 8):
                self.index += 4
            elif opcode in (3, 4, 9):
                self.index += 2

            if len(self.output) == 2:
                self.saved_index = self.index
                return self.output, False

class Panel():
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color


def robot_move(coords, turn, direction):
    down = {1: ("<", [coords[0] - 1, coords[1]]), 0: (">", [coords[0] + 1, coords[1]])}
    up = {1: (">", [coords[0] + 1, coords[1]]), 0: ("<", [coords[0] - 1, coords[1]])}
    right = {1: ("v", [coords[0], coords[1] - 1]), 0: ("^", [coords[0], coords[1] + 1])}
    left = {1: ("^", [coords[0], coords[1] + 1]), 0: ("v", [coords[0], coords[1] - 1])}
    
    if direction == "^":
        return up[turn][0], up[turn][1]
    if direction == "v":
        return down[turn][0], down[turn][1]
    if direction == "<":
        return left[turn][0], left[turn][1]
    if direction == ">":
        return right[turn][0], right[turn][1]


robot_instr = open("input_day11.txt", "r").read().split(",")
robot_instr = [int(x) for x in robot_instr]
robot = IntCodeComputer(robot_instr, None, True)

# panels = set()
panel_coords = [0, 0]
panels = [Panel(panel_coords, 0)]
placement = "^"

program_halt = False
color = 1

while True:
    instr, program_halt = robot.run([color])
    if program_halt:
        break
    painted_color = instr[0]
    
    for panel in panels:
        if panel.coords == panel_coords:
            panel.color = painted_color
    
    placement, panel_coords = robot_move(panel_coords, instr[1], placement)
    
    new_panel = True
    for panel in panels:
        if panel.coords == panel_coords:
            color = panel.color
            new_panel = False
    
    if new_panel:
        panels.append(Panel(panel_coords, 0))
        color = 0
    
# coords = [panel.coords for panel in panels]

coords = {}

for panel in panels:
    coords[(panel.coords[0], panel.coords[1])] = panel.color

min_x = min([panel.coords[0] for panel in panels])
max_x = max([panel.coords[0] for panel in panels])
min_y = min([panel.coords[1] for panel in panels])
max_y = max([panel.coords[1] for panel in panels])

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if coords.get((x, y)) != None:
            p = "1" if coords[(x, y)] == 1 else " "
        else:
            p = " "
        print(p, end="")
    print()