from aocd import get_data
data = get_data(year=2016, day=3)
lines = data.split("\n")

possible = 0

for line in lines:
    split_line = line.split(" ")
    x, y, z = [int(a) for a in split_line if a != ""]
    c1 = x + y > z
    c2 = x + z > y
    c3 = y + z > x

    if (c1 and c2 and c3):
        possible += 1

print(possible)