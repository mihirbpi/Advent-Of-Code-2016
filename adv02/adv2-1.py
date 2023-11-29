from aocd import get_data
from collections import defaultdict

data = get_data(year=2016, day=2)
instructions = data.split("\n")

curr_pos = [0, 0]
dir_to_move_dict = {"U": [0,1], "L": [-1,0], "R": [1,0], "D": [0,-1]}
pad_dict = defaultdict(lambda : "0")
pad_dict[(-1,1)] = "1"
pad_dict[(-1,0)] = "4"
pad_dict[(-1,-1)] = "7"
pad_dict[(0,1)] = "2"
pad_dict[(0,0)] = "5"
pad_dict[(0,-1)] = "8"
pad_dict[(1,1)] = "3"
pad_dict[(1,0)] = "6"
pad_dict[(1,-1)] = "9"
code = ""

for instruction in instructions:

    for dir in instruction:
        new_pos_x = curr_pos[0] + dir_to_move_dict[dir][0]
        new_pos_y = curr_pos[1] + dir_to_move_dict[dir][1]

        if pad_dict[(new_pos_x, new_pos_y)] != "0":
            curr_pos = [new_pos_x, new_pos_y]
    code += str(pad_dict[tuple(curr_pos)])

print(code)

