from aocd import get_data
from collections import defaultdict

data = get_data(year=2016, day=1)
instructions = data.split(", ")
dir_array = ["N", "E", "S", "W"]
dir_vector_dict = {"N": [0,1], "E": [1,0], "S": [0,-1], "W":[-1,0]}
turn_dir_dict = {"L":-1, "R":1}
pos = [0,0]
curr_idx = 0
pos_visited_dict = defaultdict(lambda : 0)
pos_visited_dict[tuple(pos)] = 1
revisited  = False

for instruction in instructions:
    turn_dir = instruction[0]
    forward_amount = int(instruction[1:])
    curr_idx = (curr_idx + turn_dir_dict[turn_dir]) % 4
    curr_dir = dir_array[curr_idx]
    curr_vector = dir_vector_dict[curr_dir].copy()

    for i in range(forward_amount):
            pos[0] += curr_vector[0]
            pos[1] += curr_vector[1]
            pos_visited_dict[tuple(pos)] += 1

            if pos_visited_dict[tuple(pos)] == 2:
                print(abs(pos[0]) + abs(pos[1]))
                revisited = True
                break

    if (revisited):
         break

