from aocd import get_data
data = get_data(year=2016, day=3)
lines = data.split("\n")

possible = 0
lines_grid = [[int(a) for a in line.split(" ") if a != ""] for line in lines ]

for col in range(3):
    
    for row in range(0,len(lines_grid)-2,3):
        x = lines_grid[row][col]
        y = lines_grid[row+1][col]
        z = lines_grid[row+2][col]
        
        c1 = x + y > z
        c2 = x + z > y
        c3 = y + z > x

        if (c1 and c2 and c3):
          possible += 1

print(possible)